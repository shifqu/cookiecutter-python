# Stage 1: Base build stage
FROM python:{{ cookiecutter.python_version }}-slim AS builder

# Create the app directory
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Upgrade pip and install dependencies
RUN pip install --upgrade pip pip-tools

# Copy the requirements files first (better caching)
COPY requirements/ /app/requirements/

# Install Python dependencies
RUN pip-sync requirements/main.txt

# Stage 2: Development stage
FROM builder AS development

# Install development dependencies
COPY requirements/ /app/requirements/
RUN pip-sync requirements/dev.txt

# Copy application code
COPY . .

# Install the application in editable mode
RUN pip install --editable .[dev]

# Run the application
CMD ["python", "-m", "{{ cookiecutter.package_slug }}"]

# Stage 3: Production stage
FROM python:{{ cookiecutter.python_version }}-slim

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python{{ cookiecutter.python_version }}/site-packages/ /usr/local/lib/python{{ cookiecutter.python_version }}/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser . .

# Install the application
RUN pip install .

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Switch to non-root user
USER appuser

# Run the application
CMD ["python", "-m", "{{ cookiecutter.package_slug }}"]
