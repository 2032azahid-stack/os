import subprocess
import os

def start_linux_xfce():
    # Pull a lightweight Linux image (Debian slim)
    subprocess.run(["docker", "pull", "dorowu/ubuntu-desktop-lxde-vnc"], check=True)

    # Run container with VNC exposed
    subprocess.run([
        "docker", "run", "-d",
        "-p", "6080:80",  # Web VNC access
        "--name", "linux_xfce",
        "dorowu/ubuntu-desktop-lxde-vnc"
    ], check=True)

    print("Minimal Linux with XFCE-like desktop is running at http://localhost:6080")

def stop_linux_xfce():
    subprocess.run(["docker", "stop", "linux_xfce"], check=True)
    subprocess.run(["docker", "rm", "linux_xfce"], check=True)
    print("Linux XFCE environment stopped and removed.")

if __name__ == "__main__":
    if not os.environ.get("STOP"):
        start_linux_xfce()
    else:
        stop_linux_xfce()
