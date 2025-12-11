# Business AI Tools API 🚀

Professional FastAPI backend for Business AI Tools with 7 powerful features.

## 📁 Project Structure

```
business-ai-tools/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── requests.py
│   │   └── responses.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── openai_service.py
│   │   ├── ads_service.py
│   │   ├── invoice_service.py
│   │   ├── email_service.py
│   │   ├── crm_service.py
│   │   ├── menu_service.py
│   │   ├── seo_service.py
│   │   └── product_service.py
│   └── routers/
│       ├── __init__.py
│       ├── ads.py
│       ├── invoice.py
│       ├── email.py
│       ├── crm.py
│       ├── menu.py
│       ├── seo.py
│       └── product.py
├── requirements.txt
├── .env
└── README.md
```

## 🎯 Features

1. **AI Ads Generator** - Create Facebook, Google, Instagram, LinkedIn ads
2. **Invoice Generator** - Generate professional invoices with calculations
3. **Email Generator** - Write marketing, follow-up, cold outreach emails
4. **CRM Tools** - Lead analysis, follow-up scheduling, customer insights
5. **Menu Generator** - Create restaurant menus with pricing
6. **SEO Tools** - Generate SEO-optimized content with meta tags
7. **Product Descriptions** - Write compelling product descriptions

## 🛠️ Setup Instructions

### Step 1: Create Project Structure

```bash
mkdir business-ai-tools
cd business-ai-tools

mkdir -p app/models app/services app/routers app/utils
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create .env File

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY
PORT=8000
```

### Step 5: Create Empty __init__.py Files

```bash
# Create empty __init__.py files
touch app/__init__.py
touch app/models/__init__.py
touch app/services/__init__.py
touch app/routers/__init__.py
touch app/utils/__init__.py
```

### Step 6: Run the Application

```bash
# Method 1: Using uvicorn directly
uvicorn app.main:app --reload --port 8000

# Method 2: Using Python
python -m app.main
```

## 📖 API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Root**: http://localhost:8000/

## 🧪 Testing the API

### 1. Ads Generator

```bash
curl -X POST "http://localhost:8000/ads/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Smart Watch Pro",
    "target_audience": "Tech-savvy professionals aged 25-40",
    "ad_type": "facebook",
    "key_features": ["Heart rate monitoring", "7-day battery life", "Water resistant"],
    "tone": "professional"
  }'
```

### 2. Invoice Generator

```bash
curl -X POST "http://localhost:8000/invoice/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "TechCorp Inc.",
    "client_name": "John Doe",
    "client_email": "john@example.com",
    "items": [
      {"name": "Web Development", "quantity": 1, "price": 2000},
      {"name": "Logo Design", "quantity": 1, "price": 500}
    ],
    "tax_rate": 10,
    "notes": "Payment due within 30 days"
  }'
```

### 3. Email Generator

```bash
curl -X POST "http://localhost:8000/email/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "email_type": "marketing",
    "recipient_name": "Sarah",
    "subject": "Exclusive Offer Just for You",
    "key_points": [
      "New product launch",
      "Limited time discount",
      "Free shipping"
    ],
    "tone": "friendly"
  }'
```

### 4. CRM Tools

```bash
curl -X POST "http://localhost:8000/crm/process" \
  -H "Content-Type: application/json" \
  -d '{
    "task": "lead_summary",
    "customer_data": {
      "name": "Jane Smith",
      "email": "jane@company.com",
      "company": "ABC Corp",
      "interest": "Enterprise Plan",
      "last_contact": "2024-01-15",
      "budget": "50000"
    }
  }'
```

### 5. Menu Generator

```bash
curl -X POST "http://localhost:8000/menu/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "restaurant_type": "restaurant",
    "cuisine": "italian",
    "items_count": 12,
    "price_range": "medium"
  }'
```

### 6. SEO Content Generator

```bash
curl -X POST "http://localhost:8000/seo/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "target_keyword": "best running shoes 2024",
    "content_type": "blog",
    "word_count": 800,
    "include_meta": true
  }'
```

### 7. Product Description

```bash
curl -X POST "http://localhost:8000/product/description" \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Wireless Earbuds Pro",
    "category": "Electronics",
    "features": [
      "Active noise cancellation",
      "30-hour battery life",
      "Premium sound quality",
      "IPX7 waterproof"
    ],
    "target_audience": "Music lovers and commuters",
    "tone": "persuasive",
    "length": "medium"
  }'
```

## 🔧 Configuration

Edit `app/config.py` to customize settings:

```python
class Settings(BaseSettings):
    OPENAI_API_KEY: str
    PORT: int = 8000
    APP_NAME: str = "Business AI Tools API"
    VERSION: str = "1.0.0"
```

## 📝 Response Format

All endpoints return a standard response format:

```json
{
  "success": true,
  "message": "Operation successful",
  "data": "Generated content here...",
  "error": null
}
```

## 🐛 Troubleshooting

### OpenAI API Key Error
```
Make sure your .env file contains the correct OPENAI_API_KEY
```

### Module Not Found Error
```bash
# Make sure all __init__.py files are created
# Run from the project root directory
```

### Port Already in Use
```bash
# Change port in .env file or use different port:
uvicorn app.main:app --reload --port 8001
```

## 🚀 Production Deployment

For production deployment:

1. Set proper CORS origins in `app/main.py`
2. Use environment variables for sensitive data
3. Enable HTTPS
4. Add rate limiting
5. Implement authentication/authorization
6. Add logging and monitoring

## 📄 License

This project is for educational and commercial use.

## 🤝 Support

For issues or questions, please create an issue in the repository.

---

**Made with ❤️ using FastAPI and OpenAI**