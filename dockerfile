# Use the official Python image.
FROM python:3.12

# Set the working directory.
WORKDIR /usr/src/app

# Copy the requirements.txt file.
COPY requirements.txt ./

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files.
COPY . .

# Expose port 8000 to the outside world.
EXPOSE 8000

# Run the Django development server.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
