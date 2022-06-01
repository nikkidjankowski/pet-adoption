from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Renders snack form (GET) or handles snack form submission (POST)"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"Created new pet: name is {name}")
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)


@app.route('/<int:pet_id>', methods=["GET"])
def show_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template("showpet.html", pet=pet, pet_id=pet_id)