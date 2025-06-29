# ---- Builder Stage ----
# Use a full python image to get build tools if needed
FROM python:3.12 as builder

WORKDIR /app

# Install uv for faster dependency installation
RUN pip install uv

# Copy dependency file
COPY requirements.txt .

# Install dependencies to a target directory, which will be copied to the runner
RUN uv pip install --no-cache -r requirements.txt --target /app/deps


# ---- Runner Stage ----
# Use a slim image for the final, smaller container
FROM python:3.12-slim

WORKDIR /app

# Copy dependencies from the builder stage
COPY --from=builder /app/deps /usr/local/lib/python3.12/site-packages

# Copy the application source code
COPY src/ ./src

# Create a non-root user for better security
RUN addgroup --system app && adduser --system --group app
USER app

# Expose the port Streamlit runs on
EXPOSE 8501

# Set headless mode for running in a container
ENV STREAMLIT_SERVER_HEADLESS=true

# Command to run the application
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"] 