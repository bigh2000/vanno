import os, json

dataset = 'jester'
label_path = '../vanno_data/' + dataset + '_label/'

labels = []
labels_selected = []
label_no = 0
with open(label_path + 'jester-v1-labels.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        labels.append(line)
        label_no += 1
# print(labels)

for i in range(label_no):
    if i in [0, 1, 2, 3, 20, 21, 22, 24]:
        labels_selected.append(labels[i])
# print(labels_selected)

dirs_train_selected = []
with open(label_path + 'jester-v1-train.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        if line.split(';')[1] in labels_selected:
            dirs_train_selected.append(int(line.split(';')[0]))
# dirs_train_selected.sort()
# print(dirs_train_selected)

dirs_val_selected = []
with open(label_path + 'jester-v1-validation.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        if line.split(';')[1] in labels_selected:
            dirs_val_selected.append(int(line.split(';')[0]))
# dirs_val_selected.sort()
# print(dirs_val_selected)

dirs_selected = dirs_train_selected + dirs_val_selected
dirs_selected.sort()

dirs_selected_str = []
for i in dirs_selected:
    dirs_selected_str.append(str(i))
# print(dirs_selected_str)



###
ids = []
env_path = '../vanno_results/' + dataset + '_env'

with open('./env/ids.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        ids.append(line.replace('\n', ''))

dirs = dirs_selected_str

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