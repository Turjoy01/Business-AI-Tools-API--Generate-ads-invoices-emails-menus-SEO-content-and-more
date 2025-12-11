from app.services.openai_service import OpenAIService

class ProductService:
    def __init__(self):
        self.openai_service = OpenAIService()
    
    async def generate_product_description(self, product_name: str, category: str,
                                          features: list, target_audience: str,
                                          tone: str = "persuasive", length: str = "medium"):
        features_text = "\n".join([f"- {feature}" for feature in features])
        
        length_words = {"short": 100, "medium": 250, "long": 500}
        word_target = length_words.get(length, 250)
        
        prompt = f"""Write a compelling product description for:

Product: {product_name}
Category: {category}
Target Audience: {target_audience}
Tone: {tone}
Length: ~{word_target} words

Features:
{features_text}

Create:
1. Attention-grabbing headline
2. Engaging product description
3. Benefits-focused content (not just features)
4. Social proof elements
5. Strong call-to-action
6. SEO-friendly keywords

Make it persuasive and conversion-focused."""
        
        return await self.openai_service.generate_completion(prompt, max_tokens=2000)