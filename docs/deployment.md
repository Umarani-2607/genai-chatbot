# Deployment Notes

This project is designed to be deployed using containerized workflows.

---

## Local Execution

The application can be run locally using Python for development and testing.

---

## Docker Execution

Docker is used as the primary deployment artifact.

- The Dockerfile defines a minimal Python runtime
- Application dependencies are installed during build
- The container exposes the required application interface

---

## CI/CD Deployment

- GitHub Actions builds the Docker image on every push
- Cloud credentials are not required in CI
- The pipeline validates that the container builds successfully

This approach mirrors production CI/CD workflows.
