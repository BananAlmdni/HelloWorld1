# Component Documentation

This section provides comprehensive documentation for all reusable components in HelloWorld1.

## 📋 Table of Contents

- [Core Components](#core-components)
- [Form Components](#form-components)
- [Layout Components](#layout-components)
- [Navigation Components](#navigation-components)
- [Data Display Components](#data-display-components)
- [Feedback Components](#feedback-components)
- [Component API Reference](#component-api-reference)

## 📝 Documentation Format

Each component is documented with:
- **Purpose**: What the component does and when to use it
- **Props/Attributes**: Input properties with types and descriptions
- **Events**: Events emitted by the component
- **Slots/Children**: Content areas and their usage
- **Styling**: CSS classes, custom properties, and theming
- **Examples**: Working code examples
- **Accessibility**: ARIA attributes and keyboard navigation
- **Browser Support**: Compatibility information

---

## 🧩 Core Components

### `HelloButton`

A versatile button component with multiple variants and states.

**Purpose:**
Provides a consistent button interface across the application with support for different styles, sizes, and states.

#### Props (React/Vue)

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `'primary' \| 'secondary' \| 'danger' \| 'ghost'` | `'primary'` | Button style variant |
| `size` | `'small' \| 'medium' \| 'large'` | `'medium'` | Button size |
| `disabled` | `boolean` | `false` | Whether button is disabled |
| `loading` | `boolean` | `false` | Shows loading spinner |
| `icon` | `string \| Component` | `undefined` | Icon to display |
| `iconPosition` | `'left' \| 'right'` | `'left'` | Icon position relative to text |
| `fullWidth` | `boolean` | `false` | Makes button full width |
| `href` | `string` | `undefined` | Makes button act as a link |
| `target` | `string` | `undefined` | Link target (when href is provided) |

#### Events

| Event | Payload | Description |
|-------|---------|-------------|
| `click` | `MouseEvent` | Fired when button is clicked |
| `focus` | `FocusEvent` | Fired when button receives focus |
| `blur` | `FocusEvent` | Fired when button loses focus |

#### Examples

**React:**
```jsx
import { HelloButton } from 'helloworld1';

// Basic button
<HelloButton onClick={() => console.log('clicked')}>
  Click me
</HelloButton>

// Primary button with icon
<HelloButton 
  variant="primary" 
  icon="plus" 
  onClick={handleCreate}
>
  Create New
</HelloButton>

// Loading state
<HelloButton 
  loading={isSubmitting}
  disabled={isSubmitting}
  onClick={handleSubmit}
>
  {isSubmitting ? 'Saving...' : 'Save'}
</HelloButton>

// Danger button
<HelloButton 
  variant="danger" 
  size="small"
  onClick={handleDelete}
>
  Delete
</HelloButton>

// Button as link
<HelloButton 
  href="https://example.com"
  target="_blank"
  variant="ghost"
>
  External Link
</HelloButton>
```

**Vue:**
```vue
<template>
  <div>
    <!-- Basic button -->
    <HelloButton @click="handleClick">
      Click me
    </HelloButton>

    <!-- Primary button with icon -->
    <HelloButton 
      variant="primary" 
      icon="plus" 
      @click="handleCreate"
    >
      Create New
    </HelloButton>

    <!-- Loading state -->
    <HelloButton 
      :loading="isSubmitting"
      :disabled="isSubmitting"
      @click="handleSubmit"
    >
      {{ isSubmitting ? 'Saving...' : 'Save' }}
    </HelloButton>
  </div>
</template>

<script>
import { HelloButton } from 'helloworld1';

export default {
  components: {
    HelloButton
  },
  data() {
    return {
      isSubmitting: false
    };
  },
  methods: {
    handleClick() {
      console.log('clicked');
    },
    handleCreate() {
      // Create logic
    },
    async handleSubmit() {
      this.isSubmitting = true;
      try {
        // Submit logic
      } finally {
        this.isSubmitting = false;
      }
    }
  }
};
</script>
```

**Angular:**
```typescript
// component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-example',
  template: `
    <!-- Basic button -->
    <hello-button (click)="handleClick()">
      Click me
    </hello-button>

    <!-- Primary button with icon -->
    <hello-button 
      variant="primary" 
      icon="plus" 
      (click)="handleCreate()">
      Create New
    </hello-button>

    <!-- Loading state -->
    <hello-button 
      [loading]="isSubmitting"
      [disabled]="isSubmitting"
      (click)="handleSubmit()">
      {{ isSubmitting ? 'Saving...' : 'Save' }}
    </hello-button>
  `
})
export class ExampleComponent {
  isSubmitting = false;

  handleClick() {
    console.log('clicked');
  }

  handleCreate() {
    // Create logic
  }

  async handleSubmit() {
    this.isSubmitting = true;
    try {
      // Submit logic
    } finally {
      this.isSubmitting = false;
    }
  }
}
```

#### Styling

**CSS Custom Properties:**
```css
.hello-button {
  --button-bg: #007bff;
  --button-color: #ffffff;
  --button-border: 1px solid transparent;
  --button-border-radius: 4px;
  --button-padding: 8px 16px;
  --button-font-size: 14px;
  --button-font-weight: 500;
  --button-transition: all 0.2s ease;
}

/* Variants */
.hello-button--primary {
  --button-bg: #007bff;
  --button-color: #ffffff;
}

.hello-button--secondary {
  --button-bg: #6c757d;
  --button-color: #ffffff;
}

.hello-button--danger {
  --button-bg: #dc3545;
  --button-color: #ffffff;
}

.hello-button--ghost {
  --button-bg: transparent;
  --button-color: #007bff;
  --button-border: 1px solid #007bff;
}

/* Sizes */
.hello-button--small {
  --button-padding: 4px 8px;
  --button-font-size: 12px;
}

.hello-button--large {
  --button-padding: 12px 24px;
  --button-font-size: 16px;
}
```

**Overriding Styles:**
```css
/* Custom theme */
.my-custom-button {
  --button-bg: #28a745;
  --button-border-radius: 8px;
  --button-font-weight: 600;
}
```

#### Accessibility

- Supports keyboard navigation (Enter and Space keys)
- Proper ARIA attributes (`aria-disabled`, `aria-pressed`)
- Focus management with visible focus indicators
- Screen reader compatible
- High contrast mode support

---

### `HelloInput`

A flexible input component with validation and various input types.

**Purpose:**
Provides consistent text input functionality with built-in validation, error handling, and accessibility features.

#### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `'text' \| 'email' \| 'password' \| 'number' \| 'tel' \| 'url'` | `'text'` | Input type |
| `value` | `string \| number` | `''` | Input value |
| `placeholder` | `string` | `''` | Placeholder text |
| `label` | `string` | `''` | Input label |
| `required` | `boolean` | `false` | Whether input is required |
| `disabled` | `boolean` | `false` | Whether input is disabled |
| `readonly` | `boolean` | `false` | Whether input is readonly |
| `error` | `string` | `''` | Error message to display |
| `helpText` | `string` | `''` | Help text below input |
| `maxLength` | `number` | `undefined` | Maximum character length |
| `minLength` | `number` | `undefined` | Minimum character length |
| `pattern` | `string` | `undefined` | Validation pattern (regex) |
| `autocomplete` | `string` | `undefined` | Autocomplete attribute |
| `size` | `'small' \| 'medium' \| 'large'` | `'medium'` | Input size |

#### Events

| Event | Payload | Description |
|-------|---------|-------------|
| `input` | `string \| number` | Fired when input value changes |
| `change` | `string \| number` | Fired when input loses focus after change |
| `focus` | `FocusEvent` | Fired when input receives focus |
| `blur` | `FocusEvent` | Fired when input loses focus |
| `keydown` | `KeyboardEvent` | Fired on key press |
| `validation` | `{ isValid: boolean, errors: string[] }` | Fired after validation |

#### Examples

**React:**
```jsx
import { HelloInput } from 'helloworld1';

// Basic input
<HelloInput 
  label="Full Name"
  placeholder="Enter your full name"
  value={name}
  onChange={setName}
/>

// Email input with validation
<HelloInput 
  type="email"
  label="Email Address"
  placeholder="you@example.com"
  value={email}
  onChange={setEmail}
  required
  error={emailError}
/>

// Password input
<HelloInput 
  type="password"
  label="Password"
  placeholder="Enter password"
  value={password}
  onChange={setPassword}
  minLength={8}
  helpText="Must be at least 8 characters"
/>

// Number input with constraints
<HelloInput 
  type="number"
  label="Age"
  value={age}
  onChange={setAge}
  min={18}
  max={120}
  required
/>
```

**Vue:**
```vue
<template>
  <div>
    <!-- Basic input -->
    <HelloInput 
      label="Full Name"
      placeholder="Enter your full name"
      v-model="name"
    />

    <!-- Email input with validation -->
    <HelloInput 
      type="email"
      label="Email Address"
      placeholder="you@example.com"
      v-model="email"
      :required="true"
      :error="emailError"
      @validation="handleValidation"
    />

    <!-- Password input -->
    <HelloInput 
      type="password"
      label="Password"
      placeholder="Enter password"
      v-model="password"
      :min-length="8"
      help-text="Must be at least 8 characters"
    />
  </div>
</template>

<script>
import { HelloInput } from 'helloworld1';

export default {
  components: {
    HelloInput
  },
  data() {
    return {
      name: '',
      email: '',
      password: '',
      emailError: ''
    };
  },
  methods: {
    handleValidation(result) {
      if (!result.isValid) {
        this.emailError = result.errors[0];
      } else {
        this.emailError = '';
      }
    }
  }
};
</script>
```

---

## 📋 Form Components

### `HelloForm`

A comprehensive form wrapper with validation and submission handling.

**Purpose:**
Provides form-level validation, error handling, and submission management for complex forms.

#### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `schema` | `ValidationSchema` | `{}` | Form validation schema |
| `initialValues` | `Object` | `{}` | Initial form values |
| `onSubmit` | `Function` | `undefined` | Form submission handler |
| `loading` | `boolean` | `false` | Shows loading state |
| `disabled` | `boolean` | `false` | Disables entire form |
| `resetOnSubmit` | `boolean` | `false` | Reset form after successful submit |

#### Events

| Event | Payload | Description |
|-------|---------|-------------|
| `submit` | `{ values: Object, isValid: boolean }` | Fired on form submission |
| `change` | `{ field: string, value: any, values: Object }` | Fired when any field changes |
| `validation` | `{ isValid: boolean, errors: Object }` | Fired after form validation |

#### Example

```jsx
import { HelloForm, HelloInput, HelloButton } from 'helloworld1';

const schema = {
  required: ['name', 'email'],
  types: {
    name: 'string',
    email: 'string',
    age: 'number'
  },
  constraints: {
    name: { minLength: 2 },
    email: { pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/ },
    age: { min: 18, max: 120 }
  }
};

function UserForm() {
  const handleSubmit = async (data) => {
    try {
      await createUser(data.values);
      console.log('User created successfully');
    } catch (error) {
      console.error('Failed to create user:', error);
    }
  };

  return (
    <HelloForm 
      schema={schema}
      onSubmit={handleSubmit}
      initialValues={{ name: '', email: '', age: '' }}
    >
      {({ values, errors, isValid, isSubmitting }) => (
        <>
          <HelloInput 
            name="name"
            label="Full Name"
            value={values.name}
            error={errors.name}
            required
          />
          
          <HelloInput 
            name="email"
            type="email"
            label="Email"
            value={values.email}
            error={errors.email}
            required
          />
          
          <HelloInput 
            name="age"
            type="number"
            label="Age"
            value={values.age}
            error={errors.age}
          />
          
          <HelloButton 
            type="submit"
            disabled={!isValid || isSubmitting}
            loading={isSubmitting}
          >
            Create User
          </HelloButton>
        </>
      )}
    </HelloForm>
  );
}
```

---

## 🎛️ Layout Components

### `HelloGrid`

A flexible grid system for responsive layouts.

**Purpose:**
Provides a CSS Grid-based layout system with responsive breakpoints and flexible configurations.

#### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `columns` | `number \| string \| Object` | `12` | Number of columns or CSS grid template |
| `gap` | `string \| number` | `'16px'` | Gap between grid items |
| `responsive` | `boolean` | `true` | Enable responsive behavior |
| `alignItems` | `'start' \| 'center' \| 'end' \| 'stretch'` | `'stretch'` | Vertical alignment |
| `justifyItems` | `'start' \| 'center' \| 'end' \| 'stretch'` | `'stretch'` | Horizontal alignment |

#### Examples

```jsx
import { HelloGrid, HelloGridItem } from 'helloworld1';

// Basic 12-column grid
<HelloGrid columns={12} gap="20px">
  <HelloGridItem span={4}>
    <div>Column 1</div>
  </HelloGridItem>
  <HelloGridItem span={8}>
    <div>Column 2</div>
  </HelloGridItem>
</HelloGrid>

// Responsive grid
<HelloGrid 
  columns={{ 
    xs: 1, 
    sm: 2, 
    md: 3, 
    lg: 4 
  }}
  gap="16px"
>
  <HelloGridItem>Item 1</HelloGridItem>
  <HelloGridItem>Item 2</HelloGridItem>
  <HelloGridItem>Item 3</HelloGridItem>
  <HelloGridItem>Item 4</HelloGridItem>
</HelloGrid>

// Custom grid template
<HelloGrid 
  columns="200px 1fr 100px"
  gap="12px"
  alignItems="center"
>
  <HelloGridItem>Sidebar</HelloGridItem>
  <HelloGridItem>Main Content</HelloGridItem>
  <HelloGridItem>Actions</HelloGridItem>
</HelloGrid>
```

---

## 📊 Data Display Components

### `HelloTable`

A feature-rich table component with sorting, filtering, and pagination.

**Purpose:**
Displays tabular data with advanced features like sorting, filtering, pagination, and row selection.

#### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `data` | `Array<Object>` | `[]` | Table data |
| `columns` | `Array<ColumnConfig>` | `[]` | Column definitions |
| `sortable` | `boolean` | `true` | Enable sorting |
| `filterable` | `boolean` | `false` | Enable filtering |
| `selectable` | `boolean` | `false` | Enable row selection |
| `pagination` | `boolean \| PaginationConfig` | `false` | Pagination settings |
| `loading` | `boolean` | `false` | Show loading state |
| `emptyMessage` | `string` | `'No data available'` | Message when no data |

#### Column Configuration

```typescript
interface ColumnConfig {
  key: string;
  title: string;
  sortable?: boolean;
  filterable?: boolean;
  width?: string | number;
  align?: 'left' | 'center' | 'right';
  render?: (value: any, row: Object) => ReactNode;
  filter?: {
    type: 'text' | 'select' | 'date' | 'number';
    options?: Array<{ label: string, value: any }>;
  };
}
```

#### Events

| Event | Payload | Description |
|-------|---------|-------------|
| `sort` | `{ column: string, direction: 'asc' \| 'desc' }` | Fired when column is sorted |
| `filter` | `{ column: string, value: any }` | Fired when filter changes |
| `select` | `Array<Object>` | Fired when row selection changes |
| `rowClick` | `{ row: Object, index: number }` | Fired when row is clicked |

#### Example

```jsx
import { HelloTable } from 'helloworld1';

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
    filterable: true,
    filter: { type: 'text' }
  },
  {
    key: 'email',
    title: 'Email',
    sortable: true,
    filterable: true
  },
  {
    key: 'status',
    title: 'Status',
    align: 'center',
    filterable: true,
    filter: {
      type: 'select',
      options: [
        { label: 'Active', value: 'active' },
        { label: 'Inactive', value: 'inactive' }
      ]
    },
    render: (value) => (
      <span className={`status-badge status-${value}`}>
        {value}
      </span>
    )
  },
  {
    key: 'actions',
    title: 'Actions',
    width: 120,
    align: 'center',
    render: (value, row) => (
      <div>
        <HelloButton size="small" onClick={() => editUser(row.id)}>
          Edit
        </HelloButton>
        <HelloButton 
          size="small" 
          variant="danger" 
          onClick={() => deleteUser(row.id)}
        >
          Delete
        </HelloButton>
      </div>
    )
  }
];

const data = [
  { id: 1, name: 'John Doe', email: 'john@example.com', status: 'active' },
  { id: 2, name: 'Jane Smith', email: 'jane@example.com', status: 'inactive' },
  // ... more data
];

function UserTable() {
  const [selectedRows, setSelectedRows] = useState([]);

  const handleSort = ({ column, direction }) => {
    console.log(`Sorting by ${column} ${direction}`);
    // Implement sorting logic
  };

  const handleFilter = ({ column, value }) => {
    console.log(`Filtering ${column} by ${value}`);
    // Implement filtering logic
  };

  return (
    <HelloTable
      data={data}
      columns={columns}
      sortable
      filterable
      selectable
      pagination={{
        pageSize: 10,
        showSizeChanger: true,
        showQuickJumper: true
      }}
      onSort={handleSort}
      onFilter={handleFilter}
      onSelect={setSelectedRows}
    />
  );
}
```

---

## 💬 Feedback Components

### `HelloModal`

A flexible modal dialog component.

**Purpose:**
Displays content in an overlay dialog with backdrop, close handling, and accessibility features.

#### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `open` | `boolean` | `false` | Whether modal is open |
| `title` | `string` | `''` | Modal title |
| `size` | `'small' \| 'medium' \| 'large' \| 'fullscreen'` | `'medium'` | Modal size |
| `closable` | `boolean` | `true` | Show close button |
| `maskClosable` | `boolean` | `true` | Close on backdrop click |
| `keyboard` | `boolean` | `true` | Close on Escape key |
| `centered` | `boolean` | `false` | Center modal vertically |
| `destroyOnClose` | `boolean` | `false` | Destroy content when closed |

#### Events

| Event | Payload | Description |
|-------|---------|-------------|
| `close` | `void` | Fired when modal should close |
| `afterOpen` | `void` | Fired after modal opens |
| `afterClose` | `void` | Fired after modal closes |

#### Slots/Children

- **header**: Custom header content
- **footer**: Custom footer content
- **default**: Main modal content

#### Example

```jsx
import { HelloModal, HelloButton } from 'helloworld1';

function UserModal({ user, open, onClose, onSave }) {
  const [loading, setLoading] = useState(false);

  const handleSave = async () => {
    setLoading(true);
    try {
      await onSave(user);
      onClose();
    } catch (error) {
      console.error('Save failed:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <HelloModal
      open={open}
      title={user ? 'Edit User' : 'Create User'}
      size="medium"
      onClose={onClose}
      footer={
        <>
          <HelloButton variant="ghost" onClick={onClose}>
            Cancel
          </HelloButton>
          <HelloButton 
            variant="primary" 
            loading={loading}
            onClick={handleSave}
          >
            Save
          </HelloButton>
        </>
      }
    >
      <HelloForm 
        initialValues={user || {}}
        onSubmit={handleSave}
      >
        {/* Form content */}
      </HelloForm>
    </HelloModal>
  );
}
```

---

### `HelloNotification`

A toast notification component for user feedback.

**Purpose:**
Displays temporary notification messages with different types and auto-dismiss functionality.

#### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `'success' \| 'error' \| 'warning' \| 'info'` | `'info'` | Notification type |
| `title` | `string` | `''` | Notification title |
| `message` | `string` | `''` | Notification message |
| `duration` | `number` | `4000` | Auto-dismiss duration (ms) |
| `closable` | `boolean` | `true` | Show close button |
| `icon` | `string \| Component` | `undefined` | Custom icon |
| `action` | `ReactNode` | `undefined` | Custom action button |

#### API Methods

```javascript
import { notification } from 'helloworld1';

// Show different types
notification.success('Operation completed successfully');
notification.error('Something went wrong');
notification.warning('Please check your input');
notification.info('New update available');

// With configuration
notification.success({
  title: 'Success',
  message: 'User created successfully',
  duration: 3000,
  action: <Button>View</Button>
});

// Custom notification
notification.open({
  type: 'info',
  title: 'Custom Notification',
  message: 'This is a custom notification',
  icon: 'bell',
  duration: 0, // Don't auto-dismiss
  action: (
    <HelloButton size="small" onClick={() => console.log('Action clicked')}>
      Action
    </HelloButton>
  )
});
```

---

## 📚 Component API Reference

### Common Props

All components support these common props:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | `''` | Additional CSS classes |
| `style` | `Object` | `{}` | Inline styles |
| `id` | `string` | `undefined` | Element ID |
| `testId` | `string` | `undefined` | Test identifier |

### Theme Support

All components support theming through CSS custom properties:

```css
:root {
  /* Colors */
  --hw-primary: #007bff;
  --hw-secondary: #6c757d;
  --hw-success: #28a745;
  --hw-danger: #dc3545;
  --hw-warning: #ffc107;
  --hw-info: #17a2b8;
  
  /* Spacing */
  --hw-spacing-xs: 4px;
  --hw-spacing-sm: 8px;
  --hw-spacing-md: 16px;
  --hw-spacing-lg: 24px;
  --hw-spacing-xl: 32px;
  
  /* Typography */
  --hw-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto;
  --hw-font-size-xs: 12px;
  --hw-font-size-sm: 14px;
  --hw-font-size-md: 16px;
  --hw-font-size-lg: 18px;
  --hw-font-size-xl: 20px;
  
  /* Borders */
  --hw-border-radius: 4px;
  --hw-border-width: 1px;
  --hw-border-color: #dee2e6;
  
  /* Shadows */
  --hw-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --hw-shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --hw-shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}
```

### Accessibility Features

All components include:

- **Keyboard Navigation**: Full keyboard support
- **ARIA Labels**: Proper ARIA attributes
- **Focus Management**: Logical focus flow
- **Screen Reader Support**: Compatible with assistive technologies
- **High Contrast**: Supports high contrast modes
- **Reduced Motion**: Respects prefers-reduced-motion

### Browser Support

- **Modern Browsers**: Chrome 60+, Firefox 55+, Safari 12+, Edge 79+
- **Mobile**: iOS Safari 12+, Chrome Mobile 60+
- **Legacy Support**: IE 11 with polyfills (limited features)

---

For specific implementation details and advanced usage, see the individual component files in this directory.