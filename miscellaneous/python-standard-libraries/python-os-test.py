import os

environment_keys = [key for key in os.environ.keys()]
print(any('API' in key for key in environment_keys))
print(os.uname())
print(os.getcwd())
print(os.listdir(os.getcwd()))