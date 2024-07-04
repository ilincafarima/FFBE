FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose the port
EXPOSE 8080

# Run the application
CMD gunicorn FIXIFY_PROD.wsgi:application --bind 0.0.0.0:$PORT
