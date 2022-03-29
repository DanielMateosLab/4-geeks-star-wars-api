from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    
    def __repr__(self):
        return self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class Planet(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(40), nullable=False, unique=True)
    climate = db.Column(String(10), nullable=False)
    terrain = db.Column(String(10), nullable=False)
    diameter = db.Column(Integer, nullable=False)
    gravity = db.Column(Integer, nullable=False)
    orbital_period = db.Column(Integer, nullable=False)
    population = db.Column(Integer, nullable=False)

    def __repr__(self):
        return self.name

class People(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    birthyear = Column(Integer, nullable=False)
    gender = Column(String(6), nullable=False)
    height = Column(Integer, nullable=False)
    homeplanet = Column(Integer, ForeignKey('planet.id'), nullable=False)

    def __repr__(self):
        return self.name