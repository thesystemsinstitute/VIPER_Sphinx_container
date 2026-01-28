"""
Sphinx AutoModAPI Example Library
==================================

This is a demonstration library showing sphinx-automodapi capabilities.
"""

from .readers import BaseReader, CSVReader, JSONReader, XMLReader
from .processors import DataProcessor, FilterProcessor, TransformProcessor
from .writers import BaseWriter, CSVWriter, JSONWriter, XMLWriter

__version__ = "1.0.0"
__author__ = "Example Author"

__all__ = [
    'BaseReader', 'CSVReader', 'JSONReader', 'XMLReader',
    'DataProcessor', 'FilterProcessor', 'TransformProcessor',
    'BaseWriter', 'CSVWriter', 'JSONWriter', 'XMLWriter',
]
