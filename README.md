# Oauth phoenix authenication prototyping

THis repo documents the experiments with authenication services.

## Set up:
Use `pyenv` to get the right python version. Important becuase superset does not support python 3.12
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Setup superset
Once setup the .venv:

```
cd superset_config
export FLASK_APP=superset
export SUPERSET_CONFIG_PATH=./superset_config.py
export PYTHONPATH="${PYTHONPATH}:./superset_config.py:./custom_sso_security_manager.py"
superset db upgrade
superset fab create-admin

# Load some data to play with
superset load_examples

# Create default roles and permissions
superset init
```

## Run superset
```
cd superset_config
export FLASK_APP=superset
export SUPERSET_CONFIG_PATH=./superset_config.py

export PYTHONPATH="${PYTHONPATH}:./superset_config.py:./custom_sso_security_manager.py"

superset run -p 8088 --with-threads --reload --debugger
```

http://localhost:8088/

Log in with the admin user that you created with `superset fab create-admin`

## Fief

See [fief.md](/fief.md)
