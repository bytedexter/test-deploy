# FastAPI Hello World - AWS Amplify Deployment

This project contains a simple FastAPI Hello World application configured for deployment on AWS Amplify using Docker.

## Project Structure

```
test-deploy/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Local development setup
├── amplify.yml         # AWS Amplify build configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Local Development

### Prerequisites
- Python 3.11+
- Docker
- Docker Compose

### Running Locally with Python

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Visit `http://localhost:8000` to see the Hello World page
4. Visit `http://localhost:8000/api/hello` for the JSON API response
5. Visit `http://localhost:8000/docs` for the interactive API documentation

### Running Locally with Docker

1. Build and run with Docker Compose:
```bash
docker-compose up --build
```

2. Visit `http://localhost:8000` to see the application

### Running with Docker only

1. Build the Docker image:
```bash
docker build -t fastapi-hello-world .
```

2. Run the container:
```bash
docker run -p 8000:8000 fastapi-hello-world
```

## AWS Amplify Deployment Steps

### Step 1: Prepare Your Repository

1. Make sure all files are committed to your Git repository:
```bash
git add .
git commit -m "Add FastAPI Hello World with Docker configuration"
git push origin main
```

### Step 2: Set Up AWS Amplify

1. **Log in to AWS Console**
   - Go to [AWS Amplify Console](https://console.aws.amazon.com/amplify/)
   - Sign in with your AWS credentials

2. **Create New App**
   - Click "Create new app"
   - Choose "Host web app"

3. **Connect Repository**
   - Select your Git provider (GitHub, GitLab, Bitbucket, etc.)
   - Authorize AWS Amplify to access your repositories
   - Select this repository (`test-deploy`)
   - Choose the `main` branch

### Step 3: Configure Build Settings

1. **Build Settings**
   - Amplify should automatically detect the `amplify.yml` file
   - If not, you can manually configure:
     - Build command: `docker build -t fastapi-hello-world .`
     - Output directory: Leave empty or set to `/`

2. **Environment Variables** (if needed)
   - Add any environment variables your app might need
   - For this simple Hello World app, none are required

### Step 4: Deploy

1. **Review and Deploy**
   - Review your settings
   - Click "Save and deploy"
   - Wait for the build and deployment to complete

2. **Access Your App**
   - Once deployed, AWS Amplify will provide a URL
   - Visit the URL to see your FastAPI Hello World application

### Step 5: Custom Domain (Optional)

1. **Add Custom Domain**
   - In the Amplify console, go to "Domain management"
   - Add your custom domain
   - Follow the DNS configuration instructions

## API Endpoints

- `GET /` - HTML Hello World page
- `GET /api/hello` - JSON API response
- `GET /api/health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## Important Notes for AWS Amplify Deployment

1. **Docker Support**: AWS Amplify supports Docker, but the configuration might need adjustments based on your specific requirements.

2. **Port Configuration**: The application is configured to run on port 8000, which is exposed in the Dockerfile.

3. **Build Process**: The `amplify.yml` file defines the build process. You may need to adjust it based on your specific deployment needs.

4. **Environment Variables**: For production deployments, consider using AWS Amplify's environment variable management for sensitive configuration.

5. **Monitoring**: Once deployed, you can monitor your application through the AWS Amplify console and CloudWatch logs.

## Troubleshooting

- **Build Failures**: Check the build logs in the AWS Amplify console
- **Port Issues**: Ensure the application is binding to `0.0.0.0:8000`
- **Docker Issues**: Verify the Dockerfile works locally before deploying

## Next Steps

- Add a database (PostgreSQL, MongoDB, etc.)
- Implement authentication
- Add more API endpoints
- Set up CI/CD pipelines
- Add monitoring and logging