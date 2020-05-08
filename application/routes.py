from datetime import datetime as dt
from flask import Blueprint, redirect, render_template, flash, request, session
from flask import url_for, make_response, jsonify
from flask import current_app as app
from flask_login import current_user, login_required, logout_user
from .models import db, User, Battle, Player, Move


# Set up a Blueprint
main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')


@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Homepage for logged in users"""
    user_status = current_user.in_game

    return render_template('dashboard.html', user_status=user_status)


@main_bp.route('/createbattle', methods=['GET'])
@login_required
def create_battle():
    """Create new tournament"""
    current_user.create_battle()
    return redirect(url_for('main_bp.join_battle'))


@main_bp.route('/leavebattle', methods=['GET'])
@login_required
def leave_battle():
    """Create new tournament"""
    current_user.change_status()
    db.session.delete(current_user.games_joined[0])
    db.session.delete(current_user.games_created[0])
    db.session.commit()
    return redirect(url_for('main_bp.dashboard'))


@main_bp.route('/joinbattle', methods=['GET'])
@login_required
def join_battle():
    """Create new tournament"""

    return render_template('battleground.html')
