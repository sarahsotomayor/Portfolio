from flask_app import app
from flask import render_template, redirect
from flask_app.models import methods

@app.route("/")
def index():
    return redirect("/portfolio")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/projects")
def view_projects():
    return render_template("view_projects.html")

@app.route("/portfolio/resume")
def view_resume():
    return render_template("view_resume.html")