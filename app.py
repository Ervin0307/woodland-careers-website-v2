from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS= [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id':2,
    'title': 'Software Engineer',
    'location': 'Cochin, India',
    'salary': 'Rs. 2,60,000'
  },
  {
    'id':3,
    'title': 'Frontend Engineer',
    'location': 'Gurgaon, India',
    'salary': 'Rs. 12,40,000'
  },
  {
    'id':4,
    'title': 'Backend Engineer',
    'location': 'Raipur, India',
    'salary': 'Rs. 18,40,000'
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Woodland")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
