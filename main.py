from pydantic import BaseModel
from typing import List

# 1.SentimentAgent
class SentimentInput(BaseModel):
    text: str

class SentimentOutput(BaseModel):
    sentiment: str
    confidence: float

class SentimentAgent:
    def run(self, input_data: SentimentInput) -> SentimentOutput:
        text_lower = input_data.text.lower()
        if "record profits" in text_lower or "beats expectations" in text_lower:
            return SentimentOutput(sentiment="positive", confidence=0.92)
        elif "loss" in text_lower or "concern" in text_lower:
            return SentimentOutput(sentiment="negative", confidence=0.88)
        else:
            return SentimentOutput(sentiment="neutral", confidence=0.7)


# 2. EntityExtractionAgent
class EntityExtractionInput(BaseModel):
    text: str

class EntityExtractionOutput(BaseModel):
    companies: List[str]
    tickers: List[str]

class EntityExtractionAgent:
    def run(self, input_data: EntityExtractionInput) -> EntityExtractionOutput:
        companies, tickers = [], []
        if "Tesla" in input_data.text:
            companies.append("Tesla")
            tickers.append("TSLA")
        if "Amazon" in input_data.text:
            companies.append("Amazon")
            tickers.append("AMZN")
        if "CureGen" in input_data.text:
            companies.append("CureGen")
            tickers.append("CURE")
        if "ByteDance" in input_data.text:
            companies.append("ByteDance")
            # No public ticker, skip
        if "FirstState" in input_data.text:
            companies.append("FirstState")
            tickers.append("FSB")
        return EntityExtractionOutput(companies=companies, tickers=tickers)


# 3. ImpactPredictionAgent
class ImpactInput(BaseModel):
    sentiment: str
    companies: List[str]
    tickers: List[str]

class ImpactOutput(BaseModel):
    prediction: str  # "up", "down", "neutral"
    reason: str

class ImpactPredictionAgent:
    def run(self, input_data: ImpactInput) -> ImpactOutput:
        if input_data.sentiment == "positive":
            prediction = "up"
            reason = "Positive news typically results in a short-term stock price increase."
        elif input_data.sentiment == "negative":
            prediction = "down"
            reason = "Negative news tends to result in a price drop."
        else:
            prediction = "neutral"
            reason = "The sentiment is unclear or balanced, so the market reaction may be neutral."
        return ImpactOutput(prediction=prediction, reason=reason)


# 4. SummaryAgent
class SummaryInput(BaseModel):
    headline: str
    prediction: str
    content: str
    published_at: str

class SummaryOutput(BaseModel):
    summary: str

class SummaryAgent:
    def run(self, input_data: SummaryInput) -> SummaryOutput:
        summary = (
            f"Headline: {input_data.headline}\n"
            f"Content: {input_data.content}\n"
            f"Predicted Market Impact: {input_data.prediction.capitalize()}\n"
            f"Published At: {input_data.published_at}\n"
        )
        return SummaryOutput(summary=summary)

if __name__ == "__main__":
    articles = [
        {
            "article_id": "FIN-001",
            "headline": "Tesla crushes Q3 expectations with record profits, but Musk warns of 'turbulent t",
            "content": "Tesla (NASDAQ: TSLA) reported stunning Q3 results with earnings of $1.05 per share",
            "published_at": "2024-10-22T16:00:00Z"
        },
        {
            "article_id": "FIN-002",
            "headline": "Small biotech CureGen soars on FDA approval, analysts remain skeptical",
            "content": "CureGen (NASDAQ: CURE), a small-cap biotech, received FDA approval for its novel compound",
            "published_at": "2024-11-01T14:30:00Z"
        },
        {
            "article_id": "FIN-003",
            "headline": "Amazon announces 'transformational' AI venture, but at massive cost",
            "content": "Amazon (NASDAQ: AMZN) unveiled Project Olympus, a $50 billion investment in AGI development",
            "published_at": "2024-09-15T09:00:00Z"
        },
        {
            "article_id": "FIN-004",
            "headline": "Regional bank FirstState posts record earnings amid industry turmoil",
            "content": "FirstState Bank (NYSE: FSB) reported record Q2 earnings of $3.20 per share, up 45%",
            "published_at": "2024-10-12T10:30:00Z"
        },
        {
            "article_id": "FIN-005",
            "headline": "China tech giant ByteDance reports stellar growth, regulatory clouds remain",
            "content": "ByteDance, TikTok's parent company, leaked financials show revenue grew 70% to $12 billion",
            "published_at": "2024-11-21T18:45:00Z"
        }
    ]

    sentiment_agent = SentimentAgent()
    entity_agent = EntityExtractionAgent()
    impact_agent = ImpactPredictionAgent()
    summary_agent = SummaryAgent()

    for article in articles:
        print(f"\nArticle ID: {article['article_id']}")

        sentiment = sentiment_agent.run(SentimentInput(text=article['content']))
        entities = entity_agent.run(EntityExtractionInput(text=article['content']))
        impact = impact_agent.run(ImpactInput(
            sentiment=sentiment.sentiment,
            companies=entities.companies,
            tickers=entities.tickers
        ))
        summary = summary_agent.run(SummaryInput(
            headline=article['headline'],
            prediction=impact.prediction,
            content=article['content'],
            published_at=article['published_at']
        ))

        print(summary.summary)
