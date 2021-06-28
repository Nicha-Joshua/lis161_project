from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route ('/about')
def about():
    return render_template ('about.html')

@app.route ('/contact')
def contact():
    return render_template ('contact.html')

@app.route ('/')
def index():
    return render_template ('index.html')

@app.route ('/login')
def login():
    return render_template ('login.html')

@app.route ('/signin')
def signin():
    return render_template ('signin.html')

@app.route ('/tutee')
def tutee():
    return render_template ('tutee.html')

@app.route ('/tutorpage')
def tutorpage():
    return render_template ('tutorpage.html')

@app.route ('/tutorlist/<tutor_type>')
def tutorlist(tutor_type):
    tutors = read_tutors_by_type(tutor_type)
    return render_template('tutorlist.html',tutor_type=tutor_type, tutors=tutors)

@app.route('/tutorlist/<int:tutor_id>')
def tutor(tutor_id):
    tutor = read_tutor_by_id(tutor_id)
    return render_template('tutorprofile.html', tutor=tutor)

@app.route('/processing', methods=['post'])
def processing():
    #Prepare Tutor Data coming from signin.html form
    tutor_type = request.form['tutor_type']
    tutor_name = request.form['tutor_name']
    tutor_age = request.form['tutor_age']
    tutor_gender = request.form['tutor_gender']
    tutor_contact = request.form['tutor_contact']
    tutor_elementary = request.form['tutor_elementary']
    tutor_highschool = request.form['tutor_highschool']
    tutor_college = request.form['tutor_college']
    tutor_academicachievements = request.form['tutor_academicachievements']
    tutor_subject = request.form['tutor_subject']
    tutor_hobbies = request.form['tutor_hobbies']
    tutor_language = request.form['tutor_language']
    tutor_schedule = request.form['tutor_schedule']
    tutor_url = request.form['tutor_url']


    tutor_data = {  'name': tutor_name,
                    'age': tutor_age,
                    'gender': tutor_gender,
                    'contact': tutor_contact,
                    'elementary': tutor_elementary,
                    'highschool': tutor_highschool,
                    'college': tutor_college,
                    'academicachievements': tutor_academicachievements,
                    'subject': tutor_subject,
                    'hobbies': tutor_hobbies,
                    'language': tutor_language,
                    'schedule': tutor_schedule,
                    'url': tutor_url,
                    'type': tutor_type}

    insert_tutor(tutor_data)
    return redirect(url_for('tutorlist', tutor_type=request.form['tutor_type']))

@app.route('/modify/<tutor_type>/<int:tutor_id>', methods=['POST'])
def modify(tutor_type, tutor_id):
    tutor = read_tutor_by_id(tutor_id)
    if request.form['action'] == 'Edit':
        return render_template('edit.html', tutor=tutor)
    elif request.form['action'] == 'Delete':
        delete_tutor(tutor_id)
        return redirect(url_for('tutorlist', tutor_type=tutor['type']))

@app.route('/update/<int:tutor_id>', methods=['POST'])
def update(tutor_id):
    # Get data from the form
    tutor_name = request.form['tutor_name']
    tutor_age = request.form['tutor_age']
    tutor_gender = request.form['tutor_gender']
    tutor_contact = request.form['tutor_contact']
    tutor_elementary = request.form['tutor_elementary']
    tutor_highschool = request.form['tutor_highschool']
    tutor_college = request.form['tutor_college']
    tutor_academicachievements = request.form['tutor_academicachievements']
    tutor_subject = request.form['tutor_subject']
    tutor_hobbies = request.form['tutor_hobbies']
    tutor_language = request.form['tutor_language']
    tutor_schedule = request.form['tutor_schedule']
    tutor_url = request.form['tutor_url']
    tutor_type = request.form['tutor_type']

    # Prepare data for DB update
    tutor_data = {'name': tutor_name,
                  'age': tutor_age,
                  'gender': tutor_gender,
                  'contact': tutor_contact,
                  'elementary': tutor_elementary,
                  'highschool': tutor_highschool,
                  'college': tutor_college,
                  'academicachievements': tutor_academicachievements,
                  'subject': tutor_subject,
                  'hobbies': tutor_hobbies,
                  'language': tutor_language,
                  'schedule': tutor_schedule,
                  'url': tutor_url,
                  'type': tutor_type,
                  'id': tutor_id
                  }

    #Update DB
    update_tutor(tutor_data)
    # Redirect User
    return redirect(url_for('tutor', tutor_id=tutor_id))
    pass


if __name__ == '__main__':
    app.run(debug=True)