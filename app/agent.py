# -*- coding: utf-8 -*-
"""app/agent.py
Root workflow agent for Customer Support.
Instead of relying on unstable Graph/Node/Edge imports, it inherits from the 
Antigravity Agent and orchestrates the sub-modules directly.
"""

from google.antigravity import Agent, LocalAgentConfig

# Import supporting modules
from agents.classifier import ShippingClassifier
from agents.shipping_faq_agent import ShippingFAQAgent
from agents.polite_decline_node import PoliteDeclineAgent

class CustomerSupportAgent(Agent):
    """Customer Support Agent that routes queries.
    
    Checks if a query is shipping-related. If yes, it delegates to the 
    FAQ Agent. If no, it declines politely.
    """
    def __init__(self, config: LocalAgentConfig = None):
        if config is None:
            config = LocalAgentConfig()
        super().__init__(config)
        
        # Initialize internal nodes/handlers
        self.classifier = ShippingClassifier()
        self.faq_agent = ShippingFAQAgent()
        self.decline_agent = PoliteDeclineAgent()

    async def handle_query(self, query: str) -> str:
        """Route the user query and return the final text response.
        
        Args:
            query: The user query string.
        """
        # Step 1: Classify
        classification = self.classifier.run(query)
        
        # Step 2: Route and execute the appropriate handler
        if classification.get("is_shipping", False):
            result = self.faq_agent.run({"query": query})
        else:
            result = self.decline_agent.run({"query": query})
            
        return result.get("response", "")
