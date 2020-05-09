from datetime import datetime as dt
from flask import Blueprint, redirect, render_template, flash, request, session
from flask import url_for, make_response, jsonify
from flask import current_app as app
from flask_login import current_user, login_required, logout_user
from .models import db, User, Battle, Player, Move, History
from . import login_manager, socketio, emit

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
    current_user.create_battle()
    return redirect(url_for('main_bp.battle'))


@main_bp.route('/battle', methods=['GET', 'POST'])
@login_required
def battle():
    if request.method == 'POST':
        if request.form.get('leaveBattle'):
            current_battle = current_user.games_joined[0]
            current_user.leave_battle(current_battle)
            socketio.emit('remove player', current_user.username, broadcast=True)
            return redirect(url_for('main_bp.dashboard'))
        current_user.join_battle(request.form.get('battle_id'))
        socketio.emit('add player', current_user.username, broadcast=True)
        current_battle = current_user.games_joined[0]
        current_players = Player.query.filter(Player.battle_id==current_battle.battle_id).all()
        return render_template('battleground.html', current_battle=current_battle, current_players=current_players)
    current_battle = current_user.games_joined[0]
    current_players = Player.query.filter(Player.battle_id==current_battle.battle_id).all()
    return render_template('battleground.html', current_battle=current_battle, current_players=current_players)







"""



@main_bp.route('/leavebattle', methods=['GET'])
@login_required
def leave_battle():
    current_user.change_status()
    current_battle = current_user.games_joined[0]
    history = History(battle_id=current_battle.battle_id, user_id=current_battle.user_id,
                        user_status=current_battle.user_status, time_created=current_battle.time_created)
    db.session.add(history)
    db.session.delete(current_battle)
    db.session.commit()
    return redirect(url_for('main_bp.dashboard'))


@main_bp.route('/battle', methods=['GET', 'POST'])
@login_required
def battle():

    if request.method == 'POST':
        current_user.join_battle(request.form.get('battle_id'))
        current_battle = current_user.games_joined[0]
        current_players = Player.query.filter(Player.battle_id==current_battle.battle_id).all()
        username = {"username": ""}
        username['username'] = current_user.username
        socketio.emit('add player', username , broadcast=True)
        return render_template('battleground.html', current_battle=current_battle, current_players=current_players)
    current_battle = current_user.games_joined[0]
    current_players = Player.query.filter(Player.battle_id==current_battle.battle_id).all()
    return render_template('battleground.html', current_battle=current_battle, current_players=current_players)
"""
