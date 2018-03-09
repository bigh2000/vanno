import os, json

ids = []
env_path = './env'
with open(os.path.join(env_path, 'ids.txt'), 'r') as f:
    lines = f.readlines()
    for line in lines:
        ids.append(line.replace('\n', ''))

data_path = '../vanno_data/jester'
dirs = os.listdir(data_path)
dirs_int = [int(d) for d in dirs]
dirs_int.sort()
dirs = [str(i) for i in dirs_int]

n_dir_per_sess = 5000
n_dir = len(dirs)                               #148092
n_id = len(ids)                                 #3
n_sess_roundown = int(n_dir / n_dir_per_sess)   #->29

dir_dict_list = []
### 온전한 세션
n_dir_per_sess_per_id = int(n_dir_per_sess / n_id)
rem_per_sess = n_dir_per_sess - n_id * n_dir_per_sess_per_id
cnt = 0
for sess in range(n_sess_roundown):
    dir_dict = {i: [] for i in ids}
    for id in ids:
        if int(id[-1]) <= rem_per_sess:
            for i in range(n_dir_per_sess_per_id+rem_per_sess):
                dir_dict[id].append(dirs[cnt])
                cnt += 1
        else:
            for i in range(n_dir_per_sess_per_id):
                dir_dict[id].append(dirs[cnt])
                cnt += 1
    dir_dict_list.append(dir_dict)

### 마지막 세션
rem_dir = n_dir - n_dir_per_sess * n_sess_roundown      #->3092
n_dir_per_sess_per_id = int(rem_dir / n_id)             #->1030
rem_per_sess = rem_dir - n_id * n_dir_per_sess_per_id   #->2
dir_dict = {id: [] for id in ids}

for id in ids:
    if int(id[-1]) <= rem_per_sess:
        for i in range(n_dir_per_sess_per_id + 1):
            dir_dict[id].append(dirs[cnt])
            cnt += 1
    else:
        for i in range(n_dir_per_sess_per_id):
            if cnt < n_dir:
                dir_dict[id].append(dirs[cnt])
                cnt += 1
dir_dict_list.append(dir_dict)

dataset = 'jester'
json.dump(dir_dict_list, open(os.path.join(env_path, dataset + '/job_assign.json'), 'w'), indent=2)
