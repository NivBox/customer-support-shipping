# -*- coding: utf-8 -*-
"""agents/classifier.py
Keyword-based classifier to check if the query is shipping-related.
"""

class ShippingClassifier:
    def __init__(self):
        # Broad keywords associated with rates, tracking, delivery, and returns
        self.keywords = [
            "shipping", "rate", "cost", "price", "track", "tracking", "where is my", 
            "delivery", "deliver", "shipment", "transit", "return", "refund", "exchange",
            "package", "parcel", "send", "postage", "carrier"
        ]

    def run(self, query: str) -> dict:
        """Classify a query.
        
        Args:
            query: The user query string.
            
        Returns:
            dict: {"is_shipping": bool}
        """
        # If the input is passed as a dict, extract the query
        if isinstance(query, dict):
            query = query.get("query", "") or query.get("message", "")
            
        normalized = str(query).lower()
        is_shipping = any(kw in normalized for kw in self.keywords)
        return {"is_shipping": is_shipping}
