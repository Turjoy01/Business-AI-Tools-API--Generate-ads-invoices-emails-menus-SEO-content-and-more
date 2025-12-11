from fastapi import APIRouter, HTTPException
from app.models.requests import CRMRequest
from app.models.responses import APIResponse
from app.services.crm_service import CRMService

router = APIRouter(prefix="/crm", tags=["CRM Tools"])
crm_service = CRMService()

@router.post("/process", response_model=APIResponse)
async def process_crm(request: CRMRequest):
    """
    Process CRM tasks with AI analysis
    
    - **task**: CRM task type (lead_summary, follow_up_schedule, customer_analysis)
    - **customer_data**: Customer information as JSON object
    
    Example customer_data:
    {
        "name": "John Doe",
        "email": "john@example.com",
        "company": "ABC Corp",
        "interest": "Product X",
        "last_contact": "2024-01-15"
    }
    """
    try:
        result = await crm_service.process_crm_task(
            task=request.task,
            customer_data=request.customer_data
        )
        return APIResponse(success=True, message="CRM task processed successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))