# Financial-news-impact-analyze

##  Design Decisions
1. Modular Agent Architecture
Each agent is implemented as a standalone class with a focused responsibility:
- SentimentAgent for tone classification
- EntityExtractionAgent for company/ticker identification
- ImpactPredictionAgent for market movement prediction
- SummaryAgent for human-readable output

2. Typed Interfaces with Pydantic
Inputs and outputs of all agents are defined using BaseModel from Pydantic, allowing structured validation and smooth handoffs between agents.

3. Rule-Based Heuristics in Place of Prompts
Since pydantic_ai and LLM APIs were not usable in the test environment, all agents rely on hardcoded logic and keyword matching. These can later be swapped out with LLM-based prompt templates.

4. Simple NLP for Sentiment Analysis
Sentiment classification relies on keyword heuristics ("record profits", "loss", "concern", etc.) to approximate real-world tone without relying on an AI model.

5. String-Template Summary Generation
The SummaryAgent uses f-strings to simulate prompt output, structured similarly to how a language model might respond to a summarization request.

6. Inline Evaluation Framework
Evaluation logic is included directly in the main script to simplify testing. All five articles from the case study are processed end-to-end to demonstrate system performance.




