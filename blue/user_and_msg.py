class UserBody:
    def __init__(self):
        self.user_name = ''
        self.user_passwd = ''

    def sing_user(self, user_name, user_passwd):
        self.user_name = user_name
        self.user_passwd = user_passwd


class WelcomeMsg:
    def __init__(self):
        self.msg_in = 'Nice to see you here'
        self.msg_out = 'You successfully logout'
        self.msg_add_user = 'User add successfully'
        self.msg_add_data = 'Data add successfully'
        self.msg_user_exi = 'User already exist'
        self.msg_welcome_friend = 'Welcome friend'
        self.msg_not_match = "Password don't match"
        self.msg_bad_passwd = "Bad user/password, try again!"
        self.msg_insert = ' Insert your data, and see chart'
        self.fix_temp = 'Fix Temprature data'
        self.fix_rain = 'Fix rain data'
        self.fix_date = 'Fix data, should be YYYY-MM-DD'




