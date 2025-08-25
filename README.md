# FastAPI Hello World - AWS Deployment Guide

This project contains a FastAPI Hello World application with multiple deployment options for AWS.

## Project Structure

```
test-deploy/
├── main.py              # FastAPI application (original)
├── app.py              # FastAPI with Lambda support (Mangum)
├── index.html          # Static landing page for Amplify
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Local development setup
├── amplify.yml         # AWS Amplify build configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Important Note About AWS Amplify

**AWS Amplify is primarily designed for static websites and frontend applications.** While it can host your FastAPI code as files, it cannot run the Python server directly. 

For a working FastAPI backend, you have several AWS deployment options:

### Option 1: AWS Lambda + API Gateway (Recommended for FastAPI)

1. **Use the `app.py` file** which includes Mangum for Lambda compatibility
2. **Deploy using AWS SAM or Serverless Framework:**

```bash
# Install AWS SAM CLI
# Then create a SAM template or use Serverless Framework
pip install mangum
```

3. **Alternative: Use Zappa for easy Lambda deployment:**
```bash
pip install zappa
zappa init
zappa deploy dev
```

### Option 2: AWS App Runner (Easiest for Docker)

1. **Push your Docker image to ECR:**
```bash
aws ecr create-repository --repository-name fastapi-hello-world
docker build -t fastapi-hello-world .
docker tag fastapi-hello-world:latest <your-account>.dkr.ecr.us-east-1.amazonaws.com/fastapi-hello-world:latest
docker push <your-account>.dkr.ecr.us-east-1.amazonaws.com/fastapi-hello-world:latest
```

2. **Create App Runner service** in AWS Console pointing to your ECR image

### Option 3: AWS ECS with Fargate

1. **Use the provided Dockerfile**
2. **Create ECS cluster and service**
3. **Deploy using AWS Console or CLI**

### Option 4: AWS EC2

1. **Launch EC2 instance**
2. **Install Docker or Python**
3. **Run your application**

## What AWS Amplify Will Do

AWS Amplify will:
- ✅ Host the `index.html` as a static landing page
- ✅ Serve your FastAPI code files for download/reference
- ❌ **NOT run the Python FastAPI server**

The deployed Amplify site will show a landing page explaining the FastAPI project and provide links to the source code.

## Local Development

### Running with Python

```bash
pip install -r requirements.txt
python main.py
# Visit http://localhost:8000
```

### Running with Docker

```bash
docker-compose up --build
# Visit http://localhost:8000
```

## AWS Amplify Deployment (Static Site)

### Step 1: Commit and Push

```bash
git add .
git commit -m "Add FastAPI project with static landing page"
git push origin main
```

### Step 2: Deploy to Amplify

1. Go to [AWS Amplify Console](https://console.aws.amazon.com/amplify/)
2. Create new app → Host web app
3. Connect your repository
4. Deploy

**Result:** You'll get a static website with a landing page explaining your FastAPI project.

## Recommended Next Steps for Production FastAPI

### For Serverless (Lambda):

1. **Update your FastAPI app for Lambda:**
   - Use the `app.py` file (includes Mangum)
   - Deploy with AWS SAM, Serverless Framework, or Zappa

2. **Example with Zappa:**
```bash
pip install zappa
zappa init
zappa deploy production
```

### For Containerized (App Runner/ECS):

1. **Push to ECR:**
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com
docker build -t fastapi-hello-world .
docker tag fastapi-hello-world:latest <account>.dkr.ecr.us-east-1.amazonaws.com/fastapi-hello-world:latest
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/fastapi-hello-world:latest
```

2. **Create App Runner service** pointing to your ECR image

## API Endpoints (When Deployed Properly)

- `GET /` - HTML Hello World page
- `GET /api/hello` - JSON API response
- `GET /api/health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## Troubleshooting

- **"Illegal path found for appRoot"** - Fixed in this version
- **FastAPI not running on Amplify** - Expected behavior; use Lambda/App Runner instead
- **Local Docker issues** - Ensure Docker is running and ports are available

## Summary

This repository provides:
1. ✅ **Working FastAPI application** (runs locally)
2. ✅ **Docker configuration** (for local development and ECS/App Runner deployment)
3. ✅ **Lambda-ready version** (`app.py` with Mangum)
4. ✅ **Static landing page** (for AWS Amplify)
5. ✅ **Multiple deployment options** documented above

Choose the deployment method that best fits your needs!