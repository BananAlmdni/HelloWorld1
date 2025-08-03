# API Quick Reference

Fast reference for the most commonly used HelloWorld1 APIs and functions.

## 🚀 Quick Setup

```javascript
import { HelloWorld1, init } from 'helloworld1';

const hw1 = await init({
  apiKey: 'your-api-key'
});
```

---

## 🔐 Authentication

### API Key Authentication
```javascript
const hw1 = new HelloWorld1({
  apiKey: 'your-api-key'
});
```

### OAuth 2.0
```javascript
const authUrl = await hw1.auth.getAuthorizationUrl({
  clientId: 'your-client-id',
  redirectUri: 'https://yourapp.com/callback',
  scope: 'read write'
});
```

### JWT Tokens
```javascript
const token = await hw1.auth.exchangeCodeForToken(authCode);
hw1.setAuthToken(token);
```

---

## 👥 Users API

### Get User
```javascript
GET /users/{id}

const user = await hw1.users.get('user_123');
```

### Create User
```javascript
POST /users

const user = await hw1.users.create({
  name: 'John Doe',
  email: 'john@example.com'
});
```

### Update User
```javascript
PUT /users/{id}

const user = await hw1.users.update('user_123', {
  name: 'Jane Doe'
});
```

### Delete User
```javascript
DELETE /users/{id}

await hw1.users.delete('user_123');
```

### List Users
```javascript
GET /users?page=1&limit=20

const users = await hw1.users.list({
  page: 1,
  limit: 20,
  sort: 'created_at'
});
```

---

## 📊 Data API

### Get Data
```javascript
GET /data/{id}

const data = await hw1.data.get('data_123');
```

### Create Data
```javascript
POST /data

const data = await hw1.data.create({
  title: 'My Data',
  value: 42
});
```

### Query Data
```javascript
GET /data?filter[status]=active

const results = await hw1.data.query({
  filter: { status: 'active' },
  sort: { created_at: -1 },
  limit: 50
});
```

### Batch Operations
```javascript
POST /data/batch

const results = await hw1.data.batch([
  { action: 'create', data: { title: 'Item 1' } },
  { action: 'update', id: 'data_123', data: { title: 'Updated' } },
  { action: 'delete', id: 'data_456' }
]);
```

---

## 🔧 Utility Functions

### Validation
```javascript
import { validateEmail, validateInput } from 'helloworld1';

const isValid = validateEmail('user@example.com');

const result = validateInput(data, schema);
if (!result.isValid) {
  console.error(result.errors);
}
```

### Date Formatting
```javascript
import { formatDate } from 'helloworld1';

const formatted = formatDate(new Date(), 'YYYY-MM-DD HH:mm');
```

### ID Generation
```javascript
import { generateId } from 'helloworld1';

const id = generateId('user'); // Returns: user_a1b2c3d4
```

### Configuration
```javascript
import { getConfig, setConfig } from 'helloworld1';

setConfig('apiUrl', 'https://api.example.com');
const apiUrl = getConfig('apiUrl');
```

---

## 🎯 Event Handling

### Add Event Listener
```javascript
import { addEventListener } from 'helloworld1';

const listenerId = addEventListener('dataUpdate', (data) => {
  console.log('Data updated:', data);
});
```

### Remove Event Listener
```javascript
import { removeEventListener } from 'helloworld1';

removeEventListener(listenerId);
```

### Emit Event
```javascript
import { emitEvent } from 'helloworld1';

emitEvent('customEvent', { key: 'value' });
```

---

## 🌐 Real-time Features

### WebSocket Connection
```javascript
const ws = hw1.realtime.connect();

ws.on('connected', () => {
  console.log('Connected to real-time service');
});
```

### Subscribe to Events
```javascript
ws.subscribe('channel:updates', (data) => {
  console.log('Received update:', data);
});
```

### Publish Events
```javascript
ws.publish('channel:message', {
  text: 'Hello World!',
  timestamp: new Date()
});
```

---

## 🧩 React Components

### Basic Components
```jsx
import { HelloButton, HelloInput, HelloCard } from 'helloworld1/react';

<HelloButton variant="primary" onClick={handleClick}>
  Click Me
</HelloButton>

<HelloInput 
  label="Email"
  type="email"
  value={email}
  onChange={setEmail}
  required
/>

<HelloCard title="My Card">
  Card content goes here
</HelloCard>
```

### Form Components
```jsx
import { HelloForm } from 'helloworld1/react';

<HelloForm 
  schema={validationSchema}
  onSubmit={handleSubmit}
  initialValues={{ name: '', email: '' }}
>
  {({ values, errors, isValid }) => (
    <>
      <HelloInput name="name" label="Name" />
      <HelloInput name="email" label="Email" type="email" />
      <HelloButton type="submit" disabled={!isValid}>
        Submit
      </HelloButton>
    </>
  )}
</HelloForm>
```

### Data Display
```jsx
import { HelloTable, HelloModal } from 'helloworld1/react';

<HelloTable
  data={users}
  columns={columns}
  sortable
  filterable
  pagination={{ pageSize: 10 }}
/>

<HelloModal
  open={isOpen}
  title="Edit User"
  onClose={() => setIsOpen(false)}
>
  Modal content
</HelloModal>
```

---

## 📱 React Hooks

### useHelloWorld
```jsx
import { useHelloWorld } from 'helloworld1/react';

function MyComponent() {
  const { hw1, loading, error } = useHelloWorld();
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return <div>Ready to use HelloWorld1!</div>;
}
```

### useApi
```jsx
import { useApi } from 'helloworld1/react';

function UserProfile({ userId }) {
  const { data: user, loading, error } = useApi(`/users/${userId}`);
  
  return loading ? <div>Loading...</div> : <div>{user.name}</div>;
}
```

### useRealtime
```jsx
import { useRealtime } from 'helloworld1/react';

function ChatRoom() {
  const { connected, send, subscribe } = useRealtime();
  
  useEffect(() => {
    return subscribe('message', handleNewMessage);
  }, []);
  
  return <div>Connected: {connected ? 'Yes' : 'No'}</div>;
}
```

---

## ⚠️ Error Handling

### Common Error Codes
```javascript
try {
  const result = await hw1.api.call('/endpoint');
} catch (error) {
  switch (error.code) {
    case 'INVALID_API_KEY':
      // Handle authentication error
      break;
    case 'RATE_LIMIT_EXCEEDED':
      // Handle rate limiting
      break;
    case 'VALIDATION_ERROR':
      // Handle validation errors
      console.log(error.details);
      break;
    case 'NETWORK_ERROR':
      // Handle network issues
      break;
    default:
      // Handle unexpected errors
      break;
  }
}
```

### Retry Logic
```javascript
async function apiCallWithRetry(fn, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
    }
  }
}
```

---

## 🔍 Common Patterns

### Pagination
```javascript
async function loadPage(page = 1) {
  const result = await hw1.data.list({
    page,
    limit: 20
  });
  
  return {
    items: result.data,
    totalPages: Math.ceil(result.total / 20),
    hasNext: page < Math.ceil(result.total / 20)
  };
}
```

### Search with Debouncing
```javascript
import { debounce } from 'helloworld1';

const debouncedSearch = debounce(async (query) => {
  const results = await hw1.data.search(query);
  setSearchResults(results);
}, 300);
```

### Infinite Scrolling
```javascript
function useInfiniteScroll() {
  const [items, setItems] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);
  
  const loadMore = async () => {
    setLoading(true);
    const newItems = await hw1.data.list({ page, limit: 20 });
    setItems(prev => [...prev, ...newItems.data]);
    setPage(prev => prev + 1);
    setLoading(false);
  };
  
  return { items, loadMore, loading };
}
```

---

## 🔧 Configuration Options

### Global Configuration
```javascript
const hw1 = new HelloWorld1({
  apiKey: 'your-api-key',
  baseUrl: 'https://api.helloworld1.com',
  timeout: 30000,
  retries: 3,
  debug: true,
  cache: {
    enabled: true,
    ttl: 300000
  },
  realtime: {
    autoConnect: true,
    reconnect: true
  }
});
```

### Environment Variables
```bash
HELLOWORLD1_API_KEY=your_api_key
HELLOWORLD1_BASE_URL=https://api.helloworld1.com
HELLOWORLD1_DEBUG=true
```

---

## 📊 Response Formats

### Success Response
```json
{
  "success": true,
  "data": {
    "id": "123",
    "name": "Example"
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "version": "1.0.0"
  }
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "field": "email",
      "reason": "Invalid email format"
    }
  }
}
```

### Paginated Response
```json
{
  "success": true,
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

---

## 🚀 Performance Tips

1. **Use pagination** for large datasets
2. **Implement caching** for frequently accessed data
3. **Use batch operations** for multiple API calls
4. **Enable compression** for large payloads
5. **Use CDN** for static assets
6. **Implement retry logic** for network resilience

---

For complete documentation, see the [full API documentation](./README.md).