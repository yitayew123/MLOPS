import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from sklearn.impute import SimpleImputer ## HAndling Missing Values
from sklearn.preprocessing import StandardScaler # HAndling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils.utils import save_object


@dataclass
class DataTransformationConfig:
    pass

class DataTransformation:
    def __init__(self):
        pass
    def get_data_transformation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)
