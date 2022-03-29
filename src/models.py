from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

planet_favourites = db.Table('planet_favourites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planet.id'), nullable=False, primary_key=True)
)

people_favourites = db.Table('people_favourites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True),
    db.Column('people_id', db.Integer, db.ForeignKey('people.id', nullable=False), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    planet_favourites = db.relationship('Planet', secondary=planet_favourites, lazy='subquery',
        backref=db.backref('favourite_of', lazy=True))
    people_favourites = db.relationship('People', secondary=people_favourites, lazy='subquery',
        backref=db.backref('favourite_of', lazy=True))
    
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