# 📦 Offline Asset Manager – PWA  
🛠️ **Tech Stack:** Django + Vue.js + Celery + Redis + scikit-learn  
🎓 **SESAME University | 3ING Web Programming in Python**  
👨‍🏫 Supervised by Mr. Chaouki Bayoudhi  
📅 Academic Year 2024–2025

---

## 🎯 Project Overview  
This is a **Progressive Web Application (PWA)** that:

✅ Caches assets offline using a service worker  
✅ Lets users install the app on their device  
✅ Uses AI-based analytics to group users into clusters with scikit-learn KMeans  
✅ Sends push notifications via VAPID with subscription checks  
✅ Runs background tasks asynchronously using Celery + Redis  
✅ Exposes data through REST + GraphQL APIs  

---

## 🧠 What’s Inside  

### 🔍 AI Analytics  
- Clusters users using scikit-learn’s KMeans  
- Behavior analysis runs in background tasks with Celery  

### 🌐 API Support  
- REST API via Django REST Framework  
- GraphQL API via Graphene-Django  
- Serializers include custom validation  

### 🔐 Security  
- Token-based authentication  
- Role-based access control  
- Configured CORS and CSRF  

### 🔄 Celery + Redis  
- Handles background async jobs  
- Redis message broker  

### 🔔 Push Notifications  
- Uses VAPID protocol  
- When enabling notifications, checks subscription status  
- Prevents duplicate subscriptions  

### 💻 Frontend – Vue.js  
- Built with Vue.js for a responsive user interface  
- Implements Progressive Web App standards  
- Uses service workers to cache assets for offline use  
- Provides UI for:  
  - Installing the app on desktop and mobile  
  - Managing push notification subscriptions  

### 📱 PWA Features  
- Offline asset caching with service workers ensures fast load and offline use  
- Installable on mobile and desktop devices  
- Push notifications with subscription management to avoid duplicates  

---

## ⚙️ How to Run It  

### 📁 1. Clone the Repository 
git clone https://github.com/nad02k/ExamDjangoPWA.git 

🐍 2. Setup Backend (Django)
python -m venv venv
# Windows:
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuse

🌐 3. Setup Frontend (Vue.js)
cd frontend
npm install
npm run build
▶️ 4. Run the Application
python manage.py runserver
