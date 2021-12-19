from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Responses
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///funny_word.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/questionnaire")
def quest():
    return render_template('quest.html')


@app.route('/process', methods=['get'])
def answer_process():
    if not request.args:
        return redirect(url_for('quest'))

    birth = request.args.get('birth')
    gender = request.args.get('gender')

    user = User(
        birth=birth,
        gender=gender
    )

    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)

    understand = request.args.get('understand')
    funny = request.args.get('funny')
    frequent = request.args.get('frequent')

    responses = Responses(id=user.id, understand=understand, funny=funny, frequent=frequent)
    db.session.add(responses)
    db.session.commit()

    return 'OK'


@app.route('/statistics')
def statistics():
    total = User.query.count()
    all_info = {}
    age_stats = db.session.query(
        func.avg(User.birth),
        func.min(User.birth),
        func.max(User.birth)
    ).one()

    all_info['birth_mean'] = age_stats[0]
    all_info['birth_min'] = age_stats[1]
    all_info['birth_max'] = age_stats[2]
    all_info['understand_mean'] = db.session.query(func.avg(Responses.understand)).one()[0]
    all_info['funny_mean'] = db.session.query(func.avg(Responses.funny)).one()[0]
    all_info['frequent_mean'] = db.session.query(func.avg(Responses.frequent)).one()[0]

    return render_template('statistics.html', all_info=all_info, total=total)


if __name__ == '__main__':
    app.run(debug=False)