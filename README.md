  # E-Commerce Platform

  ## Author

  Leul Misganaw

  ## Description

  This is a **Django REST Framework based e-commerce platform**.
  Users can browse products, search, filter, and place orders. Admins can manage products, categories, and users.

  The project demonstrates **CRUD operations, authentication, filtering, ordering, and nested relationships** in a real-world style web API.

  ***
  ## 🌐 Live Demo

Test the live API here: [Inventory Management API Live](https://ecommerce-api-rb25.onrender.com)

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

  ***

  ## Installation & Setup
  1. Clone the repository:

  ```bash
  git clone https://github.com/yourusername/ecommerce_api_capstone.git
  cd ecommerce_api_capstone
  ```

  2. (Optional) Create and activate a virtual environment (recommended):

  ```bash
  python -m venv .venv
  # Windows PowerShell
  .\.venv\Scripts\Activate.ps1
  # Windows CMD
  .\.venv\Scripts\activate.bat
  ```

  3. Install dependencies:

  ```bash
  python -m pip install -r requirements.txt
  ```

  4. Apply migrations and run the server:

  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

  ***

  ## API Endpoints

  Base URL: `/api/`
  - **Products**
    - `GET /api/products/` — list products (supports pagination, `?page=`)
    - `POST /api/products/` — create product (authenticated)
    - `GET /api/products/<id>/` — retrieve product details
    - `PUT/PATCH /api/products/<id>/` — update product (owner/admin)
    - `DELETE /api/products/<id>/` — delete product (owner/admin)

  - **Users**
    - `GET /api/users/` — list users
    - `POST /api/users/` — create/register user

  - **Authentication**
    - `POST /api/login/` — login endpoint (returns auth token/session)

  - **Categories**
    - `GET /api/categories/` — list categories
    - `POST /api/categories/` — create category (admin)
    - `GET /api/categories/<id>/` — category details

  - **Orders**
    - `GET /api/orders/` — list orders (user-scoped)
    - `POST /api/orders/` — create an order
    - `GET /api/admin/orders/` — admin order list view

  ### Example curl requests

  List products (first page):

  ```bash
  curl -X GET "http://127.0.0.1:8000/api/products/"
  ```

  Create product (replace TOKEN with your auth token):

  ```bash
  curl -X POST "http://127.0.0.1:8000/api/products/" \
    -H "Authorization: Token TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"name":"speaker","description":"JBL speakers","price":100,"stock_quantity":35,"category":"Audio","image_url":"https://example.com/speaker.jpg"}'
  ```

  Login (example):

  ```bash
  curl -X POST "http://127.0.0.1:8000/api/login/" \
    -H "Content-Type: application/json" \
    -d '{"username":"youruser","password":"yourpass"}'
  ```

  Create order (example):

  ```bash
  curl -X POST "http://127.0.0.1:8000/api/orders/" \
    -H "Authorization: Token TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"items":[{"product":1,"quantity":2},{"product":3,"quantity":1}]}'
  ```

  ***

  ## Screenshots

  I captured screenshots of the running API views during development. Place screenshots in `docs/screenshots/` and they will render in the README. Suggested filenames (matching attached captures):
  - <img width="1366" height="768" alt="Screenshot (63)" src="https://github.com/user-attachments/assets/fc572c26-62a8-4045-9aa0-e741cbd2f8fa" />

   <img width="1366" height="768" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/3b967d13-d93f-49e8-92af-60e90c7f4165" />
— Product list & pagination
  - <img width="1366" height="768" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/57d83745-962f-4cfb-a957-b843af8bfc37" />
 — Product create response
  - <img width="1366" height="768" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/f0f7eb42-16f6-48fe-b08e-21d3b5af6ca0" />

   <img width="1366" height="768" alt="Screenshot (68)" src="https://github.com/user-attachments/assets/c9346761-0661-4487-8a31-d1c9cad54866" />
— Filters / search / ordering UI
  - <img width="1366" height="675" alt="Screenshot (62)" src="https://github.com/user-attachments/assets/d6f86dfe-802f-40b1-aa63-44a548a34604" />
 — Login endpoint (method not allowed / POST form)
  - <img width="1366" height="768" alt="Screenshot (69)" src="https://github.com/user-attachments/assets/57206947-2b40-44c8-9769-42fac3eb16aa" />
 — Category list/create
  - <img width="1366" height="697" alt="Screenshot (70)" src="https://github.com/user-attachments/assets/055844fc-2969-4104-ae13-3b06bb38c4d7" />
 — Orders list
  - <img width="1366" height="768" alt="Screenshot (71)" src="https://github.com/user-attachments/assets/8d05de59-32e8-4d29-90e2-adbc96b54a49" />

 <img width="1366" height="768" alt="Screenshot (72)" src="https://github.com/user-attachments/assets/05b41051-cf7f-4a55-ac14-999558507cd5" />
— Admin dashboard and product list

