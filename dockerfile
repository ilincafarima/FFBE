# Use the official Python image.
FROM python:3.12

# Set the working directory.
WORKDIR /FIXIFY/FIXIFY_PROD

# Copy the requirements.txt file.
COPY requirements.txt ./

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files.
COPY . .

# Expose port 8000 to the outside world.
EXPOSE 8080

# Run the Django development server.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
