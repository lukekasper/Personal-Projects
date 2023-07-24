FROM python:latest

# Set the environment variables with default values
ENV ADMIN_USER=default_admin \
    ADMIN_PASSWORD=default_password

RUN mkdir -p /home/Recipies
COPY . /home/Recipies
WORKDIR /home/Recipies

# Install system-level dependencies (for macOS, use brew instead of apt-get)
RUN brew update && \
    brew install mysql-connector-c pkg-config

# install dependencies from requirements file
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
