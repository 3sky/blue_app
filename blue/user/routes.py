from blue.user.__init__ import *
from blue import app
from blue.models import *
import blue.user_and_msg


app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
user_body = blue.user_and_msg.UserBody()
msg = blue.user_and_msg.WelcomeMsg()


@user_mod.route('/', methods=['POST', 'GET'])
def user_index():
    if user_body.user_name == '':
        abort(404)
    else:
        return render_template('user/index.html', name=user_body.user_name, info=msg.msg_in)


@user_mod.route('homepage',  methods=['POST', 'GET'])
def homepage_a():
    homepage_action = request.form['what_to_do']
    if homepage_action == 'adddata':
        return render_template('user/add_data.html', func=user_body.user_name, info=msg.msg_insert)
    elif homepage_action == 'showchart':
        return redirect(url_for('user.show_chart'))
    elif homepage_action == 'contact':
        return show('contact', msg.msg_in)
    elif homepage_action == 'logout':
        user_body.__init__()
        return redirect(url_for('guest.index'))


@user_mod.route('add_data',  methods=['POST', 'GET'])
def add_action():
    temprature = request.form['temperature']
    if not temprature.isdigit():
        return render_template('user/add_data.html', func=user_body.user_name, info=msg.fix_temp)
    rain = request.form['rain']
    if not rain.isdigit():
        return render_template('user/add_data.html', func=user_body.user_name, info=msg.fix_rain)
    surv_date = request.form['date']
    try:
        datetime.datetime.strptime(surv_date, '%Y-%m-%d')
    except ValueError:
        return render_template('user/add_data.html', func=user_body.user_name, info=msg.fix_date)
    save = request.form['adddata']
    if save == 'save_data':
        data = ChartData(temperature=temprature, rain=rain, date=surv_date, user_id=user_body.user_name)
        db.session.add(data)
        db.session.commit()
        return render_template('user/index.html', info=msg.msg_add_data, name=user_body.user_name)


@user_mod.route('show_site')
def show_chart():
    labels = []
    tempe = []
    rainy = []
    for line in db.session.query(ChartData).\
            filter(ChartData.user_id == user_body.user_name).\
            order_by(desc(text('date'))).limit(10):
        labels.append(line.date)
    for line in db.session.query(ChartData).\
            filter(ChartData.user_id == user_body.user_name).\
            order_by(desc(text('date'))).limit(10):
        tempe.append(line.temperature)
    for line in db.session.query(ChartData).\
            filter(ChartData.user_id == user_body.user_name).\
            order_by(desc(text('date'))).limit(10):
        rainy.append(line.rain)

    return render_template('user/chart.html', values=tempe[::-1], values2=rainy[::-1],
                           labels=labels[::-1], func=user_body.user_name)


@user_mod.route('check',  methods=['POST', 'GET'])
def check_action():
    if request.form['q1'] == "Login":
        user_name = request.form['username']
        passwd = request.form['password']
        user_passwd = hashlib.sha512(passwd.encode('utf-8'))
        passwd_from_db = User.query.filter_by(username=user_name).first()
        if str(user_passwd.hexdigest()) == str(passwd_from_db):
            user_body.sing_user(user_name, passwd)
            return redirect(url_for('user.user_index'))
        else:
            return show('sing_in', msg.msg_bad_passwd)
    elif request.form['q1'] == "Regi":
        user_name = request.form['username']
        passwd1 = request.form['password1']
        passwd2 = request.form['password2']
        if passwd1 == passwd2:
            if User.query.filter_by(username=user_name).scalar() is None:
                user_passwd = hashlib.sha512(passwd1.encode('utf-8'))
                guest = User(user_name, user_passwd.hexdigest())
                db.session.add(guest)
                db.session.commit()
                user_body.sing_user(user_name, user_passwd)
                return render_template('user/index.html', info=msg.msg_add_user, name=user_body.user_name)
            else:
                return show('sing_in_better', msg.msg_user_exi)
        else:
            return show('sing_up', msg.msg_not_match)
