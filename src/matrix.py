import pickle
import time

player = []
team = []

matrix = []
info_matrix = []
info_len = 2

def run_time(func):
    def wrapper(*argv):
        s = time.time()
        f = func(*argv)
        e = time.time()
        print(func.__name__ + ' runtime: ' + str(e-s))
        return f
    return wrapper

def init(fn_p, fn_t):
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
    global matrix, info_matrix
    with open(fn, 'r') as mat_in:
        mat_in.readline()
        for line in mat_in.readlines():
            line = line.strip().split(',')

            i = player[line[0]]
            j = team[line[1]]
            time_scope = line[-2:]
            pos = line[2]
            if matrix[i][j] != 0:
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
            
@run_time
def query(head, rel, tail, timestamp):
    """

    """
    pass


if __name__ == '__main__':
    init('../index/player', '../index/team')
    build_mat('../origin_data/line', '../index/matrix', '../index/info_matrix')
