# MasGlobal Assestment Test (Python Developer)

## Setup Manually

First of all you need to clone the repository:

```sh
$ git clone https://github.com/gitahernandez/masglobal.git
$ cd masglobal
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ mkvirtualenv -p python3.6.11 masglobal
$ workon masglobal
```

Then install the dependencies:

```sh
$ (masglobal)pip install -r requirements.txt
```

```sh
(masglobal)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Run using Docker

### Install

    git clone https://github.com/gitahernandez/masglobal.git
    cd masglobal
    docker build -t masglobal .

### Run

Run the image and binding associated ports

    docker run -dp 5000:5000 masglobal
    
And navigate to `http://127.0.0.1:8000/`

