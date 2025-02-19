# 📚 RumiPress Expense Tracker

**RumiPress Expense Tracker** is a Django-based web application designed to help RumiPress manage their **book distribution expenses**. The system allows users to **track books, authors, categories, and distribution costs** efficiently.

---

## 🚀 Features

✅ **Manage Books** (CRUD: Create, Read, Update, Delete)  
✅ **Manage Authors & Categories**  
✅ **Import Data from CSV**  
✅ **Track Distribution Expenses**  
✅ **Generate Reports using Chart.js**  
✅ **Pagination for Books, Authors, and Categories**  
✅ **Bootstrap-based Responsive UI**

---

## 🛠️ Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/honghuynhit/RumiPress-expense_tracker.git
cd RumiPress-expense_tracker
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Create a Superuser**
```sh
python manage.py createsuperuser
Follow the prompts to set up an admin account.
```

### **6️⃣ Run the Development Server**
```sh
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.
```

## 📊 Reports & Charts
The application includes Chart.js integration for visualizing book distribution expenses.

- 📈 View total expenses by category
- 📊 Filter and sort expense data
- 📄 Export reports for further analysis
## 🔍 Technologies Used
- Django (Backend)
- SQLite / PostgreSQL (Database)
- Bootstrap (Frontend UI)
- Chart.js (Reports & Charts)
- Django ORM (Database Management)
## 🤝 Contributing
1. Fork the repository.
2. Create a new branch: git checkout -b feature-name
3. Commit your changes: git commit -m "Add feature"
4. Push to the branch: git push origin feature-name
5. Open a Pull Request
## 🛠️ Deployment
For deployment, you can use Heroku, Render, or AWS.
Example for Heroku:

```sh
heroku login
heroku create rumipress-expense-tracker
git push heroku main
```