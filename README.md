# DevOps Demo: Flask + Docker + CI/CD

A simple reference project demonstrating a basic DevOps pipeline using Python Flask, Docker, and GitHub Actions.

## Project Structure
- `app.py`: Simple Flask web application.
- `Dockerfile`: Configuration for containerizing the app.
- `.github/workflows/ci-cd.yml`: Automated pipeline for testing and building.
- `tests/`: Unit tests for the application.

## Getting Started

### Prerequisites
- Python 3.9+
- Docker (optional, for running containers)

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests:**
   ```bash
   pytest
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   Access at `http://localhost:5000`

### Docker Usage

1. **Build the image:**
   ```bash
   docker build -t devops-demo .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 devops-demo
   ```

### CI/CD Pipeline
This project includes a GitHub Actions workflow that automatically runs on every push to `main` or pull request. It performs:
1. **Linting**: Checks code quality with `flake8`.
2. **Testing**: Runs unit tests with `pytest`.
3. **Build**: Verifies the Docker image builds successfully.
