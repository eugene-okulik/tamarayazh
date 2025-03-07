import csv
import os
import mysql.connector as mysql
import dotenv


dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
print(eugene_file_path)

with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        query = """
        SELECT students.id as student_id, students.name, students.second_name, 
        `groups`.title as group_title, 
        books.title as book_title, marks.value as mark, lessons.title as lesson_title, 
        subjets.title as subject_title
        FROM students
        LEFT JOIN `groups` ON students.group_id = `groups`.id
        LEFT JOIN books ON students.id = books.taken_by_student_id
        LEFT JOIN marks ON students.id = marks.student_id
        LEFT JOIN lessons ON marks.lesson_id = lessons.id
        LEFT JOIN subjets ON lessons.subject_id = subjets.id
        WHERE students.name = %s 
        AND students.second_name = %s 
        AND `groups`.title = %s 
        AND books.title = %s 
        AND subjets.title = %s 
        AND lessons.title = %s 
        AND marks.value = %s
                """
        columns = (
            row['name'],
            row['second_name'],
            row['group_title'],
            row['book_title'],
            row['subject_title'],
            row['lesson_title'],
            row['mark_value']
        )

        cursor.execute(query, columns)
        result = cursor.fetchone()

        if not result:
            print(f"Данные, которых не хватает в базе: {row}")

db.close()
