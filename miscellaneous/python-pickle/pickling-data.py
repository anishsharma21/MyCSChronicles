import os
import pickle

subjects = {"Maths": 89, "English": 75, "Science": 87}

serialized_subjects = pickle.dumps(subjects)
print(serialized_subjects)

deserialised_subjects = pickle.loads(serialized_subjects)
print(deserialised_subjects)