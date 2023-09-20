from application import db
from application.models import Team

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")
entry1 = Team(name="Chelsea", nation="England", tier=1)
entry2 = Team(name="Swindon Town", nation="England", tier=4)
entry3 = Team(name="Real Madrid", nation="Spain", tier=1)
entry4 = Team(name="Paris Saint-Germain", nation="France", tier=1)

db.session.add_all([entry1, entry2, entry3, entry4])
db.session.commit()