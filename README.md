# E-Commerce Platform

## Author
Leul Misganaw

## Description
This is a **Django REST Framework based e-commerce platform**.  
Users can browse products, search, filter, and place orders. Admins can manage products, categories, and users.  

The project demonstrates **CRUD operations, authentication, filtering, ordering, and nested relationships** in a real-world style web API.

---

## Key Features
- **User authentication** (login with token or session)
- **Product management**  
  - List all products  
  - Create new products (authenticated users)  
  - Update & delete products (owner/admin only)  
  - Search by name  
  - Filter by category  
  - Order by price or creation date
- **Category management**  
  - Admins can create/update/delete categories  
  - Anyone can view categories
- **Order management**  
  - Users can place orders for multiple products  
  - Total price is calculated automatically  
  - Users can view only their own orders
- **Admin dashboard**  
  - Full control over products, categories, and users  

---

## Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ecommerce_api_capstone.git
cd ecommerce_api_capstone
