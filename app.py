from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, MaintenanceRecord
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

class MaintenanceForm(FlaskForm):
    technician_name = StringField('Technician Name', validators=[DataRequired()])
    rollers_checked = BooleanField('Rollers – Grease & Lube')
    re_coilers_checked = BooleanField('Re-Coilers/De-Coilers')
    towers_checked = BooleanField('Towers')
    bridals_checked = BooleanField('Bridals')
    splicer_die_checked = BooleanField('Splicer Die')
    wash_tanks_checked = BooleanField('Wash Tanks')
    tension_stand_checked = BooleanField('Tension Stand')
    chem_coater_checked = BooleanField('Chem Coater & Dryer')
    coater_checked = BooleanField('Coater')
    ovens_checked = BooleanField('Ovens & Incinerator')
    tracking_units_checked = BooleanField('Tracking Units')
    quench_tanks_checked = BooleanField('Quench Tanks/Air Dryer/Cooling Tower')
    electrical_cabinets_checked = BooleanField('Electrical Cabinets')
    comments = TextAreaField('Comments')
    submit = SubmitField('Submit')

@app.before_request
def create_tables():
    """This function will run before each request to ensure the database tables are created."""
    if not os.path.exists('maintenance.db'):
        db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MaintenanceForm()
    if form.validate_on_submit():
        record = MaintenanceRecord(
            technician_name=form.technician_name.data,
            rollers_checked=form.rollers_checked.data,
            re_coilers_checked=form.re_coilers_checked.data,
            towers_checked=form.towers_checked.data,
            bridals_checked=form.bridals_checked.data,
            splicer_die_checked=form.splicer_die_checked.data,
            wash_tanks_checked=form.wash_tanks_checked.data,
            tension_stand_checked=form.tension_stand_checked.data,
            chem_coater_checked=form.chem_coater_checked.data,
            coater_checked=form.coater_checked.data,
            ovens_checked=form.ovens_checked.data,
            tracking_units_checked=form.tracking_units_checked.data,
            quench_tanks_checked=form.quench_tanks_checked.data,
            electrical_cabinets_checked=form.electrical_cabinets_checked.data,
            comments=form.comments.data
        )
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('form.html', form=form)

@app.route('/log')
def log():
    records = MaintenanceRecord.query.all()
    return render_template('log.html', records=records)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created at startup
    app.run(debug=True)
