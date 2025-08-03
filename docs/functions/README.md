# Function Documentation

This section provides comprehensive documentation for all public functions in HelloWorld1.

## 📋 Table of Contents

- [Core Functions](#core-functions)
- [Utility Functions](#utility-functions)
- [Helper Functions](#helper-functions)
- [Validation Functions](#validation-functions)
- [Configuration Functions](#configuration-functions)
- [Event Handler Functions](#event-handler-functions)

## 📝 Documentation Format

Each function is documented with:
- **Purpose**: What the function does
- **Parameters**: Input parameters with types and descriptions
- **Return Value**: Return type and description
- **Examples**: Working code examples
- **Error Handling**: Possible errors and how to handle them
- **See Also**: Related functions and resources

---

## 🔧 Core Functions

### `init(config?: Config): Promise<HelloWorldInstance>`

Initializes a new HelloWorld instance with optional configuration.

**Purpose:**
Creates and configures a new HelloWorld application instance with the provided configuration options.

**Parameters:**
- `config` (Config, optional): Configuration object for the HelloWorld instance
  - `apiKey` (string, optional): API key for authentication
  - `debug` (boolean, optional): Enable debug mode (default: false)
  - `timeout` (number, optional): Request timeout in milliseconds (default: 5000)
  - `baseUrl` (string, optional): Base URL for API calls (default: https://api.helloworld1.com)

**Return Value:**
- `Promise<HelloWorldInstance>`: A promise that resolves to a configured HelloWorld instance

**Examples:**

```javascript
// Basic initialization
const helloWorld = await init();

// With configuration
const helloWorld = await init({
  apiKey: 'your-api-key',
  debug: true,
  timeout: 10000
});

// With custom base URL
const helloWorld = await init({
  baseUrl: 'https://custom-api.example.com',
  apiKey: 'your-api-key'
});
```

**Error Handling:**
```javascript
try {
  const helloWorld = await init({ apiKey: 'invalid-key' });
} catch (error) {
  if (error.code === 'INVALID_API_KEY') {
    console.error('Please check your API key');
  } else if (error.code === 'NETWORK_ERROR') {
    console.error('Network connection failed');
  }
}
```

**Possible Errors:**
- `INVALID_API_KEY`: The provided API key is invalid
- `NETWORK_ERROR`: Network connection failed
- `TIMEOUT_ERROR`: Request timed out

**See Also:**
- [`configure()`](#configureoptions-object-void)
- [`destroy()`](#destroy-promisevoid)

---

### `configure(options: Object): void`

Updates the configuration of an existing HelloWorld instance.

**Purpose:**
Modifies configuration settings for an already initialized HelloWorld instance.

**Parameters:**
- `options` (Object, required): Configuration options to update
  - `debug` (boolean, optional): Enable/disable debug mode
  - `timeout` (number, optional): Update request timeout
  - `retries` (number, optional): Number of retry attempts (default: 3)

**Return Value:**
- `void`: No return value

**Examples:**

```javascript
// Enable debug mode
helloWorld.configure({ debug: true });

// Update timeout and retries
helloWorld.configure({
  timeout: 8000,
  retries: 5
});

// Multiple options
helloWorld.configure({
  debug: false,
  timeout: 3000,
  retries: 2
});
```

**Error Handling:**
```javascript
try {
  helloWorld.configure({ timeout: -1 });
} catch (error) {
  console.error('Invalid timeout value:', error.message);
}
```

**Possible Errors:**
- `INVALID_OPTION`: One or more options have invalid values
- `INSTANCE_NOT_INITIALIZED`: HelloWorld instance not initialized

---

### `destroy(): Promise<void>`

Cleanup and destroy a HelloWorld instance.

**Purpose:**
Properly cleanup resources, close connections, and destroy the HelloWorld instance.

**Parameters:**
None

**Return Value:**
- `Promise<void>`: A promise that resolves when cleanup is complete

**Examples:**

```javascript
// Basic destroy
await helloWorld.destroy();

// With error handling
try {
  await helloWorld.destroy();
  console.log('HelloWorld instance destroyed successfully');
} catch (error) {
  console.error('Error during cleanup:', error.message);
}
```

---

## 🛠️ Utility Functions

### `validateEmail(email: string): boolean`

Validates an email address format.

**Purpose:**
Checks if the provided email address follows a valid email format.

**Parameters:**
- `email` (string, required): The email address to validate

**Return Value:**
- `boolean`: `true` if email is valid, `false` otherwise

**Examples:**

```javascript
// Valid emails
console.log(validateEmail('user@example.com')); // true
console.log(validateEmail('test.email+tag@domain.co.uk')); // true

// Invalid emails
console.log(validateEmail('invalid-email')); // false
console.log(validateEmail('user@')); // false
console.log(validateEmail('')); // false
```

**Error Handling:**
```javascript
try {
  const isValid = validateEmail(null); // Throws error
} catch (error) {
  console.error('Email validation error:', error.message);
}
```

**Possible Errors:**
- `INVALID_INPUT`: Input is null, undefined, or not a string

---

### `formatDate(date: Date | string, format?: string): string`

Formats a date according to the specified format.

**Purpose:**
Converts a Date object or date string into a formatted string representation.

**Parameters:**
- `date` (Date | string, required): The date to format
- `format` (string, optional): Date format pattern (default: 'YYYY-MM-DD')

**Return Value:**
- `string`: Formatted date string

**Format Patterns:**
- `YYYY`: 4-digit year
- `MM`: 2-digit month
- `DD`: 2-digit day
- `HH`: 2-digit hour (24-hour)
- `mm`: 2-digit minute
- `ss`: 2-digit second

**Examples:**

```javascript
const date = new Date('2024-01-15T14:30:00Z');

// Default format
console.log(formatDate(date)); // '2024-01-15'

// Custom formats
console.log(formatDate(date, 'MM/DD/YYYY')); // '01/15/2024'
console.log(formatDate(date, 'DD-MM-YYYY HH:mm')); // '15-01-2024 14:30'

// String input
console.log(formatDate('2024-01-15', 'YYYY/MM/DD')); // '2024/01/15'
```

**Error Handling:**
```javascript
try {
  const formatted = formatDate('invalid-date');
} catch (error) {
  if (error.code === 'INVALID_DATE') {
    console.error('Invalid date provided');
  }
}
```

---

### `generateId(prefix?: string, length?: number): string`

Generates a unique identifier string.

**Purpose:**
Creates a unique identifier with optional prefix and custom length.

**Parameters:**
- `prefix` (string, optional): Prefix for the generated ID
- `length` (number, optional): Length of the random part (default: 8)

**Return Value:**
- `string`: Generated unique identifier

**Examples:**

```javascript
// Basic ID generation
console.log(generateId()); // 'a7b9c2d4'

// With prefix
console.log(generateId('user')); // 'user_e5f8a1b2'

// Custom length
console.log(generateId('order', 12)); // 'order_a1b2c3d4e5f6'

// Multiple IDs are unique
console.log(generateId('test')); // 'test_x9y8z7w6'
console.log(generateId('test')); // 'test_m5n4p3q2'
```

---

## ✅ Validation Functions

### `validateInput(input: any, schema: ValidationSchema): ValidationResult`

Validates input data against a schema.

**Purpose:**
Validates input data structure and types against a predefined schema.

**Parameters:**
- `input` (any, required): The data to validate
- `schema` (ValidationSchema, required): Validation schema object

**Return Value:**
- `ValidationResult`: Object containing validation results
  - `isValid` (boolean): Whether validation passed
  - `errors` (string[]): Array of validation error messages
  - `warnings` (string[]): Array of validation warnings

**Schema Properties:**
- `required` (string[]): Required field names
- `types` (Object): Field type definitions
- `constraints` (Object): Field constraints (min, max, pattern, etc.)

**Examples:**

```javascript
// Define validation schema
const userSchema = {
  required: ['name', 'email'],
  types: {
    name: 'string',
    email: 'string',
    age: 'number'
  },
  constraints: {
    name: { minLength: 2, maxLength: 50 },
    email: { pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/ },
    age: { min: 0, max: 120 }
  }
};

// Valid input
const validUser = {
  name: 'John Doe',
  email: 'john@example.com',
  age: 30
};

const result = validateInput(validUser, userSchema);
console.log(result.isValid); // true
console.log(result.errors); // []

// Invalid input
const invalidUser = {
  name: 'A', // Too short
  email: 'invalid-email', // Invalid format
  age: -5 // Below minimum
};

const invalidResult = validateInput(invalidUser, userSchema);
console.log(invalidResult.isValid); // false
console.log(invalidResult.errors); 
// ['name must be at least 2 characters', 'email format is invalid', 'age must be at least 0']
```

---

## ⚙️ Configuration Functions

### `getConfig(key?: string): any`

Retrieves configuration values.

**Purpose:**
Gets current configuration values, either all config or a specific key.

**Parameters:**
- `key` (string, optional): Specific configuration key to retrieve

**Return Value:**
- `any`: Configuration value(s) - object if no key specified, specific value if key provided

**Examples:**

```javascript
// Get all configuration
const allConfig = getConfig();
console.log(allConfig);
// { debug: true, timeout: 5000, apiKey: 'xxx', baseUrl: 'https://api.example.com' }

// Get specific configuration
const timeout = getConfig('timeout');
console.log(timeout); // 5000

const debug = getConfig('debug');
console.log(debug); // true

// Non-existent key
const missing = getConfig('nonexistent');
console.log(missing); // undefined
```

---

### `setConfig(key: string, value: any): void`
### `setConfig(config: Object): void`

Sets configuration values.

**Purpose:**
Updates configuration with new values, either single key-value or multiple values.

**Parameters:**
- `key` (string, required): Configuration key to set (single value version)
- `value` (any, required): Value to set (single value version)
- `config` (Object, required): Configuration object (bulk update version)

**Return Value:**
- `void`: No return value

**Examples:**

```javascript
// Set single value
setConfig('debug', false);
setConfig('timeout', 10000);

// Set multiple values
setConfig({
  debug: true,
  timeout: 8000,
  retries: 3
});

// Verify changes
console.log(getConfig('debug')); // true
console.log(getConfig('timeout')); // 8000
```

---

## 🎯 Event Handler Functions

### `addEventListener(event: string, handler: Function): string`

Adds an event listener.

**Purpose:**
Registers an event handler function for specific events.

**Parameters:**
- `event` (string, required): Event name to listen for
- `handler` (Function, required): Function to call when event occurs

**Return Value:**
- `string`: Unique listener ID for removing the listener later

**Examples:**

```javascript
// Add event listener
const listenerId = addEventListener('dataUpdate', (data) => {
  console.log('Data updated:', data);
});

// Add multiple listeners
const errorListenerId = addEventListener('error', (error) => {
  console.error('Error occurred:', error.message);
});

const successListenerId = addEventListener('success', (result) => {
  console.log('Operation successful:', result);
});
```

---

### `removeEventListener(listenerId: string): boolean`

Removes an event listener.

**Purpose:**
Unregisters a previously added event listener using its ID.

**Parameters:**
- `listenerId` (string, required): The listener ID returned by addEventListener

**Return Value:**
- `boolean`: `true` if listener was found and removed, `false` otherwise

**Examples:**

```javascript
// Remove specific listener
const removed = removeEventListener(listenerId);
console.log('Listener removed:', removed); // true

// Try to remove non-existent listener
const notRemoved = removeEventListener('invalid-id');
console.log('Listener removed:', notRemoved); // false
```

---

### `emitEvent(event: string, data?: any): void`

Emits an event to all registered listeners.

**Purpose:**
Triggers an event, calling all registered handlers for that event.

**Parameters:**
- `event` (string, required): Event name to emit
- `data` (any, optional): Data to pass to event handlers

**Return Value:**
- `void`: No return value

**Examples:**

```javascript
// Emit event without data
emitEvent('userLoggedOut');

// Emit event with data
emitEvent('dataUpdate', {
  type: 'user',
  id: 'user_123',
  changes: ['name', 'email']
});

// Emit error event
emitEvent('error', {
  code: 'VALIDATION_ERROR',
  message: 'Invalid input provided',
  field: 'email'
});
```

---

## 🔍 Advanced Usage Examples

### Chaining Functions

```javascript
// Initialize and configure in one chain
const helloWorld = await init({ debug: true })
  .then(instance => {
    instance.configure({ timeout: 8000 });
    return instance;
  });

// Validation with formatted output
const validationResult = validateInput(userData, schema);
if (!validationResult.isValid) {
  const timestamp = formatDate(new Date(), 'YYYY-MM-DD HH:mm:ss');
  console.error(`[${timestamp}] Validation failed:`, validationResult.errors);
}
```

### Error Handling Best Practices

```javascript
// Comprehensive error handling
async function safeInit(config) {
  try {
    const instance = await init(config);
    
    // Set up error event listener
    addEventListener('error', (error) => {
      console.error(`[${formatDate(new Date())}] Error:`, error.message);
    });
    
    return instance;
  } catch (error) {
    console.error('Initialization failed:', error.message);
    throw error;
  }
}

// Use with proper cleanup
const helloWorld = await safeInit({ apiKey: 'your-key' });
try {
  // Use the instance
} finally {
  await helloWorld.destroy();
}
```

---

## 📚 Function Reference Summary

| Function | Purpose | Parameters | Return Type |
|----------|---------|------------|-------------|
| `init()` | Initialize HelloWorld instance | `config?` | `Promise<HelloWorldInstance>` |
| `configure()` | Update configuration | `options` | `void` |
| `destroy()` | Cleanup instance | None | `Promise<void>` |
| `validateEmail()` | Validate email format | `email` | `boolean` |
| `formatDate()` | Format date string | `date, format?` | `string` |
| `generateId()` | Generate unique ID | `prefix?, length?` | `string` |
| `validateInput()` | Validate data against schema | `input, schema` | `ValidationResult` |
| `getConfig()` | Get configuration values | `key?` | `any` |
| `setConfig()` | Set configuration values | `key, value` or `config` | `void` |
| `addEventListener()` | Add event listener | `event, handler` | `string` |
| `removeEventListener()` | Remove event listener | `listenerId` | `boolean` |
| `emitEvent()` | Emit event | `event, data?` | `void` |

---

For implementation details and source code, see the individual function files in this directory.