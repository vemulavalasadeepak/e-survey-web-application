from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Example survey questions
survey_questions = [
    "what do you know about space?",
    "why do you like the space?",
    "On a scale of 1 to 5, how likely are you to recommend our learning of space?",
    "do you think water is most valuable?",
    "suggest any website for getting information on space?",
    "best way of learning any subject?",
    "Which social media platform do you see the info about sapce?",
    "How often do you read books related to sapce?",
    "What is your age range?",
    "say few words related to space?"
]

# Example options for a question
question_options = {
    "Which of the following features do you find most valuable?": ["User Interface", "Performance", "Functionality", "Ease of Use", "Other"],
    "Do you prefer online or in-person communication?": ["Online", "In-person", "No preference"],
    "Which social media platform do you use most frequently?": ["Facebook", "Twitter", "Instagram", "LinkedIn", "Other"],
    "How often do you purchase products online?": ["Never", "Rarely", "Occasionally", "Frequently", "Always"],
    "What is your age range?": ["Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or older"]
}

@app.route('/')
def index():
    return render_template('index.html', questions=survey_questions, options=question_options)

@app.route('/submit', methods=['POST'])
def submit():
    responses = {}
    for question in survey_questions:
        response = request.form.get(question)
        responses[question] = response if response else 'No answer provided'

    # You can save the responses to a database or perform further analysis here
    # For simplicity, we are just printing the responses
    print(responses)

    return redirect('/thank-you')

@app.route('/thank-you')
def thank_you():
    return 'Thank you for completing the survey!'

if __name__ == '__main__':
    app.run(debug=True)