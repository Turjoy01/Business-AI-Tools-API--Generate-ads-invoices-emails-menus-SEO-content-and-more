from fastapi import APIRouter, HTTPException
from app.models.requests import AdsRequest
from app.models.responses import APIResponse
from app.services.ads_service import AdsService

router = APIRouter(prefix="/ads", tags=["Ads Generator"])
ads_service = AdsService()

@router.post("/generate", response_model=APIResponse)
async def generate_ad(request: AdsRequest):
    """
    Generate AI-powered advertisement content
    
    - **product_name**: Name of the product or service
    - **target_audience**: Description of target audience
    - **ad_type**: Type of ad (facebook, google, instagram, linkedin)
    - **key_features**: List of key features to highlight
    - **tone**: Tone of the ad (professional, casual, friendly, etc.)
    """
    try:
        result = await ads_service.generate_ad(
            product_name=request.product_name,
            target_audience=request.target_audience,
            ad_type=request.ad_type,
            key_features=request.key_features,
            tone=request.tone
        )
        return APIResponse(success=True, message="Ad generated successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))