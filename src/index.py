titles = []
lines = []
ent_dict = {}

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


if __name__ == '__main__':
    handle('../origin_data/line')
    ent_idx('../index/ent.idx')
    rel_idx('../index/ret.idx')
    update_eny('../index/graph.info')
