"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app,db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from .forms import PropertyForm
from wtforms.validators import DataRequired
import os
from werkzeug.utils import secure_filename
#from . import db
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import traceback
from app.models import PropertyInfo


###
# Routing for your application.
###

@app.route('/properties')
def properties():
    properties=PropertyInfo.query.all()
    return render_template('properties.html',properties=properties)

@app.route('/properties/create',  methods=['GET', 'POST'])
def create():
    form=PropertyForm()
    if request.method=='POST' and form.validate_on_submit():
        title = form.title.data
        bedrooms=form.bedrooms.data
        bathrooms=form.bathrooms.data
        location=form.location.data
        price=form.price.data
        type=form.type.data
        description=form.description.data
        photo=form.photo.data

        #flash('You have successfully entered a new piece of property', 'success')
        file = photo 
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        try:
            property=PropertyInfo(title, bedrooms, bathrooms, location, price, type, description, filename)
            db.session.add(property)
            db.session.commit()
            #db.close()

            flash('You have successfully entered a new piece of property', 'success')
        except:
            traceback.print_exc()


        return redirect(url_for('properties'))


    flash_errors(form)
    return render_template('createProp.html', form=form)




    

@app.route('/properties/<propertyid>')
def oneProperty(propertyid):
    property = PropertyInfo.query.filter_by(id=propertyid).first()
    return render_template('propInfo.html', property=property)

@app.route('/')
def home():
    """Render website's home page."""
    properties=PropertyInfo.query.all()
    return render_template('properties.html',properties=properties)


@app.route('/properties')
def about():
    """Render the website's about page."""
    return render_template('properties.html')


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

#def connect_db():
#    return psycopg2.connect(host="localhost", port="5432", database="property", user="postgres", password="password")


@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)