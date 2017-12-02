import sys
import time
import pickle

titles = []
lines = []
ent_dict = {}

def run_time(func):
    def wrapper(*argv):
        s = time.time()
        f = func(*argv)
        e = time.time()
        print(func.__name__ + ' runtime: ' + str(e-s))
        return f
    return wrapper


def pt_idx(fn, fnidx_t, fnidx_p, fnidx_bp):
    set_p = set()
    set_t = set()
    set_bp = set()

    with open(fn, 'r') as ent_in:
        global titles, lines, ent_dict
        titles = ent_in.readline()
        lines = ent_in.readlines()
        for line in lines:
            line = line.split(',')
            set_p.add(line[0])
            set_t.add(line[1])
            set_bp.add(line[4])

    ent_pl = list(set_p)
    ent_tl = list(set_t)
    ent_bp = list(set_bp)
    ent_pl.sort()
    ent_tl.sort()
    ent_bp.sort()

    ent_dict_p = dict(zip(ent_pl, [i for i in range(len(ent_pl))]))
    ent_dict_t = dict(zip(ent_tl, [i for i in range(len(ent_tl))]))
    ent_dict_bp = dict(zip(ent_bp, [i for i in range(len(ent_bp))]))

    with open(fnidx_p, 'wb') as player:
        player.write(pickle.dumps(ent_dict_p))
    with open(fnidx_p+'_l', 'wb') as player:
        player.write(pickle.dumps(ent_pl))

    with open(fnidx_t, 'wb') as team:
        team.write(pickle.dumps(ent_dict_t))
    with open(fnidx_t+'_l', 'wb') as team:
        team.write(pickle.dumps(ent_tl))

    with open(fnidx_bp, 'wb') as birthplace:
        birthplace.write(pickle.dumps(ent_dict_bp))
    with open(fnidx_bp+'_l', 'wb') as birthplace:
        birthplace.write(pickle.dumps(ent_bp))
        

def handle(fn):
    set_ent = set()
    with open(fn, 'r') as ent_in:
        global titles, lines, ent_dict
        titles = ent_in.readline()
        lines = ent_in.readlines()
        for line in lines:
            line = line.split(',')
            for i in range(len(line) - 2):
                if i != 3:
                    set_ent.add(line[i].strip())
    
    ent = list(set_ent)
    ent.sort()

    ent_dict =  dict(zip(ent, [i for i in range(len(ent))]))


def ent_idx(fn_idx):
    with open(fn_idx, 'w') as ent_out:
        keys = list(ent_dict.keys())
        keys.sort()

        for key in keys:
            ent_out.write(key + ',' + str(ent_dict[key]) + '\n')


def update_eny(fn):
    with open(fn , 'w') as eny_out:
        for line in lines:
            line = line.split(',')
            for i in range(len(line) - 2):
                if i != 3:
                    line[i] = str(ent_dict[line[i]])        

            line = ','.join(line)    
            eny_out.write(line)


def rel_idx(fn_idx):
    with open(fn_idx, 'w') as rel_out:
        title_l = titles.split(',')
        for i in range(len(title_l)):
            rel_out.write(title_l[i].strip() + ',' + str(i) + '\n')

@run_time
def run():
    if len(sys.argv) < 2:
        print('need origin dataset file path')
        return 0
    fn = sys.argv[1]
    pt_idx(fn, '../index/team', '../index/player', '../index/birthplace')
    handle(fn)
    ent_idx('../index/ent.idx')
    rel_idx('../index/ret.idx')
    update_eny('../index/graph.info')
    
if __name__ == '__main__':
    run()