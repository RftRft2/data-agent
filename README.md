# Data Visualization Agent 📊

A powerful, production-ready data visualization agent built with **LangChain** and **OpenRouter** that transforms natural language queries into insightful data visualizations and analysis.

## 🎯 Overview

This project demonstrates advanced **LangChain** capabilities including:
- **LCEL (LangChain Expression Language)** - Modern chain composition
- **Pipe operators** - Functional composition of chains
- **Runnable interfaces** - Composable, reusable components
- **Tool integration** - Custom tools for data visualization
- **Pandas DataFrame Agent** - Intelligent data analysis
- **OpenRouter integration** - Free LLM access

## ✨ Features

- 🤖 **Natural Language Queries** - Ask questions about your data in plain English
- 📈 **Automatic Visualization** - Generate charts, graphs, and heatmaps
- 🔍 **Data Analysis** - Get insights and statistics from your data
- 🛠️ **Custom Tools** - Extensible tool system for custom operations
- 🚀 **Production Ready** - Error handling, logging, and configuration management
- 📦 **Easy Integration** - Simple API for embedding in your applications

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│         Natural Language Query                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│    LangChain LCEL Chain (Pipe Operators)               │
│  ┌──────────────┐    ┌──────────────┐                 │
│  │ Prompt       │ -> │ LLM (OpenAI) │                 │
│  └──────────────┘    └──────────────┘                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│    Pandas DataFrame Agent                              │
│  - Analyzes data structure                             │
│  - Generates Python code                               │
│  - Executes queries                                    │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│    Visualization Tools                                 │
│  - Bar Charts      - Line Charts                       │
│  - Scatter Plots   - Heatmaps                          │
│  - Custom Plots                                        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│         Visualization Output                           │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenRouter API key (free at https://openrouter.ai)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/data-viz-agent.git
cd data-viz-agent
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API key**
```bash
cp .env.example .env
# Edit .env and add your OpenRouter API key
```

### Usage

```python
import pandas as pd
from src.agent import create_agent

# Load your data
df = pd.read_csv('your_data.csv')

# Create agent
agent = create_agent(df)

# Query your data
response = agent.query("Show me a bar chart of sales by region")
print(response['output'])

# Get generated code
code = agent.get_agent_code(response)
print(code)
```

## 📚 LangChain Features Demonstrated

### 1. LCEL (LangChain Expression Language)
```python
# Modern chain composition using LCEL
chain = prompt | llm | output_parser
result = chain.invoke({"input": "your query"})
```

### 2. Pipe Operators
```python
# Functional composition
chain = (
    {"input": RunnablePassthrough()}
    | prompt
    | llm
    | output_parser
)
```

### 3. Runnable Interfaces
```python
# Composable, reusable components
class CustomRunnable(Runnable):
    def invoke(self, input):
        # Custom logic
        pass
```

### 4. Tool Integration
```python
@tool
def create_visualization(data: Dict) -> str:
    """Create a visualization from data"""
    # Implementation
    pass
```

### 5. Pandas DataFrame Agent
```python
# Intelligent data analysis
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    return_intermediate_steps=True
)
```

## 📖 Example Queries

```python
# Data Analysis
agent.query("What is the average salary by department?")
agent.query("Show me the top 5 products by revenue")

# Visualization
agent.query("Create a bar chart of monthly sales")
agent.query("Generate a scatter plot of age vs salary")
agent.query("Show me a heatmap of correlations")

# Complex Analysis
agent.query("What is the trend of sales over time?")
agent.query("Compare performance across regions")
```

## 🔧 Configuration

Edit `src/config.py` to customize:

```python
# Model Configuration
MODEL_NAME = "mistralai/mistral-7b-instruct"
MODEL_TEMPERATURE = 0.0
MODEL_MAX_TOKENS = 2048

# Agent Configuration
AGENT_VERBOSE = True
AGENT_RETURN_INTERMEDIATE_STEPS = True

# Visualization Configuration
PLOT_STYLE = "seaborn-v0_8-darkgrid"
FIGURE_SIZE = (12, 6)
```

## 📁 Project Structure

```
data-viz-agent/
├── src/
│   ├── __init__.py
│   ├── agent.py           # Main agent class
│   ├── tools.py           # Custom visualization tools
│   └── config.py          # Configuration
├── tests/
│   ├── __init__.py
│   └── test_agent.py      # Unit tests
├── data/                  # Sample data directory
├── main.py               # Example usage
├── requirements.txt      # Dependencies
├── .env.example         # Environment template
└── README.md            # This file
```

## 🧪 Testing

Run tests with:
```bash
python -m pytest tests/
# or
python -m unittest discover tests/
```

## 🔌 API Reference

### DataVisualizationAgent

#### `__init__(dataframe, api_key=None)`
Initialize the agent with a DataFrame.

#### `query(question: str) -> Dict`
Execute a natural language query.

#### `analyze_data(question: str) -> str`
Analyze data and return insights.

#### `get_data_summary() -> Dict`
Get summary statistics.

#### `get_agent_code(response: Dict) -> Optional[str]`
Extract generated code from response.

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LCEL Guide](https://python.langchain.com/docs/expression_language/)
- [OpenRouter API](https://openrouter.ai/docs)
- [Pandas Documentation](https://pandas.pydata.org/)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Powered by [OpenRouter](https://openrouter.ai/)
- Data visualization with [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/)

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ to showcase LangChain expertise**

