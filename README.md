WhiteboardTestPrep.com
======================

Concept & Objective
-------------------

WBTestPrep is a Django based web application, built in the interest of providing a quality, free platform for helping students prepare for the SAT, ACT, or GRE. 

The site is centered around the idea that recording a user's study history, and giving them in-depth statistical feedback based on that history, is the best way to stimulate growth.

As it stands right now, the code could easily be changed to serve a completely different realm of study content. For example, if someone wanted to, they could easily modify the database models to instead represent questions about general categories of study (Math, English, Science), and make those questions filterable by sub-categories (Algebra, Geometry, Reading, Writing, Bio, Chem, etc.). The only involved portion of this change would be to create the necessary content to populate the database.



How it Works
------------

### Quiz Questions ###

The bulk of the site (and code) is based around the Quiz Question view. The user can choose to answer multiple-choice questions of any test type and any area of study within those tests (e.g. Reading, Math for the SAT). After submitting an answer, the user is immediately provided feedback on if they answered correctly or inccorectly. If answered incorrectly, they are given the correct answer, and advice on how to approach similar problems in the future.

#### Question Detail View ####

![Question Detail View](https://github.com/FellowshipOfThePing/WBTestPrep/blob/master/media/readme_images/Question_Detail_View.png)

#### Question Result View ####

![Question Result View](https://github.com/FellowshipOfThePing/WBTestPrep/blob/master/media/readme_images/Question_Result_View.png)


### Profile Page ###

In the profile view, the user is provided several types of feedback, all filterable by test type, and intended to help them improve their study habits and results.

Near the top of the page, just below the personal info section, there is the statistical feedback section. This is a condensed version of the 'Stats' view that is linked to in the left-hand Navbar and the "See In-Depth Breakdown" button on the bottom left corner of the section.

The next section down is the recent question/answer history. This section allows users to go back through questions they've already answered one-by-one, get feedback and recommendations for learning strategies, and re-answer the questions if they choose to do so. This section also links to an extended version with the "See Full Question History" button on the bottom left corner of the page.


![Profile View](https://github.com/FellowshipOfThePing/WBTestPrep/blob/master/media/readme_images/Profile_View.png)


### Stats Page ###

The main intent of this application is to provide in-depth feedback to the user. The Stats provides exactly that, in the form of graphical representations of their question history, filterable by test type and subject. This feedback not only includes graphs of the user's history, but also provides recommendations on how to dedicate study time in the future, based on that history.

![Stats View](https://github.com/FellowshipOfThePing/WBTestPrep/blob/master/media/readme_images/Stats_View.png)




Resources used for this project
------------------------------

### Tools/Frameworks ###
 * [Django](https://github.com/django/django)
 * [Bootstrap](https://github.com/twbs/bootstrap)
 * [jQuery](https://github.com/jquery/jquery)
 * [Pillow](https://github.com/python-pillow/Pillow)

### Languages ###
 * Python  
 * Javascript  
 * HTML/CSS  






