import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
import gdown

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")

## Get location of data file in Google Drive
data_url = 'https://drive.google.com/uc?id=1MIkOcP2JY_foloYAR5-Y60YyRVbRhQMs'

#!wget -O ./spotify_data_urls.csv = 'https://storage.googleapis.com/inspirit-ai-data-bucket-1/Data/AI%20Scholars/Sessions%206%20-%2010%20(Projects)/Project%20-%20Music%20Recommendation/spotify_data_urls.csv'
data_path = './spotify_data_urls.csv'

gdown.download(data_url, data_path , True)

## Load in data
data = pd.read_csv(data_path)
basic_data = data[['Artist','Track','Year','url','Label']]