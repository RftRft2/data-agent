"""
Configuration module for Data Visualization Agent
Enhanced with logging and additional customization options
"""
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# OpenRouter Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Model Configuration
MODEL_NAME = os.getenv("MODEL_NAME", "mistralai/mistral-7b-instruct")
MODEL_TEMPERATURE = float(os.getenv("MODEL_TEMPERATURE", "0.0"))
MODEL_MAX_TOKENS = int(os.getenv("MODEL_MAX_TOKENS", "2048"))

# Agent Configuration
AGENT_VERBOSE = os.getenv("AGENT_VERBOSE", "True").lower() == "true"
AGENT_RETURN_INTERMEDIATE_STEPS = os.getenv("AGENT_RETURN_INTERMEDIATE_STEPS", "True").lower() == "true"
AGENT_HANDLE_PARSING_ERRORS = os.getenv("AGENT_HANDLE_PARSING_ERRORS", "True").lower() == "true"

# Visualization Configuration
PLOT_STYLE = os.getenv("PLOT_STYLE", "seaborn-v0_8-darkgrid")
FIGURE_SIZE_WIDTH = int(os.getenv("FIGURE_SIZE_WIDTH", "12"))
FIGURE_SIZE_HEIGHT = int(os.getenv("FIGURE_SIZE_HEIGHT", "6"))
FIGURE_SIZE = (FIGURE_SIZE_WIDTH, FIGURE_SIZE_HEIGHT)
DPI = int(os.getenv("DPI", "100"))

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "agent.log")

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

