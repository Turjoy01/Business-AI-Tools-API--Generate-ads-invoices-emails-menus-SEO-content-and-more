from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.routers import ads, invoice, email, crm, menu, seo, product

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Professional Business AI Tools API - Generate ads, invoices, emails, menus, SEO content, and more",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(ads.router)
app.include_router(invoice.router)
app.include_router(email.router)
app.include_router(crm.router)
app.include_router(menu.router)
app.include_router(seo.router)
app.include_router(product.router)

@app.get("/")
async def root():
    """
    API Root - Welcome endpoint with available features
    """
    return {
        "message": "Welcome to Business AI Tools API",
        "version": settings.VERSION,
        "features": {
            "ads_generator": "Generate compelling advertisements",
            "invoice_generator": "Create professional invoices",
            "email_generator": "Write business emails",
            "crm_tools": "Analyze leads and customers",
            "menu_generator": "Create restaurant menus",
            "seo_tools": "Generate SEO-optimized content",
            "product_descriptions": "Write product descriptions"
        },
        "endpoints": {
            "ads": "/ads/generate",
            "invoice": "/invoice/generate",
            "email": "/email/generate",
            "crm": "/crm/process",
            "menu": "/menu/generate",
            "seo": "/seo/generate",
            "product": "/product/description"
        },
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc"
        }
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "service": "Business AI Tools API",
        "version": settings.VERSION
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)