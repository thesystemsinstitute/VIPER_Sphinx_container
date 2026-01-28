"""Data writers."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List
import csv
import json

class BaseWriter(ABC):
    """Base class for data writers."""
    
    @abstractmethod
    def write(self, data: List[Dict[str, Any]], filepath: str) -> None:
        """Write data to file."""
        pass

class CSVWriter(BaseWriter):
    """CSV file writer."""
    
    def write(self, data: List[Dict[str, Any]], filepath: str) -> None:
        """Write data to CSV file."""
        if not data:
            return
        
        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

class JSONWriter(BaseWriter):
    """JSON file writer."""
    
    def write(self, data: List[Dict[str, Any]], filepath: str) -> None:
        """Write data to JSON file."""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

class XMLWriter(BaseWriter):
    """XML file writer."""
    
    def write(self, data: List[Dict[str, Any]], filepath: str) -> None:
        """Write data to XML file."""
        import xml.etree.ElementTree as ET
        root = ET.Element('data')
        for item in data:
            elem = ET.SubElement(root, 'item')
            for key, value in item.items():
                elem.set(key, str(value))
        tree = ET.ElementTree(root)
        tree.write(filepath, encoding='utf-8', xml_declaration=True)
