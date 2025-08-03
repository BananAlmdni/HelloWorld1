# Examples & Tutorials

This section provides comprehensive examples and tutorials for using HelloWorld1 in various scenarios.

## 📋 Table of Contents

- [Quick Start Guide](#quick-start-guide)
- [Basic Examples](#basic-examples)
- [Advanced Use Cases](#advanced-use-cases)
- [Integration Tutorials](#integration-tutorials)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start Guide

### Installation

```bash
# Using npm
npm install helloworld1

# Using yarn
yarn add helloworld1

# Using pnpm
pnpm add helloworld1
```

### Basic Setup

**JavaScript/Node.js:**
```javascript
// ES6 imports
import { HelloWorld1, init } from 'helloworld1';

// CommonJS
const { HelloWorld1, init } = require('helloworld1');

// Initialize
const app = await init({
  apiKey: 'your-api-key',
  debug: true
});
```

**TypeScript:**
```typescript
import { HelloWorld1, init, Config } from 'helloworld1';

const config: Config = {
  apiKey: 'your-api-key',
  debug: process.env.NODE_ENV === 'development',
  timeout: 5000
};

const app = await init(config);
```

**React:**
```jsx
import React, { useState, useEffect } from 'react';
import { HelloWorld1Provider, useHelloWorld } from 'helloworld1/react';

function App() {
  return (
    <HelloWorld1Provider apiKey="your-api-key">
      <MyComponent />
    </HelloWorld1Provider>
  );
}

function MyComponent() {
  const { init, loading, error } = useHelloWorld();
  
  useEffect(() => {
    init();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return <div>HelloWorld1 is ready!</div>;
}
```

**Vue 3:**
```vue
<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error.message }}</div>
    <div v-else>HelloWorld1 is ready!</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { init } from 'helloworld1';

const loading = ref(true);
const error = ref(null);
const app = ref(null);

onMounted(async () => {
  try {
    app.value = await init({
      apiKey: 'your-api-key'
    });
  } catch (err) {
    error.value = err;
  } finally {
    loading.value = false;
  }
});
</script>
```

---

## 📚 Basic Examples

### Example 1: User Management System

A complete example showing user creation, editing, and display.

**React Implementation:**
```jsx
import React, { useState, useEffect } from 'react';
import { 
  HelloButton, 
  HelloInput, 
  HelloForm, 
  HelloTable, 
  HelloModal,
  notification 
} from 'helloworld1/react';

function UserManagement() {
  const [users, setUsers] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingUser, setEditingUser] = useState(null);
  const [loading, setLoading] = useState(false);

  // Load users on component mount
  useEffect(() => {
    loadUsers();
  }, []);

  const loadUsers = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/users');
      const userData = await response.json();
      setUsers(userData);
    } catch (error) {
      notification.error('Failed to load users');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateUser = () => {
    setEditingUser(null);
    setModalOpen(true);
  };

  const handleEditUser = (user) => {
    setEditingUser(user);
    setModalOpen(true);
  };

  const handleDeleteUser = async (userId) => {
    try {
      await fetch(`/api/users/${userId}`, { method: 'DELETE' });
      setUsers(users.filter(u => u.id !== userId));
      notification.success('User deleted successfully');
    } catch (error) {
      notification.error('Failed to delete user');
    }
  };

  const handleSaveUser = async (userData) => {
    try {
      const method = editingUser ? 'PUT' : 'POST';
      const url = editingUser ? `/api/users/${editingUser.id}` : '/api/users';
      
      const response = await fetch(url, {
        method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData)
      });
      
      const savedUser = await response.json();
      
      if (editingUser) {
        setUsers(users.map(u => u.id === savedUser.id ? savedUser : u));
        notification.success('User updated successfully');
      } else {
        setUsers([...users, savedUser]);
        notification.success('User created successfully');
      }
      
      setModalOpen(false);
    } catch (error) {
      notification.error('Failed to save user');
    }
  };

  const columns = [
    {
      key: 'id',
      title: 'ID',
      width: 80,
      sortable: true
    },
    {
      key: 'name',
      title: 'Name',
      sortable: true,
      filterable: true
    },
    {
      key: 'email',
      title: 'Email',
      sortable: true,
      filterable: true
    },
    {
      key: 'role',
      title: 'Role',
      filterable: true,
      filter: {
        type: 'select',
        options: [
          { label: 'Admin', value: 'admin' },
          { label: 'User', value: 'user' },
          { label: 'Guest', value: 'guest' }
        ]
      }
    },
    {
      key: 'actions',
      title: 'Actions',
      width: 150,
      align: 'center',
      render: (_, user) => (
        <div style={{ display: 'flex', gap: '8px' }}>
          <HelloButton 
            size="small" 
            onClick={() => handleEditUser(user)}
          >
            Edit
          </HelloButton>
          <HelloButton 
            size="small" 
            variant="danger" 
            onClick={() => handleDeleteUser(user.id)}
          >
            Delete
          </HelloButton>
        </div>
      )
    }
  ];

  const userSchema = {
    required: ['name', 'email'],
    types: {
      name: 'string',
      email: 'string',
      role: 'string'
    },
    constraints: {
      name: { minLength: 2, maxLength: 50 },
      email: { pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/ }
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <div style={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center',
        marginBottom: '20px' 
      }}>
        <h1>User Management</h1>
        <HelloButton 
          variant="primary" 
          icon="plus"
          onClick={handleCreateUser}
        >
          Create User
        </HelloButton>
      </div>

      <HelloTable
        data={users}
        columns={columns}
        loading={loading}
        sortable
        filterable
        pagination={{
          pageSize: 10,
          showSizeChanger: true
        }}
      />

      <HelloModal
        open={modalOpen}
        title={editingUser ? 'Edit User' : 'Create User'}
        onClose={() => setModalOpen(false)}
        size="medium"
      >
        <HelloForm
          schema={userSchema}
          initialValues={editingUser || { name: '', email: '', role: 'user' }}
          onSubmit={({ values }) => handleSaveUser(values)}
        >
          {({ values, errors, isValid, isSubmitting }) => (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              <HelloInput
                name="name"
                label="Full Name"
                value={values.name}
                error={errors.name}
                placeholder="Enter full name"
                required
              />
              
              <HelloInput
                name="email"
                type="email"
                label="Email Address"
                value={values.email}
                error={errors.email}
                placeholder="Enter email address"
                required
              />
              
              <HelloInput
                name="role"
                type="select"
                label="Role"
                value={values.role}
                options={[
                  { label: 'User', value: 'user' },
                  { label: 'Admin', value: 'admin' },
                  { label: 'Guest', value: 'guest' }
                ]}
              />
              
              <div style={{ 
                display: 'flex', 
                gap: '12px', 
                justifyContent: 'flex-end',
                marginTop: '20px' 
              }}>
                <HelloButton 
                  variant="ghost" 
                  onClick={() => setModalOpen(false)}
                >
                  Cancel
                </HelloButton>
                <HelloButton 
                  type="submit"
                  variant="primary"
                  loading={isSubmitting}
                  disabled={!isValid}
                >
                  {editingUser ? 'Update' : 'Create'}
                </HelloButton>
              </div>
            </div>
          )}
        </HelloForm>
      </HelloModal>
    </div>
  );
}

export default UserManagement;
```

### Example 2: Data Dashboard

A dashboard showing data visualization and real-time updates.

```jsx
import React, { useState, useEffect } from 'react';
import { 
  HelloGrid, 
  HelloGridItem, 
  HelloCard, 
  HelloChart,
  HelloButton,
  HelloSelect,
  notification 
} from 'helloworld1/react';

function Dashboard() {
  const [timeRange, setTimeRange] = useState('7d');
  const [data, setData] = useState({
    metrics: [],
    charts: [],
    loading: true
  });

  useEffect(() => {
    loadDashboardData();
    
    // Set up real-time updates
    const interval = setInterval(loadDashboardData, 30000);
    return () => clearInterval(interval);
  }, [timeRange]);

  const loadDashboardData = async () => {
    try {
      const response = await fetch(`/api/dashboard?range=${timeRange}`);
      const dashboardData = await response.json();
      setData({ ...dashboardData, loading: false });
    } catch (error) {
      notification.error('Failed to load dashboard data');
      setData(prev => ({ ...prev, loading: false }));
    }
  };

  const handleExport = async () => {
    try {
      const response = await fetch('/api/dashboard/export', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ timeRange, format: 'csv' })
      });
      
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `dashboard-${timeRange}.csv`;
      a.click();
      
      notification.success('Dashboard data exported successfully');
    } catch (error) {
      notification.error('Failed to export data');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <div style={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center',
        marginBottom: '20px' 
      }}>
        <h1>Dashboard</h1>
        <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
          <HelloSelect
            value={timeRange}
            onChange={setTimeRange}
            options={[
              { label: 'Last 24 hours', value: '1d' },
              { label: 'Last 7 days', value: '7d' },
              { label: 'Last 30 days', value: '30d' },
              { label: 'Last 90 days', value: '90d' }
            ]}
          />
          <HelloButton 
            variant="ghost" 
            icon="download"
            onClick={handleExport}
          >
            Export
          </HelloButton>
        </div>
      </div>

      <HelloGrid columns={{ xs: 1, sm: 2, lg: 4 }} gap="20px">
        {data.metrics.map((metric, index) => (
          <HelloGridItem key={index}>
            <HelloCard>
              <div style={{ textAlign: 'center' }}>
                <h3 style={{ margin: '0 0 8px 0', color: '#666' }}>
                  {metric.title}
                </h3>
                <div style={{ 
                  fontSize: '2rem', 
                  fontWeight: 'bold',
                  color: metric.trend > 0 ? '#28a745' : '#dc3545'
                }}>
                  {metric.value}
                </div>
                <div style={{ 
                  fontSize: '0.875rem', 
                  color: metric.trend > 0 ? '#28a745' : '#dc3545' 
                }}>
                  {metric.trend > 0 ? '↗' : '↘'} {Math.abs(metric.trend)}%
                </div>
              </div>
            </HelloCard>
          </HelloGridItem>
        ))}
      </HelloGrid>

      <HelloGrid columns={{ xs: 1, lg: 2 }} gap="20px" style={{ marginTop: '20px' }}>
        {data.charts.map((chart, index) => (
          <HelloGridItem key={index}>
            <HelloCard title={chart.title}>
              <HelloChart
                type={chart.type}
                data={chart.data}
                options={chart.options}
                loading={data.loading}
              />
            </HelloCard>
          </HelloGridItem>
        ))}
      </HelloGrid>
    </div>
  );
}

export default Dashboard;
```

---

## 🎯 Advanced Use Cases

### Use Case 1: Real-time Chat Application

```jsx
import React, { useState, useEffect, useRef } from 'react';
import { 
  HelloInput, 
  HelloButton, 
  HelloCard,
  HelloAvatar,
  useWebSocket,
  formatDate 
} from 'helloworld1/react';

function ChatApp() {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [typing, setTyping] = useState([]);
  const messagesEndRef = useRef(null);
  
  const { 
    connected, 
    send, 
    subscribe, 
    unsubscribe 
  } = useWebSocket('ws://localhost:8080/chat');

  useEffect(() => {
    // Subscribe to chat events
    const unsubscribeMessage = subscribe('message', (message) => {
      setMessages(prev => [...prev, message]);
    });
    
    const unsubscribeTyping = subscribe('typing', (data) => {
      setTyping(data.users);
    });
    
    const unsubscribeUserJoined = subscribe('user_joined', (data) => {
      setMessages(prev => [...prev, {
        id: Date.now(),
        type: 'system',
        content: `${data.user.name} joined the chat`,
        timestamp: new Date()
      }]);
    });

    return () => {
      unsubscribeMessage();
      unsubscribeTyping();
      unsubscribeUserJoined();
    };
  }, [subscribe]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSendMessage = () => {
    if (!newMessage.trim() || !connected) return;
    
    send('message', {
      content: newMessage,
      timestamp: new Date()
    });
    
    setNewMessage('');
  };

  const handleTyping = (value) => {
    setNewMessage(value);
    
    if (connected) {
      send('typing', { isTyping: value.length > 0 });
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div style={{ 
      height: '100vh', 
      display: 'flex', 
      flexDirection: 'column',
      maxWidth: '800px',
      margin: '0 auto',
      padding: '20px'
    }}>
      <HelloCard 
        title="Chat Room" 
        style={{ 
          flex: 1, 
          display: 'flex', 
          flexDirection: 'column',
          overflow: 'hidden' 
        }}
      >
        <div style={{ 
          flex: 1, 
          overflowY: 'auto', 
          padding: '16px',
          borderBottom: '1px solid #eee'
        }}>
          {messages.map((message) => (
            <div key={message.id} style={{ marginBottom: '16px' }}>
              {message.type === 'system' ? (
                <div style={{ 
                  textAlign: 'center', 
                  color: '#666',
                  fontStyle: 'italic' 
                }}>
                  {message.content}
                </div>
              ) : (
                <div style={{ display: 'flex', gap: '12px' }}>
                  <HelloAvatar 
                    src={message.user.avatar} 
                    name={message.user.name}
                    size="small"
                  />
                  <div style={{ flex: 1 }}>
                    <div style={{ 
                      display: 'flex', 
                      gap: '8px', 
                      alignItems: 'center',
                      marginBottom: '4px' 
                    }}>
                      <strong>{message.user.name}</strong>
                      <span style={{ 
                        fontSize: '0.75rem', 
                        color: '#666' 
                      }}>
                        {formatDate(message.timestamp, 'HH:mm')}
                      </span>
                    </div>
                    <div>{message.content}</div>
                  </div>
                </div>
              )}
            </div>
          ))}
          
          {typing.length > 0 && (
            <div style={{ 
              color: '#666', 
              fontStyle: 'italic',
              fontSize: '0.875rem' 
            }}>
              {typing.join(', ')} {typing.length === 1 ? 'is' : 'are'} typing...
            </div>
          )}
          
          <div ref={messagesEndRef} />
        </div>
        
        <div style={{ 
          padding: '16px', 
          display: 'flex', 
          gap: '12px' 
        }}>
          <HelloInput
            value={newMessage}
            onChange={handleTyping}
            onKeyPress={handleKeyPress}
            placeholder={connected ? "Type a message..." : "Connecting..."}
            disabled={!connected}
            multiline
            rows={2}
            style={{ flex: 1 }}
          />
          <HelloButton
            variant="primary"
            onClick={handleSendMessage}
            disabled={!connected || !newMessage.trim()}
            icon="send"
          >
            Send
          </HelloButton>
        </div>
      </HelloCard>
    </div>
  );
}

export default ChatApp;
```

### Use Case 2: E-commerce Product Catalog

```jsx
import React, { useState, useEffect } from 'react';
import { 
  HelloGrid, 
  HelloGridItem, 
  HelloCard, 
  HelloButton,
  HelloInput,
  HelloSelect,
  HelloPagination,
  HelloBadge,
  HelloRating,
  notification 
} from 'helloworld1/react';

function ProductCatalog() {
  const [products, setProducts] = useState([]);
  const [filters, setFilters] = useState({
    search: '',
    category: '',
    priceRange: '',
    sortBy: 'name'
  });
  const [pagination, setPagination] = useState({
    page: 1,
    pageSize: 12,
    total: 0
  });
  const [loading, setLoading] = useState(false);
  const [cart, setCart] = useState([]);

  useEffect(() => {
    loadProducts();
  }, [filters, pagination.page]);

  const loadProducts = async () => {
    setLoading(true);
    try {
      const params = new URLSearchParams({
        ...filters,
        page: pagination.page,
        pageSize: pagination.pageSize
      });
      
      const response = await fetch(`/api/products?${params}`);
      const data = await response.json();
      
      setProducts(data.products);
      setPagination(prev => ({ ...prev, total: data.total }));
    } catch (error) {
      notification.error('Failed to load products');
    } finally {
      setLoading(false);
    }
  };

  const handleAddToCart = (product) => {
    const existingItem = cart.find(item => item.id === product.id);
    
    if (existingItem) {
      setCart(cart.map(item => 
        item.id === product.id 
          ? { ...item, quantity: item.quantity + 1 }
          : item
      ));
    } else {
      setCart([...cart, { ...product, quantity: 1 }]);
    }
    
    notification.success(`${product.name} added to cart`);
  };

  const handleFilterChange = (key, value) => {
    setFilters(prev => ({ ...prev, [key]: value }));
    setPagination(prev => ({ ...prev, page: 1 }));
  };

  const categories = [
    { label: 'All Categories', value: '' },
    { label: 'Electronics', value: 'electronics' },
    { label: 'Clothing', value: 'clothing' },
    { label: 'Books', value: 'books' },
    { label: 'Home & Garden', value: 'home' }
  ];

  const sortOptions = [
    { label: 'Name A-Z', value: 'name' },
    { label: 'Price Low-High', value: 'price_asc' },
    { label: 'Price High-Low', value: 'price_desc' },
    { label: 'Rating', value: 'rating' },
    { label: 'Newest', value: 'created_desc' }
  ];

  return (
    <div style={{ padding: '20px' }}>
      <div style={{ marginBottom: '24px' }}>
        <h1>Product Catalog</h1>
        
        <HelloGrid columns={{ xs: 1, sm: 2, md: 4 }} gap="16px" style={{ marginTop: '16px' }}>
          <HelloGridItem>
            <HelloInput
              placeholder="Search products..."
              value={filters.search}
              onChange={(value) => handleFilterChange('search', value)}
              icon="search"
            />
          </HelloGridItem>
          
          <HelloGridItem>
            <HelloSelect
              placeholder="Category"
              value={filters.category}
              onChange={(value) => handleFilterChange('category', value)}
              options={categories}
            />
          </HelloGridItem>
          
          <HelloGridItem>
            <HelloSelect
              placeholder="Price Range"
              value={filters.priceRange}
              onChange={(value) => handleFilterChange('priceRange', value)}
              options={[
                { label: 'Any Price', value: '' },
                { label: 'Under $25', value: '0-25' },
                { label: '$25-$50', value: '25-50' },
                { label: '$50-$100', value: '50-100' },
                { label: 'Over $100', value: '100+' }
              ]}
            />
          </HelloGridItem>
          
          <HelloGridItem>
            <HelloSelect
              placeholder="Sort by"
              value={filters.sortBy}
              onChange={(value) => handleFilterChange('sortBy', value)}
              options={sortOptions}
            />
          </HelloGridItem>
        </HelloGrid>
      </div>

      <HelloGrid columns={{ xs: 1, sm: 2, md: 3, lg: 4 }} gap="20px">
        {products.map((product) => (
          <HelloGridItem key={product.id}>
            <HelloCard style={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
              <div style={{ position: 'relative', marginBottom: '12px' }}>
                <img 
                  src={product.image} 
                  alt={product.name}
                  style={{ 
                    width: '100%', 
                    height: '200px', 
                    objectFit: 'cover',
                    borderRadius: '4px'
                  }}
                />
                {product.onSale && (
                  <HelloBadge 
                    color="danger"
                    style={{ 
                      position: 'absolute', 
                      top: '8px', 
                      right: '8px' 
                    }}
                  >
                    Sale
                  </HelloBadge>
                )}
              </div>
              
              <div style={{ flex: 1 }}>
                <h3 style={{ 
                  margin: '0 0 8px 0', 
                  fontSize: '1rem',
                  lineHeight: '1.4'
                }}>
                  {product.name}
                </h3>
                
                <div style={{ 
                  display: 'flex', 
                  alignItems: 'center', 
                  gap: '8px',
                  marginBottom: '8px'
                }}>
                  <HelloRating 
                    value={product.rating} 
                    readonly 
                    size="small"
                  />
                  <span style={{ fontSize: '0.875rem', color: '#666' }}>
                    ({product.reviewCount})
                  </span>
                </div>
                
                <p style={{ 
                  margin: '0 0 12px 0', 
                  color: '#666',
                  fontSize: '0.875rem',
                  lineHeight: '1.4'
                }}>
                  {product.description}
                </p>
                
                <div style={{ 
                  display: 'flex', 
                  justifyContent: 'space-between', 
                  alignItems: 'center',
                  marginBottom: '12px'
                }}>
                  <div>
                    {product.onSale ? (
                      <div>
                        <span style={{ 
                          fontSize: '1.125rem', 
                          fontWeight: 'bold',
                          color: '#dc3545'
                        }}>
                          ${product.salePrice}
                        </span>
                        <span style={{ 
                          fontSize: '0.875rem', 
                          textDecoration: 'line-through',
                          color: '#666',
                          marginLeft: '8px'
                        }}>
                          ${product.price}
                        </span>
                      </div>
                    ) : (
                      <span style={{ 
                        fontSize: '1.125rem', 
                        fontWeight: 'bold'
                      }}>
                        ${product.price}
                      </span>
                    )}
                  </div>
                  
                  <HelloBadge 
                    color={product.stock > 10 ? 'success' : product.stock > 0 ? 'warning' : 'danger'}
                  >
                    {product.stock > 0 ? `${product.stock} in stock` : 'Out of stock'}
                  </HelloBadge>
                </div>
              </div>
              
              <HelloButton
                variant="primary"
                fullWidth
                disabled={product.stock === 0}
                onClick={() => handleAddToCart(product)}
                icon="cart"
              >
                {product.stock > 0 ? 'Add to Cart' : 'Out of Stock'}
              </HelloButton>
            </HelloCard>
          </HelloGridItem>
        ))}
      </HelloGrid>

      {products.length === 0 && !loading && (
        <div style={{ 
          textAlign: 'center', 
          padding: '40px',
          color: '#666'
        }}>
          No products found. Try adjusting your filters.
        </div>
      )}

      {pagination.total > pagination.pageSize && (
        <div style={{ 
          display: 'flex', 
          justifyContent: 'center', 
          marginTop: '32px' 
        }}>
          <HelloPagination
            current={pagination.page}
            pageSize={pagination.pageSize}
            total={pagination.total}
            onChange={(page) => setPagination(prev => ({ ...prev, page }))}
            showSizeChanger
            showQuickJumper
          />
        </div>
      )}

      {cart.length > 0 && (
        <div style={{ 
          position: 'fixed', 
          bottom: '20px', 
          right: '20px' 
        }}>
          <HelloButton 
            variant="primary" 
            size="large"
            icon="cart"
            onClick={() => console.log('Open cart:', cart)}
          >
            Cart ({cart.reduce((sum, item) => sum + item.quantity, 0)})
          </HelloButton>
        </div>
      )}
    </div>
  );
}

export default ProductCatalog;
```

---

## 🔧 Integration Tutorials

### Tutorial 1: Setting up with Next.js

**Step 1: Installation**
```bash
npm install helloworld1 next react react-dom
```

**Step 2: Configuration (next.config.js)**
```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  transpilePackages: ['helloworld1'],
}

module.exports = nextConfig
```

**Step 3: Provider Setup (app/layout.js)**
```jsx
'use client';
import { HelloWorld1Provider } from 'helloworld1/react';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <HelloWorld1Provider 
          apiKey={process.env.NEXT_PUBLIC_HW1_API_KEY}
          baseUrl={process.env.NEXT_PUBLIC_HW1_BASE_URL}
        >
          {children}
        </HelloWorld1Provider>
      </body>
    </html>
  );
}
```

**Step 4: Using in Pages (app/page.js)**
```jsx
'use client';
import { HelloButton, HelloCard } from 'helloworld1/react';

export default function Home() {
  return (
    <main>
      <HelloCard title="Welcome to HelloWorld1">
        <p>Your Next.js app is ready!</p>
        <HelloButton variant="primary">
          Get Started
        </HelloButton>
      </HelloCard>
    </main>
  );
}
```

### Tutorial 2: Express.js Backend Integration

**Step 1: Setup**
```bash
npm install helloworld1 express cors helmet
```

**Step 2: Server Configuration (server.js)**
```javascript
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const { HelloWorld1 } = require('helloworld1');

const app = express();
const port = process.env.PORT || 3001;

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Initialize HelloWorld1
const hw1 = new HelloWorld1({
  apiKey: process.env.HW1_API_KEY,
  environment: process.env.NODE_ENV
});

// Routes
app.get('/api/users', async (req, res) => {
  try {
    const users = await hw1.users.list(req.query);
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/api/users', async (req, res) => {
  try {
    const user = await hw1.users.create(req.body);
    res.status(201).json(user);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

---

## 💡 Best Practices

### Performance Optimization

**1. Lazy Loading Components**
```jsx
import { lazy, Suspense } from 'react';

const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}
```

**2. Memoization**
```jsx
import { memo, useMemo, useCallback } from 'react';

const ExpensiveComponent = memo(({ data, onUpdate }) => {
  const processedData = useMemo(() => {
    return data.map(item => ({
      ...item,
      computed: expensiveCalculation(item)
    }));
  }, [data]);

  const handleUpdate = useCallback((id, changes) => {
    onUpdate(id, changes);
  }, [onUpdate]);

  return (
    <div>
      {processedData.map(item => (
        <div key={item.id} onClick={() => handleUpdate(item.id, {})}>
          {item.name}
        </div>
      ))}
    </div>
  );
});
```

**3. Virtual Scrolling for Large Lists**
```jsx
import { HelloVirtualList } from 'helloworld1/react';

function LargeList({ items }) {
  const renderItem = ({ index, style }) => (
    <div style={style}>
      <ItemComponent data={items[index]} />
    </div>
  );

  return (
    <HelloVirtualList
      height={400}
      itemCount={items.length}
      itemSize={50}
      renderItem={renderItem}
    />
  );
}
```

### Error Handling

**1. Error Boundaries**
```jsx
import { HelloErrorBoundary } from 'helloworld1/react';

function App() {
  return (
    <HelloErrorBoundary
      fallback={({ error, resetError }) => (
        <div>
          <h2>Something went wrong:</h2>
          <pre>{error.message}</pre>
          <button onClick={resetError}>Try again</button>
        </div>
      )}
    >
      <MyComponent />
    </HelloErrorBoundary>
  );
}
```

**2. Async Error Handling**
```jsx
import { useAsync } from 'helloworld1/react';

function DataComponent() {
  const {
    data,
    error,
    loading,
    execute
  } = useAsync(async () => {
    const response = await fetch('/api/data');
    if (!response.ok) throw new Error('Failed to fetch');
    return response.json();
  });

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return <div>{data?.message}</div>;
}
```

### Security Best Practices

**1. Input Validation**
```jsx
import { validateInput } from 'helloworld1';

const userSchema = {
  required: ['email', 'password'],
  types: {
    email: 'string',
    password: 'string'
  },
  constraints: {
    email: { 
      pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
      maxLength: 255
    },
    password: { 
      minLength: 8,
      pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/
    }
  }
};

function LoginForm() {
  const handleSubmit = (data) => {
    const validation = validateInput(data, userSchema);
    
    if (!validation.isValid) {
      console.error('Validation errors:', validation.errors);
      return;
    }
    
    // Proceed with login
  };
}
```

**2. XSS Prevention**
```jsx
import { sanitizeHtml } from 'helloworld1';

function UserContent({ content }) {
  const safeContent = sanitizeHtml(content, {
    allowedTags: ['p', 'br', 'strong', 'em'],
    allowedAttributes: {}
  });

  return (
    <div dangerouslySetInnerHTML={{ __html: safeContent }} />
  );
}
```

---

## 🐛 Troubleshooting

### Common Issues

**1. Component Not Rendering**
```jsx
// ❌ Wrong - Missing provider
function App() {
  return <HelloButton>Click me</HelloButton>;
}

// ✅ Correct - With provider
function App() {
  return (
    <HelloWorld1Provider apiKey="your-key">
      <HelloButton>Click me</HelloButton>
    </HelloWorld1Provider>
  );
}
```

**2. API Call Failures**
```javascript
// ❌ Wrong - No error handling
const data = await fetch('/api/data').then(r => r.json());

// ✅ Correct - With error handling
try {
  const response = await fetch('/api/data');
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }
  const data = await response.json();
} catch (error) {
  console.error('API call failed:', error);
  // Handle error appropriately
}
```

**3. Memory Leaks**
```jsx
// ❌ Wrong - No cleanup
useEffect(() => {
  const interval = setInterval(() => {
    fetchData();
  }, 1000);
}, []);

// ✅ Correct - With cleanup
useEffect(() => {
  const interval = setInterval(() => {
    fetchData();
  }, 1000);
  
  return () => clearInterval(interval);
}, []);
```

### Debug Mode

Enable debug mode for detailed logging:

```javascript
import { HelloWorld1 } from 'helloworld1';

const hw1 = new HelloWorld1({
  debug: true,
  logLevel: 'verbose'
});
```

### Performance Monitoring

```jsx
import { HelloPerformanceMonitor } from 'helloworld1/react';

function App() {
  return (
    <HelloPerformanceMonitor
      onMetric={(metric) => {
        console.log('Performance metric:', metric);
        // Send to analytics service
      }}
    >
      <MyApp />
    </HelloPerformanceMonitor>
  );
}
```

---

For more specific examples and use cases, explore the individual example files in this directory.