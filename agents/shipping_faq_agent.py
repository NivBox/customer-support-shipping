# -*- coding: utf-8 -*-
"""agents/shipping_faq_agent.py
FAQ Agent answering common shipping questions.
"""

class ShippingFAQAgent:
    def __init__(self):
        self.faqs = {
            "rates": "Our standard domestic shipping starts at $5.99. Express is $14.99. International rates vary by destination.",
            "tracking": "You can track your package by entering your tracking number on our website's tracking page.",
            "delivery": "Standard delivery takes 3-5 business days. Express delivery takes 1-2 business days.",
            "returns": "We offer free returns within 30 days of delivery. Please print a return label from our online portal."
        }

    def run(self, data: dict) -> dict:
        """Process the shipping query and return an FAQ answer.
        
        Args:
            data: Incoming data dictionary.
            
        Returns:
            dict: {"response": str}
        """
        query = data.get("query", "") or data.get("message", "")
        normalized = str(query).lower()
        
        # Match specific topics within the shipping query
        if "rate" in normalized or "cost" in normalized or "price" in normalized:
            response = self.faqs["rates"]
        elif "track" in normalized or "where is" in normalized:
            response = self.faqs["tracking"]
        elif "return" in normalized or "refund" in normalized or "exchange" in normalized:
            response = self.faqs["returns"]
        else:
            # General shipping or delivery query
            response = self.faqs["delivery"]
            
        return {"response": response}
