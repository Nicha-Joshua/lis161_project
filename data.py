import sqlite3

db_path = 'am.db'


# Connect to a database
def connect_db(path):
    conn = sqlite3.connect(path)
    # Convert tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# Read all tutors by tutor type
def read_tutors_by_type(tutor_type):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM tutors WHERE type=?'
    results = cur.execute(query, (tutor_type,)).fetchall()
    conn.close()
    return results

# Read all tutors by tutor id
def read_tutor_by_id(tutor_id):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM tutors WHERE id=?'
    result = cur.execute(query, (tutor_id,)).fetchone()
    conn.close()
    return result

# Insert Tutor Data to DB
def insert_tutor(tutor_data):
    conn, cur = connect_db(db_path)
    query = 'INSERT INTO tutors (name, age, gender, contact, elementary, highschool, college, academicachievements, type, subject, hobbies, language, schedule, url) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    values = (tutor_data['name'],
              tutor_data['age'],
              tutor_data['gender'],
              tutor_data['contact'],
              tutor_data['elementary'],
              tutor_data['highschool'],
              tutor_data['college'],
              tutor_data['academicachievements'],
              tutor_data['type'],
              tutor_data['subject'],
              tutor_data['hobbies'],
              tutor_data['language'],
              tutor_data['schedule'],
              tutor_data['url'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

# Delete a tutor record
def delete_tutor(tutor_id):
    conn, cur = connect_db(db_path)
    query = 'DELETE FROM tutors WHERE id=?'
    cur.execute(query, (tutor_id,))
    conn. commit()
    conn. close()

# Update Tutor Data from DB
def update_tutor(tutor_data):
    conn, cur = connect_db(db_path)
    query = 'UPDATE tutors SET name=?, age=?, gender=?, contact=?, elementary=?, highschool=?, college=?, academicachievements=?, type=?, subject=?, hobbies=?, language=?, schedule=?, url=? WHERE id=?'
    values = (tutor_data['name'],
              tutor_data['age'],
              tutor_data['gender'],
              tutor_data['contact'],
              tutor_data['elementary'],
              tutor_data['highschool'],
              tutor_data['college'],
              tutor_data['academicachievements'],
              tutor_data['type'],
              tutor_data['subject'],
              tutor_data['hobbies'],
              tutor_data['language'],
              tutor_data['schedule'],
              tutor_data['url'],
              tutor_data['id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()