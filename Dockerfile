# Base image: Ubuntu desktop with XFCE + VNC + web frontend
FROM dorowu/ubuntu-desktop-lxde-vnc

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy your app code
COPY . /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the VNC web port (default 6080)
EXPOSE 6080

# Start both the desktop environment and your Python app
CMD ["bash", "-c", "python3 main.py & /startup.sh"]
