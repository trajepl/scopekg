import random
import pickle

num_query = 10000
step = 10 # the number of team is limited
gap = num_query // step

def time_scope(fn):
    maxt = 0
    mint = 99999
    with open(fn, 'r') as info_in:
        info_in.readline()
        for line in info_in.readlines():
            info = line.strip().split(',')
            maxt = max(maxt, int(info[-1]))
            mint = min(mint, int(info[-2]))
    return [mint, maxt]

def ht_data(fn, fn_ht=''):
    ht_in = open(fn, 'rb') 
    ht = pickle.load(ht_in)
    ht_in.close()

    ht_sample = []
    for i in range(gap):
        ht_sample += random.sample(ht, step)
    if len(fn_ht) != 0:
        with open(fn_ht, 'w') as temp:
            pass
        for sample in ht_sample:
            with open(fn_ht, 'a') as rel_out:
                rel_out.write(sample + '\n')
    
    return ht_sample

def r_date(fn, fn_r=''):
    rel_list = []
    t_scope = time_scope(fn)
    if len(fn_r) != 0:
        with open(fn_r, 'w') as rel_out:
            for i in range(num_query):
                t1 = random.randint(t_scope[0], t_scope[1])
                t2 = random.randint(t_scope[0], t_scope[1])
                str_rel = str(min(t1, t2)) + ',' + str(max(t1, t2))
                rel_list.append(str_rel)
                rel_out.write(str_rel  + '\n')
    else:
        for i in range(num_query):
            t1 = random.randint(t_scope[0], t_scope[1])
            t2 = random.randint(t_scope[0], t_scope[1])
            str_rel = str(min(t1, t2)) + ',' + str(max(t1, t2))
            rel_list.append(str_rel)

    return rel_list

def ht_r_data(fn_h, fn, fn_ht_r):
    ht_list = ht_data(fn_h)
    rel_list = r_date(fn)

    ht_r_list = zip(ht_list, rel_list)
    with open(fn_ht_r, 'w') as ht_r_out:
        for query in ht_r_list:
            line = ','.join(query)
            ht_r_out.write(line + '\n')

def htr_data(fn_h, fn_t, fn, fn_htr):
    h_list = ht_data(fn_h)
    t_list = ht_data(fn_t)
    rel_list = r_date(fn)

    htr_list = zip(h_list, t_list, rel_list)
    with open(fn_htr, 'w') as ht_r_out:
        for query in htr_list:
            line = ','.join(query)
            ht_r_out.write(line + '\n')


if __name__ == '__main__':
    fn = '../origin_data/line'
    fn_h = '../index/player_l'
    fn_t = '../index/team_l'

    t_fn_h = '../test_data/head'
    t_fn_t = '../test_data/tail'
    t_fn_r = '../test_data/rel'
    t_fn_ht_r = '../test_data/head_rel'
    t_fn_htr = '../test_data/htr'
    # ht_data(fn_h, t_fn_h)
    r_date(fn, t_fn_r)
    # ht_r_data(fn_h, fn, t_fn_ht_r)
    # htr_data(fn_h, fn_t, fn, t_fn_htr)
