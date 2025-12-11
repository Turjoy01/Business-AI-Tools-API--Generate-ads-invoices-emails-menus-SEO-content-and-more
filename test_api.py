"""
API Testing Script for Business AI Tools
Run this after starting the server to test all endpoints
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_ads_generator():
    print("\n🎯 Testing Ads Generator...")
    data = {
        "product_name": "Smart Watch Pro",
        "target_audience": "Tech-savvy professionals aged 25-40",
        "ad_type": "facebook",
        "key_features": ["Heart rate monitoring", "7-day battery life", "Water resistant"],
        "tone": "professional"
    }
    response = requests.post(f"{BASE_URL}/ads/generate", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_invoice_generator():
    print("\n💰 Testing Invoice Generator...")
    data = {
        "company_name": "TechCorp Inc.",
        "client_name": "John Doe",
        "client_email": "john@example.com",
        "items": [
            {"name": "Web Development", "quantity": 1, "price": 2000},
            {"name": "Logo Design", "quantity": 1, "price": 500}
        ],
        "tax_rate": 10,
        "notes": "Payment due within 30 days"
    }
    response = requests.post(f"{BASE_URL}/invoice/generate", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_email_generator():
    print("\n📧 Testing Email Generator...")
    data = {
        "email_type": "marketing",
        "recipient_name": "Sarah",
        "subject": "Exclusive Offer Just for You",
        "key_points": [
            "New product launch",
            "Limited time discount",
            "Free shipping"
        ],
        "tone": "friendly"
    }
    response = requests.post(f"{BASE_URL}/email/generate", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_crm_tools():
    print("\n📊 Testing CRM Tools...")
    data = {
        "task": "lead_summary",
        "customer_data": {
            "name": "Jane Smith",
            "email": "jane@company.com",
            "company": "ABC Corp",
            "interest": "Enterprise Plan",
            "last_contact": "2024-01-15",
            "budget": "50000"
        }
    }
    response = requests.post(f"{BASE_URL}/crm/process", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_menu_generator():
    print("\n🍽️ Testing Menu Generator...")
    data = {
        "restaurant_type": "restaurant",
        "cuisine": "italian",
        "items_count": 8,
        "price_range": "medium"
    }
    response = requests.post(f"{BASE_URL}/menu/generate", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_seo_generator():
    print("\n🔍 Testing SEO Content Generator...")
    data = {
        "target_keyword": "best running shoes 2024",
        "content_type": "blog",
        "word_count": 500,
        "include_meta": True
    }
    response = requests.post(f"{BASE_URL}/seo/generate", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_product_description():
    print("\n📦 Testing Product Description Generator...")
    data = {
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
    }
    response = requests.post(f"{BASE_URL}/product/description", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_health():
    print("\n❤️ Testing Health Check...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Business AI Tools API - Testing Script")
    print("=" * 60)
    
    try:
        # Test health first
        test_health()
        
        # Test all endpoints (comment out the ones you don't want to test)
        test_ads_generator()
        test_invoice_generator()
        test_email_generator()
        test_crm_tools()
        test_menu_generator()
        test_seo_generator()
        test_product_description()
        
        print("\n" + "=" * 60)
        print("✅ All tests completed!")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to the server!")
        print("Make sure the server is running on http://localhost:8000")
        print("Run: uvicorn app.main:app --reload")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")