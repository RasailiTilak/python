# UV[https://docs.astral.sh/uv/]

1. installation
2. working on projects
    - ```uv init project```
    - ```cd project```
    - ```uv run main.py```
    - ```uv add fastapi ```

    - FOR THE WHILE FILES
    -  ```uv build```
    - for the help
    - ``` uv```
    
3. running scripts
- ```ex.py``` this is the single script 
- ```uv run ex.py``` this through the error
- ```uv run --with 'flask' --with'paho-mqtt' ex.py``` with out installing the dependies lib 
- ```uv ad --script ex.py 'flask''paho-mqtt'``` run this dependencies in the directly terminal after that run ``` uv run ex.py```







# system run with the UV
# 🖥️ Running a Python Project with uv on Linux and Autostart via systemd

## ✅ Step 1: Install uv on Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Or with pipx:
```bash
pipx install uv
```

---

## 📁 Step 2: Initialize Your Project with uv
Navigate to your project directory:
```bash
cd /path/to/your-project
uv init
```
This creates `pyproject.toml`, `.python-version`, and `.venv/`.

---

## 📦 Step 3: Add Dependencies
```bash
uv add flask  # or any other package your app needs
```

---

## 🚀 Step 4: Run Your Project with uv
```bash
uv run python app.py
```
This runs your script in the uv-managed environment.

---

## 🧪 Step 5: Use Inline Dependency Scripts (Optional)
In a Python script (e.g., `script.py`):
```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests"]
# ///
import requests
print(requests.get("https://example.com"))
```
Then run:
```bash
uv run script.py
```

---

## 🔁 Step 6: Run Script from Outside the Project Directory
```bash
uv run --project /path/to/project /path/to/project/script.py
```

---

## 🔄 Step 7: Change Python Version
Edit `.python-version` in your project directory:
```
3.11.7
```
Then run:
```bash
uv sync
```

---

## 🧹 Step 8: Remove or Upgrade Dependencies
```bash
uv remove flask
uv lock --upgrade-package flask
```

---

# ⚙️ Step 9: Auto-Start Python Project on Boot with systemd

## 📝 9.1 Create a Service File
```bash
sudo nano /etc/systemd/system/myproject.service
```

### Example Content:
```ini
[Unit]
Description=My UV Python Project Service
After=network.target

[Service]
WorkingDirectory=/home/youruser/myproject
ExecStart=/home/youruser/.local/bin/uv run python app.py
Restart=always
RestartSec=5
User=youruser
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```
> Replace `/home/youruser/...` with the actual path to your user and project.

---

## ⚡ 9.2 Enable and Start the Service
```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable myproject.service
sudo systemctl start myproject.service
```

---

## 🔍 9.3 Check Status and Logs
```bash
sudo systemctl status myproject.service
journalctl -u myproject.service -f
```

---

✅ Your uv-based Python project will now start automatically after system reboot. 