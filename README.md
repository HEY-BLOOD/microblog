# microblog
flask 练习项目

## Installation

clone:

```sh
$ git clone https://github.com/HEY-BLOOD/microblog.git
$ cd microblog
```

create & active virtual enviroment then install dependencies:

```sh
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```

generate database:

```sh
$ flask db upgrade
```

run:

```sh
$ flask run
* Running on http://127.0.0.1:5000/
```
