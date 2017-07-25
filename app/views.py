from flask import render_template, redirect, url_for, flash, request, abort
from app import app, db
from datetime import date, datetime, timedelta
from .models import Player, Day

@app.route('/')
@app.route('/index')
def index():
    today = date.today()
    return render_template('index.html',
                           title="Home",
                           today=today,
                           timedelta=timedelta,
                           Day=Day)

@app.route('/<player_name>', methods=["GET", "POST"])
def player(player_name):
    allowed_list = ["colin", "mike", "carolyn", "rachel"]
    if str(player_name).lower() not in allowed_list:
        return abort(404)

    pname_title = str(player_name).title()
    player = Player.query.filter_by(person=pname_title).first()

    if request.method == "POST":
        selected = request.form.getlist('chosen_day')
        print(selected)
        for each in selected:
            print(type(each))
        for each_date in selected:
            each_date = datetime.strptime(each_date, "%Y-%m-%d").date()
            check_date = Day.query.filter_by(daystamp=each_date).first()
            if check_date:
                # If the date already exists, add the user to the association table
                player.days.append(check_date)
                db.session.add(player)
                db.session.commit()
            else:
                # Add the new date and create it in the association table
                d1 = Day(daystamp=each_date)
                db.session.add(d1)
                player.days.append(d1)
                db.session.add(player)
                db.session.commit()
        return redirect(url_for('index'))


    today = date.today()
    return render_template('player.html',
                           title=player_name,
                           player=player,
                           today=today,
                           timedelta=timedelta,
                           Day=Day)