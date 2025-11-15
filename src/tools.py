"""
Custom tools for Data Visualization Agent
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Any, Dict, List
from langchain.tools import tool
from src.config import PLOT_STYLE, FIGURE_SIZE, DPI


@tool
def create_bar_chart(data: Dict[str, List], title: str, xlabel: str, ylabel: str) -> str:
    """Create a bar chart from data"""
    try:
        plt.figure(figsize=FIGURE_SIZE)
        plt.style.use(PLOT_STYLE)

        x = list(data.keys())
        y = list(data.values())

        plt.bar(x, y, color='steelblue', edgecolor='black', alpha=0.7)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('output_chart.png', dpi=DPI, bbox_inches='tight')
        plt.close()

        return "Bar chart created successfully and saved as 'output_chart.png'"
    except Exception as e:
        return f"Error creating bar chart: {str(e)}"


@tool
def create_line_chart(data: Dict[str, List], title: str, xlabel: str, ylabel: str) -> str:
    """Create a line chart from data"""
    try:
        plt.figure(figsize=FIGURE_SIZE)
        plt.style.use(PLOT_STYLE)

        for label, values in data.items():
            plt.plot(values, marker='o', label=label, linewidth=2)

        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('output_chart.png', dpi=DPI, bbox_inches='tight')
        plt.close()

        return "Line chart created successfully and saved as 'output_chart.png'"
    except Exception as e:
        return f"Error creating line chart: {str(e)}"


@tool
def create_scatter_plot(x_data: List, y_data: List, title: str, xlabel: str, ylabel: str) -> str:
    """Create a scatter plot from data"""
    try:
        plt.figure(figsize=FIGURE_SIZE)
        plt.style.use(PLOT_STYLE)

        plt.scatter(x_data, y_data, alpha=0.6, s=100, color='steelblue', edgecolors='black')
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('output_chart.png', dpi=DPI, bbox_inches='tight')
        plt.close()

        return "Scatter plot created successfully and saved as 'output_chart.png'"
    except Exception as e:
        return f"Error creating scatter plot: {str(e)}"


def get_tools() -> List:
    """Return list of available tools"""
    return [create_bar_chart, create_line_chart, create_scatter_plot]

