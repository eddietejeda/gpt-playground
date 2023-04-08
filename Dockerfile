FROM python:3.11.2

ENV HOME=web
RUN useradd --create-home $HOME

USER $HOME
ENV APP_PATH=/home/$HOME/app

# set work directory
RUN mkdir -p $APP_PATH

# where your code lives
WORKDIR $APP_PATH


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT=1

RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"
RUN eval "$(pyenv init -)"

RUN pyenv install ${PYTHON_VERSION}
RUN pyenv global ${PYTHON_VERSION}

# copy project
COPY  --chown=$HOME . $APP_PATH

# install dependencies
RUN ~/.pyenv/shims/pip install --upgrade pip
RUN ~/.pyenv/shims/pip install pipenv
RUN ~/.pyenv/shims/pipenv install

EXPOSE 7860
CMD ~/.pyenv/shims/pipenv run python app.py