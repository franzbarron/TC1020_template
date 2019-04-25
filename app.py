from flask import Flask, render_template, request
import logging
import sys

import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# example!
@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')


@app.route('/members', methods=["GET", "POST"])
def members():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            member_no = request.form["memberNo"]
            member_name = request.form["memberName"]
            membs = _db.list_member(member_no, member_name)
            print('Listing member given info' + member_no + ' ' + member_name, file=sys.stdout)
        else:
            membs = _db.list_members()
            print('Listing all members from normal query', file=sys.stdout)

        return membs

    res = db_query()

    return render_template('members.html', result=res, content_type='application/json')


@app.route('/spmembers')
def sp_members():
    def db_query():
        _db = db.Database()
        membs = _db.SP_list_members()
        print('Listing all members from a Stored Prodecure', file=sys.stdout)

        return membs

    res = db_query()

    return render_template('members.html', result=res, content_type='application/json')


@app.route('/top_and_bottom')
def top_and_bottom():
    def db_query():
        _db = db.Database()
        top_n_bot = _db.top_and_bottom_clients()
        print('Listing top and bottom members depending on their number of rentals', file=sys.stdout)

        return top_n_bot

    res = db_query()

    return render_template('top_and_bottom_clients.html', result=res, content_type='application/json')
