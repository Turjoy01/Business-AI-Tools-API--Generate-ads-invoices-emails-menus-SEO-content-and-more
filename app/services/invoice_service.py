from app.services.openai_service import OpenAIService
import json

class InvoiceService:
    def __init__(self):
        self.openai_service = OpenAIService()
    
    async def generate_invoice(self, company_name: str, client_name: str, 
                              client_email: str, items: list, tax_rate: float = 0.0, 
                              notes: str = None):
        items_json = json.dumps(items, indent=2)
        
        prompt = f"""Generate a professional invoice with the following details:

Company: {company_name}
Client: {client_name}
Client Email: {client_email}
Tax Rate: {tax_rate}%
Additional Notes: {notes or 'None'}

Items:
{items_json}

Create a detailed invoice including:
1. Invoice number (generate a realistic one)
2. Date (today's date)
3. Itemized list with calculations
4. Subtotal
5. Tax calculation
6. Total amount
7. Payment terms
8. Professional formatting

Output in a clear, structured format."""
        
        return await self.openai_service.generate_completion(prompt)