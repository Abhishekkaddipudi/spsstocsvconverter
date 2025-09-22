

```markdown
# SAV to CSV Converter (Flask + HTML)

This project provides a simple **web interface** to convert `.sav` (SPSS data files) into `.csv` format using **Flask** for backend and **HTML/CSS** for frontend.  
It uses the [`pyreadstat`](https://pypi.org/project/pyreadstat/) library to handle `.sav` files.

---

## 🚀 Features
- Upload `.sav` files from a web browser.
- Automatic conversion to `.csv`.
- Download converted `.csv` instantly.
- Simple, clean interface.
- Error handling (invalid file types, missing files, etc.).

---

## 📂 Project Structure
sav\_to\_csv/
│
├── app.py                # Flask backend
├── templates/
│   └── index.html        # HTML upload page
├── uploads/              # Stores uploaded .sav files
├── converted/            # Stores converted .csv files
└── README.md             # Documentation

````

---

## ⚙️ Installation

1. **Clone the repository**

```bash

   git clone https://github.com/yourusername/sav-to-csv.git
   cd sav-to-csv
   
````

2. **Create virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install flask pyreadstat pandas
   ```

---

## ▶️ Usage

1. **Run the Flask server**

   ```bash
   python app.py
   ```

2. **Open in browser**

   ```
   http://127.0.0.1:5000/
   ```

3. **Upload a `.sav` file** → Convert → Download `.csv`.



## 🛠️ Technologies Used

* **Python** (Flask, Pandas, Pyreadstat)
* **HTML/CSS** (basic styling)
* **Bootstrap/Custom CSS** (optional for styling)

---

```
