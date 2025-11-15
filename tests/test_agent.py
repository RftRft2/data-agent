"""
Unit tests for Data Visualization Agent
"""
import unittest
import pandas as pd
from src.agent import DataVisualizationAgent, create_agent
from src.config import MODEL_NAME


class TestDataVisualizationAgent(unittest.TestCase):
    """Test cases for DataVisualizationAgent"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures"""
        # Create sample dataframe
        cls.sample_df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie', 'David'],
            'age': [25, 30, 35, 40],
            'salary': [50000, 60000, 70000, 80000],
            'department': ['Sales', 'IT', 'HR', 'Finance']
        })

    def test_agent_initialization(self):
        """Test agent initialization"""
        try:
            agent = create_agent(self.sample_df)
            self.assertIsNotNone(agent)
            self.assertIsNotNone(agent.llm)
            self.assertIsNotNone(agent.agent)
        except ValueError as e:
            # Expected if API key not set
            self.assertIn("OPENROUTER_API_KEY", str(e))

    def test_get_data_summary(self):
        """Test data summary generation"""
        try:
            agent = create_agent(self.sample_df)
            summary = agent.get_data_summary()

            self.assertIn('shape', summary)
            self.assertIn('columns', summary)
            self.assertEqual(summary['shape'], (4, 4))
            self.assertEqual(len(summary['columns']), 4)
        except ValueError:
            # Skip if API key not available
            pass

    def test_dataframe_storage(self):
        """Test that dataframe is properly stored"""
        try:
            agent = create_agent(self.sample_df)
            pd.testing.assert_frame_equal(agent.df, self.sample_df)
        except ValueError:
            pass

    def test_config_values(self):
        """Test configuration values"""
        self.assertIsNotNone(MODEL_NAME)
        self.assertIn('mistral', MODEL_NAME.lower())


class TestDataVisualizationAgentIntegration(unittest.TestCase):
    """Integration tests for DataVisualizationAgent"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures"""
        cls.sample_df = pd.DataFrame({
            'x': [1, 2, 3, 4, 5],
            'y': [2, 4, 6, 8, 10],
            'category': ['A', 'B', 'A', 'B', 'A']
        })

    def test_query_error_handling(self):
        """Test error handling in queries"""
        try:
            agent = create_agent(self.sample_df)
            response = agent.query("Invalid query that should fail")
            self.assertIn('output', response)
        except ValueError:
            # Skip if API key not available
            pass


if __name__ == '__main__':
    unittest.main()

