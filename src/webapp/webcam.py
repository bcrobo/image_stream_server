from flask import Blueprint, render_template
from flask_login import login_required, current_user

webcam = Blueprint('webcam', __name__)

@webcam.route('/webcam')
@login_required
def live():
    return render_template('webcam.html', name=current_user.email)
