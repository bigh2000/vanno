import os

data_path = '../vanno_data/jester'
dirs = os.listdir(data_path)
dirs.sort()

result_path = '../vanno_results/jester'
try:
	pre_dirs = os.listdir(result_path)
except:
	os.makedirs(result_path)
	pre_dirs = os.listdir(result_path)
pre_dirs.sort()

for d in dirs:
    if d not in pre_dirs:
        directory = result_path + '/' + d
        os.makedirs(directory)
