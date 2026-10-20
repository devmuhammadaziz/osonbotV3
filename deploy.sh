#!/usr/bin/env bash
set -e

echo "=== OsonBot Ubuntu VPS Deployment Script ==="

# 1. Update system packages and install prerequisites
echo "[1/4] Installing system packages..."
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip python3-venv libjpeg-dev zlib1g-dev

# 2. Setup Python virtual environment
echo "[2/4] Setting up Python virtual environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# 3. Install Python dependencies
echo "[3/4] Installing Python requirements..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

# 4. Check .env file
echo "[4/4] Checking environment configuration..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "Created .env from .env.example. Please configure your tokens and database credentials inside .env!"
    fi
fi

echo ""
echo "=== Setup Complete! ==="
echo "Option A (Docker):"
echo "  docker compose up -d --build"
echo ""
echo "Option B (Systemd Service):"
echo "  sudo cp osonbot.service /etc/systemd/system/"
echo "  sudo systemctl daemon-reload"
echo "  sudo systemctl enable --now osonbot"
echo ""
echo "Option C (Manual start):"
echo "  .venv/bin/python app.py"
