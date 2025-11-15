"""
Advanced LangChain LCEL Examples
Demonstrates LCEL chains, pipes, runnables, and composition patterns
"""
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, AIMessage
from langchain.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from src.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, MODEL_NAME


def example_1_basic_lcel_chain():
    """Example 1: Basic LCEL Chain with Pipe Operator"""
    print("\n" + "="*60)
    print("Example 1: Basic LCEL Chain")
    print("="*60)
    
    llm = ChatOpenAI(
        model_name=MODEL_NAME,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
    )
    
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="Tell me a short fact about {topic}"
    )
    
    # LCEL Chain using pipe operator
    chain = prompt | llm | StrOutputParser()
    
    result = chain.invoke({"topic": "Python"})
    print(f"Result: {result}")


def example_2_runnable_passthrough():
    """Example 2: Runnable with Passthrough"""
    print("\n" + "="*60)
    print("Example 2: Runnable with Passthrough")
    print("="*60)
    
    llm = ChatOpenAI(
        model_name=MODEL_NAME,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
    )
    
    prompt = PromptTemplate(
        input_variables=["input"],
        template="Analyze this data: {input}"
    )
    
    # Chain with RunnablePassthrough
    chain = (
        {"input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    result = chain.invoke("Sales data for Q1 2024")
    print(f"Result: {result}")


def example_3_runnable_lambda():
    """Example 3: Runnable with Lambda Functions"""
    print("\n" + "="*60)
    print("Example 3: Runnable with Lambda Functions")
    print("="*60)
    
    llm = ChatOpenAI(
        model_name=MODEL_NAME,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
    )
    
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize: {text}"
    )
    
    # Chain with RunnableLambda for preprocessing
    def preprocess(text):
        return {"text": text.upper()}
    
    chain = (
        RunnableLambda(preprocess)
        | prompt
        | llm
        | StrOutputParser()
    )
    
    result = chain.invoke("This is important data")
    print(f"Result: {result}")


def example_4_complex_composition():
    """Example 4: Complex Chain Composition"""
    print("\n" + "="*60)
    print("Example 4: Complex Chain Composition")
    print("="*60)
    
    llm = ChatOpenAI(
        model_name=MODEL_NAME,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
    )
    
    # Multiple prompts
    analysis_prompt = PromptTemplate(
        input_variables=["data"],
        template="Analyze this data: {data}"
    )
    
    summary_prompt = PromptTemplate(
        input_variables=["analysis"],
        template="Summarize this analysis: {analysis}"
    )
    
    # Complex chain
    chain = (
        {"data": RunnablePassthrough()}
        | analysis_prompt
        | llm
        | StrOutputParser()
        | RunnableLambda(lambda x: {"analysis": x})
        | summary_prompt
        | llm
        | StrOutputParser()
    )
    
    result = chain.invoke("Customer satisfaction scores: 8.5/10")
    print(f"Result: {result}")


def example_5_data_processing_chain():
    """Example 5: Data Processing Chain"""
    print("\n" + "="*60)
    print("Example 5: Data Processing Chain")
    print("="*60)
    
    # Create sample data
    df = pd.DataFrame({
        'product': ['A', 'B', 'C'],
        'sales': [100, 200, 150]
    })
    
    def format_data(df):
        return {"data": df.to_string()}
    
    llm = ChatOpenAI(
        model_name=MODEL_NAME,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
    )
    
    prompt = PromptTemplate(
        input_variables=["data"],
        template="Analyze this sales data:\n{data}"
    )
    
    # Data processing chain
    chain = (
        RunnableLambda(lambda _: df)
        | RunnableLambda(format_data)
        | prompt
        | llm
        | StrOutputParser()
    )
    
    result = chain.invoke(None)
    print(f"Result: {result}")


if __name__ == "__main__":
    print("LangChain LCEL Examples")
    print("Demonstrating advanced chain composition patterns")
    
    try:
        example_1_basic_lcel_chain()
        example_2_runnable_passthrough()
        example_3_runnable_lambda()
        example_4_complex_composition()
        example_5_data_processing_chain()
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure OPENROUTER_API_KEY is set in .env file")

