from blue.__init__ import db


class User(db.Model):

    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    hash_passwd = db.Column(db.String(128))

    def __init__(self, username, hash_passwd):
        self.username = username
        self.hash_passwd = hash_passwd

    def __repr__(self):
        return self.hash_passwd


class ChartData (db.Model):

    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    temperature = db.Column(db.String(3))
    rain = db.Column(db.String(3))
    date = db.Column(db.String(10))
    user_id = db.Column(db.String(80))

    def __init__(self, temperature, rain, date, user_id):
        self.temperature = temperature
        self.rain = rain
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return "<ChartData(temperature='%s', rain='%s', date='%s', user_id='%s' )>" % (
            self.temperature, self.rain, self.date, self.user_id)