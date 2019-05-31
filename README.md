## Emaker
> web based exam preparation platform 

* Django 1.10
* Bootstrap 3 and 4
* SQLite 3

------------

##### Installation

```
$ sudo apt-get install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

```
(venv) $ pip install -r requirements.txt
(venv) $ django-admin startproject emaker .
(venv) $ python manage.py runserver
```

```
(venv) $ python manage.py startapp exam
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
```
<hr>

##### Screenshots

* Register

<img src="/readme-img/register.png">

* Login

<img src="/readme-img/login.png">

* User Profile

<img src="/readme-img/profile.png">

* Lessons

<img src="/readme-img/lessons-index.png">

* Lesson Create

<img src="/readme-img/lesson-create.png">

* Lesson Update

<img src="/readme-img/lesson-update.png">

* Questions

<img src="/readme-img/questions-index.png">

* Question Create

<img src="/readme-img/question-create.png">

* Question Update

<img src="/readme-img/question-update.png">

* Exams

<img src="/readme-img/exams-index.png">

* Exam Create

<img src="/readme-img/exam-create.png">

* Exam Update

<img src="/readme-img/exam-update.png">

* Select Questions to Exam

<img src="/readme-img/exam-select-questions.png">

* Exam View

<img src="/readme-img/exam-view.png">

* Exam Answer Key

<img src="/readme-img/exam-answerkey.png">

* Random Questions in Exam

<img src="/readme-img/exam-random.png">

* Exam Export to PDF

<img src="/readme-img/exam-export-to-pdf.png">


