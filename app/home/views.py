from flask import Blueprint, render_template, g, session

home_blueprint = Blueprint(
  'home', __name__, template_folder='templates'
)

@home_blueprint.route('/')
def index():
    user_authenticated = 'user_id' in session
    if user_authenticated:
        return render_template('welcome.html')
    return render_template('index.html')

@home_blueprint.route('/about')
def about():
    return render_template('about.html')