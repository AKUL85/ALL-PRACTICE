# 🚀 Quick Start Guide

## Your Backend is Ready! 

Complete full-stack authentication system with Docker Compose, MySQL, and real API integration.

---

## ⚡ One Command to Run Everything

```bash
docker-compose up
```

That's it! This will start:
- ✓ **MySQL Database** (port 3306)
- ✓ **Node.js Backend API** (port 5000)
- ✓ **React Frontend** (port 3000)

---

## 🌐 Access Your Application

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:5000 |
| Health Check | http://localhost:5000/health |

---

## 🧪 Test the Application

### Create New Account
1. Go to http://localhost:3000
2. Click "Sign up"
3. Fill in details:
   - Name: `John Doe`
   - Email: `john@example.com`
   - Password: `password123`
   - Confirm: `password123`
4. Click "Create Account"
5. You'll be switched to login screen

### Sign In
1. Enter your email: `john@example.com`
2. Enter password: `password123`
3. Click "Sign In"
4. See your welcome page with user info!

---

## 📁 Project Structure

```
Shop/
├── src/                    # React Frontend
│   ├── App.jsx            # Main app with login/signup
│   ├── main.jsx           # Entry point
│   ├── App.css            # Styles
│   └── index.css          # Global styles
├── backend/               # Node.js/Express API
│   ├── server.js          # Main server
│   ├── database.js        # MySQL connection
│   ├── routes/
│   │   └── auth.js        # Auth endpoints
│   ├── package.json       # Backend dependencies
│   ├── Dockerfile         # Backend Docker image
│   └── .env               # Backend config
├── Dockerfile             # Frontend Docker image
├── docker-compose.yml     # Docker Compose config
├── package.json           # Frontend dependencies
└── .env                   # Frontend config
```

---

## 🔌 API Endpoints

### Signup
```bash
POST http://localhost:5000/api/auth/signup
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

### Login
```bash
POST http://localhost:5000/api/auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "password123"
}
```

### Get Profile (Protected)
```bash
GET http://localhost:5000/api/auth/profile
Authorization: Bearer <your-jwt-token>
```

### Health Check
```bash
GET http://localhost:5000/health
```

---

## 🛑 Stop Services

```bash
docker-compose down
```

---

## 📊 View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f mysql
docker-compose logs -f app
```

---

## 🔧 Useful Commands

### Rebuild everything
```bash
docker-compose up --build
```

### Check MySQL data
```bash
docker exec -it shop-mysql mysql -u shop_user -p shop_db
# Password: shop_password

# View users
SELECT * FROM users;
```

### Check backend health
```bash
curl http://localhost:5000/health
```

---

## 🎨 Frontend Features

✓ Modern responsive design with Tailwind CSS  
✓ Real-time form validation  
✓ Beautiful error messages  
✓ Loading states  
✓ JWT token management  
✓ Session persistence  
✓ Easy login/signup toggle  

---

## 🔒 Backend Security

✓ Password hashing (bcryptjs)  
✓ JWT authentication  
✓ Input validation  
✓ CORS enabled  
✓ Database connection pooling  
✓ Protected routes  

---

## 📦 What's Included

**Frontend:**
- React 19
- Vite (fast build tool)
- React Router
- Tailwind CSS
- Axios (API calls)

**Backend:**
- Express.js
- MySQL 8.0
- JWT authentication
- bcryptjs (password hashing)
- CORS

**Database:**
- Auto-created users table
- Timestamp support
- Unique email constraint

---

## 🐛 Troubleshooting

### Port already in use?
```bash
docker-compose down
# OR change ports in docker-compose.yml
```

### API connection error?
```bash
# Check if backend is running
curl http://localhost:5000/health

# Check logs
docker-compose logs backend
```

### Can't login?
```bash
# Check if user exists in database
docker exec -it shop-mysql mysql -u shop_user -pshop_password shop_db
SELECT * FROM users;
```

---

## 📝 Environment Variables

**Frontend (.env)**
```
REACT_APP_API_URL=http://localhost:5000
```

**Backend (backend/.env)**
```
PORT=5000
DB_HOST=mysql
DB_USER=shop_user
DB_PASSWORD=shop_password
DB_NAME=shop_db
JWT_SECRET=shop-secret-key-change-in-production
CLIENT_URL=http://localhost:3000
```

---

## 🎯 Next Steps

1. Run `docker-compose up`
2. Open http://localhost:3000
3. Create an account
4. Try logging in
5. Check backend logs: `docker-compose logs backend`
6. Query database: `docker exec -it shop-mysql mysql...`

---

## 📚 Full Documentation

See [BACKEND_SETUP.md](BACKEND_SETUP.md) for complete documentation including:
- Database schema
- Security features
- Development setup
- Performance notes

---

## ✨ You're all set!

Your full-stack application is Docker-ready and production-configured. 

Start building! 🎉
