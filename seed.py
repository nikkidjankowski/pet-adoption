"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()



river = Pet(name="River", species="Dog", age=3, available=True)
davis = Pet(name="Davis", species="Cat", age=1, available=True)
bourbon = Pet(name="Bourbon", species="Dog", photo_url="https://www.k9web.com/wp-content/uploads/2021/04/sitting-blue-doxie-780x529.jpg", age=5, available=True)
chloe = Pet(name="Chloe", species="Dog", photo_url="https://www.hepper.com/wp-content/uploads/2021/11/Brindle-pit-bull-puppy.jpg", age=7, available=False)

db.session.add_all([river, davis, bourbon, chloe])
db.session.commit()