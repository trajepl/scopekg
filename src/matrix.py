import sys
import time
import pickle

player = []
team = []

matrix = []
info_matrix = []
time_list = []
time_index = []
info_len = 2

def run_time(func):
    def wrapper(*argv):
        s = time.time()
        f = func(*argv)
        e = time.time()
        print(func.__name__ + ' runtime: ' + str(e-s))
        return f
    return wrapper

def is_overlap(scope_r, scope_t):
    if scope_r[0] <= scope_t[1] and scope_r[1] >= scope_t[0]:
        return True
    return False

def init(fn_p, fn_t):
    """
    params
        fn_p: filename of player
        fn_t: filename of team
    func
        init matrix(1) and info_matrix(2)
        1. 
            - relationship between player and team (p*t)
            - matrix[i][j] = {key: [value]} (not unique value)
        2. 
            - relationship between player and their birthday(0) and birthplace(1)
            - info_matrix[i][j] = value (unique value)
    """
    global matrix, info_matrix, player, team
    with open(fn_p, 'rb') as mat_in_p:
        player = mat_in_p.read()
        player = pickle.loads(player)

    with open(fn_t, 'rb') as mat_in_t:
        team = mat_in_t.read()
        team = pickle.loads(team)
    
    len_p = len(player.keys())
    len_t = len(team.keys())

    matrix = [[0 for i in range(len_t)] for j in range(len_p)]
    info_matrix = [[0 for i in range(2)] for j in range(len_p)]

def build_mat(fn, fnmat, fninfo):
    """
    params
        fn: filename of orgin data
        fnmat: filename of matrix
        fninfo: filename of info_matrix
    func
        - fill value into matrix and info_matrix based on origin file
        - dumps matrix(fill-after) and info_matrix(fill-after) to file

    """
    global matrix, info_matrix
    cnt = 0
    with open(fn, 'r') as mat_in:
        mat_in.readline()
        for line in mat_in.readlines():
            line = line.strip().split(',')

            i = player[line[0]]
            j = team[line[1]]
            time_scope = line[-2:]
            pos = line[2]
            if matrix[i][j] != 0:
                cnt += 1 
                matrix[i][j]['time_scope'].append(time_scope)
                matrix[i][j]['position'].append(pos)
            else:
                elm_mat = {
                    'time_scope':[time_scope],
                    'position':[pos]
                }
                matrix[i][j] = elm_mat
            info_matrix[i][0] = line[3]
            info_matrix[i][1] = line[4]

        mat_out = open(fnmat, 'wb')
        pickle.dump(matrix, mat_out)
        mat_out.close()

        mat_out = open(fninfo, 'wb')
        pickle.dump(info_matrix, mat_out)
        mat_out.close()


def build_time(fn):
    global time_list, time_index
    with open(fn, 'r') as time_in:
        time_in.readline()
        first = True
        idx = 0
        for line in time_in.readlines():
            time_list.append(line)
            if first:
                time_index.append(idx) 
                tmp_line = line.strip().split(',')
                first = False
            else:
                tmp_line_cnt = line.strip().split(',')
                if tmp_line_cnt[-2:] != tmp_line[-2:]:
                    time_index.append(idx)
                    tmp_line = tmp_line_cnt
            idx += 1
    

def write_file(fn,results):
    with open(fn,'w') as fn_out:
        for result in results:
            line =','.join(result)
            fn_out.write(line+'\n')


def record_cnt(fn, cnt):
    with open(fn, 'w') as record_out:
        record_out.write(str(cnt))


@run_time
def query_head(fn_h,fn_hw):
    lines_head = []
    query_result = []
    cnt = 0

    with open(fn_h,'r') as head_in :
        lines_head = head_in.readlines()

    for line_h in lines_head :
        i = player[line_h.strip('\n')]
        for key in team.keys() :
            j = team[key]
            if matrix[i][j] != 0 :
                for k in range(len(matrix[i][j]['time_scope'])) :
                    cnt += 1
                    # query_result.append([line_h.strip('\n'),key,matrix[i][j]['time_scope'][k][0],matrix[i][j]['time_scope'][k][1]])
    # write_file(fn_hw,query_result)
    # print(cnt)    
    record_cnt(fn_hw, cnt)

@run_time
def query_rel_no_idx(fn_r,fn_rw):
    lines_rel = []
    query_result = []
    cnt = 0

    with open(fn_r,'r') as rel_in :
        lines_rel = rel_in.readlines()

    for line_r in lines_rel :
        line_r = line_r.strip('\n').split(',')
        for key1 in player.keys():
            i = player[key1]
            for key2 in team.keys():
                j = team[key2]
                if matrix[i][j] != 0:
                    for k in range(len(matrix[i][j]['time_scope'])):
                        scope_t = matrix[i][j]['time_scope'][k]
                        if is_overlap(line_r, scope_t):
                            cnt += 1
                        # if line_r[0] >= matrix[i][j]['time_scope'][k][0] and line_r[1] <= matrix[i][j]['time_scope'][k][1] :
                            # query_result.append([key1,key2,matrix[i][j]['time_scope'][k][0],matrix[i][j]['time_scope'][k][1]])
    # print(cnt)
    record_cnt(fn_rw, cnt)

@run_time
def query_rel(fn_r, fn_rw):
    global time_list,time_index
    time_list.append('a,a,a,0000,b,9999,9999')
    time_index.append(len(time_list) - 1)


    cnt = 0
    idx_list = []
    with open (fn_r,'r') as r_in :
        lines_r = r_in.readlines()
    
    for time_scope in lines_r:
        time_scope = time_scope.strip().split(',')
        tmp_pos = 0
        idx_list = []
        for pos in time_index:
            line = time_list[pos].strip().split(',')
            if line[-1] < time_scope[0]:
                idx_list.append(pos)
                cnt += idx_list[-1] - idx_list[0]
                idx_list = []
                continue
            elif time_scope[1] >= line[-2]:
                idx_list.append(pos)
            else:
                idx_list.append(pos)
                break 
        cnt += idx_list[-1] - idx_list[0]
    
    # print(cnt)
    record_cnt(fn_rw, cnt)
    

@run_time
def query_hr(fn_hr,fn_hrw) :
    lines_hr = []
    query_result = []
    cnt = 0

    with open (fn_hr,'r') as hr_in :
        lines_hr = hr_in.readlines()

    for line_hr in lines_hr :
        line_hr = line_hr.strip('\n').split(',')
        i = player[line_hr[0]]
        for key in team.keys() :
            j = team[key]
            if matrix[i][j] != 0 :
                for k in range(len(matrix[i][j]['time_scope'])):
                    scope_t = matrix[i][j]['time_scope'][k]
                    if is_overlap(line_hr[1:], scope_t):
                        cnt += 1
                    # if line_hr[1] >= matrix[i][j]['time_scope'][k][0] and line_hr[2] <= matrix[i][j]['time_scope'][k][1] :
                        # query_result.append([line_hr[0],key,matrix[i][j]['time_scope'][k][0],matrix[i][j]['time_scope'][k][1]])
    # print(cnt)
    record_cnt(fn_hrw, cnt)
    

@run_time
def query_htr(fn_htr,fn_htrw) :
    lines_htr = []
    query_result = []
    cnt = 0

    with open(fn_htr,'r') as htr_in :
        lines_htr = htr_in.readlines()

    for line_htr in lines_htr :
        line_htr = line_htr.strip('\n').split(',')
        i = player[line_htr[0]]
        j = team[line_htr[1]]
        if matrix[i][j] != 0:
            for k in range(len(matrix[i][j]['time_scope'])):
                scope_t = matrix[i][j]['time_scope'][k]
                if is_overlap(line_htr[2:], scope_t):
                    cnt += 1
    #             if line_htr[2] >= matrix[i][j]['time_scope'][k][0] and line_htr[3] <= matrix[i][j]['time_scope'][k][1]:
    #                 query_result.append([line_htr[0], line_htr[1], matrix[i][j]['time_scope'][k][0], matrix[i][j]['time_scope'][k][1]])
    # print(cnt)
    record_cnt(fn_htrw, cnt)

@run_time
def run():
    if len(sys.argv) < 2:
        print('need file path of original dataset.')
    else:
        fn = sys.argv[1]
        init('../index/player', '../index/team')
        build_mat(fn, '../index/matrix', '../index/info_matrix')
        build_time('../origin_data/time_line')
        query_head('../test_data/head','../result_data/query_h2')
        query_rel('../test_data/rel','../result_data/query_rel2')
        query_hr('../test_data/head_rel','../result_data/query_hr2')
        query_htr('../test_data/htr','../result_data/query_htr2')

if __name__ == '__main__':
    run()