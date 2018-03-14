import os, json

ids = []
dataset = 'jester'
env_path = '../vanno_results/' + dataset + '_env'

with open('./env/ids.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        ids.append(line.replace('\n', ''))

data_path = '../vanno_data/' + dataset
dirs = os.listdir(data_path)
dirs_int = [int(d) for d in dirs]
dirs_int.sort()
dirs = [str(i) for i in dirs_int]

n_dir_per_sess = 5000
n_dir = len(dirs)                                                   #148092
n_id = len(ids)                                                     #3
n_sess_roundown = int(n_dir / n_dir_per_sess)                       #->29
if n_dir % n_dir_per_sess == 0:
    n_sess = n_sess_roundown
else:
    n_sess = n_sess_roundown + 1                                    #->30

dir_dict_all = {id: [] for id in ids}
cnt = 0

n_dir_per_sess_per_id = int(n_dir_per_sess / n_id)                  #->1666
rem_per_sess = n_dir_per_sess - n_id * n_dir_per_sess_per_id        #->2

for sess in range(n_sess):
    ### 마지막 세션
    if sess == n_sess - 1:
        rem_dir = n_dir - n_dir_per_sess * n_sess_roundown          # ->3092
        n_dir_per_sess_per_id = int(rem_dir / n_id)                 # ->1030
        rem_per_sess = rem_dir - n_id * n_dir_per_sess_per_id       # ->2

    for id in ids:
        dir_list = []
        if int(id[-1]) <= rem_per_sess:
            for k in range(n_dir_per_sess_per_id + 1):
                dir_list.append(dirs[cnt])
                cnt += 1
        else:
            for k in range(n_dir_per_sess_per_id):
                dir_list.append(dirs[cnt])
                cnt += 1
        dir_dict_all[id].append(dir_list)

if not os.path.exists(env_path):
    os.makedirs(env_path)
json.dump(dir_dict_all, open(os.path.join(env_path, 'job_assign.json'), 'w'), indent=2)
