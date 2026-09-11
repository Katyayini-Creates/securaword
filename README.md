# 🔐 SecuraWord

A modern password security application that analyzes password strength, estimates entropy, provides actionable security feedback, and generates strong passwords through an interactive cyberpunk-inspired user interface.

---

## 🚀 Live Demo

🔗 **Live Application:** https://securaword-1.onrender.com

🔗 **API Documentation:** https://securaword.onrender.com/docs

---

## 📌 Overview

SecuraWord is a full-stack password security application designed to help users evaluate password strength and improve password security.

The application analyzes passwords using entropy calculation, rule-based validation, common-password detection, and multiple pattern-based checks. It classifies password strength and provides actionable feedback to help users create stronger passwords.

SecuraWord also includes a password generator that uses the browser's Web Crypto API for cryptographically secure random character selection and password shuffling.

---

## ✨ Features

### 🔍 Password Strength Analysis

- Real-time password analysis
- Password strength classification (Weak / Medium / Strong)
- Password entropy calculation
- Evaluation against 5 fundamental password criteria:
  - Length
  - Uppercase characters
  - Lowercase characters
  - Numbers
  - Special characters
- Common password and dictionary-based detection
- Repeated consecutive character detection
- Sequential pattern detection
- Repeated block detection
- Word + number pattern detection
- Keyboard pattern detection
- Dynamic security score
- Visual strength meter
- Actionable security feedback and improvement suggestions

### 🔐 Secure Password Generator

- Generates passwords using the browser's Web Crypto API
- Uses `crypto.getRandomValues()` for cryptographically secure random selection
- Uses Fisher–Yates shuffling for password character arrangement
- Includes:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- One-click password generation
- One-click clipboard copy
- Automatically analyzes generated passwords

### 🎨 User Interface

- Retro cyberpunk-inspired design
- Neon-themed UI
- Interactive strength meter
- Password visibility toggle
- Responsive layout
- Smooth animations and visual effects

---

## 🛠 Tech Stack

### Frontend

- React
- Vite
- JavaScript
- CSS3
- React Icons

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

### API

- REST APIs

### Security

- Password entropy analysis
- Regex and rule-based validation
- Pattern detection
- Common-password detection
- Web Crypto API (`crypto.getRandomValues()`)

### Deployment

- Render
- Render Static Site
- Render Web Service

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```text
SecuraWord/
│
├── backend/
│   └── src/
│       ├── core/
│       │   ├── attacks.py
│       │   ├── checker.py
│       │   ├── entropy.py
│       │   └── feedback.py
│       │
│       ├── api.py
│       └── main.py
│
├── data/
│   └── common_passwords.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── tests/
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Katyayini-Creates/securaword.git
cd securaword
```

### 2. Backend Setup

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI backend:

```bash
PYTHONPATH=backend python -m uvicorn src.api:app --reload --port 8000
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI API documentation:

```text
http://127.0.0.1:8000/docs
```

### 3. Frontend Setup

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install the frontend dependencies:

```bash
npm install
```

Create a `.env` file inside the `frontend` directory:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Start the frontend development server:

```bash
npm run dev
```

The frontend will run at:

```text
http://localhost:5173
```

### 4. Running the Application

Make sure both the backend and frontend development servers are running.

Open the application in your browser:

```text
http://localhost:5173
```

The React frontend communicates with the FastAPI backend through the REST API.

You can also access the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

### 5. Live Deployment

The application is deployed online using Render.

**Live Application:**  
https://securaword-1.onrender.com

**Backend API Documentation:**  
https://securaword.onrender.com/docs

---

## 🚀 How It Works

1. The user enters a password in the React frontend.
2. The frontend sends the password to the FastAPI backend through a REST API request.
3. The backend analyzes the password using:
   - Password length and character composition
   - Entropy calculation
   - Regex and rule-based validation
   - Common-password and dictionary checks
   - Repeated consecutive character detection
   - Sequential pattern detection
   - Repeated block detection
   - Word + number pattern detection
   - Keyboard pattern detection
4. The backend calculates a security score and classifies the password strength.
5. Actionable feedback is generated based on the detected weaknesses.
6. The analysis results are returned to the React frontend.
7. The frontend displays the strength level, score, entropy, and security recommendations.

The built-in password generator uses the browser's Web Crypto API for cryptographically secure random selection and automatically analyzes the generated password.

---


## 🧪 Testing

The application was tested using:

- 30+ password test cases covering different password strengths and patterns
- 15+ testers for functional validation and usability feedback
- Frontend-backend integration testing during local development
- Production testing after deployment

Testing focused on password classification, security feedback, API communication, password generation, and clipboard functionality.

---


## 🌐 Deployment

SecuraWord is deployed as a full-stack application using Render.

### Production Architecture

```text
React + Vite Frontend
        │
        │ REST API
        ▼
FastAPI Backend
        │
        ├── Entropy Calculation
        ├── Password Rule Validation
        ├── Pattern Detection
        ├── Common Password Detection
        └── Security Feedback
```

### Deployment Services

- **Frontend:** Render Static Site
- **Backend:** Render Web Service
- **API Documentation:** FastAPI Swagger UI

### Production Configuration

- The frontend uses the `VITE_API_URL` environment variable to connect to the deployed backend.
- The backend uses the `ALLOWED_ORIGINS` environment variable for production CORS configuration.
- The FastAPI backend is served using Uvicorn.

---

## 📸 Screenshots

### Home Screen

> <img width="1907" height="905" alt="image" src="https://github.com/user-attachments/assets/dd822ff5-ef8b-48a1-9c12-d5dc4717a19c" />

---

### Weak Password Example

<img width="1063" height="897" alt="image" src="https://github.com/user-attachments/assets/4c188219-3427-4494-b81c-0f7f0c7d337f" />

---

### Strong Password Example

<img width="1077" height="886" alt="image" src="https://github.com/user-attachments/assets/9bb27204-f668-4a61-b4fc-a59b5fd0319e" />

---

### Secure Password Generator

<img width="1056" height="908" alt="image" src="https://github.com/user-attachments/assets/e5476a40-b60d-47cb-aae7-04b5e3d46166" />

---

## 📈 Future Improvements

- Password breach detection using the Have I Been Pwned API
- Password history
- Password statistics dashboard
- Crack-time estimation
- Advanced password generation controls
- Dark/Light themes
- Exportable security reports

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- React and Vite development
- FastAPI backend development
- REST API integration
- Frontend-backend communication
- Password security concepts
- Entropy calculation
- Rule-based and pattern-based password analysis
- Web Crypto API and secure random password generation
- UI/UX design and responsive interfaces
- Git and GitHub workflow
- Environment-based application configuration
- CORS configuration
- Full-stack application deployment
- Production testing and debugging

---

## 👩‍💻 Author

**Katyayini Singh**

Cybersecurity & Forensics Undergraduate  
UPES Dehradun

GitHub: https://github.com/Katyayini-Creates

---

## 📄 License

This project is licensed under the MIT License.

