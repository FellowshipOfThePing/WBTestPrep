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