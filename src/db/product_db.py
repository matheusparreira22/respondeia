"""
Module for handling product database operations.
"""
import json
import os
from typing import Dict, List, Optional, Any

class ProductDB:
    """Class for handling product database operations."""
    
    def __init__(self, db_path: str = None):
        """
        Initialize the product database.
        
        Args:
            db_path (str, optional): Path to the product database file.
                If not provided, uses the default path.
        """
        if db_path is None:
            # Get the directory of the current file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(current_dir, 'products.json')
        
        self.db_path = db_path
        self.products = self._load_products()
    
    def _load_products(self) -> List[Dict[str, Any]]:
        """
        Load products from the database file.
        
        Returns:
            List[Dict[str, Any]]: List of product dictionaries.
        """
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('products', [])
        except Exception as e:
            print(f"Error loading product database: {e}")
            return []
    
    def get_product_by_id(self, product_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a product by its ID.
        
        Args:
            product_id (str): The ID of the product to retrieve.
            
        Returns:
            Optional[Dict[str, Any]]: The product dictionary if found, None otherwise.
        """
        for product in self.products:
            if product.get('id') == product_id:
                return product
        return None
    
    def get_all_products(self) -> List[Dict[str, Any]]:
        """
        Get all products in the database.
        
        Returns:
            List[Dict[str, Any]]: List of all product dictionaries.
        """
        return self.products
