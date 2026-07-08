<div align="center">

# 🚀 hanServer

### Backend Server for **hanChat** — Real-Time Messaging App

Built with ❤️ by [hanChat AI](https://han-chates.vercel.app)

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
- **Hosting:** _(hanServer)_

---


---

## 📡 API Endpoints (Example)

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/signup` | Sameyso account cusub |
| POST | `/api/auth/login` | Soo gal account |
| GET | `/api/messages/:chatId` | Hel fariimaha chat gaar ah |
| POST | `/api/messages` | Dir fariin cusub |

---



---

## 📜 License

Licenda MIT — arag [LICENSE](LICENSE) file-ka.

---

<div align="center">

Made with 💻 & ☕ in **Somaliland** 🇸🇴 by **hanServer**

</div>
