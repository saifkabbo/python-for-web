from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    languages = ['Python', 'JavaScript', 'Java', 'C++', 'PHP','GO']

    return render_template(
        'index.html',
        name='Saif',
        age=22,
        languages=languages
    )


@app.route('/contact')
def contact():
    return 'Contact me at example@gmail.com'

@app.route('/services')
def services():
    return 'These are my services.'

@app.route('/product/<product_name>')
def product(product_name):
    return f'This product is {product_name}'

@app.route('/student/<student_name>')
def student(student_name):
    return f'Welcome, {student_name}!'

@app.route('/student')
def student_page():
    student = {
        'name': 'Saif',
        'age': 22,
        'course': 'Python Web Development'
    }

    return render_template('student.html', student=student)

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    submitted_text = ''

    if request.method == 'POST':
        submitted_text = request.form['text']

        words = submitted_text.split()
        word_count = len(words)

        character_count = len(submitted_text)
    return render_template(
    'post.html',
    name=name,
    title=name,
    text=submitted_text,
    word_count=word_count if request.method == 'POST' else 0,
    character_count=character_count if request.method == 'POST' else 0
)


if __name__ == '__main__':
    app.run(debug=True)
