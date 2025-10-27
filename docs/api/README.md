# API Documentation

This section provides comprehensive documentation for all public APIs in HelloWorld1.

## 📋 Table of Contents

- [Authentication](#authentication)
- [Base URL & Versioning](#base-url--versioning)
- [Request/Response Format](#requestresponse-format)
- [Error Handling](#error-handling)
- [Rate Limiting](#rate-limiting)
- [API Endpoints](#api-endpoints)
- [SDK Integration](#sdk-integration)

## 🔐 Authentication

### API Key Authentication
```javascript
// Include API key in headers
const headers = {
  'Authorization': 'Bearer YOUR_API_KEY',
  'Content-Type': 'application/json'
};
```

### JWT Token Authentication
```javascript
// Include JWT token in headers
const headers = {
  'Authorization': 'Bearer JWT_TOKEN',
  'Content-Type': 'application/json'
};
```

## 🌐 Base URL & Versioning

```
Base URL: https://api.helloworld1.com/v1
Current Version: v1
```

All API endpoints are versioned. Include the version in the URL path.

## 📨 Request/Response Format

### Request Format
All requests should include:
- `Content-Type: application/json` header
- Valid JSON body (for POST/PUT requests)
- Authentication headers

### Response Format
```json
{
  "success": true,
  "data": {
    // Response data here
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "version": "1.0.0"
  }
}
```

### Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request data is invalid",
    "details": {
      "field": "email",
      "reason": "Invalid email format"
    }
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "request_id": "req_123456789"
  }
}
```

## ⚠️ Error Handling

### HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Validation Error |
| 429 | Rate Limit Exceeded |
| 500 | Internal Server Error |

### Error Codes

| Error Code | Description | Solution |
|------------|-------------|----------|
| `INVALID_API_KEY` | API key is missing or invalid | Check your API key |
| `VALIDATION_ERROR` | Request data validation failed | Fix the invalid fields |
| `RATE_LIMIT_EXCEEDED` | Too many requests | Wait before retrying |
| `RESOURCE_NOT_FOUND` | Requested resource doesn't exist | Check the resource ID |

## 🚦 Rate Limiting

- **Rate Limit**: 1000 requests per hour per API key
- **Headers**: Check `X-RateLimit-Limit` and `X-RateLimit-Remaining` headers
- **Reset**: Rate limits reset every hour

```javascript
// Example rate limit headers
{
  "X-RateLimit-Limit": "1000",
  "X-RateLimit-Remaining": "999",
  "X-RateLimit-Reset": "1640995200"
}
```

## 🛠️ API Endpoints

### Users API

#### Get User Profile
```http
GET /users/{user_id}
```

**Parameters:**
- `user_id` (string, required): The unique user identifier

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "user_123",
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```javascript
const response = await fetch('https://api.helloworld1.com/v1/users/user_123', {
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY'
  }
});
const userData = await response.json();
```

#### Create User
```http
POST /users
```

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "secure_password"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "user_123",
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```javascript
const response = await fetch('https://api.helloworld1.com/v1/users', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'John Doe',
    email: 'john@example.com',
    password: 'secure_password'
  })
});
const newUser = await response.json();
```

#### Update User
```http
PUT /users/{user_id}
```

**Parameters:**
- `user_id` (string, required): The unique user identifier

**Request Body:**
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

**Example:**
```javascript
const response = await fetch('https://api.helloworld1.com/v1/users/user_123', {
  method: 'PUT',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'Jane Doe',
    email: 'jane@example.com'
  })
});
```

#### Delete User
```http
DELETE /users/{user_id}
```

**Parameters:**
- `user_id` (string, required): The unique user identifier

**Response:**
```json
{
  "success": true,
  "data": {
    "message": "User deleted successfully"
  }
}
```

### Data API

#### Get Data List
```http
GET /data?page=1&limit=10&sort=created_at&order=desc
```

**Query Parameters:**
- `page` (integer, optional): Page number (default: 1)
- `limit` (integer, optional): Items per page (default: 10, max: 100)
- `sort` (string, optional): Sort field (default: created_at)
- `order` (string, optional): Sort order - asc/desc (default: desc)
- `filter` (string, optional): Filter criteria

**Response:**
```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "data_123",
        "title": "Sample Data",
        "value": 42,
        "created_at": "2024-01-01T00:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 100,
      "total_pages": 10
    }
  }
}
```

## 📦 SDK Integration

### JavaScript/Node.js SDK

```javascript
import { HelloWorld1API } from 'helloworld1-sdk';

const api = new HelloWorld1API({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://api.helloworld1.com/v1'
});

// Get user
const user = await api.users.get('user_123');

// Create user
const newUser = await api.users.create({
  name: 'John Doe',
  email: 'john@example.com'
});

// Get data with pagination
const data = await api.data.list({
  page: 1,
  limit: 20,
  sort: 'created_at'
});
```

### Python SDK

```python
from helloworld1 import HelloWorld1API

api = HelloWorld1API(
    api_key='YOUR_API_KEY',
    base_url='https://api.helloworld1.com/v1'
)

# Get user
user = api.users.get('user_123')

# Create user
new_user = api.users.create({
    'name': 'John Doe',
    'email': 'john@example.com'
})

# Get data with pagination
data = api.data.list(page=1, limit=20, sort='created_at')
```

## 🔍 Testing

### Using curl

```bash
# Get user
curl -X GET \
  'https://api.helloworld1.com/v1/users/user_123' \
  -H 'Authorization: Bearer YOUR_API_KEY'

# Create user
curl -X POST \
  'https://api.helloworld1.com/v1/users' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "secure_password"
  }'
```

### Using Postman

1. Import our [Postman Collection](./postman/HelloWorld1.postman_collection.json)
2. Set your API key in the collection variables
3. Run the requests

---

For more specific endpoint documentation, see the individual API reference files in this directory.