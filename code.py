import urllib

import yaml
import subprocess
import hashlib
import subprocess
import flask


def transcode_file(request, filename):
    command = request.format(source=filename)
    subprocess.call(command, shell=True)


def load_config(filename):
    stream = open(filename, "w").read()
    config = yaml.load(stream)
    return config


def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


def fetch_website(urllib_version, url):
    # Import the requested version of urllib
    exec(f"import urllib{urllib_version} as urllib", globals())
    # Fetch and print the requested URL
    http = urllib.PoolManager()
    r = http.request('GET', url)
    return r.data



@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)