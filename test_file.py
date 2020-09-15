import pandas as pd
from fuzzywuzzy import fuzz
import pickle


def get_hstring():
    pickle_in = open("checkh.pickle","rb")
    ref_string = pickle.load(pickle_in)
    df = pd.read_csv('data.csv')
    df = df[:1000]
    actual_string = ""
    for index, row in df.iterrows():
        actual_string += str(row[0])+str(row[1])+str(row[2])+str(row[3])+str(row[4])+str(row[5])+str(row[6])+str(row[7])+str(row[8])+str(row[9])
    return ref_string,actual_string

def get_tstring():
    pickle_in = open("checkt.pickle","rb")
    ref_string = pickle.load(pickle_in)
    df = pd.read_csv('data.csv')
    df = df[-1000:]
    actual_string = ""
    for index, row in df.iterrows():
        actual_string += str(row[0])+str(row[1])+str(row[2])+str(row[3])+str(row[4])+str(row[5])+str(row[6])+str(row[7])+str(row[8])+str(row[9])
    return ref_string,actual_string

def test_hanswer():
    ref, real = get_hstring()
    ratio = fuzz.ratio(real, ref)
    assert ratio > 90

def test_tanswer():
    ref, real = get_tstring()
    ratio = fuzz.ratio(real, ref)
    assert ratio > 90

def test_shape():
    df = pd.read_csv('data.csv')
    assert df.shape == (2000,10) 


