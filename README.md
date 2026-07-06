<div align="center">

# 🚀 hanServer

### Backend Server for **hanChat** — Real-Time Messaging App

Built with ❤️ by [Hanadora](https://hanadora.site)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/hanServer?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/YOUR_USERNAME/hanServer?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

</div>

---

## 📖 Overview

**hanServer** waa backend-ka (server-ka) uu ku shaqeeyo app-ka **hanChat**, oo ah messaging app dadka isugu xira si degdeg ah oo ammaan ah. Server-kani wuxuu maamulaa:

- 🔐 User authentication (isdiiwaangelinta & login)
- 💬 Messages iyo real-time chat
- 📡 API endpoints oo frontend-ka hanChat isticmaalo
- 🗄️ Database connection (Supabase / PostgreSQL)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔑 Authentication | Login iyo Signup oo ammaan ah (JWT / Supabase Auth) |
| 💬 Real-Time Messaging | Fariimaha isla markiiba loo diro/loo helo |
| 🗃️ Database | Supabase (PostgreSQL) oo leh RLS (Row Level Security) |
| 📩 Push Notifications | FCM / OneSignal integration |
| 🔒 Secure API | Endpoints la ilaaliyay oo token-based |

---

## 🛠️ Tech Stack

- **Backend Framework:** Python (Flask)
- **Database:** PostgreSQL via Supabase
- **Authentication:** JWT / Supabase Auth
- **Realtime:** Supabase Realtime / WebSockets
- **Hosting:** _(fadlan buuxi — tusaale: Render, Railway, VPS)_

---

## 📂 Project Structure

```
hanServer/
├── app.py                # Main Flask app
├── routes/                # API endpoints
│   ├── auth.py
│   └── messages.py
├── models/                 # Database models
├── config.py               # Environment configuration
├── requirements.txt         # Python dependencies
├── .env.example              # Sample environment variables
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/hanServer.git
cd hanServer
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables
Samee file magaciisu yahay `.env`, kadibna geli:
```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your_secret_key
```

### 5️⃣ Run the server
```bash
python app.py
```

Server-ku wuxuu ku shaqayn doonaa: `http://localhost:5000`

---

## 📡 API Endpoints (Example)

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/signup` | Sameyso account cusub |
| POST | `/api/auth/login` | Soo gal account |
| GET | `/api/messages/:chatId` | Hel fariimaha chat gaar ah |
| POST | `/api/messages` | Dir fariin cusub |

---

## 🤝 Contributing

Contributions waa la soo dhaweynayaa! Fadlan samee fork, samee changes-kaaga, ka dibna soo dir pull request.

---

## 📜 License

Licenda MIT — arag [LICENSE](LICENSE) file-ka.

---

<div align="center">

Made with 💻 & ☕ in **Somaliland** 🇸🇴 by **Hanadora**

</div>
