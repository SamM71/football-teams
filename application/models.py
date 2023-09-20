from application import app, db

app.app_context().push()

class Team(db.Model):
  __tablename__ = "teams"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  nation = db.Column(db.String(50), nullable=False)
  tier = db.Column(db.Integer, nullable=False)

  def __init__(self, name, nation, tier):
    self.name = name
    self.nation = nation
    self.tier = tier

  def __repr__(self):
    return f"Team(id: {self.id}, name: {self.name})"
  
  @property
  def json(self):
    return {"id": self.id, "name": self.name, "nation": self.nation, "tier": self.tier}