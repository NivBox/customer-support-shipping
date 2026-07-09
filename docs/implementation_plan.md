# Customer Support Agent Project Implementation Plan

## Goal Description
Create a new Google Antigravity ADK 2.0 graph workflow agent project named **customer-support-agent**. The agent will act as a customer support representative for a shipping company. It should:
1. Classify incoming user queries as **shipping‑related** (covering rates, tracking, delivery, returns) or **unrelated**.
2. If shipping‑related, forward the query to a **Shipping FAQ** sub‑agent that answers common shipping questions.
3. If unrelated, respond politely refusing to answer.

Deployment files are omitted as the user does not want to deploy the agent.

## User Review Required
> [!IMPORTANT]
> Verify the chosen language (Python) and the high‑level workflow design. If you prefer a different language or want additional nodes (e.g., logging, fallback), let us know before we generate code.

## Open Questions
- Should the Shipping FAQ agent be a simple hard‑coded Q&A map, or do you want it to call an external knowledge base/API?
- Do you need any custom tooling (e.g., a classifier tool) or can we rely on a simple rule‑based classifier?
- Do you want the polite decline response to be customizable?

## Proposed Changes
---
### Project Scaffold
- **[NEW]** `customer-support-agent/` (project root)
- **[NEW]** `customer-support-agent/pyproject.toml` – project metadata and ADK dependency.
- **[NEW]** `customer-support-agent/requirements.txt` – pin ADK 2.0 and any needed packages (e.g., `langdetect` if using rule‑based classifier).
- **[NEW]** `customer-support-agent/agents/` – package for agents.
- **[NEW]** `customer-support-agent/agents/main_agent.py` – entry‑point graph workflow agent.
- **[NEW]** `customer-support-agent/agents/shipping_faq_agent.py` – simple FAQ sub‑agent.
- **[NEW]** `customer-support-agent/agents/polite_decline_node.py` – node that returns a polite refusal.
- **[NEW]** `customer-support-agent/agents/classifier.py` – optional helper that classifies queries.
- **[NEW]** `customer-support-agent/.gitignore` – ignore typical Python artefacts.
---
### Graph Workflow Definition (main_agent.py)
- Define a **GraphWorkflow** with three nodes:
  1. `classify_query` – uses the classifier to emit a boolean `is_shipping`.
  2. `shipping_faq` – routes to `ShippingFAQAgent` if `is_shipping` is true.
  3. `polite_decline` – routes to `PoliteDeclineNode` otherwise.
- Connect nodes using ADK's `GraphNode` routing primitives.

### Shipping FAQ Agent (shipping_faq_agent.py)
- Simple **Agent** subclass with a hard‑coded FAQ dictionary covering rates, tracking, delivery, returns.
- Implements `handle` that looks up the user's intent and returns an appropriate answer.

### Polite Decline Node (polite_decline_node.py)
- Minimal **Agent** that returns a static polite message such as:
  > "I’m sorry, I can only help with shipping‑related questions."

### Optional Classifier (classifier.py)
- Lightweight rule‑based classifier using keyword matching for the four shipping topics.
- Returns `True` if any keyword matches; otherwise `False`.

## Verification Plan
### Automated Tests
- Run `pytest` on generated unit tests (to be added) that verify:
  * Classification correctness for sample queries.
  * Shipping FAQ answers are returned for known intents.
  * Unrelated queries trigger the polite decline response.
### Manual Verification
- Launch the agent locally with `agents-cli run main_agent` and manually test a few queries.
- Ensure the graph routes correctly and no deployment files are generated.
