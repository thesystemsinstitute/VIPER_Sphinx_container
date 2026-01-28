"""Data processors."""

from typing import Any, Callable, Dict, List

class DataProcessor:
    """
    Generic data processor.
    
    Parameters
    ----------
    transformations : List[Callable], optional
        List of transformation functions to apply
    
    Examples
    --------
    >>> processor = DataProcessor()
    >>> result = processor.process(data)
    """
    
    def __init__(self, transformations: List[Callable] = None):
        self.transformations = transformations or []
    
    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process data through all transformations.
        
        Parameters
        ----------
        data : List[Dict[str, Any]]
            Input data
        
        Returns
        -------
        List[Dict[str, Any]]
            Processed data
        """
        result = data
        for transform in self.transformations:
            result = [transform(item) for item in result]
        return result

class FilterProcessor(DataProcessor):
    """
    Processor that filters data based on conditions.
    
    Parameters
    ----------
    filter_func : Callable, optional
        Function to filter items
    """
    
    def __init__(self, filter_func: Callable = None):
        super().__init__()
        self.filter_func = filter_func
    
    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter data using the filter function."""
        if self.filter_func:
            return [item for item in data if self.filter_func(item)]
        return data

class TransformProcessor(DataProcessor):
    """
    Processor that transforms data fields.
    
    Parameters
    ----------
    field_mapping : Dict[str, str], optional
        Mapping of old field names to new field names
    """
    
    def __init__(self, field_mapping: Dict[str, str] = None):
        super().__init__()
        self.field_mapping = field_mapping or {}
    
    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Transform field names in the data."""
        result = []
        for item in data:
            new_item = {}
            for key, value in item.items():
                new_key = self.field_mapping.get(key, key)
                new_item[new_key] = value
            result.append(new_item)
        return result
