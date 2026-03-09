<p align="center">
  <img src="https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-4.4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
</p>

# 📸 PicShare

**PicShare** is a modern photo-sharing web application built with Django. Create galleries, upload images, share them with anyone via unique links, and interact through likes and comments — all wrapped in a clean, Tailwind CSS-styled interface.

---

## ✨ Features

### 🔐 Authentication
- User **signup**, **login**, and **logout**
- All core routes are protected with `@login_required`

### 🖼️ Gallery Management
- **Create galleries** with a title and multiple images in a single upload
- **Public / Private** galleries — private ones are password-protected
- **Per-gallery permissions** — toggle downloads, comments, and likes
- **Shareable links** — each gallery gets a unique slug URL
- **Delete galleries** you own

### ❤️ Social Interactions
- **Like / Unlike** images (toggleable, one like per user per image)
- **Comment** on images in real time via AJAX
- Likes and comments return JSON responses for a seamless experience

### 📊 Activity Feed
- Track actions (likes, comments) on **your** galleries
- Chronologically ordered feed on a dedicated activity page

### 🎨 Polished UI
- Styled with **Tailwind CSS** via `django-tailwind`
- Responsive base template with consistent navigation

---

## 🏗️ Project Structure

```
picshare/
├── accounts/          # Auth app — signup, login, logout, dashboard, activity feed
│   ├── views.py
│   └── urls.py
├── gallery/           # Core app — galleries, images, likes, comments
│   ├── models.py      # Gallery, Image, Like, Comment, Activity
│   ├── views.py       # CRUD + AJAX endpoints
│   └── urls.py
├── config/            # Django project settings & root URL config
│   ├── settings.py
│   └── urls.py
├── templates/         # All HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── view_gallery.html
│   ├── my_galleries.html
│   ├── enter_gallery.html
│   ├── share_success.html
│   ├── activity.html
│   ├── login.html
│   └── signup.html
├── media/             # User-uploaded gallery images
├── theme/             # Tailwind CSS theme app
├── manage.py
└── requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **Node.js & npm** (required by `django-tailwind` for building CSS)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/picshare.git
   cd picshare
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS / Linux
   source .venv/bin/activate
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tailwind CSS dependencies**

   ```bash
   python manage.py tailwind install
   ```

5. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** *(optional — for admin access)*

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Tailwind watcher** *(in a separate terminal)*

   ```bash
   python manage.py tailwind start
   ```

8. **Run the development server**

   ```bash
   python manage.py runserver
   ```

9. Open **http://127.0.0.1:8000/** in your browser 🎉

---

## 📡 API-style Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| `GET/POST` | `/signup/` | Register a new account |
| `GET/POST` | `/login/` | Log in |
| `GET` | `/logout/` | Log out |
| `GET` | `/dashboard/` | User dashboard |
| `GET` | `/activity/` | Activity feed for your galleries |
| `GET/POST` | `/gallery/upload/` | Create a new gallery with images |
| `GET` | `/gallery/my/` | View your galleries |
| `POST` | `/gallery/delete/<id>/` | Delete a gallery |
| `GET/POST` | `/gallery/view/` | Enter a gallery by slug + password |
| `GET` | `/gallery/<slug>/` | View a specific gallery |
| `POST` | `/gallery/like/<image_id>/` | Like / unlike an image (JSON) |
| `POST` | `/gallery/comment/<image_id>/` | Add a comment (JSON) |

---

## 🗃️ Data Models

| Model | Key Fields |
|-------|------------|
| **Gallery** | `owner`, `title`, `slug`, `is_public`, `password`, `allow_download`, `allow_comment`, `allow_like` |
| **Image** | `gallery` (FK), `image` (file), `uploaded_at` |
| **Like** | `image` (FK), `user` (FK) — unique together |
| **Comment** | `image` (FK), `user` (FK), `text` |
| **Activity** | `user` (FK), `action`, `image` (FK), `created_at` |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 6.0 |
| **Frontend** | Tailwind CSS 4.4 via `django-tailwind` |
| **Database** | SQLite (default — swap for PostgreSQL in production) |
| **Image Handling** | Pillow |
| **Language** | Python 3 |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with ❤️ using Django & Tailwind CSS
</p>
