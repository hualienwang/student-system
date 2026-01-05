# Deploying to Render.com

This document provides instructions for deploying the Student Management System to Render.com using the provided `render.yaml` configuration.

## Overview

The application consists of two services:
- **Backend**: FastAPI application serving the API
- **Frontend**: Vue.js application serving the user interface

## Deployment Steps

### 1. Prepare Your Repository

1. Push your code to a Git repository (GitHub, GitLab, or Bitbucket)
2. Make sure the `render.yaml` file is in the root of your repository

### 2. Create a New Web Service on Render

1. Go to https://dashboard.render.com/
2. Click "New +" and select "Web Service"
3. Connect your Git repository
4. Render will automatically detect the `render.yaml` file and use it for configuration

### 3. Configure Environment Variables (Optional)

The `render.yaml` file specifies the following environment variables:

#### Backend Service
- `DB_TYPE`: Set to `sqlite`
- `DATABASE_URL`: Points to local SQLite database
- `ALLOWED_ORIGINS`: Specifies allowed origins for CORS
- `PORT`: Set to `8000`

#### Frontend Service
- `VITE_API_BASE_URL`: Automatically set to the backend service URL

### 4. Deployment Process

1. After connecting your repository, Render will:
   - Build the backend service using `./backend/Dockerfile`
   - Build the frontend service using `./frontend/Dockerfile`
   - Deploy both services
   - Set up the proper connection between frontend and backend

### 5. Access Your Application

Once deployed:
- The frontend will be available at: `https://student-system-frontend.onrender.com`
- The backend API will be available at: `https://student-system-backend.onrender.com`
- API documentation will be available at: `https://student-system-backend.onrender.com/docs`

## Configuration Details

### Backend Service (`student-system-backend`)
- Built using Docker with `./backend/Dockerfile`
- Uses SQLite as the database (file-based)
- Exposes port 8000
- CORS is configured to allow connections from the frontend

### Frontend Service (`student-system-frontend`)
- Built using Docker with `./frontend/Dockerfile`
- Uses Nginx to serve the Vue.js application
- Automatically configured to connect to the backend service
- Exposes port 80

## Environment Configuration

The configuration includes:
- Both services deployed to the same region (Oregon) for optimal performance
- Free plan selected for both services
- Auto-deployment disabled by default (enable after initial deployment)
- CORS configured to allow connections between services

## Using MySQL Instead of SQLite (Optional)

If you prefer to use MySQL instead of SQLite, uncomment the database section in `render.yaml` and update the backend configuration:

1. Uncomment the MySQL database section in `render.yaml`
2. Update your backend's database configuration to use MySQL
3. Change the `DB_TYPE` environment variable to `mysql`

## Troubleshooting

### Common Issues

1. **Connection Issues Between Services**
   - Ensure both services are deployed to the same region
   - Verify that the frontend is using the correct backend URL

2. **Build Failures**
   - Check that Dockerfiles are properly configured
   - Verify that all dependencies are correctly specified

3. **CORS Errors**
   - Confirm that `ALLOWED_ORIGINS` includes your frontend URL
   - Check that the backend is properly configured to accept requests from your frontend

### Health Checks

- Backend health check: `GET /health`
- Frontend: Should load without errors
- Database: Automatically managed by Render if using the database service

## Performance Considerations

- The free plan has limitations on resource usage and sleep after inactivity
- For production use, consider upgrading to paid plans
- SQLite is suitable for development and low-traffic applications
- For higher traffic, consider using MySQL or PostgreSQL

## Updating Your Deployment

After the initial deployment, you can enable auto-deploy in the Render dashboard to automatically deploy changes when you push to your Git repository.