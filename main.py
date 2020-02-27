from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("C:/Programming/Яндекс.Лицей/2 год/WEB 10. Знакомство с flask-sqlalchemy/Журнал "
                           "работ/db/mars_explorer.db")
    app.run(port=5000, host='127.0.0.1')


@app.route('/')
def index():
    session = db_session.create_session()
    jobs = []
    users = []
    for job in session.query(Jobs).all():
        jobs.append(job)
    for user in session.query(User).all():
        users.append(user)
    return render_template('index.html', title="Журнал работ", actions=jobs, users=users)


if __name__ == '__main__':
    main()
