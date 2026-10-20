#!/usr/bin/env bash
set -e

echo "=== OsonBot Ubuntu VPS Deployment Script ==="

# 1. Update system packages and install prerequisites
echo "[1/4] Installing system packages..."
sudo apt-get update -y
sudo apt-get install -y curl git build-essential libpq-dev

# 2. Setup Python 3.12 using uv (guarantees pre-built wheels for asyncpg and pydantic)
echo "[2/4] Setting up Python 3.12 virtual environment..."
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

if [ -d ".venv" ]; then
    # Check if .venv python is >= 3.14 (which breaks asyncpg/pydantic wheels)
    PY_VER=$(.venv/bin/python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || echo "unknown")
    if [ "$PY_VER" = "3.14" ] || [ "$PY_VER" = "unknown" ]; then
        echo "Removing incompatible .venv (Python $PY_VER)..."
        rm -rf .venv
    fi
fi

if [ ! -d ".venv" ]; then
    uv python install 3.12
    uv venv --python 3.12 .venv
fi

# 3. Install Python dependencies
echo "[3/4] Installing Python requirements..."
uv pip install -r requirements.txt

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
