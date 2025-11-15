"""
Advanced Data Visualization Agent Examples
Demonstrates real-world usage patterns
"""
import pandas as pd
from src.agent import create_agent


def example_1_basic_query():
    """Example 1: Basic Data Query"""
    print("\n" + "="*60)
    print("Example 1: Basic Data Query")
    print("="*60)
    
    # Load sample data
    df = pd.read_csv(
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
        "ZNoKMJ9rssJn-QbJ49kOzA/student-mat.csv"
    )
    
    agent = create_agent(df)
    
    # Simple query
    response = agent.query("How many students are in the dataset?")
    print(f"Query: How many students are in the dataset?")
    print(f"Response: {response['output']}")


def example_2_data_summary():
    """Example 2: Get Data Summary"""
    print("\n" + "="*60)
    print("Example 2: Data Summary")
    print("="*60)
    
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'salary': [50000, 60000, 70000]
    })
    
    agent = create_agent(df)
    summary = agent.get_data_summary()
    
    print(f"Shape: {summary['shape']}")
    print(f"Columns: {summary['columns']}")
    print(f"Data Types: {summary['dtypes']}")


def example_3_visualization_query():
    """Example 3: Visualization Query"""
    print("\n" + "="*60)
    print("Example 3: Visualization Query")
    print("="*60)
    
    df = pd.read_csv(
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
        "ZNoKMJ9rssJn-QbJ49kOzA/student-mat.csv"
    )
    
    agent = create_agent(df)
    
    # Visualization query
    response = agent.query(
        "Create a bar chart showing the distribution of students by gender"
    )
    print(f"Response: {response['output']}")
    
    # Show generated code
    code = agent.get_agent_code(response)
    if code:
        print(f"\nGenerated Code:\n{code}")


def example_4_statistical_analysis():
    """Example 4: Statistical Analysis"""
    print("\n" + "="*60)
    print("Example 4: Statistical Analysis")
    print("="*60)
    
    df = pd.read_csv(
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
        "ZNoKMJ9rssJn-QbJ49kOzA/student-mat.csv"
    )
    
    agent = create_agent(df)
    
    # Statistical query
    response = agent.query(
        "What is the correlation between study time and final grades?"
    )
    print(f"Response: {response['output']}")


def example_5_complex_analysis():
    """Example 5: Complex Data Analysis"""
    print("\n" + "="*60)
    print("Example 5: Complex Data Analysis")
    print("="*60)
    
    df = pd.read_csv(
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
        "ZNoKMJ9rssJn-QbJ49kOzA/student-mat.csv"
    )
    
    agent = create_agent(df)
    
    # Complex query
    response = agent.query(
        "Analyze the relationship between alcohol consumption and academic performance. "
        "Show me the average final grade for different levels of alcohol consumption."
    )
    print(f"Response: {response['output']}")


def example_6_intermediate_steps():
    """Example 6: Inspect Intermediate Steps"""
    print("\n" + "="*60)
    print("Example 6: Intermediate Steps")
    print("="*60)
    
    df = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]
    })
    
    agent = create_agent(df)
    
    response = agent.query("What is the average value of x?")
    
    print(f"Output: {response['output']}")
    
    # Show intermediate steps
    steps = agent.get_intermediate_steps(response)
    print(f"\nNumber of intermediate steps: {len(steps)}")
    
    for i, (action, observation) in enumerate(steps):
        print(f"\nStep {i+1}:")
        print(f"  Action: {action.tool}")
        print(f"  Input: {action.tool_input}")
        print(f"  Observation: {observation}")


if __name__ == "__main__":
    print("Data Visualization Agent Examples")
    print("Demonstrating real-world usage patterns")
    
    try:
        example_1_basic_query()
        example_2_data_summary()
        # Uncomment to run visualization examples (requires API key)
        # example_3_visualization_query()
        # example_4_statistical_analysis()
        # example_5_complex_analysis()
        # example_6_intermediate_steps()
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure OPENROUTER_API_KEY is set in .env file")

