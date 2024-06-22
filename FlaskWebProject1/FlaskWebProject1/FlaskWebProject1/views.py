
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from datetime import datetime
from FlaskWebProject1 import app


def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.commit()
    connection.row_factory = sqlite3.Row
    return connection


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route("/")
@app.route("/home")
def index():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template("index.html", posts=posts)


@app.route("/<int:post_id>")
def post(post_id):
    post = get_post(post_id)
    return render_template("post.html", post=post)


@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        auctor = request.form["auctor"]

        if not title:
            flash("Название!")
        else:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO posts (title, content, auctor) VALUES (?, ?, ?)",
                (title, content, auctor),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("create.html")


@app.route("/<int:id>/edit", methods=("GET", "POST"))
def edit(id):
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        auctor = request.form["auctor"]
        if not title:
            flash("Название!")
        else:
            conn = get_db_connection()
            conn.execute(
                "UPDATE posts SET title = ?, content = ?, auctor = ?" " WHERE id = ?",
                (title, content, auctor, id),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("edit.html", post=post)


@app.route("/<int:id>/delete", methods=("POST",))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute("DELETE FROM posts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    flash('"{}" успешно удалено!'.format(post["title"]))
    return redirect(url_for("index"))