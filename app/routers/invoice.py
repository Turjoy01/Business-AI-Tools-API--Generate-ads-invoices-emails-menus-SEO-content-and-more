from fastapi import APIRouter, HTTPException
from app.models.requests import InvoiceRequest
from app.models.responses import APIResponse
from app.services.invoice_service import InvoiceService

router = APIRouter(prefix="/invoice", tags=["Invoice Generator"])
invoice_service = InvoiceService()

@router.post("/generate", response_model=APIResponse)
async def generate_invoice(request: InvoiceRequest):
    """
    Generate professional invoice with automatic calculations
    
    - **company_name**: Your company name
    - **client_name**: Client's name
    - **client_email**: Client's email
    - **items**: List of items [{"name": "Item", "quantity": 1, "price": 100}]
    - **tax_rate**: Tax percentage (optional)
    - **notes**: Additional notes (optional)
    """
    try:
        result = await invoice_service.generate_invoice(
            company_name=request.company_name,
            client_name=request.client_name,
            client_email=request.client_email,
            items=request.items,
            tax_rate=request.tax_rate,
            notes=request.notes
        )
        return APIResponse(success=True, message="Invoice generated successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))