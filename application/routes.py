from datetime import datetime as dt
from flask import Blueprint, redirect, render_template, flash, request, session
from flask import url_for, make_response, jsonify
from flask import current_app as app
from flask_login import current_user, login_required, logout_user
from .models import db, User


# Set up a Blueprint
main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')


@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Homepage for logged in users"""
    return render_template('dashboard.html')
