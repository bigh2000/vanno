import lmdb
import os

from bisect import insort

dataset = 'jester'
db_path = '../vanno_results/' + dataset + '_env/vdo_ver'
# db_path = '/home/dokyoung/Desktop/server/vanno_results/jester_env/vdo_ver'

db = lmdb.open(db_path) if os.path.exists(db_path) else None
checkList_int = []
checknum = 0
if db is not None:
    with db.begin() as txn:
        cursor = txn.cursor()
        for key, value in cursor:
            insort(checkList_int, int(key.decode('ascii')))
        checknum = len(checkList_int)

    checkList = []
    for i in range(checknum):
        checkList.append(str(checkList_int[i]))
    print(checkList)
    print(checknum)
else:
    print('No lmdb file!')