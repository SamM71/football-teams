from application import db
from application.models import Team

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

entry1 = Team(name="Chelsea", nation="England", tier=1)

db.session.add(entry1)
db.session.commit()