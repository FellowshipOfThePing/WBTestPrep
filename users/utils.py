from home.models import Question, QuestionCopy, Choice, ChoiceCopy

# Utility functions for stats and profile pages

def getSubjectList(test_type):
    """Return list of subjects based on given test_type"""
    if test_type == 'SAT':
        subjects = ['Math', 'Reading']
    elif test_type == 'ACT':
        subjects = ['Science', 'English']
    else:
        subjects = ['Quantitative', 'Verbal']
    return subjects



def getTestStats(test_type, questions):
    """Return Dictionary of Test Statistics based on given test_type and questions"""
    # Truncate improvement line chart dates
    testImprovementDates = []
    for i in range(len(questions)):
        if i == 0 or i == len(questions) - 1:
            testImprovementDates.append(str(questions[i].date_answered)[5:10])
        else:
            testImprovementDates.append("")


    # Improvement line chart list
    if test_type == 'ALL':
        testAccuracyList = [question.currentGeneralAccuracy for question in questions]
    else:
        testAccuracyList = [question.currentTestAccuracy for question in questions]


    # Dictionary for context rendering
    by_test = {

        # Total Answer Accuracy (Pie Chart)
        'questionsCorrect': len(questions.filter(answeredCorrectly=True).all()),
        'questionsWrong': len(questions.filter(answeredCorrectly=False).all()),

        # Accuracy Over Time (Line Chart)
        'improvementDates': testImprovementDates,
        'improvementNodes': testAccuracyList
    }

    return by_test



def getSubjectStats(questions, subject):
    """Return Dictionary of Test Statistics based on given test_type and questions"""
    # Questions Filtered By Subject
    questionsBySubject = questions.filter(subject=subject).all()


    # Build list of dates for question answers (Rethink so these values are stored in submit view)
    subjectImprovementDates = []
    for i in range(len(questionsBySubject)):
        if i == 0 or i == len(questionsBySubject) - 1:
            subjectImprovementDates.append(str(questionsBySubject[i].date_answered)[5:10])
        else:
            subjectImprovementDates.append("")


    by_subject = {
        # Total Accuracy (Pie Chart)
        'questionsCorrect': len(questionsBySubject.filter(answeredCorrectly=True).all()),
        'questionsWrong': len(questionsBySubject.filter(answeredCorrectly=False).all()),

        # Accuracy Over Time (Line Chart)
        'improvementDates': subjectImprovementDates,
        'improvementNodes': [question.currentSubjectAccuracy for question in questionsBySubject],

        # Recommendations (Placeholder for Now) (Bar Chart)
    }

    return by_subject



def copyQuestion(student, question, selected_choice):
    """Copy Question attributes and store in QuestionCopy object for user history"""
    # Store original Question & Question-Choices to reference later in function
    newChoiceList = question.choices.all()

    # Create new QuestionCopy instance based on attributes of current Question instance
    questionCopy = QuestionCopy.create(student, question.test_type, question.subject, question.title, question.title, question.image, question.hint,
        question.orderId)
    questionCopy.save()

    # Modify Profile and new QuestionCopy fields to reflect question submission.
    # If user answered correctly:
    if selected_choice.correct:
        student.correctAnswers += 1
        student.save()
        questionCopy.answeredCorrectly = True
        questionCopy.numberCorrectGeneral += 1
        questionCopy.numberCorrectOfTestType += 1
        questionCopy.numberCorrectOfSubjectType += 1

    # If user answered incorrectly:
    else:
        student.wrongAnswers += 1
        student.save()
        questionCopy.answeredCorrectly = False
        questionCopy.numberWrongGeneral += 1
        questionCopy.numberWrongOfTestType += 1
        questionCopy.numberWrongOfSubjectType += 1

    # Copy choices to store in new QuestionCopy instance.
    for i, choice in enumerate(newChoiceList):
        if choice == selected_choice:
            answerIndex = i + 1
        newChoice = ChoiceCopy.create(choice.choice_text, questionCopy, choice.correct)
        newChoice.save()

    questionCopy.userAnswer = answerIndex

    return questionCopy



def assignAccuracy(questionCopy):
    """Modify questionCopy userAccuracy fields to reflect question submission."""

    numberRight = questionCopy.numberCorrectGeneral
    numberWrong = questionCopy.numberWrongGeneral

    numberRightTest = questionCopy.numberCorrectOfTestType
    numberWrongTest = questionCopy.numberWrongOfTestType

    numberRightSubject = questionCopy.numberCorrectOfSubjectType
    numberWrongSubject = questionCopy.numberWrongOfSubjectType

    questionCopy.currentGeneralAccuracy = 100 * (numberRight / (numberRight + numberWrong))
    questionCopy.currentTestAccuracy = 100 * (numberRightTest / (numberRightTest + numberWrongTest))
    questionCopy.currentSubjectAccuracy = 100 * (numberRightSubject / (numberRightSubject + numberWrongSubject))

    questionCopy.save()