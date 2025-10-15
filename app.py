from flask import Flask, render_template, send_file
import mysql.connector
import io
from config import db_config, branch_code

app = Flask(__name__)

def get_top_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"""
        SELECT
            b.borrowernumber,
            b.cardnumber,
            CONCAT(b.title, ' ', b.surname) AS name,
            COUNT(i.issue_id) AS borrow_count,
            br.branchname
        FROM borrowers b
        LEFT JOIN issues i ON b.borrowernumber = i.borrowernumber
        LEFT JOIN branches br ON b.branchcode = br.branchcode
        WHERE b.branchcode = %s
          AND i.issuedate > DATE_SUB(CURDATE(), INTERVAL 30 DAY)
        GROUP BY b.borrowernumber, b.surname, b.branchcode
        ORDER BY borrow_count DESC
        LIMIT 8;
    """
    cursor.execute(query, (branch_code,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


@app.route('/')
def index():
    top_users = get_top_users()
    return render_template('index.html', users=top_users)


@app.route('/images/<int:borrowernumber>')
def image(borrowernumber):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT imagefile FROM patronimage WHERE borrowernumber = %s"
    cursor.execute(query, (borrowernumber,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        image_data = result[0]
        return send_file(
            io.BytesIO(image_data),
            mimetype='image/jpeg',
            as_attachment=False,
            download_name=f"{borrowernumber}.jpg"
        )
    else:
        return "Image not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
