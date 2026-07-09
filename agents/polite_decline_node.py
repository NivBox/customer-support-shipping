# -*- coding: utf-8 -*-
"""agents/polite_decline_node.py
Agent to politely decline answering unrelated questions.
"""

class PoliteDeclineAgent:
    def run(self, data: dict) -> dict:
        """Politely decline the user request.
        
        Args:
            data: Incoming data dictionary.
            
        Returns:
            dict: {"response": str}
        """
        response = (
            "I'm sorry, but I can only assist with shipping-related inquiries "
            "(such as shipping rates, tracking, delivery status, or returns)."
        )
        return {"response": response}
