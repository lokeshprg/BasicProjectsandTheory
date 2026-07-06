# What is Backend? (Detailed Explanation)

The **backend** is the part of a website or application that runs on a
**server** and performs all the work that users cannot see. It receives
requests from users, processes them, interacts with databases or other
services, and sends the required information back to the frontend.

> **The backend is the brain of an application.**

------------------------------------------------------------------------

# How a Website Actually Works

``` text
          User
            │
            ▼
     Frontend (HTML, CSS, JavaScript)
            │
      HTTP Request
            │
            ▼
      Backend (Server)
            │
      Process Request
            │
     Database (Videos, Users)
            │
      HTTP Response
            │
            ▼
     Frontend Updates Screen
```

The backend performs all the important work, while the frontend simply
displays the result.

------------------------------------------------------------------------

# Why Do We Need a Backend?

Without a backend:

-   Where are usernames and passwords stored?
-   Who verifies login credentials?
-   How are orders processed?
-   Where are messages and files stored?

**These tasks are handled by the backend.**

------------------------------------------------------------------------

# Main Responsibilities of the Backend

## 1. Handling Client Requests

Example:

``` text
Browser → GET /profile
        ↓
Backend receives request
        ↓
Checks user login
        ↓
Fetches profile from database
        ↓
Returns response
```

------------------------------------------------------------------------

## 2. Business Logic

Example:

``` text
Price      = ₹500
Discount   = 20%
GST        = 18%
Shipping   = ₹50

Final Price = ₹522
```

The backend performs the calculations and the frontend displays the
result.

------------------------------------------------------------------------

## 3. Authentication

Authentication answers:

> **Who are you?**

``` text
Username + Password
        ↓
Backend verifies credentials
        ↓
Login Successful / Failed
```

------------------------------------------------------------------------

## 4. Authorization

Authorization answers:

> **What are you allowed to do?**

Example:

-   Admin → Can delete users.
-   Normal User → Cannot delete users.

------------------------------------------------------------------------

## 5. Database Operations (CRUD)

-   **Create** -- Insert new records
-   **Read** -- Retrieve data
-   **Update** -- Modify existing data
-   **Delete** -- Remove data

Example table:

  ID   Name     Age
  ---- -------- -----
  1    Lokesh   19
  2    Rahul    20

------------------------------------------------------------------------

## 6. APIs

APIs allow the frontend and backend to communicate.

Example:

Frontend requests user information.

``` json
{
  "name": "Lokesh",
  "age": 19
}
```

The frontend displays:

``` text
Welcome Lokesh
```

------------------------------------------------------------------------

## 7. File Handling

The backend can:

-   Upload files
-   Download files
-   Store images
-   Store videos
-   Delete files

Example:

``` text
Upload Image
      ↓
Backend stores image
      ↓
Returns image URL
      ↓
Frontend displays image
```

------------------------------------------------------------------------

## 8. Sending Emails

The backend can send:

-   OTPs
-   Password reset emails
-   Welcome emails
-   Order confirmations

------------------------------------------------------------------------

## 9. Security

The backend protects:

-   Passwords
-   User data
-   Payment details

It also helps prevent:

-   SQL Injection
-   Cross-Site Scripting (XSS)
-   Unauthorized access
-   Data leaks

------------------------------------------------------------------------

## 10. Payment Processing

``` text
Buy Now
   ↓
Backend
   ↓
Payment Gateway
   ↓
Bank
   ↓
Payment Success
   ↓
Database Updated
   ↓
Order Confirmed
```

------------------------------------------------------------------------

# Backend Components

## Server

A server is a computer that receives and processes client requests.

Examples:

-   Apache
-   Nginx
-   Node.js server

## Application

The application contains the backend code and business logic.

Example:

``` python
if username == "Lokesh":
    print("Welcome")
```

## Database

Stores application data such as:

-   Users
-   Products
-   Orders
-   Comments
-   Images
-   Videos

Popular databases:

### SQL

-   MySQL
-   PostgreSQL
-   SQLite

### NoSQL

-   MongoDB
-   Firebase
-   Redis (Caching)

------------------------------------------------------------------------

# Request--Response Cycle

``` text
User searches "Laptop"
        ↓
Frontend sends request
        ↓
Backend processes request
        ↓
Database searches records
        ↓
Backend returns JSON
        ↓
Frontend displays results
```

------------------------------------------------------------------------

# Login Flow

``` text
User enters credentials
        ↓
Frontend sends request
        ↓
Backend verifies credentials
        ↓
Database confirms user
        ↓
Generate token/session
        ↓
Dashboard opens
```

------------------------------------------------------------------------

# Backend Technologies

## Languages

-   Python
-   Java
-   JavaScript (Node.js)
-   PHP
-   C#
-   Go
-   Ruby
-   Kotlin

## Frameworks

-   Django
-   Flask
-   FastAPI
-   Express.js
-   NestJS
-   Spring Boot
-   Laravel
-   ASP.NET Core

------------------------------------------------------------------------

# Real-World Example (Amazon)

``` text
Buy Now
   ↓
Frontend sends request
   ↓
Backend checks:
- Login
- Inventory
- Payment
- Shipping
   ↓
Database updates order
   ↓
Backend sends confirmation
   ↓
Frontend displays "Order Placed Successfully"
```

------------------------------------------------------------------------

# Frontend vs Backend

  Frontend                    Backend
  --------------------------- -----------------------------
  Visible to users            Runs on the server
  HTML, CSS, JavaScript       Python, Java, Node.js, PHP
  Displays data               Processes data
  Handles UI                  Handles business logic
  Sends requests              Handles requests
  No direct database access   Communicates with databases

------------------------------------------------------------------------

# Learning Roadmap

1.  Learn HTTP (GET, POST, PUT, DELETE).
2.  Learn JavaScript thoroughly.
3.  Learn Node.js.
4.  Learn Express.js.
5.  Learn MySQL or MongoDB.
6.  Build projects:
    -   Login system
    -   Notes app
    -   To-do app
    -   Weather API
    -   Chat app
    -   E-commerce backend
    -   ESP8266 IoT dashboard
