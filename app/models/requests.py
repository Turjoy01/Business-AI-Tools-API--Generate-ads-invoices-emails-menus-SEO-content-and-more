from pydantic import BaseModel, Field
from typing import Optional, List

class AdsRequest(BaseModel):
    product_name: str = Field(..., description="Product or service name")
    target_audience: str = Field(..., description="Target audience description")
    ad_type: str = Field(..., description="Ad type: facebook, google, instagram, linkedin")
    key_features: Optional[List[str]] = Field(None, description="Key features to highlight")
    tone: Optional[str] = Field("professional", description="Tone of the ad")

class InvoiceRequest(BaseModel):
    company_name: str
    client_name: str
    client_email: str
    items: List[dict] = Field(..., description="List of items with name, quantity, price")
    tax_rate: Optional[float] = Field(0.0, description="Tax rate percentage")
    notes: Optional[str] = Field(None, description="Additional notes")

class EmailRequest(BaseModel):
    email_type: str = Field(..., description="Type: marketing, followup, cold_outreach, thank_you")
    recipient_name: Optional[str] = None
    subject: str
    key_points: List[str] = Field(..., description="Main points to include")
    tone: Optional[str] = Field("professional", description="Email tone")

class CRMRequest(BaseModel):
    task: str = Field(..., description="Task: lead_summary, follow_up_schedule, customer_analysis")
    customer_data: dict = Field(..., description="Customer information")

class MenuRequest(BaseModel):
    restaurant_type: str = Field(..., description="Type: cafe, restaurant, bar, fast_food")
    cuisine: str = Field(..., description="Cuisine type")
    items_count: Optional[int] = Field(10, description="Number of menu items")
    price_range: Optional[str] = Field("medium", description="Price range: low, medium, high")

class SEORequest(BaseModel):
    target_keyword: str = Field(..., description="Primary keyword")
    content_type: str = Field(..., description="Type: blog, product_page, landing_page")
    word_count: Optional[int] = Field(500, description="Target word count")
    include_meta: Optional[bool] = Field(True, description="Include meta tags")

class ProductDescriptionRequest(BaseModel):
    product_name: str
    category: str
    features: List[str]
    target_audience: str
    tone: Optional[str] = Field("persuasive", description="Description tone")
    length: Optional[str] = Field("medium", description="Length: short, medium, long")