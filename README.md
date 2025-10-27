# 🤖 AI Data Assistant

A powerful AI Assistant built with Python and pandas for data analysis and insights. This assistant provides an intuitive chat interface and web application to help you explore, analyze, and visualize your data.

## ✨ Features

- **🔍 Data Loading**: Support for CSV and Excel files
- **📊 Data Analysis**: Statistical analysis, correlations, and clustering
- **💡 AI Insights**: Automated data quality checks and recommendations  
- **📈 Visualizations**: Correlation heatmaps and distribution plots
- **💬 Natural Language Queries**: Ask questions about your data in plain English
- **🌐 Web Interface**: Beautiful, responsive web application
- **📝 Conversation History**: Track all interactions and analysis results

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone or download the project**
```bash
git clone <repository-url>
cd ai-assistant
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Generate sample data (optional)**
```bash
python generate_sample_data.py
```

4. **Test the assistant**
```bash
python test_assistant.py
```

5. **Start the web interface**
```bash
python app.py
```

6. **Open your browser**
Navigate to `http://localhost:5000`

## 📖 How It Works

### Core Components

#### 1. AIAssistant Class (`ai_assistant.py`)
The main AI Assistant class that handles:
- **Data Loading**: Reads CSV/Excel files using pandas
- **Analysis**: Performs statistical, correlation, and clustering analysis
- **Insights**: Generates automated insights and recommendations
- **Queries**: Processes natural language questions about data
- **Visualizations**: Creates charts and plots
- **Conversation**: Maintains chat history and context

#### 2. Web Interface (`app.py` + `templates/index.html`)
A Flask web application providing:
- **File Upload**: Drag-and-drop interface for data files
- **Chat Interface**: Real-time conversation with the AI
- **Data Management**: View and manage loaded datasets
- **Quick Actions**: Shortcut buttons for common tasks
- **Responsive Design**: Works on desktop and mobile devices

#### 3. Sample Data (`generate_sample_data.py`)
Creates realistic datasets for demonstration:
- **Sales Data**: E-commerce transactions with customer demographics
- **Employee Data**: HR information with salary and performance metrics
- **Customer Survey**: Satisfaction and feedback data
- **Stock Market**: Financial time series data
- **IoT Sensors**: Temperature, humidity, and environmental data

## 🔧 Usage Examples

### Command Line Interface

```python
from ai_assistant import AIAssistant

# Initialize the assistant
assistant = AIAssistant()

# Load data
result = assistant.load_data('data/sales_data.csv')
print(f"Loaded dataset: {result['dataset_name']}")

# Analyze data
analysis = assistant.analyze_data('sales_data', 'overview')
print(f"Dataset shape: {analysis['shape']}")

# Get insights
insights = assistant.generate_insights('sales_data')
for insight in insights:
    print(f"• {insight}")

# Query data
result = assistant.query_data('sales_data', 'What are the mean values?')
print(result['answer'])

# Create visualizations
viz = assistant.create_visualization('sales_data', 'correlation_heatmap')
print(f"Visualization saved: {viz['file']}")
```

### Web Interface

1. **Upload Data**: Drag and drop CSV/Excel files or click to browse
2. **Chat**: Type natural language questions like:
   - "What's the shape of my data?"
   - "Show me missing values"
   - "Analyze my data"
   - "Give me insights"
   - "What are the correlations?"

3. **Quick Actions**: Use buttons for common tasks
4. **View Results**: See analysis results, insights, and visualizations

### Natural Language Queries

The assistant understands various question types:

```python
# Data overview
"What is the shape of the data?"
"Show me the columns"
"How many rows and columns are there?"

# Data quality
"Are there any missing values?"
"Show me null values"
"What about missing data?"

# Statistics
"What are the mean values?"
"Show me the maximum values"
"What are the minimum values?"

# Analysis
"Analyze my data"
"Give me insights"
"What patterns do you see?"
```

## 📊 Analysis Types

### 1. Overview Analysis
- Dataset shape and structure
- Column types and information
- Missing value analysis
- Duplicate row detection
- Memory usage statistics
- Basic statistics for numeric columns
- Value counts for categorical columns

### 2. Statistical Analysis
- Descriptive statistics (mean, std, min, max, quartiles)
- Correlation matrix
- Skewness and kurtosis
- Distribution analysis

### 3. Correlation Analysis
- Correlation coefficients between numeric variables
- Strong correlation identification (>0.7)
- Relationship discovery

### 4. Clustering Analysis
- K-means clustering on numeric data
- Data standardization
- Cluster center identification
- Inertia calculation

## 💡 AI Insights

The assistant automatically generates insights including:

- **Data Quality Issues**: Missing values, duplicates, constant columns
- **Distribution Analysis**: Skewed data, outliers
- **Correlation Patterns**: Strong relationships between variables
- **Cardinality Issues**: High/low cardinality categorical variables
- **Dataset Size Recommendations**: Sampling suggestions for large datasets

## 📈 Visualizations

### Correlation Heatmap
Shows relationships between numeric variables with color-coded correlation coefficients.

### Distribution Plots
Displays histograms for all numeric columns to understand data distributions.

## 🗂️ File Structure

```
ai-assistant/
├── ai_assistant.py          # Core AI Assistant class
├── app.py                   # Flask web application
├── requirements.txt         # Python dependencies
├── generate_sample_data.py  # Sample data generation
├── test_assistant.py        # Test suite
├── templates/
│   └── index.html          # Web interface template
├── sample_data/            # Generated sample datasets
│   ├── sales_data.csv
│   ├── employee_data.csv
│   ├── customer_survey.csv
│   ├── stock_data.csv
│   └── iot_sensor_data.csv
└── uploads/                # Uploaded files directory
```

## 🔍 API Endpoints

The web application provides RESTful API endpoints:

- `POST /chat` - Send chat messages
- `POST /upload` - Upload data files
- `GET /analyze/<dataset>/<type>` - Perform analysis
- `GET /insights/<dataset>` - Get insights
- `GET /query/<dataset>?q=<query>` - Query data
- `GET /visualize/<dataset>/<type>` - Create visualizations
- `GET /datasets` - List loaded datasets
- `GET /conversation_history` - Get chat history
- `GET /health` - Health check

## 🛠️ Technical Details

### Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Basic plotting
- **seaborn**: Statistical visualizations
- **plotly**: Interactive charts
- **scikit-learn**: Machine learning algorithms
- **flask**: Web framework
- **werkzeug**: WSGI utilities

### Data Processing Pipeline

1. **File Upload**: Secure file handling with type validation
2. **Data Loading**: Pandas-based CSV/Excel reading with error handling
3. **Data Analysis**: Multiple analysis types with caching
4. **Insight Generation**: Rule-based pattern detection
5. **Visualization**: Matplotlib/Seaborn chart generation
6. **Response Formatting**: User-friendly result presentation

### Security Features

- File type validation (CSV, Excel only)
- Secure filename handling
- File size limits (16MB)
- Input sanitization
- Error handling and validation

## 🎯 Use Cases

### Business Intelligence
- Sales performance analysis
- Customer behavior insights
- Market trend identification
- Revenue optimization

### Data Science
- Exploratory data analysis
- Feature correlation discovery
- Data quality assessment
- Preprocessing insights

### Research
- Survey data analysis
- Experimental result exploration
- Pattern identification
- Statistical validation

### Operations
- Performance monitoring
- Quality control
- Trend analysis
- Anomaly detection

## 🚀 Advanced Features

### Conversation Context
The assistant maintains conversation history and can reference previous analyses and loaded datasets.

### Caching
Analysis results are cached to improve performance for repeated queries.

### Extensible Architecture
Easy to add new analysis types, visualization options, and data sources.

### Error Handling
Comprehensive error handling with user-friendly messages.

## 🔮 Future Enhancements

Potential improvements and extensions:

- **Machine Learning**: Predictive modeling and classification
- **Advanced Visualizations**: Interactive plotly charts
- **Database Support**: SQL database connectivity
- **Export Features**: PDF/PowerPoint report generation
- **Collaboration**: Multi-user support and sharing
- **API Integration**: Connect to external data sources
- **Advanced NLP**: More sophisticated query understanding

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

For questions, issues, or feature requests:

1. Check the documentation
2. Run the test suite: `python test_assistant.py`
3. Review the conversation history in the web interface
4. Check the browser console for JavaScript errors

## 🎉 Getting Started

1. **Try the demo**: Run `python test_assistant.py` to see all features
2. **Explore sample data**: Generated datasets showcase different use cases  
3. **Upload your data**: Use the web interface to analyze your own files
4. **Ask questions**: Use natural language to explore your data
5. **Get insights**: Let the AI discover patterns and issues automatically

The AI Assistant makes data analysis accessible to everyone, from beginners to experts. Start exploring your data today! 🚀