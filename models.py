from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class MaintenanceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    technician_name = db.Column(db.String(50), nullable=False)
    date_performed = db.Column(db.DateTime, default=datetime.utcnow)
    rollers_checked = db.Column(db.Boolean, default=False)
    re_coilers_checked = db.Column(db.Boolean, default=False)
    towers_checked = db.Column(db.Boolean, default=False)
    bridals_checked = db.Column(db.Boolean, default=False)
    splicer_die_checked = db.Column(db.Boolean, default=False)
    wash_tanks_checked = db.Column(db.Boolean, default=False)
    tension_stand_checked = db.Column(db.Boolean, default=False)
    chem_coater_checked = db.Column(db.Boolean, default=False)
    coater_checked = db.Column(db.Boolean, default=False)
    ovens_checked = db.Column(db.Boolean, default=False)
    tracking_units_checked = db.Column(db.Boolean, default=False)
    quench_tanks_checked = db.Column(db.Boolean, default=False)
    electrical_cabinets_checked = db.Column(db.Boolean, default=False)
    comments = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<MaintenanceRecord {self.technician_name} - {self.date_performed}>'
