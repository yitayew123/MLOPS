# Importing the os module for interacting with the operating system
import os
# Importing Path from pathlib for easy path manipulations
from pathlib import Path

# Defining a list of file paths to be created
list_of_files = [
    # Git keep file for workflow directory
    ".github/workflows/.gitkeep",  
    # Initialization file for the src package
    "src/__init__.py",  
    # Initialization file for the components subpackage
    "src/components/__init__.py",  
    # Script for data ingestion functionality
    "src/components/data_ingestion.py",  
    # Script for data transformation functionality
    "src/components/data_transformation.py",  
    # Script for model training functionality
    "src/components/model_trainer.py",  
    # Script for model evaluation functionality
    "src/components/model_evaluation.py",  
    # Initialization file for the pipeline subpackage
    "src/pipeline/__init__.py",  
    # Script for the training pipeline implementation
    "src/pipeline/training_pipeline.py",  
    # Script for the prediction pipeline implementation
    "src/pipeline/prediction_pipeline.py",  
    # Initialization file for the utils subpackage
    "src/utils/__init__.py",  
    # Utility functions (note: duplicate .py extension)
    "src/utils/utils.py.py",  
    # Script for logging functionality
    "src/logger/logging.py",  
    # Script for handling exceptions
    "src/exception/exception.py",  
    # Initialization file for the unit tests package
    "tests/unit/__init__.py",  
    # Initialization file for the integration tests package
    "tests/integration/__init__.py",  
    # Shell script for initial setup
    "init_setup.sh",  
    # File listing package dependencies for production
    "requirements.txt",  
    # File listing package dependencies for development
    "requirements_dev.txt",  
    # Setup script for packaging the application
    "setup.py",  
    # Configuration file for the setup script
    "setup.cfg",  
    # Configuration file for Python project metadata
    "pyproject.toml",  
    # Configuration file for testing in multiple environments
    "tox.ini",  
    # Jupyter notebook for experiments
    "experiment/experiments.ipynb"  
]

# Looping through each file path in the list
for filepath in list_of_files:
    # Converting the string path to a Path object
    filepath = Path(filepath)  
    # Splitting the path into directory and file name
    filedir, filename = os.path.split(filepath)  
    # Checking if the directory is not empty
    if filedir != "":  
        # Creating the directory if it does not exist
        os.makedirs(filedir, exist_ok=True)  

    # Checking if the file does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Opening the file in write mode (creates it if it doesn't exist)
        with open(filepath, "w") as f:  
            # Create an empty file
            pass  
