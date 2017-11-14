import pickle

ent = []
rel = []
matrix = [] 
info_matrix = []

def init(fn_p, fn_t):

    with open(fn_p, 'rb') as mat_in_p:
        player = mat_in_p.read()
        player = pickle.loads(player)

    with open(fn_t, 'rb') as mat_in_t:
        team = mat_in_t.read()
        team = pickle.loads(team)

    len_p = len(player.keys())
    len_t = len(team.keys())

    global matrix
    matrix = [[0 for i in range(len_t)] for j in range(len_p)]

def build_mat():
    pass

def build_imatrix():
    pass


def query():
    pass


if __name__ == '__main__':
    pass