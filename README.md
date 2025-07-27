# Selenium-React-Node Framework

This project demonstrates a simple full-stack automation testing setup:
- React frontend (not fully included here)
- Node.js/Express backend API
- Selenium-based UI automation using Python

## Setup

### Backend
```
cd backend
npm install express cors
node server.js
```

### Tests
Ensure you have Python, Selenium, and ChromeDriver installed.

```
pip install selenium pytest
pytest tests/test_ui.py
```

Frontend assumed to be running at `http://localhost:3000`