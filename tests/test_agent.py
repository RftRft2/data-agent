"""
Unit tests for Data Visualization Agent
"""
import unittest
import pandas as pd
from src.config import MODEL_NAME, OPENROUTER_API_KEY


class TestConfiguration(unittest.TestCase):
    """Test configuration values"""

    def test_model_name_configured(self):
        """Test that model name is configured"""
        self.assertIsNotNone(MODEL_NAME)
        self.assertIsInstance(MODEL_NAME, str)
        self.assertGreater(len(MODEL_NAME), 0)

    def test_model_name_contains_mistral(self):
        """Test that model name contains mistral"""
        self.assertIn('mistral', MODEL_NAME.lower())


class TestDataFrameHandling(unittest.TestCase):
    """Test DataFrame handling"""

    def setUp(self):
        """Set up test fixtures"""
        self.sample_df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie', 'David'],
            'age': [25, 30, 35, 40],
            'salary': [50000, 60000, 70000, 80000],
            'department': ['Sales', 'IT', 'HR', 'Finance']
        })

    def test_dataframe_shape(self):
        """Test DataFrame shape"""
        self.assertEqual(self.sample_df.shape, (4, 4))

    def test_dataframe_columns(self):
        """Test DataFrame columns"""
        expected_columns = ['name', 'age', 'salary', 'department']
        self.assertEqual(list(self.sample_df.columns), expected_columns)

    def test_dataframe_dtypes(self):
        """Test DataFrame data types"""
        self.assertEqual(self.sample_df['age'].dtype, 'int64')
        self.assertEqual(self.sample_df['salary'].dtype, 'int64')


class TestToolsImport(unittest.TestCase):
    """Test tools import"""

    def test_tools_can_be_imported(self):
        """Test that tools can be imported"""
        try:
            from src.tools import get_tools
            tools = get_tools()
            self.assertIsInstance(tools, list)
            self.assertGreater(len(tools), 0)
        except ImportError:
            self.fail("Could not import tools")


if __name__ == '__main__':
    unittest.main()

