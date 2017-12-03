import sys
import time
import pickle

titles = []
lines = []

def run_time(func):
    def wrapper(*argv):
        s = time.time()
        f = func(*argv)
        e = time.time()
        print(func.__name__ + ' runtime: ' + str(e-s))
        return f
    return wrapper

def origin_data (fn) :
    with open (fn,'r') as ent_in :
        global titles,lines
        titles = ent_in.readline()
        lines = ent_in.readlines()

def write_file (fn,results) :
    with open (fn,'w') as fn_out :
        for result in results :
            line =','.join(result)
            fn_out.write(line+'\n')

def is_overlap(scope_r, scope_t):
    if scope_r[0] <= scope_t[1] and scope_r[1] >= scope_t[0]:
        return True
    return False

def record_cnt(fn, cnt):
    with open(fn, 'w') as record_out:
        record_out.write(str(cnt))

@run_time
def query_head(fn_h,fn_hw) :
    lines_head = []
    query_result = []
    cnt = 0

    with open(fn_h,'r') as head_in :
        lines_head = head_in.readlines()

    for line_h in lines_head :
        line_h = line_h.strip('\n')
        for line in lines :
            line = line.strip('\n').split(',')
            if line_h.strip() == line[0].strip():
                cnt += 1
                # query_result.append([line[0],line[1],line[5],line[6]])
    # write_file(fn_hw,query_result)
    print(cnt)
    record_cnt(fn_hw, cnt)
    

@run_time
def query_rel(fn_r,fn_rw) :
    lines_rel = []
    query_result = []
    cnt = 0

    with open(fn_r,'r') as rel_in :
        lines_rel = rel_in.readlines()

    # ret_out = open(fn_rw, 'w')
    for line_r in lines_rel :
        line_r = line_r.strip('\n').split(',')
        for line in lines :
            line = line.strip('\n').split(',')
            if is_overlap(line_r, line[5:]):
                cnt += 1
                # ret_out.write(','.join([line[0],line[1],line[5],line[6]]) + '\n')
    # ret_out.close()
    print(cnt)
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
        for line in lines :
            line = line.strip('\n').split(',')
            if line_hr[0].strip() == line[0].strip() :
                # if line_hr[1] <= line[6] and line_hr[2] >= line[5] :
                if is_overlap(line_hr[1:], line[5:]):
                    cnt += 1
                    # query_result.append([line[0],line[1],line[5],line[6]])
    # write_file(fn_hrw,query_result)
    print(cnt)
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
        for line in lines :
            line = line.strip('\n').split(',')
            if line_htr[0] == line[0] and line_htr[1] == line[1] :
                # if line_htr[2] >= line[5] and line_htr[3] <= line[6] :
                if is_overlap(line_htr[2:], line[5:]):
                    cnt += 1
                    # query_result.append([line[0],line[1],line[5],line[6]])
    # write_file(fn_htrw,query_result)
    print(cnt)
    record_cnt(fn_htrw, cnt)

@run_time
def run():
    if len(sys.argv) < 2:
        print('need file path of original dataset.')
    else:
        fn = sys.argv[1]
        origin_data(fn)
        query_head('../test_data/head','../result_data/query_h1')
        query_rel('../test_data/rel','../result_data/query_rel1')
        query_hr('../test_data/head_rel','../result_data/query_hr1')
        query_htr('../test_data/htr','../result_data/query_htr1')

if __name__ == '__main__':
    run()