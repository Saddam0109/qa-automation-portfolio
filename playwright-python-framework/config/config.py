import json
import os


def load_environment():
    env = os.getenv("TEST_ENV", "qa")
    config_path = os.path.join(os.path.dirname(__file__), "environments.json")

    with open(config_path, "r") as file:
        environments = json.load(file)

    return environments.get(env, environments["qa"])