#Full-Stack DevOps Demo

An advanced DevOps reference project demonstrating a Full-Stack application (React + Flask) with a comprehensive CI/CD pipeline.

## Architecture
- **Frontend**: React (Vite) - Serves the UI.
- **Backend**: Python Flask - Serves the API.
- **Infrastructure**: Docker & Docker Compose.
- **CI/CD**: GitHub Actions -> GitHub Container Registry (GHCR).

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Node.js 18+ (for local frontend dev)
- Python 3.9+ (for local backend dev)

### Quick Start (Docker)
Run the entire stack with one command:
```bash
docker-compose up --build
```
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:5000`

### Local Development

1. **Backend**:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

2. **Frontend**:
   ```bash
   cd client
   npm install
   npm run dev
   ```

## CI/CD Pipeline
The GitHub Actions workflow (`.github/workflows/ci-cd.yml`) automatically:
1. **Tests** both Frontend and Backend in parallel.
2. **Builds** Docker images for both services.
3. **Publishes** images to GitHub Container Registry (GHCR) upon success.

## Live Deployment (Render)
This project is configured for **Render.com**.

1. Create a [Render Account](https://render.com).
2. Click **New +** -> **Blueprint**.
3. Connect your GitHub account and select this repository.
4. Click **Apply**.

Render will automatically:
- Build and deploy the Flask Backend.
- Build the React Frontend (injecting the correct Backend URL).
- Give you a live public URL (e.g., `https://pipeline-pulse-frontend.onrender.com`).
