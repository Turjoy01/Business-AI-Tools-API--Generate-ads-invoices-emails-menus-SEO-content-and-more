from fastapi import APIRouter, HTTPException
from app.models.requests import ProductDescriptionRequest
from app.models.responses import APIResponse
from app.services.product_service import ProductService

router = APIRouter(prefix="/product", tags=["Product Description"])
product_service = ProductService()

@router.post("/description", response_model=APIResponse)
async def generate_product_description(request: ProductDescriptionRequest):
    """
    Generate compelling product descriptions
    
    - **product_name**: Name of the product
    - **category**: Product category
    - **features**: List of product features
    - **target_audience**: Target audience description
    - **tone**: Description tone (persuasive, informative, casual, etc.)
    - **length**: Description length (short, medium, long)
    """
    try:
        result = await product_service.generate_product_description(
            product_name=request.product_name,
            category=request.category,
            features=request.features,
            target_audience=request.target_audience,
            tone=request.tone,
            length=request.length
        )
        return APIResponse(success=True, message="Product description generated successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))