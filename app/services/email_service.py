from app.services.openai_service import OpenAIService

class EmailService:
    def __init__(self):
        self.openai_service = OpenAIService()
    
    async def generate_email(self, email_type: str, subject: str, key_points: list,
                            recipient_name: str = None, tone: str = "professional"):
        points_text = "\n".join([f"- {point}" for point in key_points])
        recipient = recipient_name if recipient_name else "[Recipient Name]"
        
        prompt = f"""Write a {tone} {email_type} email with:

Recipient: {recipient}
Subject: {subject}
Tone: {tone}

Key Points to Cover:
{points_text}

Generate a complete email including:
1. Subject line (if different from provided)
2. Greeting
3. Body paragraphs
4. Call-to-action
5. Professional closing

Make it natural and engaging."""
        
        return await self.openai_service.generate_completion(prompt)