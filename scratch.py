from datetime import date, datetime
from app import app, db
from app.models import Player, Day


# p1 = Player.query.first()
# d1 = Day.query.first()
#
#
# db.session.add(p1)
# p1.days.append(d1)
# db.session.add(p1)
# db.session.commit()

# print(d1.players)
# print(len(d1.players))
#
# d1 = date(2017, 7, 23)
# print(Day.num_people(d1))

# d2 = Day.query.filter_by(daystamp=date(2017, 7, 23)).first()
# print(d1.players)
#
# print(p1 in d1.players)
#
# print(Day.has_player(d1, p1))

d1 = "2017-07-29"
d2 = datetime.strptime(d1, "%Y-%m-%d").date()
print(d2)
print(type(d2))
