import mysql.connector as mysql


db = mysql.connect(
    username = 'st-onl',
    password = 'AVNS_tegPDkI5BlB2lW5eASC',
    host = 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port = 25060,
    database = 'st-onl'
)
cursor = db.cursor()

query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
student_value = ('Sancho', 'Pancho')
cursor.execute(query, student_value)
db.commit()
student_id = cursor.lastrowid
print("Id студента:", student_id)

query_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
group_value =  ('super tester', 'abr 2024', 'sep 2024')
cursor.execute(query_group, group_value)
db.commit()
group_id = cursor.lastrowid
print("ID группы:", group_id)

student_in_group= "UPDATE students SET group_id = %s WHERE id = %s"
value_for_group = (group_id, student_id)
cursor.execute(student_in_group, value_for_group)
db.commit()

query_books = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
books_values = [
    ('Kolobok', student_id),
    ('English for beginners', student_id),
    ('The little prince', student_id)
]
cursor.executemany(query_books, books_values)
db.commit()

query_subject = "INSERT INTO subjets (title) VALUES (%s)"
subject_value = [('Spanish level 2',), ('Biology. Level 3',), ('Geometry',)]
cursor.executemany(query_subject, subject_value)
db.commit()

cursor.execute('''SELECT id, title
FROM subjets
WHERE title IN (%s, %s, %s)''',
('Spanish level 2', 'Biology. Level 3', 'Geometry'))
subjects = cursor.fetchall()
for subject in subjects:
    print(f"ID предметов: {subject[0]}, Название: {subject[1]}")

lesson_values = [
    ('Spanish - group 1', subjects[0][0]),
    ('Spanish - group 2', subjects[0][0]),
    ('Biology. Insects', subjects[1][0]),
    ('Biology. Anatomy', subjects[1][0]),
    ('Geometry. Beginners', subjects[2][0]),
    ('Geometry. Adv', subjects[2][0])
]
lesson_ids = []
for lesson, subject_id in lesson_values:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (lesson, subject_id))
    db.commit()
    lesson_ids.append(cursor.lastrowid)
print("Добавленные уроки:", lesson_ids)

query_marks = "INSERT INTO marks (`value`, lesson_id, student_id) VALUES (%s, %s, %s)"
marks_values = [
    (8, lesson_ids[0], student_id), (7, lesson_ids[1], student_id ),
    (7, lesson_ids[2], student_id ), (6, lesson_ids[3], student_id ),
    (5, lesson_ids[4], student_id), (7, lesson_ids[5], student_id)
]
cursor.executemany(query_marks, marks_values)
db.commit()

cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
print("Оценки студента:", cursor.fetchall())

cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print("Книги у студента:", cursor.fetchall())

query_all = '''
SELECT students.id as student_id, students.name, students.second_name, `groups`.title as group_title,
    books.title as book_title, marks.value as mark, lessons.title as lesson_title,
    subjets.title as subject_title 
FROM students
LEFT JOIN `groups` ON students.group_id = `groups`.id
LEFT JOIN books ON students.id = books.taken_by_student_id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id
WHERE students.id = %s
'''
cursor.execute(query_all, (student_id,))
print("Все о студенте:", cursor.fetchall())

db.close()
