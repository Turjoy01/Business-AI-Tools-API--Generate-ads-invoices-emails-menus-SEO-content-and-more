from app.services.openai_service import OpenAIService
import json

class CRMService:
    def __init__(self):
        self.openai_service = OpenAIService()
    
    async def process_crm_task(self, task: str, customer_data: dict):
        customer_json = json.dumps(customer_data, indent=2)
        
        task_prompts = {
            "lead_summary": f"""Analyze this lead and create a comprehensive summary:
{customer_json}

Provide:
1. Lead Quality Score (1-10)
2. Key Insights
3. Recommended Actions
4. Priority Level
5. Next Steps""",
            
            "follow_up_schedule": f"""Create a follow-up schedule for this customer:
{customer_json}

Generate:
1. Immediate follow-up (24 hours)
2. Short-term follow-ups (1 week)
3. Long-term nurturing plan
4. Recommended communication channels
5. Key talking points for each touchpoint""",
            
            "customer_analysis": f"""Perform detailed customer analysis:
{customer_json}

Analyze:
1. Customer Profile
2. Behavior Patterns
3. Purchase Potential
4. Pain Points
5. Personalized Recommendations"""
        }
        
        prompt = task_prompts.get(task, f"Process this CRM task '{task}' with data: {customer_json}")
        return await self.openai_service.generate_completion(prompt)