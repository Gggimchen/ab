from flask import Flask, render_template, request, redirect,url_for
import sqlite3
import math

app = Flask(__name__)
conn = sqlite3.connect('questions.db', check_same_thread=False)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

currentPage = 1
max = 1
project = 1

@app.route("/<currentPage>", methods =['GET', 'POST'])
def OurProjects(currentPage=1):
    global max

    startIn = ((int(currentPage)-1)*2)+int(currentPage)
    endIn = int(currentPage)*3

    query = "SELECT * FROM projects"
    cursor.execute(query)
    data = cursor.fetchall()
    max = math.ceil(len(data)/3)

    cursor.execute("SELECT * FROM projects WHERE ID BETWEEN " + str(startIn) + " AND " + str(endIn))


    rows = cursor.fetchall()

    return render_template('ourProjects.html', rows = rows, currentPage = currentPage, max = max)

@app.route("/change/<action>", methods =['GET', 'POST'])
def changePage(action):
    global currentPage
    global max
    if action == "INC":
        if currentPage + 1 <= max:
            currentPage += 1
    else:
        if currentPage - 1 > 0:
            currentPage -= 1
    return redirect(url_for('OurProjects', currentPage=currentPage))

@app.route("/project/<ID>", methods =['GET', 'POST'])
def ProjectPage(ID=1):

    cursor.execute("SELECT * FROM projectImages WHERE ID == " + ID)


    rows = cursor.fetchall()

    print("----------------"+str(rows))
    return render_template('projectDetailsPage.html', data = rows[0])