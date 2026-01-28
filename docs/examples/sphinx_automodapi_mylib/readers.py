"""Data readers for various formats."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List
import csv
import json
import xml.etree.ElementTree as ET

class BaseReader(ABC):
    """
    Base class for data readers.
    
    All readers should inherit from this class and implement
    the read method.
    """
    
    @abstractmethod
    def read(self, filepath: str) -> List[Dict[str, Any]]:
        """
        Read data from file.
        
        Parameters
        ----------
        filepath : str
            Path to the file to read
        
        Returns
        -------
        List[Dict[str, Any]]
            List of dictionaries containing the data
        """
        pass

class CSVReader(BaseReader):
    """
    CSV file reader.
    
    Parameters
    ----------
    delimiter : str, optional
        Field delimiter (default: ',')
    quotechar : str, optional
        Quote character (default: '"')
    
    Examples
    --------
    >>> reader = CSVReader()
    >>> data = reader.read('data.csv')
    """
    
    def __init__(self, delimiter: str = ',', quotechar: str = '"'):
        self.delimiter = delimiter
        self.quotechar = quotechar
    
    def read(self, filepath: str) -> List[Dict[str, Any]]:
        """Read CSV file."""
        with open(filepath, 'r') as f:
            reader = csv.DictReader(
                f,
                delimiter=self.delimiter,
                quotechar=self.quotechar
            )
            return list(reader)

class JSONReader(BaseReader):
    """
    JSON file reader.
    
    Examples
    --------
    >>> reader = JSONReader()
    >>> data = reader.read('data.json')
    """
    
    def read(self, filepath: str) -> List[Dict[str, Any]]:
        """Read JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return [data]

class XMLReader(BaseReader):
    """
    XML file reader.
    
    Examples
    --------
    >>> reader = XMLReader()
    >>> data = reader.read('data.xml')
    """
    
    def read(self, filepath: str) -> List[Dict[str, Any]]:
        """Read XML file."""
        tree = ET.parse(filepath)
        root = tree.getroot()
        return [elem.attrib for elem in root]
