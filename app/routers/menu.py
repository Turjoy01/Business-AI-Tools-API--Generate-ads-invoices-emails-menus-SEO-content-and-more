from fastapi import APIRouter, HTTPException
from app.models.requests import MenuRequest
from app.models.responses import APIResponse
from app.services.menu_service import MenuService

router = APIRouter(prefix="/menu", tags=["Menu Generator"])
menu_service = MenuService()

@router.post("/generate", response_model=APIResponse)
async def generate_menu(request: MenuRequest):
    """
    Generate restaurant menu with items and pricing
    
    - **restaurant_type**: Type of restaurant (cafe, restaurant, bar, fast_food)
    - **cuisine**: Cuisine type (italian, chinese, indian, american, etc.)
    - **items_count**: Number of menu items to generate
    - **price_range**: Price range (low, medium, high)
    """
    try:
        result = await menu_service.generate_menu(
            restaurant_type=request.restaurant_type,
            cuisine=request.cuisine,
            items_count=request.items_count,
            price_range=request.price_range
        )
        return APIResponse(success=True, message="Menu generated successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))