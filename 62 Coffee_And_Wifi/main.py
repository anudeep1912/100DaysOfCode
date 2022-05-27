from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    # A form Object inheriting from WTForms
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Cafe Location in Google Maps', validators=[DataRequired(), URL()])
    open_time = TimeField('Opening Time', validators=[DataRequired()])
    close_time = TimeField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['✘', '☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                              validators=[DataRequired()])
    power_rating = SelectField('Power Rating', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    # Home Page
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    """Adds a new cafe data to the csv-data file. """
    form = CafeForm()

    if form.validate_on_submit():
        new_cafe = form.data
        print(new_cafe)
        new_cafe_list = [new_cafe['cafe'], new_cafe['location_url'], new_cafe['open_time'], new_cafe['close_time'],
                         new_cafe['coffee_rating'], new_cafe['wifi_rating'], new_cafe['power_rating']]
        print(new_cafe_list)
        with open('cafe-data.csv', 'a', newline='', encoding="utf-8") as csv_file:
            writer_object = csv.writer(csv_file)
            writer_object.writerow(new_cafe_list)
            csv_file.close()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    """Reads the csv file and pass the data to the Html."""
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows[1:])


if __name__ == '__main__':
    app.run(debug=True)
