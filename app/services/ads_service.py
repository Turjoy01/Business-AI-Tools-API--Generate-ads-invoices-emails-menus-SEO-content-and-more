from app.services.openai_service import OpenAIService

class AdsService:
    def __init__(self):
        self.openai_service = OpenAIService()
    
    async def generate_ad(self, product_name: str, target_audience: str, ad_type: str, 
                         key_features: list = None, tone: str = "professional"):
        features_text = "\n".join(key_features) if key_features else "N/A"
        
        prompt = f"""Create a compelling {ad_type} ad for:
Product: {product_name}
Target Audience: {target_audience}
Tone: {tone}
Key Features: {features_text}

Generate:
1. Headline (attention-grabbing)
2. Ad Copy (persuasive description)
3. Call-to-Action (clear and actionable)
4. Hashtags (if applicable for social media)

Format the output in a structured way."""
        
        return await self.openai_service.generate_completion(prompt)