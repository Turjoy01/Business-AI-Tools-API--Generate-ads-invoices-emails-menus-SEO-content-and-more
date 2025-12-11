from app.services.openai_service import OpenAIService

class SEOService:
    def __init__(self):
        self.openai_service = OpenAIService()
    
    async def generate_seo_content(self, target_keyword: str, content_type: str,
                                  word_count: int = 500, include_meta: bool = True):
        prompt = f"""Create SEO-optimized content:

Target Keyword: {target_keyword}
Content Type: {content_type}
Word Count: ~{word_count} words

Generate:
1. SEO-optimized title (with keyword)
2. Main content (naturally incorporate keyword)
3. Subheadings (H2, H3 with variations)
4. Internal linking suggestions
"""
        
        if include_meta:
            prompt += """5. Meta Title (55-60 characters)
6. Meta Description (150-160 characters)
7. Focus Keywords (primary and secondary)
8. URL slug suggestion"""
        
        return await self.openai_service.generate_completion(prompt, max_tokens=2500)