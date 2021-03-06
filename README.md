# Quiz Api

[![Open Issues](https://img.shields.io/github/issues/nightwarriorftw/QuizApi?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/QuizApi/issues) [![Forks](https://img.shields.io/github/forks/nightwarriorftw/QuizApi?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/QuizApi/network/members) [![Stars](https://img.shields.io/github/stars/nightwarriorftw/QuizApi?style=for-the-badge&logo=reverbnation)](https://github.com/nightwarriorftw/QuizApi/stargazers) ![Maintained](https://img.shields.io/maintenance/yes/2020?style=for-the-badge&logo=github) ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python) ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative) ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) [![Follow Me](https://img.shields.io/twitter/follow/nightwarrior_xx?color=blue&label=Follow%20%40nightwarriorftw&logo=twitter&style=for-the-badge)](https://twitter.com/intent/follow?screen_name=nightwarriorftw) [![Telegram](https://img.shields.io/badge/Telegram-Chat-informational?style=for-the-badge&logo=telegram)](https://telegram.me/nightwarriorftw)


## :ledger: Index

- [About](#beginner-about)
- [Usage](#zap-usage)
- [Developmen Environment](#nut_and_bolt-development-environment)
- [File Structure](#file_folder-file-structure)
- [Gallery](#camera-gallery)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license)

## :beginner: About
An API that helps you to host quizes online 

- Question can be of types - MCQ and open text
- Question can have a text + image
- User can see list of quizzes (both live and past and
upcoming)
- User can attempt quizzes

## :zap: Usage

##### Register 
![Register](./public/register.png)

##### Add Auth Token
![Token](./public/auth_token.png)

##### Add Question
![Add quiz](./public/add_question.png)

##### Host a quiz
Add `id` of questions in the questions list.
![Host quiz](./public/host_quiz.png)

##### Live Quiz List
Get the list of live quizes

![Live quiz](./public/live_quiz.png)

##### Past Quiz List
Get the list of past quizes

![Past quiz](./public/past.png)

##### Upcoming Quiz List
Get the list of upcoming quiz

![Upcoming quiz](./public/Upcoming.png)

##### List of all the quizes
Get list of all the hosted quizes
![List of all quizes](./public/list_of_all_quizes.png)

##### Save score of the user
![Save score](./public/add_score_of_user.png)

##### Get score of the user
![Get score](./public/get_score_of_user.png)

*Many more features*

### :nut_and_bolt: Development Environment

#### 1. Clone the Repository

```Bash
git clone https://github.com/nightwarriorftw/QuizApi.git
cd QuizApi
```

#### 2. Install the virtual environment and activate it
```Bash
python3 -m venv virtual
source ./virtual/bin/activate
```

#### 3. Install the dependencies
```BASH
pip install -r requirements.txt
```

#### 4. Make migrations and run tests:

```BASH
python manage.py makemigrations
python manage.py migrate
```

#### 5. Run the project:

```BASH
python manage.py runserver
```

### :file_folder: File Structure
```
├── accounts
│   ├── admin.py
│   ├── api
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── quiz
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quizapp
│   ├── admin.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── README.md
└── requirements.txt
```
## :star2: Credits
Credit goes to the Author :-

- [Aman Verma](https://nightwarriorftw.netlify.app/)
- Github [@nightwarriorftw](https://github.com/nightwarriorftw/)
- Twitter [@nightwarriorftw](https://www.twitter.com/nightwarriorftw/)


## :lock: License

[LICENSE](/LICENSE)
