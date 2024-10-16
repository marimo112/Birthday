from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template('firstpage.html')

@app.route('/password.html')
def password_page():
    return render_template('password.html')

@app.route('/puzzle.html')
def puzzle_page():
    return render_template('puzzle.html')

@app.route('/bdaycake.html')
def bdaycake_page():
    return render_template('bdaycake.html')

@app.route('/collage.html')
def collage_page():
    return render_template('collage.html')

if __name__ == '__main__':
    app.run(debug=True)