"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import Flask, request, render_template, url_for, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, ALL
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from webpro.forms import AddAsset, ProjectDetail, WarrentyDetail, ReferanceDoc, LegalDocu, InvestmentInfo, AddProjectDocument,AddTechDocument, AssetSpecification, AssetCorrespondance, Investment, Installment
from webpro.sa import db,app, addasset_data_model, User, investment, legaldocu, investmentinfo, installments,assetcorespondance_data_model, projectdetails, assetspecification_data_model, addprojectdocu, addtechnichaldocu, referancedoc, WARRENTYDETAILS

files = UploadSet('files', ALL)

app.config['UPLOADED_FILES_DEST'] = 'uploads'
configure_uploads(app, files)
files = UploadSet('files', ALL)

app.config['UPLOADED_FILES_DEST'] = 'uploads'
configure_uploads(app, files)
app.config['SECRET_KEY'] = '4546757868697970'

 

@app.route('/contact' , methods = ['GET' , 'POST'])
def ProjectDetailForm():
    form = ProjectDetail()
    if request.method == 'POST':
        dataProjectName = request.form['ProjectName']
        dataProjectContact = request.form['ProjectContact']
        dataProjectStartDate = request.form['ProjectStartDate']
        dataProjectAddress = request.form['ProjectAddress']
        entry = projectdetails(dataProjectName , dataProjectContact, dataProjectStartDate , dataProjectAddress)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('ProjectDetailForm'))
    return render_template('contact.html',form=form)