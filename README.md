# financial-news-impact-analyze

##  Design Decisions
Modular Agent Architecture
Each agent is implemented as a standalone class with a focused responsibility:

SentimentAgent for tone classification

EntityExtractionAgent for company/ticker identification

ImpactPredictionAgent for market movement prediction

SummaryAgent for human-readable output

Typed Interfaces with Pydantic
Inputs and outputs of all agents are defined using BaseModel from Pydantic, allowing structured validation and smooth handoffs between agents.

Rule-Based Heuristics in Place of Prompts
Since pydantic_ai and LLM APIs were not usable in the test environment, all agents rely on hardcoded logic and keyword matching. These can later be swapped out with LLM-based prompt templates.

Simple NLP for Sentiment Analysis
Sentiment classification relies on keyword heuristics ("record profits", "loss", "concern", etc.) to approximate real-world tone without relying on an AI model.

String-Template Summary Generation
The SummaryAgent uses f-strings to simulate prompt output, structured similarly to how a language model might respond to a summarization request.

Inline Evaluation Framework
Evaluation logic is included directly in the main script to simplify testing. All five articles from the case study are processed end-to-end to demonstrate system performance.

🔁 Prompt Iteration / Logic Refinement
Although no actual prompt templates were used due to the environment, the agent logic was refined iteratively in the same spirit as prompt tuning. Below is a breakdown:

Agent	Iteration	Changes Made
SentimentAgent	V1 → V2	Added more nuanced financial keywords like "beats expectations" and "concern"
EntityExtractionAgent	V1 → V2	Expanded static detection to include CureGen, ByteDance, and FirstState
ImpactPredictionAgent	V1 → V2	Originally returned just the direction — added reason for explainability
SummaryAgent	V1 → V2	Trimmed down output to match submission expectations (no sentiment/companies)
