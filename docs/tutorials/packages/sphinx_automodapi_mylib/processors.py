"""
Data Processor Classes
======================

Classes for processing and transforming data.
"""

from typing import Any, Callable, Dict, List, Optional


class DataProcessor:
    """
    Generic data processor for applying transformations.
    
    Parameters
    ----------
    data : Any
        Input data to process
    config : Dict[str, Any], optional
        Processing configuration options
        
    Attributes
    ----------
    data : Any
        The data being processed
    config : Dict[str, Any]
        Processing configuration
    operations : List[Callable]
        List of operations to apply
        
    Examples
    --------
    >>> processor = DataProcessor(data, config={'normalize': True})
    >>> result = processor.process()
    """
    
    def __init__(self, data: Any, config: Optional[Dict[str, Any]] = None):
        self.data = data
        self.config = config or {}
        self.operations: List[Callable] = []
    
    def add_operation(self, operation: Callable) -> 'DataProcessor':
        """
        Add a processing operation.
        
        Parameters
        ----------
        operation : Callable
            Function to apply to data
            
        Returns
        -------
        DataProcessor
            Self for method chaining
            
        Examples
        --------
        >>> processor.add_operation(normalize).add_operation(filter_outliers)
        """
        self.operations.append(operation)
        return self
    
    def process(self) -> Any:
        """
        Execute all operations on the data.
        
        Returns
        -------
        Any
            Processed data
            
        Raises
        ------
        ValueError
            If no operations are defined
        """
        if not self.operations:
            raise ValueError("No operations defined")
        
        result = self.data
        for operation in self.operations:
            result = operation(result)
        return result


class FilterProcessor:
    """
    Filter data based on conditions.
    
    Parameters
    ----------
    data : List[Any]
        Input data to filter
    conditions : List[Callable], optional
        Filter conditions to apply
        
    Examples
    --------
    >>> processor = FilterProcessor(data)
    >>> processor.add_condition(lambda x: x > 0)
    >>> filtered = processor.filter()
    """
    
    def __init__(self, data: List[Any], conditions: Optional[List[Callable]] = None):
        self.data = data
        self.conditions = conditions or []
    
    def add_condition(self, condition: Callable[[Any], bool]) -> 'FilterProcessor':
        """
        Add a filter condition.
        
        Parameters
        ----------
        condition : Callable[[Any], bool]
            Filtering function
            
        Returns
        -------
        FilterProcessor
            Self for method chaining
        """
        self.conditions.append(condition)
        return self
    
    def filter(self) -> List[Any]:
        """
        Apply all filter conditions.
        
        Returns
        -------
        List[Any]
            Filtered data
        """
        result = self.data
        for condition in self.conditions:
            result = [item for item in result if condition(item)]
        return result

    def process(self) -> List[Any]:
        """
        Alias for ``filter`` to support autosummary expectations.

        Returns
        -------
        List[Any]
            Filtered data
        """
        return self.filter()


class TransformProcessor:
    """
    Transform data using mapping functions.
    
    Parameters
    ----------
    data : Any
        Input data to transform
    transformers : Dict[str, Callable], optional
        Named transformation functions
        
    Attributes
    ----------
    data : Any
        The data being transformed
    transformers : Dict[str, Callable]
        Available transformation functions
        
    Examples
    --------
    >>> processor = TransformProcessor(data)
    >>> processor.register('uppercase', str.upper)
    >>> result = processor.apply('uppercase')
    """
    
    def __init__(self, data: Any, transformers: Optional[Dict[str, Callable]] = None):
        self.data = data
        self.transformers = transformers or {}
    
    def register(self, name: str, transformer: Callable) -> 'TransformProcessor':
        """
        Register a transformation function.
        
        Parameters
        ----------
        name : str
            Transformer name
        transformer : Callable
            Transformation function
            
        Returns
        -------
        TransformProcessor
            Self for method chaining
        """
        self.transformers[name] = transformer
        return self
    
    def apply(self, name: str) -> Any:
        """
        Apply a registered transformer.
        
        Parameters
        ----------
        name : str
            Name of transformer to apply
            
        Returns
        -------
        Any
            Transformed data
            
        Raises
        ------
        KeyError
            If transformer name not registered
        """
        if name not in self.transformers:
            raise KeyError(f"Transformer '{name}' not registered")
        return self.transformers[name](self.data)

    def process(self) -> Any:
        """
        Alias for applying a default transformer named ``default``.

        Returns
        -------
        Any
            Transformed data
        """
        if 'default' not in self.transformers:
            raise KeyError("Transformer 'default' not registered")
        return self.apply('default')
