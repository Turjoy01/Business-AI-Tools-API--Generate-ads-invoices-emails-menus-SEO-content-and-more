from fastapi import APIRouter, HTTPException
from app.models.requests import EmailRequest
from app.models.responses import APIResponse
from app.services.email_service import EmailService

router = APIRouter(prefix="/email", tags=["Email Generator"])
email_service = EmailService()

@router.post("/generate", response_model=APIResponse)
async def generate_email(request: EmailRequest):
    """
    Generate professional emails for various purposes
    
    - **email_type**: Type of email (marketing, followup, cold_outreach, thank_you)
    - **recipient_name**: Recipient's name (optional)
    - **subject**: Email subject line
    - **key_points**: List of key points to include in email
    - **tone**: Email tone (professional, casual, friendly, etc.)
    """
    try:
        result = await email_service.generate_email(
            email_type=request.email_type,
            subject=request.subject,
            key_points=request.key_points,
            recipient_name=request.recipient_name,
            tone=request.tone
        )
        return APIResponse(success=True, message="Email generated successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
