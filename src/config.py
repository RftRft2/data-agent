"""
Configuration module for Data Visualization Agent
"""
import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Model Configuration
MODEL_NAME = "mistralai/mistral-7b-instruct"  # Free model on OpenRouter
MODEL_TEMPERATURE = 0.0
MODEL_MAX_TOKENS = 2048

# Agent Configuration
AGENT_VERBOSE = True
AGENT_RETURN_INTERMEDIATE_STEPS = True
AGENT_HANDLE_PARSING_ERRORS = True

# Visualization Configuration
PLOT_STYLE = "seaborn-v0_8-darkgrid"
FIGURE_SIZE = (12, 6)
DPI = 100

