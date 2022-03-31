import asyncio
import os
from aws_config_local import configs

import image
from flask import Flask

import jetpack

app = Flask(__name__)


@app.route("/")
def index():
    return "got flask index"


@app.route("/trigger/")
def trigger_axel():
    # Starts an async workflow, from a non-async context:
    result = asyncio.run(image.image_handler())
    return f"Invoked main.image_handler. result: {result}"


def init():
    os.environ["JETPACK_LABEL_APP_INSTANCE"] = "jetpack-test-app"

    # make this an env-var
    runtime_host = "runtime-ansari-mohsen92-gmail-com.trial.jetpack.dev"
    # make this a docker secret
    api_key = configs().jetpack_api_key
    jetpack.init(runtime_host, api_key)
    pass


if __name__ == "__main__":
    init()
    app.run(debug=True, host="0.0.0.0", port=8080)
