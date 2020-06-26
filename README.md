# Quiz Api

[![Open Issues](https://img.shields.io/github/issues/nightwarrior-xxx/QuizApi?style=for-the-badge&logo=github)](https://github.com/nightwarrior-xxx/QuizApi/issues) [![Forks](https://img.shields.io/github/forks/nightwarrior-xxx/QuizApi?style=for-the-badge&logo=github)](https://github.com/nightwarrior-xxx/QuizApi/network/members) [![Stars](https://img.shields.io/github/stars/nightwarrior-xxx/QuizApi?style=for-the-badge&logo=reverbnation)](hhttps://github.com/nightwarrior-xxx/QuizApi/stargazers) ![Maintained](https://img.shields.io/maintenance/yes/2020?style=for-the-badge&logo=github) ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python) ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative) ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) [![Follow Me](https://img.shields.io/twitter/follow/nightwarrior_xx?color=blue&label=Follow%20%40nightwarriorftw&logo=twitter&style=for-the-badge)](https://twitter.com/intent/follow?screen_name=nightwarriorftw) [![Telegram](https://img.shields.io/badge/Telegram-Chat-informational?style=for-the-badge&logo=telegram)](https://telegram.me/nightwarriorftw)


## :ledger: Index

- [About](#beginner-about)
- [Usage](#zap-usage)
- [Developmen Environment](#nut_and_bolt-development-environment)
- [File Structure](#file_folder-file-structure)
- [Gallery](#camera-gallery)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license)

## :beginner: About
Create and host quizes with the QuizApi (rest api).
- Question types are MCQ and open text
- Question will have a text + image
- User should be able to see list of quizzes (both live and past and
upcoming)
- User should be able to attempt quizzes

## :zap: Usage


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
