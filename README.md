# 🔐 SecuraWord

A modern password security application that analyzes password strength, estimates entropy, provides actionable security feedback, and generates strong passwords through an interactive cyberpunk-inspired user interface.

---

## 📌 Overview

SecuraWord helps users create and evaluate secure passwords by combining password strength analysis with a built-in secure password generator.

The application evaluates passwords based on multiple security criteria, calculates entropy, classifies the password strength, and provides personalized recommendations to improve password security.

---

## ✨ Features

### 🔍 Password Strength Analysis
- Real-time password analysis
- Password strength classification (Weak / Medium / Strong)
- Password entropy calculation
- Dynamic security score
- Visual strength meter
- Security report with improvement suggestions

### 🔐 Secure Password Generator
- Generates strong random passwords
- Includes:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- One-click password copy to clipboard
- Automatically analyzes generated passwords

### 🎨 User Interface
- Retro cyberpunk inspired design
- Neon-themed UI
- Interactive strength meter
- Password visibility toggle
- Responsive layout
- Smooth animations and glowing effects

---

## 🛠 Tech Stack

### Frontend
- React
- Vite
- CSS3
- React Icons

### Backend
- FastAPI
- Python
- Pydantic
- Uvicorn

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
SecuraWord/
│
├── backend/
│   ├── src/
│   │   ├── core/
│   │   │   ├── checker.py
│   │   │   ├── entropy.py
│   │   │   ├── feedback.py
│   │   │   └── attacks.py
│   │   │
│   │   └── api.py
│   │
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Katyayini-Creates/securaword.git
```

```bash
cd securaword
```

---

## Backend Setup

Navigate to the backend folder.

```bash
cd backend
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the FastAPI server.

```bash
uvicorn src.api:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

---

## Frontend Setup

Open another terminal.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Run the React application.

```bash
npm run dev
```

Frontend will start at:

```
http://localhost:5173
```

---

## 🚀 How It Works

1. Enter a password.
2. The frontend sends the password to the FastAPI backend.
3. The backend:
   - Calculates entropy
   - Computes a security score
   - Generates feedback
4. Results are returned to the React frontend.
5. The UI updates instantly with:
   - Strength meter
   - Security level
   - Entropy
   - Security report

Users can also generate a secure password and copy it directly to the clipboard.

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

- Password breach detection (Have I Been Pwned API)
- Password history
- Password statistics dashboard
- Crack time estimation
- Custom password generation options
- Dark/Light themes
- Export security report

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- React development
- FastAPI backend development
- REST API integration
- State management
- Password security concepts
- Entropy calculation
- UI/UX design
- Git and GitHub workflow
- Frontend-backend communication

---

## 👩‍💻 Author

**Katyayini Singh**

Cybersecurity & Forensics Undergraduate  
UPES Dehradun

GitHub: https://github.com/Katyayini-Creates

---

## 📄 License

This project is licensed under the MIT License.
