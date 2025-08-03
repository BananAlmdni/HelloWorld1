import pandas as pd
import numpy as np
import json
import re
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

class AIAssistant:
    """
    An AI Assistant that can handle conversations and perform data analysis using pandas.
    
    This assistant can:
    - Process and analyze CSV/Excel files
    - Generate visualizations
    - Perform statistical analysis
    - Answer questions about data
    - Provide insights and recommendations
    """
    
    def __init__(self):
        self.conversation_history = []
        self.loaded_data = {}
        self.analysis_results = {}
        
    def add_to_conversation(self, user_input, assistant_response):
        """Add conversation to history"""
        self.conversation_history.append({
            'timestamp': datetime.now().isoformat(),
            'user': user_input,
            'assistant': assistant_response
        })
    
    def load_data(self, file_path, dataset_name=None):
        """
        Load data from CSV or Excel file using pandas
        
        Args:
            file_path (str): Path to the data file
            dataset_name (str): Optional name for the dataset
            
        Returns:
            dict: Information about the loaded dataset
        """
        try:
            if dataset_name is None:
                dataset_name = file_path.split('/')[-1].split('.')[0]
            
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path)
            else:
                return {"error": "Unsupported file format. Please use CSV or Excel files."}
            
            self.loaded_data[dataset_name] = df
            
            info = {
                "dataset_name": dataset_name,
                "shape": df.shape,
                "columns": list(df.columns),
                "dtypes": df.dtypes.to_dict(),
                "memory_usage": df.memory_usage(deep=True).sum(),
                "missing_values": df.isnull().sum().to_dict(),
                "sample_data": df.head().to_dict()
            }
            
            return info
            
        except Exception as e:
            return {"error": f"Error loading data: {str(e)}"}
    
    def analyze_data(self, dataset_name, analysis_type="overview"):
        """
        Perform various types of data analysis
        
        Args:
            dataset_name (str): Name of the dataset to analyze
            analysis_type (str): Type of analysis ('overview', 'statistical', 'correlation', 'clustering')
            
        Returns:
            dict: Analysis results
        """
        if dataset_name not in self.loaded_data:
            return {"error": f"Dataset '{dataset_name}' not found. Please load it first."}
        
        df = self.loaded_data[dataset_name]
        results = {}
        
        try:
            if analysis_type == "overview":
                results = {
                    "shape": df.shape,
                    "info": {
                        "columns": list(df.columns),
                        "dtypes": df.dtypes.to_dict(),
                        "non_null_counts": df.count().to_dict()
                    },
                    "missing_data": df.isnull().sum().to_dict(),
                    "duplicate_rows": df.duplicated().sum(),
                    "memory_usage_mb": df.memory_usage(deep=True).sum() / 1024**2
                }
                
                # Add basic statistics for numeric columns
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) > 0:
                    results["numeric_summary"] = df[numeric_cols].describe().to_dict()
                
                # Add value counts for categorical columns
                categorical_cols = df.select_dtypes(include=['object']).columns
                if len(categorical_cols) > 0:
                    results["categorical_summary"] = {}
                    for col in categorical_cols:
                        results["categorical_summary"][col] = df[col].value_counts().head(10).to_dict()
            
            elif analysis_type == "statistical":
                numeric_df = df.select_dtypes(include=[np.number])
                if numeric_df.empty:
                    return {"error": "No numeric columns found for statistical analysis"}
                
                results = {
                    "descriptive_stats": numeric_df.describe().to_dict(),
                    "correlation_matrix": numeric_df.corr().to_dict(),
                    "skewness": numeric_df.skew().to_dict(),
                    "kurtosis": numeric_df.kurtosis().to_dict()
                }
            
            elif analysis_type == "correlation":
                numeric_df = df.select_dtypes(include=[np.number])
                if numeric_df.empty:
                    return {"error": "No numeric columns found for correlation analysis"}
                
                corr_matrix = numeric_df.corr()
                
                # Find strong correlations
                strong_correlations = []
                for i in range(len(corr_matrix.columns)):
                    for j in range(i+1, len(corr_matrix.columns)):
                        corr_val = corr_matrix.iloc[i, j]
                        if abs(corr_val) > 0.7:  # Strong correlation threshold
                            strong_correlations.append({
                                "feature1": corr_matrix.columns[i],
                                "feature2": corr_matrix.columns[j],
                                "correlation": corr_val
                            })
                
                results = {
                    "correlation_matrix": corr_matrix.to_dict(),
                    "strong_correlations": strong_correlations
                }
            
            elif analysis_type == "clustering":
                numeric_df = df.select_dtypes(include=[np.number]).dropna()
                if numeric_df.empty:
                    return {"error": "No numeric data available for clustering"}
                
                if len(numeric_df) < 3:
                    return {"error": "Not enough data points for clustering"}
                
                # Standardize the data
                scaler = StandardScaler()
                scaled_data = scaler.fit_transform(numeric_df)
                
                # Perform K-means clustering
                n_clusters = min(5, len(numeric_df) // 2)  # Reasonable number of clusters
                kmeans = KMeans(n_clusters=n_clusters, random_state=42)
                clusters = kmeans.fit_predict(scaled_data)
                
                results = {
                    "n_clusters": n_clusters,
                    "cluster_centers": kmeans.cluster_centers_.tolist(),
                    "cluster_labels": clusters.tolist(),
                    "inertia": kmeans.inertia_
                }
            
            self.analysis_results[f"{dataset_name}_{analysis_type}"] = results
            return results
            
        except Exception as e:
            return {"error": f"Error during analysis: {str(e)}"}
    
    def generate_insights(self, dataset_name):
        """
        Generate insights and recommendations based on the data
        
        Args:
            dataset_name (str): Name of the dataset to analyze
            
        Returns:
            list: List of insights and recommendations
        """
        if dataset_name not in self.loaded_data:
            return ["Error: Dataset not found. Please load it first."]
        
        df = self.loaded_data[dataset_name]
        insights = []
        
        try:
            # Data quality insights
            missing_percentage = (df.isnull().sum() / len(df) * 100)
            high_missing = missing_percentage[missing_percentage > 20]
            if not high_missing.empty:
                insights.append(f"⚠️ High missing data: {', '.join(high_missing.index)} have >20% missing values")
            
            duplicates = df.duplicated().sum()
            if duplicates > 0:
                insights.append(f"🔍 Found {duplicates} duplicate rows ({duplicates/len(df)*100:.1f}% of data)")
            
            # Numeric data insights
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                for col in numeric_cols:
                    if df[col].std() == 0:
                        insights.append(f"📊 Column '{col}' has constant values")
                    elif df[col].skew() > 2:
                        insights.append(f"📈 Column '{col}' is highly right-skewed")
                    elif df[col].skew() < -2:
                        insights.append(f"📉 Column '{col}' is highly left-skewed")
            
            # Categorical data insights
            categorical_cols = df.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                unique_ratio = df[col].nunique() / len(df)
                if unique_ratio > 0.95:
                    insights.append(f"🏷️ Column '{col}' has very high cardinality (might be an identifier)")
                elif unique_ratio < 0.01:
                    insights.append(f"🏷️ Column '{col}' has very low cardinality (mostly constant)")
            
            # Correlation insights
            if len(numeric_cols) > 1:
                corr_matrix = df[numeric_cols].corr()
                high_corr = []
                for i in range(len(corr_matrix.columns)):
                    for j in range(i+1, len(corr_matrix.columns)):
                        corr_val = corr_matrix.iloc[i, j]
                        if abs(corr_val) > 0.8:
                            high_corr.append(f"{corr_matrix.columns[i]} ↔ {corr_matrix.columns[j]} ({corr_val:.2f})")
                
                if high_corr:
                    insights.append(f"🔗 Strong correlations found: {', '.join(high_corr)}")
            
            # Data distribution insights
            if len(df) > 1000:
                insights.append("📏 Large dataset - consider sampling for faster analysis")
            elif len(df) < 50:
                insights.append("📏 Small dataset - results may not be statistically significant")
            
            if not insights:
                insights.append("✅ Data appears to be in good shape with no major issues detected")
            
            return insights
            
        except Exception as e:
            return [f"Error generating insights: {str(e)}"]
    
    def query_data(self, dataset_name, query):
        """
        Process natural language queries about the data
        
        Args:
            dataset_name (str): Name of the dataset
            query (str): Natural language query
            
        Returns:
            dict: Query results
        """
        if dataset_name not in self.loaded_data:
            return {"error": f"Dataset '{dataset_name}' not found"}
        
        df = self.loaded_data[dataset_name]
        query_lower = query.lower()
        
        try:
            # Basic queries
            if "shape" in query_lower or "size" in query_lower:
                return {
                    "answer": f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns",
                    "data": {"rows": df.shape[0], "columns": df.shape[1]}
                }
            
            elif "columns" in query_lower:
                return {
                    "answer": f"The dataset has columns: {', '.join(df.columns)}",
                    "data": list(df.columns)
                }
            
            elif "missing" in query_lower or "null" in query_lower:
                missing = df.isnull().sum()
                missing_info = missing[missing > 0].to_dict()
                if missing_info:
                    return {
                        "answer": f"Missing values found in: {', '.join(missing_info.keys())}",
                        "data": missing_info
                    }
                else:
                    return {"answer": "No missing values found in the dataset", "data": {}}
            
            elif "mean" in query_lower:
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) > 0:
                    means = df[numeric_cols].mean().to_dict()
                    return {
                        "answer": f"Mean values: {', '.join([f'{k}: {v:.2f}' for k, v in means.items()])}",
                        "data": means
                    }
                else:
                    return {"answer": "No numeric columns found for mean calculation", "data": {}}
            
            elif "max" in query_lower:
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) > 0:
                    maxes = df[numeric_cols].max().to_dict()
                    return {
                        "answer": f"Maximum values: {', '.join([f'{k}: {v}' for k, v in maxes.items()])}",
                        "data": maxes
                    }
                else:
                    return {"answer": "No numeric columns found for max calculation", "data": {}}
            
            elif "min" in query_lower:
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) > 0:
                    mins = df[numeric_cols].min().to_dict()
                    return {
                        "answer": f"Minimum values: {', '.join([f'{k}: {v}' for k, v in mins.items()])}",
                        "data": mins
                    }
                else:
                    return {"answer": "No numeric columns found for min calculation", "data": {}}
            
            else:
                return {
                    "answer": "I didn't understand that query. Try asking about shape, columns, missing values, mean, max, or min.",
                    "data": None
                }
            
        except Exception as e:
            return {"error": f"Error processing query: {str(e)}"}
    
    def create_visualization(self, dataset_name, viz_type, columns=None):
        """
        Create visualizations using the data
        
        Args:
            dataset_name (str): Name of the dataset
            viz_type (str): Type of visualization
            columns (list): Columns to include in visualization
            
        Returns:
            dict: Visualization information
        """
        if dataset_name not in self.loaded_data:
            return {"error": f"Dataset '{dataset_name}' not found"}
        
        df = self.loaded_data[dataset_name]
        
        try:
            if viz_type == "correlation_heatmap":
                numeric_df = df.select_dtypes(include=[np.number])
                if numeric_df.empty:
                    return {"error": "No numeric columns for correlation heatmap"}
                
                plt.figure(figsize=(10, 8))
                sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', center=0)
                plt.title(f'Correlation Heatmap - {dataset_name}')
                plt.tight_layout()
                filename = f"{dataset_name}_correlation_heatmap.png"
                plt.savefig(filename)
                plt.close()
                
                return {"message": f"Correlation heatmap saved as {filename}", "file": filename}
            
            elif viz_type == "distribution":
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) == 0:
                    return {"error": "No numeric columns for distribution plot"}
                
                n_cols = min(3, len(numeric_cols))
                n_rows = (len(numeric_cols) + n_cols - 1) // n_cols
                
                fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
                if n_rows == 1:
                    axes = [axes] if n_cols == 1 else axes
                else:
                    axes = axes.flatten()
                
                for i, col in enumerate(numeric_cols):
                    if i < len(axes):
                        axes[i].hist(df[col].dropna(), bins=30, alpha=0.7)
                        axes[i].set_title(f'Distribution of {col}')
                        axes[i].set_xlabel(col)
                        axes[i].set_ylabel('Frequency')
                
                # Hide unused subplots
                for i in range(len(numeric_cols), len(axes)):
                    axes[i].set_visible(False)
                
                plt.tight_layout()
                filename = f"{dataset_name}_distributions.png"
                plt.savefig(filename)
                plt.close()
                
                return {"message": f"Distribution plots saved as {filename}", "file": filename}
            
            else:
                return {"error": f"Visualization type '{viz_type}' not supported. Available: correlation_heatmap, distribution"}
            
        except Exception as e:
            return {"error": f"Error creating visualization: {str(e)}"}
    
    def get_conversation_history(self):
        """Return the conversation history"""
        return self.conversation_history
    
    def get_loaded_datasets(self):
        """Return information about loaded datasets"""
        return {name: {"shape": df.shape, "columns": list(df.columns)} 
                for name, df in self.loaded_data.items()}
    
    def process_request(self, user_input):
        """
        Main method to process user requests
        
        Args:
            user_input (str): User's request
            
        Returns:
            str: Assistant's response
        """
        try:
            # Convert to lowercase for easier processing
            input_lower = user_input.lower()
            
            # Help command
            if "help" in input_lower:
                response = self._get_help_message()
            
            # Load data command
            elif "load" in input_lower and ("data" in input_lower or "file" in input_lower):
                response = "To load data, please provide the file path. Example: load_data('path/to/your/file.csv')"
            
            # Analyze command
            elif "analyze" in input_lower:
                if not self.loaded_data:
                    response = "No data loaded yet. Please load a dataset first."
                else:
                    dataset_name = list(self.loaded_data.keys())[0]  # Use first dataset
                    analysis = self.analyze_data(dataset_name, "overview")
                    if "error" in analysis:
                        response = f"Analysis error: {analysis['error']}"
                    else:
                        response = self._format_analysis_response(analysis, dataset_name)
            
            # Insights command
            elif "insight" in input_lower:
                if not self.loaded_data:
                    response = "No data loaded yet. Please load a dataset first."
                else:
                    dataset_name = list(self.loaded_data.keys())[0]
                    insights = self.generate_insights(dataset_name)
                    response = "📊 **Data Insights:**\n\n" + "\n".join([f"• {insight}" for insight in insights])
            
            # General conversation
            else:
                response = self._generate_general_response(user_input)
            
            # Add to conversation history
            self.add_to_conversation(user_input, response)
            return response
            
        except Exception as e:
            error_response = f"I encountered an error: {str(e)}. Please try again or ask for help."
            self.add_to_conversation(user_input, error_response)
            return error_response
    
    def _get_help_message(self):
        """Generate help message"""
        return """
🤖 **AI Assistant Help**

I can help you with data analysis using pandas! Here's what I can do:

**Data Operations:**
• `load_data(file_path)` - Load CSV/Excel files
• `analyze_data(dataset, type)` - Perform analysis (overview, statistical, correlation, clustering)
• `query_data(dataset, question)` - Ask questions about your data
• `generate_insights(dataset)` - Get automated insights

**Visualization:**
• `create_visualization(dataset, type)` - Create plots (correlation_heatmap, distribution)

**Example queries:**
• "What's the shape of my data?"
• "Show me missing values"
• "What are the mean values?"
• "Analyze my data"
• "Give me insights"

**Supported file formats:** CSV, Excel (.xlsx, .xls)

Just ask me anything about your data and I'll help you analyze it! 📊
        """
    
    def _format_analysis_response(self, analysis, dataset_name):
        """Format analysis results for display"""
        response = f"📊 **Analysis Results for {dataset_name}:**\n\n"
        
        if "shape" in analysis:
            response += f"• **Dataset Shape:** {analysis['shape'][0]} rows × {analysis['shape'][1]} columns\n"
        
        if "missing_data" in analysis:
            missing = {k: v for k, v in analysis['missing_data'].items() if v > 0}
            if missing:
                response += f"• **Missing Values:** {missing}\n"
            else:
                response += "• **Missing Values:** None\n"
        
        if "duplicate_rows" in analysis:
            response += f"• **Duplicate Rows:** {analysis['duplicate_rows']}\n"
        
        if "numeric_summary" in analysis:
            response += "• **Numeric Columns:** " + ", ".join(analysis['numeric_summary'].keys()) + "\n"
        
        if "categorical_summary" in analysis:
            response += "• **Categorical Columns:** " + ", ".join(analysis['categorical_summary'].keys()) + "\n"
        
        response += "\nFor more detailed analysis, try asking for insights or specific queries!"
        return response
    
    def _generate_general_response(self, user_input):
        """Generate response for general conversation"""
        responses = [
            "I'm here to help you analyze data with pandas! Do you have a dataset you'd like to explore?",
            "I can help you load, analyze, and visualize data. What would you like to do?",
            "I'm your AI data analysis assistant. Try loading a CSV or Excel file to get started!",
            "Let me help you with data analysis. Type 'help' to see what I can do!",
            "I specialize in data analysis using pandas. What data questions can I help you answer?"
        ]
        
        # Simple keyword-based responses
        input_lower = user_input.lower()
        if any(word in input_lower for word in ["hello", "hi", "hey"]):
            return "Hello! I'm your AI data analysis assistant. I can help you explore and analyze datasets using pandas. What would you like to do today?"
        elif any(word in input_lower for word in ["thanks", "thank you"]):
            return "You're welcome! I'm happy to help with your data analysis needs. Is there anything else you'd like to explore?"
        elif any(word in input_lower for word in ["goodbye", "bye", "see you"]):
            return "Goodbye! Feel free to come back anytime you need help with data analysis. Have a great day!"
        else:
            import random
            return random.choice(responses)


# Example usage and testing
if __name__ == "__main__":
    # Create an instance of the AI Assistant
    assistant = AIAssistant()
    
    print("🤖 AI Assistant initialized!")
    print("Type 'help' for available commands or 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Assistant: Goodbye!")
            break
        
        response = assistant.process_request(user_input)
        print(f"Assistant: {response}")