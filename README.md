# Customer Support Agent (Shipping FAQ)

An intelligent customer support agent wrapper built using python and the Google Antigravity SDK. It acts as a representative for a shipping company, routing and handling user requests depending on query relevance.

## Project Intent
The agent's main goal is to efficiently classify user queries:
1. If the query is related to **shipping** (rates, tracking, delivery status, returns), it routes the request to a dedicated **Shipping FAQ Agent**.
2. If the query is **unrelated**, it routes to a **Polite Decline Agent** which explains the scope of assistance.

---

## Tech Stack
* **Language**: Python (>=3.11, <3.14)
* **SDK**: Google Antigravity SDK
* **Linter**: Ruff

---

## Architecture Overview

```
customer-support-shipping/
├── app/
│   └── agent.py              # Root Agent Orchestrator
├── agents/
│   ├── classifier.py         # Keyword Router
│   ├── shipping_faq_agent.py # Answers Shipping Q&As
│   └── polite_decline_node.py# politely refuses out-of-scope prompts
└── test_workflow.py          # Script simulating user queries locally
```

### Routing Flow
1. **User Input**: A query is sent to `CustomerSupportAgent`.
2. **Classification**: The input is processed by `ShippingClassifier` to check for shipping keywords.
3. **Execution**:
   * If `is_shipping` is `True` → Routed to `ShippingFAQAgent`.
   * If `is_shipping` is `False` → Routed to `PoliteDeclineAgent`.
4. **Response**: The designated agent returns the text answer to the user.

---

## Getting Started

### Prerequisites
Make sure Python 3.11+ is installed.

### Installation
Install the Google Antigravity SDK:
```bash
pip install google-antigravity
```

### Running Tests
Execute the workflow simulation with sample test inputs:
```bash
PYTHONPATH=. python3 test_workflow.py
```
