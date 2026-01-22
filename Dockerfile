FROM python:3.10.19-slim-bookworm

# Copy in the source code
COPY . .

# Setup an app user so the container doesn't run as the root user
RUN useradd -m app 
# user exists, and /home/app is created

# Switch to non-root user
USER app

