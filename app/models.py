from app import db

player_day_assoc = db.Table(
    'Player Dates',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
    db.Column('day_id', db.Integer, db.ForeignKey('day.id'))
)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person = db.Column(db.String(128))
    email = db.Column(db.String(128))
    days = db.relationship('Day', secondary=player_day_assoc, backref='players')

    def __repr__(self):
        return '<Player {}>'.format(self.person)


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    daystamp = db.Column(db.Date, unique=True)

    @staticmethod
    def num_people(day):
        query_day = Day.query.filter_by(daystamp=day).first()
        if query_day:
            return len(query_day.players)
        return 0

    @staticmethod
    def has_player(day, player):
        return player in day.players

    def __repr__(self):
        return "<Day {}>".format(self.daystamp)

