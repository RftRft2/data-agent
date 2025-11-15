"""
Main entry point for Data Visualization Agent
Example usage demonstrating LangChain LCEL capabilities
"""
import pandas as pd
from src.agent import create_agent


def main():
    """Main function demonstrating the Data Visualization Agent"""
    
    # Load sample data
    print("Loading sample data...")
    df = pd.read_csv(
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
        "ZNoKMJ9rssJn-QbJ49kOzA/student-mat.csv"
    )
    
    print(f"Data shape: {df.shape}")
    print(f"Columns: {list(df.columns)}\n")
    
    # Create agent
    print("Initializing Data Visualization Agent...")
    agent = create_agent(df)
    
    # Example queries
    queries = [
        "How many rows of data are in this file?",
        "What is the average final grade (G3)?",
        "Generate a bar chart showing gender distribution.",
    ]
    
    for query in queries:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print('='*60)
        
        response = agent.query(query)
        print(f"\nResponse: {response['output']}")
        
        # Show generated code if available
        code = agent.get_agent_code(response)
        if code:
            print(f"\nGenerated Code:\n{code}")


if __name__ == "__main__":
    main()

