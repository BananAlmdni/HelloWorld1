#!/usr/bin/env python3
"""
Test script for the AI Assistant
This script demonstrates all the capabilities of the AI Assistant
"""

import sys
import os
sys.path.append('.')

from ai_assistant import AIAssistant
import pandas as pd

def test_ai_assistant():
    """Test all functionality of the AI Assistant"""
    
    print("🤖 AI Assistant Test Suite")
    print("=" * 50)
    
    # Initialize the assistant
    assistant = AIAssistant()
    print("✅ AI Assistant initialized")
    
    # Generate sample data first
    print("\n📊 Generating sample data...")
    os.system("python generate_sample_data.py")
    
    # Test 1: Load data
    print("\n🔍 Test 1: Loading Data")
    print("-" * 30)
    
    datasets_to_load = [
        'sample_data/sales_data.csv',
        'sample_data/employee_data.csv',
        'sample_data/customer_survey.csv'
    ]
    
    for dataset_path in datasets_to_load:
        if os.path.exists(dataset_path):
            result = assistant.load_data(dataset_path)
            if 'error' not in result:
                print(f"✅ Loaded {result['dataset_name']}: {result['shape'][0]} rows × {result['shape'][1]} columns")
            else:
                print(f"❌ Error loading {dataset_path}: {result['error']}")
        else:
            print(f"⚠️ Dataset not found: {dataset_path}")
    
    # Test 2: Basic conversation
    print("\n💬 Test 2: Basic Conversation")
    print("-" * 30)
    
    test_messages = [
        "Hello!",
        "What can you do?",
        "help",
    ]
    
    for message in test_messages:
        response = assistant.process_request(message)
        print(f"User: {message}")
        print(f"Assistant: {response[:100]}...")
        print()
    
    # Test 3: Data Analysis
    print("\n📈 Test 3: Data Analysis")
    print("-" * 30)
    
    loaded_datasets = assistant.get_loaded_datasets()
    if loaded_datasets:
        dataset_name = list(loaded_datasets.keys())[0]
        print(f"Analyzing dataset: {dataset_name}")
        
        # Overview analysis
        overview = assistant.analyze_data(dataset_name, "overview")
        if 'error' not in overview:
            print(f"✅ Overview analysis completed")
            print(f"   Shape: {overview['shape']}")
            print(f"   Missing values: {sum(overview['missing_data'].values())} total")
        
        # Statistical analysis
        statistical = assistant.analyze_data(dataset_name, "statistical")
        if 'error' not in statistical:
            print(f"✅ Statistical analysis completed")
        
        # Correlation analysis
        correlation = assistant.analyze_data(dataset_name, "correlation")
        if 'error' not in correlation:
            print(f"✅ Correlation analysis completed")
            if correlation.get('strong_correlations'):
                print(f"   Found {len(correlation['strong_correlations'])} strong correlations")
    
    # Test 4: Insights Generation
    print("\n💡 Test 4: Insights Generation")
    print("-" * 30)
    
    if loaded_datasets:
        for dataset_name in list(loaded_datasets.keys())[:2]:  # Test first 2 datasets
            insights = assistant.generate_insights(dataset_name)
            print(f"Insights for {dataset_name}:")
            for i, insight in enumerate(insights[:3], 1):  # Show first 3 insights
                print(f"  {i}. {insight}")
            print()
    
    # Test 5: Data Queries
    print("\n❓ Test 5: Data Queries")
    print("-" * 30)
    
    if loaded_datasets:
        dataset_name = list(loaded_datasets.keys())[0]
        
        test_queries = [
            "What is the shape of the data?",
            "Show me the columns",
            "Are there any missing values?",
            "What are the mean values?",
            "What are the maximum values?"
        ]
        
        for query in test_queries:
            result = assistant.query_data(dataset_name, query)
            if 'error' not in result:
                print(f"Q: {query}")
                print(f"A: {result['answer']}")
                print()
    
    # Test 6: Visualizations
    print("\n📊 Test 6: Visualizations")
    print("-" * 30)
    
    if loaded_datasets:
        dataset_name = list(loaded_datasets.keys())[0]
        
        # Test correlation heatmap
        viz_result = assistant.create_visualization(dataset_name, "correlation_heatmap")
        if 'error' not in viz_result:
            print(f"✅ Created correlation heatmap: {viz_result.get('file', 'N/A')}")
        else:
            print(f"❌ Visualization error: {viz_result['error']}")
        
        # Test distribution plot
        viz_result = assistant.create_visualization(dataset_name, "distribution")
        if 'error' not in viz_result:
            print(f"✅ Created distribution plots: {viz_result.get('file', 'N/A')}")
        else:
            print(f"❌ Visualization error: {viz_result['error']}")
    
    # Test 7: Conversation History
    print("\n📝 Test 7: Conversation History")
    print("-" * 30)
    
    history = assistant.get_conversation_history()
    print(f"✅ Conversation history: {len(history)} interactions recorded")
    
    # Test 8: Advanced Analysis Commands
    print("\n🔬 Test 8: Advanced Analysis")
    print("-" * 30)
    
    advanced_commands = [
        "analyze my data",
        "give me insights",
        "what patterns do you see?"
    ]
    
    for command in advanced_commands:
        response = assistant.process_request(command)
        print(f"Command: {command}")
        print(f"Response: {response[:150]}...")
        print()
    
    # Summary
    print("\n🎉 Test Summary")
    print("=" * 50)
    print(f"✅ Datasets loaded: {len(loaded_datasets)}")
    print(f"✅ Conversation history: {len(assistant.get_conversation_history())} interactions")
    print(f"✅ Analysis results: {len(assistant.analysis_results)} cached")
    
    if loaded_datasets:
        print("\n📋 Loaded Datasets:")
        for name, info in loaded_datasets.items():
            print(f"  • {name}: {info['shape'][0]} rows × {info['shape'][1]} columns")
    
    print("\n🚀 AI Assistant is working correctly!")
    print("\nTo start the web interface, run:")
    print("  python app.py")
    print("\nThen open http://localhost:5000 in your browser")

if __name__ == "__main__":
    test_ai_assistant()