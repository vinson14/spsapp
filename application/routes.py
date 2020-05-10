import random
from datetime import datetime as dt
from flask import Blueprint, redirect, render_template, flash, request, session
from flask import url_for, make_response, jsonify
from flask import current_app as app
from flask_login import current_user, login_required, logout_user
from .models import db, User, Battle, Player, Move, History
from . import login_manager, socketio
from flask_socketio import emit, send, join_room, leave_room

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


@main_bp.route('/leavebattle', methods=['POST'])
@login_required
def leave_battle():
    current_user.leave_battle()
    return redirect(url_for('main_bp.dashboard'))


@main_bp.route('/joinbattle', methods=['POST'])
@login_required
def join_battle():
    current_user.join_battle(request.form.get('battle_id'))
    room = current_user.battle_id()
    username = current_user.username
    socketio.emit('add player', username, room=room, broadcast=True)
    return redirect(url_for('main_bp.battle'))


@main_bp.route('/battle', methods=['GET'])
@login_required
def battle():
    current_battle = current_user.games_joined[0]
    current_players = Player.query.filter(Player.battle_id==current_battle.battle_id).all()
    return render_template('battle.html', current_battle=current_battle, current_players=current_players)


@main_bp.route('/matchup', methods=['GET'])
@login_required
def matchup():
    current_battle = current_user.games_joined[0]
    players = Player.query.filter(Player.battle_id==current_battle.battle_id).all()
    randomized_players = [];
    for i in range(len(players)):
        random_player = random.choice(players)
        players.remove(random_player)
        randomized_players.append(random_player)
    return render_template('matchup.html', players=randomized_players)


@socketio.on('join room')
def on_join():
    room = current_user.battle_id()
    username = current_user.username
    join_room(room)


@socketio.on('leave room')
def on_leave():
    room = current_user.battle_id()
    username = current_user.username
    leave_room(room)
    emit('remove player', username, room=room)
