# The ABC Success Lab – Website

Django 4.2 website for ABC Success Lab (CAC Reg. 9504456), Lagos, Nigeria.

---

## Stack
- **Backend:** Django 4.2
- **Frontend:** Bootstrap 5.3 + custom CSS (DM Sans + Playfair Display)
- **Database:** SQLite (default) – PostgreSQL-ready (see Settings)
- **Static files:** WhiteNoise
- **Production server:** Gunicorn

---

## Local Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env .env.local               # edit SECRET_KEY, DEBUG=True, ALLOWED_HOSTS

# 4. Run migrations
python manage.py migrate

# 5. Create admin superuser
python create_superuser.py
# Default: admin / ABCAdmin2026! — CHANGE immediately after first login

# 6. Collect static files (development – optional)
python manage.py collectstatic --noinput

# 7. Start dev server
python manage.py runserver
```

Visit http://127.0.0.1:8000 — Admin panel at http://127.0.0.1:8000/admin/

---

## Admin Panel Quick-Start

| Section | What to do |
|---|---|
| **Core › Services** | Add your training programmes with title, description, icon |
| **Core › Testimonials** | Add participant testimonials (mark `is_active=True`) |
| **Core › FAQs** | Add/edit FAQ items |
| **Blog › Categories** | Create categories (e.g. "Career Tips", "Microsoft Office") |
| **Blog › Posts** | Write and publish articles; set `is_published=True` + `published_at` |

---

## Registering the Google Form link

Search for `href="#"` in all templates and replace `#` with your Google Form URL.
There are ~6 occurrences across `base.html`, `home.html`, `about.html`, `services.html`, `contact.html`, and `blog/post_detail.html`.

---

## Production Deployment

```bash
# In .env set:
DEBUG=False
SECRET_KEY=<strong-random-key>
ALLOWED_HOSTS=abcsuccesslab.com.ng,www.abcsuccesslab.com.ng

# Collect static files
python manage.py collectstatic --noinput

# Start with Gunicorn
gunicorn -c gunicorn.conf.py config.wsgi:application
```

Serve with Nginx as reverse proxy pointing to port 8000.
Serve `/media/` and `/staticfiles/` directly from Nginx for best performance.

---

## Switching to PostgreSQL (when ready)

1. `pip install psycopg2-binary`
2. Add to `.env`: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
3. In `config/settings.py`, uncomment the PostgreSQL `DATABASES` block and delete the SQLite one.
4. Run `python manage.py migrate`

---

## Project Structure

```
abcsuccesslab/
├── config/               # Django project settings & URLs
├── core/                 # Home, About, Services, Testimonials, FAQs, Contact
├── blog/                 # Blog/News app with admin panel
├── templates/            # All HTML templates
│   ├── base.html         # Navbar, footer, shared layout
│   ├── core/
│   └── blog/
├── static/
│   ├── css/main.css      # All custom styles
│   └── js/main.js        # FAQ accordion, scroll reveal, nav active state
├── requirements.txt
├── gunicorn.conf.py
├── create_superuser.py
└── .env                  # Environment variables (not committed to git)
```
