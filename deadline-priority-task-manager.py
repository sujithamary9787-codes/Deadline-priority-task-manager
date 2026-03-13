from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = "tasks_database.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        deadline TEXT,
        priority TEXT
    )
    """)
    conn.commit()

    return conn


@app.route("/")
def index():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    deadline = request.form["deadline"]

    today = datetime.today().date()
    deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()

    days = (deadline_date - today).days

    if days <= 0:
        priority = "High"
    elif days <= 3:
        priority = "Medium"
    else:
        priority = "Low"

    conn = get_db()
    conn.execute(
        "INSERT INTO tasks (task, deadline, priority) VALUES (?, ?, ?)",
        (task, deadline, priority),
    )
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
