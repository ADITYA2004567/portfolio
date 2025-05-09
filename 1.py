import pandas as pd
from abc import ABC, abstractmethod

# Load the data file
file_path = "C:/Users/Sharm/Downloads/CaMS Test Case Document Sprint 1.xlsx"

# Read the Excel file and check sheet names
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names
print(f"Available sheets: {sheet_names}")

# Load the first sheet as a DataFrame
data = pd.read_excel(xls, sheet_names[0])

# Display basic info about the data
data_info = data.info()
print(data_info)

# Display the first few rows of the data
head_data = data.head()
print(head_data)

# Abstraction: Abstract base class for data analysis
class AbstractAnalyzer(ABC):
    def __init__(self, data):
        self._data = data  # Protected attribute

    @abstractmethod
    def analyze(self):
        pass

# Inheritance: Concrete class implementing analysis methods
class SummaryAnalyzer(AbstractAnalyzer):
    def analyze(self):
        return self._data.describe()

class NullsAnalyzer(AbstractAnalyzer):
    def analyze(self):
        return self._data.isnull().sum()

class TypesAnalyzer(AbstractAnalyzer):
    def analyze(self):
        return self._data.dtypes

# Create instances of the concrete analyzers
summary_analyzer = SummaryAnalyzer(data)
nulls_analyzer = NullsAnalyzer(data)
types_analyzer = TypesAnalyzer(data)

# Perform different types of analysis
print("\nSummary statistics:\n", summary_analyzer.analyze())
print("\nNull values count:\n", nulls_analyzer.analyze())
print("\nData types:\n", types_analyzer.analyze())
