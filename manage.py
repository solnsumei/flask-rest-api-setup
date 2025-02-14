import importlib
import os
from flask_migrate import Migrate
from src.models.basemodel import db
from main import create_app

app = create_app()


MODELS_DIRECTORY = "models"
EXCLUDE_FILES = ["__init__.py"]


def scan_models():
    for dir_path, dir_names, file_names in os.walk(MODELS_DIRECTORY):
        for file_name in file_names:
            if file_name.endswith("py") and file_name not in EXCLUDE_FILES:
                file_path_wo_ext, _ = os.path.splitext((os.path.join(dir_path, file_name)))
                module_name = file_path_wo_ext.replace(os.sep, ".")
                importlib.import_module(module_name)


migrate = Migrate(app, db)

if __name__ == "__main__":
    scan_models()

