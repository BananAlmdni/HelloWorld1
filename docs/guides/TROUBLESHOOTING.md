# Troubleshooting Guide

This guide helps you resolve common issues when working with HelloWorld1.

## 📋 Table of Contents

- [Quick Diagnostics](#quick-diagnostics)
- [Installation Issues](#installation-issues)
- [Authentication Problems](#authentication-problems)
- [API Errors](#api-errors)
- [Component Issues](#component-issues)
- [Performance Problems](#performance-problems)
- [Browser Compatibility](#browser-compatibility)
- [Development Tools](#development-tools)
- [Getting Help](#getting-help)

---

## 🩺 Quick Diagnostics

### Health Check Script

Run this script to quickly diagnose common issues:

```javascript
import { HelloWorld1, diagnostics } from 'helloworld1';

async function healthCheck() {
  const report = await diagnostics.run([
    'connection',
    'authentication',
    'permissions',
    'environment'
  ]);
  
  console.log('Health Check Report:', report);
  
  if (report.hasIssues) {
    console.log('Issues found:');
    report.issues.forEach(issue => {
      console.log(`- ${issue.type}: ${issue.message}`);
      if (issue.solution) {
        console.log(`  Solution: ${issue.solution}`);
      }
    });
  } else {
    console.log('✅ All systems operational');
  }
}

healthCheck();
```

### Environment Check

```bash
# Check Node.js version
node --version  # Should be 16+

# Check npm version
npm --version

# Check package installation
npm list helloworld1

# Verify configuration
npm run helloworld1:config
```

---

## 📦 Installation Issues

### Problem: Package Not Found

**Error:**
```
npm ERR! 404 Not Found - GET https://registry.npmjs.org/helloworld1
```

**Solutions:**
1. Check package name spelling
2. Verify npm registry configuration
3. Check network connectivity

```bash
# Check npm configuration
npm config list

# Set registry if needed
npm config set registry https://registry.npmjs.org/

# Clear npm cache
npm cache clean --force

# Try installation again
npm install helloworld1
```

### Problem: Version Conflicts

**Error:**
```
npm ERR! peer dep missing: react@^18.0.0
```

**Solutions:**
1. Install missing peer dependencies
2. Update existing dependencies
3. Use npm's peer dependency resolution

```bash
# Install peer dependencies
npm install react@^18.0.0 react-dom@^18.0.0

# Auto-install peer dependencies
npm install --install-peers

# Check for outdated packages
npm outdated
npm update
```

### Problem: Build Failures

**Error:**
```
Module not found: Error: Can't resolve 'helloworld1'
```

**Solutions:**
1. Restart development server
2. Clear build cache
3. Check import paths

```bash
# Clear cache and restart
rm -rf node_modules/.cache
npm start

# For Next.js
rm -rf .next
npm run dev

# For Create React App
rm -rf build
npm start
```

---

## 🔐 Authentication Problems

### Problem: Invalid API Key

**Error:**
```javascript
{
  "error": {
    "code": "INVALID_API_KEY",
    "message": "The provided API key is invalid"
  }
}
```

**Solutions:**
1. Verify API key format
2. Check environment variables
3. Regenerate API key

```javascript
// Check API key format
const apiKey = process.env.HELLOWORLD1_API_KEY;
console.log('API Key length:', apiKey?.length); // Should be 32-64 characters
console.log('API Key prefix:', apiKey?.substring(0, 4)); // Should match expected prefix

// Verify environment loading
if (!apiKey) {
  console.error('API key not found in environment variables');
  console.log('Available env vars:', Object.keys(process.env).filter(k => k.includes('HELLO')));
}
```

### Problem: Authentication Expired

**Error:**
```javascript
{
  "error": {
    "code": "AUTH_EXPIRED",
    "message": "Authentication token has expired"
  }
}
```

**Solutions:**
1. Refresh authentication token
2. Re-authenticate user
3. Check token expiration handling

```javascript
// Automatic token refresh
import { HelloWorld1 } from 'helloworld1';

const hw1 = new HelloWorld1({
  apiKey: 'your-api-key',
  autoRefresh: true,
  onTokenExpired: async () => {
    // Handle token expiration
    console.log('Token expired, refreshing...');
    return await refreshAuthToken();
  }
});
```

### Problem: Permission Denied

**Error:**
```javascript
{
  "error": {
    "code": "PERMISSION_DENIED",
    "message": "Insufficient permissions for this operation"
  }
}
```

**Solutions:**
1. Check user permissions
2. Verify API key scope
3. Request additional permissions

```javascript
// Check current permissions
const permissions = await hw1.auth.getPermissions();
console.log('Current permissions:', permissions);

// Check required permissions for operation
const required = hw1.users.getRequiredPermissions('create');
console.log('Required permissions:', required);

const hasPermission = required.every(perm => permissions.includes(perm));
console.log('Has required permissions:', hasPermission);
```

---

## 🌐 API Errors

### Problem: Network Timeouts

**Error:**
```javascript
{
  "error": {
    "code": "NETWORK_TIMEOUT",
    "message": "Request timed out after 5000ms"
  }
}
```

**Solutions:**
1. Increase timeout values
2. Check network connectivity
3. Implement retry logic

```javascript
// Configure timeouts
const hw1 = new HelloWorld1({
  timeout: 30000, // 30 seconds
  retries: 3,
  retryDelay: 1000
});

// Custom retry logic
async function apiCallWithRetry(fn, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (error.code === 'NETWORK_TIMEOUT' && i < maxRetries - 1) {
        console.log(`Retry ${i + 1}/${maxRetries}`);
        await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
        continue;
      }
      throw error;
    }
  }
}
```

### Problem: Rate Limiting

**Error:**
```javascript
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Try again in 60 seconds."
  }
}
```

**Solutions:**
1. Implement exponential backoff
2. Reduce request frequency
3. Use request batching

```javascript
// Rate limiting with exponential backoff
class RateLimitHandler {
  constructor() {
    this.requests = [];
    this.maxRequests = 100;
    this.windowMs = 60 * 1000; // 1 minute
  }

  async makeRequest(fn) {
    const now = Date.now();
    
    // Clean old requests
    this.requests = this.requests.filter(
      time => now - time < this.windowMs
    );
    
    if (this.requests.length >= this.maxRequests) {
      const oldestRequest = Math.min(...this.requests);
      const waitTime = this.windowMs - (now - oldestRequest);
      console.log(`Rate limited. Waiting ${waitTime}ms`);
      await new Promise(resolve => setTimeout(resolve, waitTime));
      return this.makeRequest(fn);
    }
    
    this.requests.push(now);
    return fn();
  }
}
```

### Problem: Invalid Response Format

**Error:**
```javascript
SyntaxError: Unexpected token < in JSON at position 0
```

**Solutions:**
1. Check API endpoint URLs
2. Verify response content type
3. Handle non-JSON responses

```javascript
// Robust response handling
async function safeApiCall(url, options = {}) {
  try {
    const response = await fetch(url, options);
    
    // Check if response is OK
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    // Check content type
    const contentType = response.headers.get('content-type');
    if (!contentType?.includes('application/json')) {
      const text = await response.text();
      console.error('Non-JSON response:', text);
      throw new Error('Invalid response format');
    }
    
    return await response.json();
  } catch (error) {
    if (error instanceof SyntaxError) {
      console.error('JSON parsing failed:', error);
      throw new Error('Invalid JSON response');
    }
    throw error;
  }
}
```

---

## 🧩 Component Issues

### Problem: Component Not Rendering

**Symptoms:**
- Blank screen
- Console errors about undefined components
- Missing styles

**Solutions:**
1. Check import statements
2. Verify provider setup
3. Check for JavaScript errors

```jsx
// Debug component rendering
import React from 'react';
import { HelloWorld1Provider, HelloButton } from 'helloworld1/react';

function DebugApp() {
  console.log('App rendering');
  
  return (
    <HelloWorld1Provider apiKey="test-key">
      <div>
        <h1>Debug App</h1>
        <HelloButton onClick={() => console.log('Button clicked')}>
          Test Button
        </HelloButton>
      </div>
    </HelloWorld1Provider>
  );
}

export default DebugApp;
```

### Problem: Styling Issues

**Symptoms:**
- Components appear unstyled
- Layout problems
- Missing CSS

**Solutions:**
1. Import CSS files
2. Check CSS module configuration
3. Verify theme provider

```jsx
// Import required styles
import 'helloworld1/dist/styles.css';

// Check theme configuration
import { ThemeProvider } from 'helloworld1/react';

function App() {
  return (
    <ThemeProvider theme="default">
      <MyComponents />
    </ThemeProvider>
  );
}
```

### Problem: Event Handlers Not Working

**Symptoms:**
- Click events not firing
- Form submissions failing
- State not updating

**Solutions:**
1. Check event handler binding
2. Verify component state
3. Debug event propagation

```jsx
// Debug event handlers
function DebugComponent() {
  const handleClick = (event) => {
    console.log('Click event:', event);
    console.log('Event target:', event.target);
    console.log('Current target:', event.currentTarget);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Form submitted:', event);
  };

  return (
    <form onSubmit={handleSubmit}>
      <button 
        type="button"
        onClick={handleClick}
        onMouseDown={(e) => console.log('Mouse down:', e)}
        onMouseUp={(e) => console.log('Mouse up:', e)}
      >
        Debug Button
      </button>
    </form>
  );
}
```

---

## ⚡ Performance Problems

### Problem: Slow Loading

**Symptoms:**
- Long initial load times
- Delayed component rendering
- Poor user experience

**Solutions:**
1. Enable code splitting
2. Implement lazy loading
3. Optimize bundle size

```jsx
// Code splitting with React.lazy
import { lazy, Suspense } from 'react';

const HeavyComponent = lazy(() => 
  import('./HeavyComponent').then(module => ({
    default: module.HeavyComponent
  }))
);

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}
```

### Problem: Memory Leaks

**Symptoms:**
- Increasing memory usage
- Browser slowdown
- App crashes

**Solutions:**
1. Clean up event listeners
2. Cancel pending requests
3. Remove timers and intervals

```jsx
// Proper cleanup with hooks
import { useEffect, useRef } from 'react';

function ComponentWithCleanup() {
  const intervalRef = useRef();
  const abortControllerRef = useRef();

  useEffect(() => {
    // Set up interval
    intervalRef.current = setInterval(() => {
      console.log('Interval tick');
    }, 1000);

    // Set up API call with cancellation
    abortControllerRef.current = new AbortController();
    
    fetch('/api/data', {
      signal: abortControllerRef.current.signal
    }).then(response => {
      // Handle response
    }).catch(error => {
      if (error.name !== 'AbortError') {
        console.error('API error:', error);
      }
    });

    // Cleanup function
    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
    };
  }, []);

  return <div>Component with proper cleanup</div>;
}
```

### Problem: Excessive Re-renders

**Symptoms:**
- Poor performance
- Flickering UI
- High CPU usage

**Solutions:**
1. Use React.memo
2. Optimize dependencies
3. Use useCallback and useMemo

```jsx
import { memo, useCallback, useMemo } from 'react';

// Memoized component
const OptimizedComponent = memo(({ data, onUpdate }) => {
  // Memoized computation
  const processedData = useMemo(() => {
    return data.map(item => ({
      ...item,
      processed: true
    }));
  }, [data]);

  // Memoized callback
  const handleUpdate = useCallback((id) => {
    onUpdate(id);
  }, [onUpdate]);

  return (
    <div>
      {processedData.map(item => (
        <div key={item.id} onClick={() => handleUpdate(item.id)}>
          {item.name}
        </div>
      ))}
    </div>
  );
});
```

---

## 🌐 Browser Compatibility

### Problem: Internet Explorer Support

**Error:**
```
Object doesn't support property or method 'includes'
```

**Solutions:**
1. Add polyfills
2. Use transpilation
3. Check feature support

```javascript
// Add polyfills for IE support
import 'core-js/stable';
import 'regenerator-runtime/runtime';

// Feature detection
function checkBrowserSupport() {
  const required = [
    'fetch',
    'Promise',
    'Map',
    'Set'
  ];

  const missing = required.filter(feature => !window[feature]);
  
  if (missing.length > 0) {
    console.warn('Missing features:', missing);
    // Load polyfills or show compatibility message
  }
}

checkBrowserSupport();
```

### Problem: Mobile Safari Issues

**Symptoms:**
- Touch events not working
- Viewport issues
- Performance problems

**Solutions:**
1. Add touch event handlers
2. Configure viewport meta tag
3. Optimize for mobile

```html
<!-- Viewport configuration -->
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">

<!-- Prevent zoom on input focus -->
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
```

```css
/* Fix iOS Safari issues */
.component {
  /* Prevent bounce scrolling */
  -webkit-overflow-scrolling: touch;
  
  /* Fix click delay */
  touch-action: manipulation;
  
  /* Prevent text selection */
  -webkit-user-select: none;
  user-select: none;
}
```

---

## 🛠️ Development Tools

### Debug Mode

Enable comprehensive debugging:

```javascript
import { HelloWorld1 } from 'helloworld1';

const hw1 = new HelloWorld1({
  debug: true,
  logLevel: 'verbose',
  enableDevTools: true
});

// Access debug information
console.log('Debug info:', hw1.debug.getInfo());
console.log('Performance metrics:', hw1.debug.getMetrics());
```

### Browser DevTools

Use browser developer tools effectively:

1. **Console Debugging**
   ```javascript
   // Enable verbose logging
   localStorage.setItem('helloworld1:debug', 'true');
   
   // Access global debug object
   window.HelloWorld1Debug = hw1.debug;
   ```

2. **Network Tab**
   - Monitor API calls
   - Check request/response headers
   - Verify payload data

3. **Performance Tab**
   - Profile component rendering
   - Identify performance bottlenecks
   - Monitor memory usage

### Testing Environment

Set up proper testing:

```javascript
// Jest configuration for testing
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
  moduleNameMapping: {
    '^helloworld1/(.*)$': '<rootDir>/node_modules/helloworld1/dist/$1'
  }
};

// Test utilities
import { render, screen } from '@testing-library/react';
import { HelloWorld1Provider } from 'helloworld1/react';

export function renderWithProvider(component, options = {}) {
  return render(
    <HelloWorld1Provider apiKey="test-key" {...options}>
      {component}
    </HelloWorld1Provider>
  );
}
```

---

## 🆘 Getting Help

### Before Asking for Help

1. **Search Existing Issues**
   - Check GitHub issues
   - Search documentation
   - Look through FAQ

2. **Gather Information**
   - Error messages
   - Browser/Node.js versions
   - Code examples
   - Steps to reproduce

3. **Create Minimal Example**
   - Isolate the problem
   - Remove unnecessary code
   - Test in clean environment

### Support Channels

1. **GitHub Issues**
   - Bug reports
   - Feature requests
   - Technical questions

2. **Community Discord**
   - Real-time help
   - General questions
   - Community discussions

3. **Stack Overflow**
   - Tag: `helloworld1`
   - Detailed technical questions
   - Code review

### Issue Template

```markdown
## Bug Report

**Environment:**
- HelloWorld1 version: 
- Node.js version: 
- Browser/OS: 
- Framework: 

**Expected Behavior:**
What you expected to happen.

**Actual Behavior:**
What actually happened.

**Steps to Reproduce:**
1. 
2. 
3. 

**Code Example:**
```javascript
// Minimal code to reproduce the issue
```

**Error Messages:**
```
Paste any error messages here
```

**Additional Context:**
Any other relevant information.
```

---

## 📊 Common Error Codes Reference

| Code | Description | Common Causes | Solutions |
|------|-------------|---------------|-----------|
| `INVALID_API_KEY` | API key is invalid | Wrong key, expired key | Verify and regenerate key |
| `RATE_LIMIT_EXCEEDED` | Too many requests | High request frequency | Implement backoff |
| `NETWORK_TIMEOUT` | Request timed out | Slow network, large payload | Increase timeout |
| `PERMISSION_DENIED` | Insufficient permissions | Wrong scope, expired token | Check permissions |
| `VALIDATION_ERROR` | Invalid input data | Missing fields, wrong format | Validate input |
| `RESOURCE_NOT_FOUND` | Resource doesn't exist | Wrong ID, deleted resource | Check resource ID |
| `INTERNAL_SERVER_ERROR` | Server error | Server issues, maintenance | Retry later |

---

Remember: When in doubt, start with the [Quick Diagnostics](#quick-diagnostics) section and work your way through the specific problem areas. Most issues can be resolved by following the systematic troubleshooting steps outlined above.