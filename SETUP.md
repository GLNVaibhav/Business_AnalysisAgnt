# 🚀 Setup Guide - Agentic Business Surveillance System

Welcome! This guide will help you get the application running on your machine.

---

## 📋 Prerequisites

Before starting, make sure you have these installed on your computer:

### Required Software

1. **Python 3.11 or higher**
   - Download: https://www.python.org/downloads/
   - During installation, **CHECK** "Add Python to PATH"
   - Verify: Open terminal and run `python --version`

2. **Node.js 18 or higher**
   - Download: https://nodejs.org/ (get the LTS version)
   - Verify: Open terminal and run `node --version`

3. **Git** (Optional, for version control)
   - Download: https://git-scm.com/downloads

### Optional (For Docker Deployment)

4. **Docker Desktop**
   - Download: https://www.docker.com/products/docker-desktop/
   - Only needed if you want to use Docker instead of local setup

---

## 🔧 Installation Steps

### Step 1: Extract the Files

Extract the zip file to a folder on your computer, for example:

- `C:\Projects\Business-Analysis-Agent` (Windows)
- `/Users/yourname/Business-Analysis-Agent` (Mac/Linux)

### Step 2: Install Backend Dependencies

Open a terminal/command prompt and navigate to the project folder:

```bash
# Navigate to the backend folder
cd path/to/Business-Analysis-Agent/backend

# Install Python dependencies
pip install -r requirements.txt
```

**Note:** If you see any errors about missing modules, run:

```bash
pip install fastapi uvicorn pandas numpy python-multipart aiofiles pydantic
```

### Step 3: Install Frontend Dependencies

Open a **new** terminal/command prompt:

```bash
# Navigate to the frontend folder
cd path/to/Business-Analysis-Agent/frontend

# Install Node.js dependencies
npm install
```

**Note:** This may take 2-5 minutes to download all packages.

---

## ▶️ Running the Application

You have **3 options** to run the application:

### Option 1: Quick Start (Windows Only) ⭐ EASIEST

1. Double-click the `start.bat` file in the root folder
2. Two terminal windows will open automatically
3. Wait 10-15 seconds for both servers to start
4. Open your browser and go to: **http://localhost:3000**

### Option 2: Manual Start (Windows/Mac/Linux)

**Terminal 1 - Backend:**

```bash
cd backend
uvicorn api:app --reload --port 8080
```

Wait until you see: `Application startup complete`

**Terminal 2 - Frontend:**

```bash
cd frontend
npm run dev
```

Wait until you see: `Local: http://localhost:3000`

**Then open your browser:** http://localhost:3000

### Option 3: Docker (Advanced)

If you have Docker Desktop installed and running:

```bash
# From the root folder
docker-compose up --build
```

Then open your browser: **http://localhost:3000**

---

## 🎯 Using the Application

Once the application is running:

1. **Upload CSV Files**
   - Go to http://localhost:3000
   - Upload 4 CSV files:
     - `orders.csv`
     - `reviews.csv`
     - `sellers.csv`
     - `inventory.csv`
   - Sample files are in: `backend/data/` folder

2. **View Analysis**
   - Click "Run Analysis" button
   - Wait for AI agents to process the data
   - View results in the dashboard

3. **Chat with AI**
   - Click on "Chat" tab
   - Ask questions about your business data
   - Get AI-powered insights and recommendations

---

## 🌐 Access Points

Once running, you can access:

- **Frontend Application:** http://localhost:3000
- **Backend API:** http://localhost:8080
- **API Documentation:** http://localhost:8080/docs (Interactive Swagger UI)
- **Health Check:** http://localhost:8080/api/health

---

## ❗ Common Issues & Solutions

### Issue 1: "Port already in use"

**Error:** `Address already in use` or `Port 8080/3000 is already in use`

**Solution:**

```bash
# Windows
netstat -ano | findstr :8080
taskkill /PID <PID_NUMBER> /F

# Mac/Linux
lsof -ti:8080 | xargs kill -9
```

### Issue 2: "Module not found" (Python)

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**

```bash
cd backend
pip install -r requirements.txt
```

### Issue 3: "command not found: npm"

**Error:** `npm is not recognized as an internal or external command`

**Solution:**

- Install Node.js from https://nodejs.org/
- Restart your terminal after installation
- Verify with: `node --version`

### Issue 4: "Python not found"

**Error:** `python is not recognized`

**Solution:**

- Install Python from https://www.python.org/
- During installation, check "Add Python to PATH"
- Restart your terminal
- Try `python --version` or `python3 --version`

### Issue 5: Docker fails to build

**Error:** Docker build errors

**Solution:**

- Make sure Docker Desktop is running
- Run: `docker-compose down`
- Then: `docker-compose up --build`

### Issue 6: Frontend shows "Cannot connect to backend"

**Solution:**

1. Make sure backend is running (check terminal for errors)
2. Verify backend is accessible: http://localhost:8080/api/health
3. Check frontend/.env file has: `VITE_API_URL=http://localhost:8080`

---

## 📂 CSV File Format

Your CSV files should have these columns:

**orders.csv:**

```csv
order_id,customer_id,product_id,order_date,amount,status
1,101,501,2024-01-15,299.99,completed
```

**reviews.csv:**

```csv
review_id,product_id,rating,review_text,review_date
1,501,5,Great product!,2024-01-16
```

**sellers.csv:**

```csv
seller_id,seller_name,rating,price,delivery_time
1,Seller A,4.5,299.99,2
```

**inventory.csv:**

```csv
product_id,stock_level,reorder_level,last_updated
501,100,20,2024-01-20
```

---

## 🛑 Stopping the Application

### If using start.bat or manual terminals:

- Press `Ctrl + C` in each terminal window
- Or simply close the terminal windows

### If using Docker:

```bash
docker-compose down
```

---

## 🔄 Restarting After Changes

If you modify any code:

**Backend changes:**

- The server will auto-reload (if running with `--reload` flag)
- Or press `Ctrl + C` and restart: `uvicorn api:app --reload --port 8080`

**Frontend changes:**

- Vite will auto-reload in the browser
- Or press `Ctrl + C` and restart: `npm run dev`

---

## 📞 Getting Help

If you encounter issues:

1. Check the terminal/console for error messages
2. Review the [Common Issues](#-common-issues--solutions) section above
3. Make sure all prerequisites are installed correctly
4. Check that both backend and frontend are running
5. Try the health check endpoint: http://localhost:8080/api/health

---

## 🎉 You're All Set!

Once you see both servers running without errors, open your browser to:

### 🌟 http://localhost:3000

Upload your CSV files and start analyzing your business data with AI! 🚀

---

## 📝 Project Structure

```
Business-Analysis-Agent/
├── backend/           # Python backend (FastAPI)
│   ├── agents/       # AI agent logic
│   ├── workflow/     # Analysis workflow
│   ├── api.py        # Main API server
│   └── requirements.txt
├── frontend/         # React frontend
│   ├── src/          # React components
│   └── package.json
├── deploy/           # Docker configurations
├── start.bat         # Quick start script (Windows)
└── SETUP.md          # This file
```

---

**Version:** 1.0.0  
**Last Updated:** January 2026  
**Hackathon Project:** Agentic AI for Autonomous Business Decision-Making
