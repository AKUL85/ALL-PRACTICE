# Shop Application - Full Stack Docker Setup

A complete full-stack authentication application with React frontend, Node.js/Express backend, and MySQL database.

## Project Structure

```
Shop/
├── src/                    # React frontend
├── backend/                # Node.js/Express backend
├── public/                 # Static assets
├── Dockerfile              # Frontend Docker image
├── docker-compose.yml      # Docker Compose configuration
└── package.json            # Frontend dependencies
```

## Features

- **Frontend (React + Vite)**
  - Beautiful login/signup form with Tailwind CSS
  - Form validation
  - Real API integration with backend
  - JWT token management
  - User session persistence

- **Backend (Node.js + Express)**
  - User authentication (signup/login)
  - Password hashing with bcryptjs
  - JWT token generation
  - Protected routes
  - CORS enabled
  - Health check endpoint

- **Database (MySQL)**
  - User table with timestamps
  - Unique email constraint
  - Password hashing support

## Prerequisites

- Docker
- Docker Compose
- No additional installations needed!

## Quick Start

### Run with Docker Compose

```bash
docker-compose up
```

This single command will:
1. Create and start a MySQL container
2. Create and start the backend API
3. Create and start the frontend application
4. Wait for all services to be healthy

### Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **Health Check**: http://localhost:5000/health

## Testing the Application

### Create an Account

1. Go to http://localhost:3000
2. Click "Sign up"
3. Fill in the form:
   - **Name**: Your full name
   - **Email**: test@example.com
   - **Password**: password123
   - **Confirm Password**: password123
4. Click "Create Account"

### Sign In

1. Click "Sign in"
2. Enter your credentials:
   - **Email**: test@example.com
   - **Password**: password123
3. Click "Sign In"
4. You'll see a welcome page with your user info

## API Endpoints

### Authentication

- **POST** `/api/auth/signup` - Create new user
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
  }
  ```

- **POST** `/api/auth/login` - User login
  ```json
  {
    "email": "john@example.com",
    "password": "password123"
  }
  ```

- **GET** `/api/auth/profile` - Get user profile (requires JWT token)
  - Header: `Authorization: Bearer <token>`

### Health Check

- **GET** `/health` - Server status

## Environment Variables

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:5000
```

### Backend (backend/.env)
```
PORT=5000
DB_HOST=mysql
DB_PORT=3306
DB_USER=shop_user
DB_PASSWORD=shop_password
DB_NAME=shop_db
JWT_SECRET=shop-secret-key-change-in-production
CLIENT_URL=http://localhost:3000
NODE_ENV=production
```

## Useful Docker Commands

### Stop all services
```bash
docker-compose down
```

### Rebuild and run
```bash
docker-compose up --build
```

### View logs
```bash
docker-compose logs -f        # All services
docker-compose logs backend    # Backend only
docker-compose logs app        # Frontend only
docker-compose logs mysql      # Database only
```

### Access MySQL directly
```bash
docker exec -it shop-mysql mysql -u shop_user -p shop_db
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## Features in Detail

### Frontend Features
- ✓ Responsive design with Tailwind CSS
- ✓ Real-time form validation
- ✓ Error handling with user feedback
- ✓ Loading states
- ✓ JWT token storage in localStorage
- ✓ User session persistence
- ✓ Logout functionality
- ✓ Beautiful UI with gradients and shadows

### Backend Features
- ✓ Express.js REST API
- ✓ Password hashing with bcryptjs
- ✓ JWT authentication
- ✓ MySQL database connection
- ✓ CORS support
- ✓ Health check endpoint
- ✓ Error handling middleware
- ✓ Input validation

### Security Features
- ✓ Password encryption (bcryptjs)
- ✓ JWT token authentication
- ✓ CORS enabled
- ✓ Input validation
- ✓ Database connection pooling
- ✓ Protected routes

## Troubleshooting

### Port Already in Use
```bash
# Change ports in docker-compose.yml or kill the process
docker-compose down  # Stop all containers
```

### Database Connection Error
```bash
# Check if MySQL is running
docker ps

# View MySQL logs
docker-compose logs mysql

# Rebuild services
docker-compose down
docker-compose up --build
```

### Frontend Can't Connect to API
- Check if backend is running: http://localhost:5000/health
- Check browser console for CORS errors
- Verify REACT_APP_API_URL is set correctly in .env

### Can't Access MySQL
```bash
# Check MySQL container status
docker exec shop-mysql mysql -u shop_user -pshop_password shop_db -e "SELECT * FROM users;"
```

## Development

### Local Development (without Docker)

#### Frontend
```bash
npm install
npm run dev
```

#### Backend
```bash
cd backend
npm install
npm run dev
```

Make sure you have MySQL running locally on port 3306.

## Performance Notes

- Multi-stage builds for optimized frontend image
- Alpine Linux for smaller image sizes
- Connection pooling in MySQL
- Health checks for all services
- Automatic restart policies

## License

MIT

## Support

For issues or questions, please check the Docker logs:
```bash
docker-compose logs
```
