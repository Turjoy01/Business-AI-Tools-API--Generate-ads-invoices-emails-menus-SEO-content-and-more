from fastapi import APIRouter, HTTPException
from app.models.requests import SEORequest
from app.models.responses import APIResponse
from app.services.seo_service import SEOService

router = APIRouter(prefix="/seo", tags=["SEO Tools"])
seo_service = SEOService()

@router.post("/generate", response_model=APIResponse)
async def generate_seo_content(request: SEORequest):
    """
    Generate SEO-optimized content with meta tags
    
    - **target_keyword**: Primary keyword to optimize for
    - **content_type**: Type of content (blog, product_page, landing_page)
    - **word_count**: Target word count for content
    - **include_meta**: Include meta tags (title, description, keywords)
    """
    try:
        result = await seo_service.generate_seo_content(
            target_keyword=request.target_keyword,
            content_type=request.content_type,
            word_count=request.word_count,
            include_meta=request.include_meta
        )
        return APIResponse(success=True, message="SEO content generated successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))