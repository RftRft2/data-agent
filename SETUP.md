# Setup Instructions

## GitHub Repository Setup

To push this project to GitHub, follow these steps:

### 1. Create a new repository on GitHub

1. Go to https://github.com/new
2. Repository name: `data-visualization-agent`
3. Description: "Advanced Data Visualization Agent using LangChain LCEL, OpenRouter, and Pandas DataFrame Agent"
4. Choose "Public" for visibility
5. Do NOT initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### 2. Add remote and push

```bash
# Add the remote repository
git remote add origin https://github.com/altuyerli/data-visualization-agent.git

# Rename branch to main if needed
git branch -M main

# Push to GitHub
git push -u origin main
```

### 3. Verify

Visit `https://github.com/altugyerli/data-visualization-agent` to see your repository.

## Local Development Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API key

```bash
cp .env.example .env
# Edit .env and add your OpenRouter API key
```

Get a free API key from: https://openrouter.ai

### 3. Run tests

```bash
python -m pytest tests/ -v
```

### 4. Run examples

```bash
# Basic example
python main.py

# LCEL examples
python examples_lcel.py

# Agent examples
python examples_agent.py
```

## Project Structure

```
data-visualization-agent/
├── src/
│   ├── __init__.py
│   ├── agent.py           # Main agent class
│   ├── tools.py           # Custom visualization tools
│   └── config.py          # Configuration
├── tests/
│   ├── __init__.py
│   └── test_agent.py      # Unit tests
├── examples_lcel.py       # LCEL examples
├── examples_agent.py      # Agent examples
├── main.py               # Main entry point
├── requirements.txt      # Dependencies
├── .env.example         # Environment template
├── README.md            # Project documentation
└── SETUP.md            # This file
```

## Troubleshooting

### Import errors

If you get import errors, make sure all dependencies are installed:
```bash
pip install -r requirements.txt --upgrade
```

### API key not found

Make sure you have created a `.env` file with your OpenRouter API key:
```bash
cp .env.example .env
# Edit .env and add OPENROUTER_API_KEY=your_key_here
```

### Test failures

Run tests with verbose output:
```bash
python -m pytest tests/ -v -s
```

## Next Steps

1. Push to GitHub
2. Add topics: `langchain`, `llm`, `data-visualization`, `openrouter`
3. Add a GitHub Actions workflow for CI/CD
4. Create releases for stable versions

