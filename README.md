# OsonBot V3

Telegram bot for real estate announcements with automatic image collaging, PostgreSQL database, and admin review panel.

## Quick Ubuntu VPS Deployment

### Option 1: Docker (Recommended)
1. Clone the repository on your VPS:
   ```bash
   git clone https://github.com/devmuhammadaziz/osonbotV3.git
   cd osonbotV3
   ```
2. Create and configure your `.env` file:
   ```bash
   cp .env.example .env
   nano .env
   ```
3. Run the bot with Docker Compose:
   ```bash
   docker compose up -d --build
   ```
4. View logs:
   ```bash
   docker compose logs -f
   ```

---

### Option 2: Automated Script (Systemd)
1. Run the deployment script:
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```
2. Configure `.env`:
   ```bash
   nano .env
   ```
3. Enable and start as a background systemd service:
   ```bash
   sudo cp osonbot.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now osonbot
   ```
4. Check service status:
   ```bash
   sudo systemctl status osonbot
   ```

---

### Option 3: PM2 Process Manager
1. Install uv and Python 3.12:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source $HOME/.local/bin/env
   uv python install 3.12
   uv venv --python 3.12 .venv
   uv pip install -r requirements.txt
   ```
2. Start with PM2:
   ```bash
   pm2 start app.py --name osonbot --interpreter .venv/bin/python
   pm2 save
   ```
3. Logs and status:
   ```bash
   pm2 status
   pm2 logs osonbot
   ```

