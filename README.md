# 📊 Koha Top Library Users (KTLU)

A simple, elegant **Flask-based web application** that displays the **top borrowers** from a **Koha Library Management System (LMS)** within the last 30 days — complete with patron images, card numbers, and branch details.

---

## 🖼️ Overview

This project provides a dynamic and visually appealing dashboard showcasing the **most active library users** based on Koha circulation data.
It connects directly to Koha’s MySQL database and presents real-time borrowing insights — perfect for use in **digital signage displays**, **library dashboards**, or **annual activity summaries**.

---

## 🏗️ Project Structure

```
ktlu/
│
├── app.py                # Main Flask application
├── config.py             # Database and branch configuration
├── templates/
│   ├── index.html        # HTML template for display
│   └── footer.html       # HTML template for footer
├── static/
│   ├── css/
│   │   └── style.css     # Custom styling
│   └── images/           # Optional static images
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Features

*  Displays **Top 8 borrowers** from Koha within the **last 30 days**
*  Shows **user photo**, **card number**, **name**, and **branch**
*  Responsive and clean UI built with **Bootstrap + Poppins font**
*  Easily configurable via `config.py`
*  Works seamlessly with Koha’s **MySQL** database
*  Modular structure with reusable templates

---
---

## 🚀 Installation and Setup

### 1️⃣ System Preparation

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-venv python3-pip git
```

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/maheshpalamuttath/ktlu.git
cd ktlu
```

### 3️⃣ Modify config.py

Update your **Koha database credentials** and branch code in `config.py`:

```bash
vim ktlu/config.py
```

```python
db_config = {
    'user': 'koha_library',
    'password': 'koha123',
    'host': 'localhost',
    'database': 'koha_library'
}

# Branch code (example: EC for East Campus)
branch_code = 'EC'
```

### 4️⃣ Create and Activate a Virtual Environment

```bash
sudo python3 -m venv myenv
source myenv/bin/activate
sudo chown -R $USER:$USER ktlu/myenv
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run the Application

```bash
python3 app.py
```

The application will start at:

👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🌐 Deployment (Production)

You can deploy using **Gunicorn** (recommended):

```bash
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

Or configure it behind **Nginx** or **Apache** for public access.

---

## 💡 Example Use Cases

* Library digital displays highlighting top readers
* Monthly or annual activity dashboards
* Reports for institutional analytics
* Interactive kiosks in reading areas

---

## 🧰 Tech Stack

* **Python 3**
* **Flask**
* **MySQL Connector (mysql-connector-python)**
* **Bootstrap 5**
* **Gunicorn (for deployment)**

---

## 📸 Screenshot

![KTLU Logo](https://github.com/maheshpalamuttath/ktlu/raw/main/static/images/ktlu.png)

---

## 👨‍💻 Author

**Mahesh Palamuttath**

📚 *Librarian | FOSS & Library Technologist*

🔗 [https://maheshpalamuttath.info](https://maheshpalamuttath.info)

---

## 🪪 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it, provided proper credit is given.

---

⭐ **If you find this project useful, please give it a star on GitHub!**
