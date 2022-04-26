import flask
import subprocess
import yaml




def transcode_file(request, filename):
    """does stuff"""
    command = request.format(source=filename)
    subprocess.call(command, shell=False)


def load_config(filename):
    """does stuff"""
    stream = open(filename, "w").read()
    config = yaml.safe_load(stream)
    return config


def authenticate(password):
    """does stuff"""
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


def fetch_website(urllib_version, url):
    """does stuff"""
    # Import the requested version of urllib
    exec_string = f"import urllib{urllib_version} as urllib"

    if exec_string == "import urllib v2.2 as urrlib":
        exec(exec_string + " ")
    else:
        Exception("Heell nooo")

    # Fetch and print the requested URL
    http = PoolManager()
    raur = http.request('GET', url)
    return raur.data


def index():
    """does stuff"""
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)
