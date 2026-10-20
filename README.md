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
