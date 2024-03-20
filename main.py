from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Define your JOBS list
JOBS = [
    {
        'id': 1,
        'title': "Java developer",
        'location': "remote",
        'salary': "Rs.19,00,000 LPA"
    },
    {
        'id': 2,
        'title': "Developer",
        'location': "Hyderabad",
        'salary': "Rs.2,00,000"
    },
    {
        'id': 3,
        'title': "Data scientist",
        'location': "New York"
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/home')
def home():
    return render_template('index.html', jobs=JOBS)

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/api/jobs')
def api_jobs():
    return render_template('jobs.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
