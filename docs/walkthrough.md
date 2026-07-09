# Walkthrough: Customer Support Agent Implementation

We have successfully created a clean, modular Python project structure for a customer support agent. It routes queries based on classification using the Google Antigravity SDK.

## What Was Completed
1. **Root Agent Orchestration (`app/agent.py`)**: Defines `CustomerSupportAgent` which inherits from Google Antigravity `Agent` and orchestrates sub-agents directly.
2. **Classifier Component (`agents/classifier.py`)**: Uses keyword matching to detect shipping-related topics (rates, tracking, delivery, returns).
3. **Shipping FAQ Agent (`agents/shipping_faq_agent.py`)**: Evaluates shipping queries to return the appropriate static FAQ answer.
4. **Polite Decline Agent (`agents/polite_decline_node.py`)**: Polite fallback when the query is unrelated.
5. **Linting & Code Verification**: Executed `ruff check .` successfully. All checks passed.

## Local Test Execution Results

We verified the agent's behavior by running:
```bash
PYTHONPATH=. python3 test_workflow.py
```

### Outputs:
* **Query:** `'Where is my package? The tracking number is 12345.'`
  * **Agent:** *You can track your package by entering your tracking number on our website's tracking page.*
* **Query:** `'How much does standard shipping cost?'`
  * **Agent:** *Our standard domestic shipping starts at $5.99. Express is $14.99. International rates vary by destination.*
* **Query:** `'What is your return policy?'`
  * **Agent:** *We offer free returns within 30 days of delivery. Please print a return label from our online portal.*
* **Query:** `'Can you recommend a good Italian restaurant nearby?'`
  * **Agent:** *I'm sorry, but I can only assist with shipping-related inquiries...*
* **Query:** `'I need help with my taxes.'`
  * **Agent:** *I'm sorry, but I can only assist with shipping-related inquiries...*
