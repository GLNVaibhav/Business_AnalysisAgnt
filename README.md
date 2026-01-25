# 🧠 Agentic Business Surveillance System

AI-powered decision intelligence platform for autonomous business monitoring and recommendations.

## 📋 Quick Start

### Using Docker (Recommended)

```bash
docker-compose up --build
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Local Development

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn api:app --reload --port 8080

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

- Frontend: http://localhost:3000
- Backend: http://localhost:8080

## ✨ Features

- 🔍 Continuous business monitoring (24/7)
- 📊 Multi-agent AI system (Surveillance → Analysis → Alternatives → Decision)
- 🎯 What-if scenario simulation
- 💡 Natural language insights and chat interface
- 🛡️ Transparent, explainable AI with confidence scores

## 🏗️ Architecture

```
React Frontend (Port 3000)
    ↓ HTTP/REST
FastAPI Backend (Port 8000/8080)
    ↓
Multi-Agent AI System
    ├── Surveillance Agent
    ├── Analysis Agent
    ├── Alternatives Agent
    └── Decision Agent
    ↓
Business Data (CSV Files)
```

## 📁 Project Structure

```
├── backend/           # Backend application
│   ├── agents/       # AI agent modules
│   ├── workflow/     # Orchestration logic
│   ├── utils/        # Utility functions
│   ├── services/     # Business logic
│   ├── data/         # Sample data
│   ├── api.py        # FastAPI app
│   └── requirements.txt
├── frontend/          # React application
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.jsx
│   └── package.json
├── deploy/            # Deployment configs
│   ├── Dockerfile.backend
│   └── Dockerfile.frontend
├── docker-compose.yml
└── README.md
```

## 🛠️ Technology Stack

**Frontend:** React 18, Vite, Recharts, Axios  
**Backend:** FastAPI, Uvicorn, Pandas, Python 3.11+  
**AI:** Multi-agent LLM system, NLP  
**DevOps:** Docker, Docker Compose

## 🔗 API Endpoints

- `GET /api/health` - Health check
- `POST /api/analysis/run` - Upload CSVs and run analysis
- `POST /api/chat` - Chat with AI advisor
- `GET /docs` - Interactive API documentation (Swagger UI)

## ⚙️ Configuration

**Environment Variables:**

- Backend: `PYTHONUNBUFFERED=1`
- Frontend: `VITE_API_URL=http://localhost:8080`

**CSV Format:**

- **orders.csv:** order_id, customer_id, product_id, order_date, amount, status
- **reviews.csv:** review_id, product_id, rating, review_text, review_date
- **sellers.csv:** seller_id, seller_name, rating, price, delivery_time
- **inventory.csv:** product_id, stock_level, reorder_level, last_updated

## 🐛 Troubleshooting

**Port already in use:**

```bash
# Windows
netstat -ano | findstr :8080
taskkill /PID <PID> /F
```

**Module not found:**

```bash
cd backend
pip install -r requirements.txt
```

**Docker issues:**

```bash
docker-compose down
docker-compose up --build
```

---

## 📄 License

MIT License - Hackathon Project 2024
