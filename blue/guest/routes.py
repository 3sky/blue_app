from blue.guest.__init__ import *
import blue.user_and_msg

msg = blue.user_and_msg.WelcomeMsg()


@guest_mod.route('/')
def index():
    return render_template('guest/index.html')


@guest_mod.route('hello',  methods=['POST', 'GET'])
def hello_action():
    hello_activity = request.form['what_to_do']
    if hello_activity == 'singin':
        return show_user('sing_in', msg.msg_welcome_friend)
    elif hello_activity == 'singup':
        return show_user('sing_up', msg.msg_welcome_friend)
    elif hello_activity == 'contact':
        return show('contact', msg.msg_in)


