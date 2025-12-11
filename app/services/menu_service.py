from app.services.openai_service import OpenAIService

class MenuService:
    def __init__(self):
        self.openai_service = OpenAIService()
    
    async def generate_menu(self, restaurant_type: str, cuisine: str, 
                           items_count: int = 10, price_range: str = "medium"):
        prompt = f"""Create a professional restaurant menu for:

Restaurant Type: {restaurant_type}
Cuisine: {cuisine}
Number of Items: {items_count}
Price Range: {price_range}

Generate a complete menu with:
1. Creative dish names
2. Appetizing descriptions
3. Realistic prices (in USD)
4. Categorized sections (appetizers, mains, desserts, drinks)
5. Dietary information (vegetarian, vegan, gluten-free markers)

Make it appealing and professional."""
        
        return await self.openai_service.generate_completion(prompt, max_tokens=3000)