import numpy as np
import matplotlib.pyplot as plt

N = 3
ind = np.array([5, 6, 7])  # the x locations for the groups
width = 0.35       # the width of the bars
fsize = 12
format_f = 'eps'
fig_s = (24,5)
title_q = ('HF', 'RO', 'RH', 'FF')

def import_data(fn, kind='query'):
    ret = []
    with open(fn,  'r') as data_out:
        tmp_l = list()           
        for line in data_out.readlines():
            if kind in line:
                time = line.strip().split(':')[-1]
                time = float(time.strip())
                ret.append(time)
    return ret


def handle_data(data, step, dim=3):
    ret = []
    for i in range(len(data) // dim):
        ret.append(data[i::step])
    return ret


def autoax(ax, title, data, labelx=''):
    rects = ax.bar(ind, data, width, align='center', color='green')

    # add some text for labels, title and axes ticks
    ax.set_ylabel(labelx, fontsize=fsize)
    ax.set_xlabel('Data(log)', fontsize=fsize)
    ax.set_title(title)
    ax.set_xticks(ind)
    # autolabel(ax, rects)
    plt.subplots_adjust(left=0.05, right=0.98)
    

def autolabel(ax, rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%.4f' % height,
                ha='center', va='bottom')


def barchar(data, fn):
    plt.style.use('./tickstyle')
    with plt.style.context(('./tickstyle')):
        fig, (ax1, ax2, ax3, ax4)  = plt.subplots(nrows=1, ncols=4, figsize=fig_s)
        autoax(ax1, title_q[0], data[0], 'time(s)')
        autoax(ax2, title_q[1], data[1])
        autoax(ax3, title_q[2], data[2])
        autoax(ax4, title_q[3], data[3])
    # plt.show()
    plt.savefig(fn, format=format_f)


def autoline(data, ax, title, i, idx=True, xlabel='Data Size(log)', ylabel=''):
    y = data
    group_labels = ['0', '1', '2', '3']  

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if not idx:
        x = [0,  5, 6, 7]
        ax.plot(x, [0] + data[0][i], 'g-', label='baseline', marker='o')
        ax.plot(x, [0] + data[1][i], 'r-', label='no-time-idx', marker='*')
        ax.plot(x, [0] + data[2][i], 'b--', label='time-idx', marker='+')
    else:
        x = [0,  1, 2, 3, 4]
        ax.set_xlabel('Query Data Size(log)')
        ax.plot(x, [0] + data[i][0], 'g-', label='10^5', marker='o')
        ax.plot(x, [0] + data[i][1], 'r-', label='10^6', marker='*')
        ax.plot(x, [0] + data[i][2], 'b--', label='10^7', marker='+')
    # ax.set_xticks(x, group_labels)
    ax.legend(bbox_to_anchor=[0.5, 1]) 
    plt.subplots_adjust(left=0.05, right=0.98)
    

def one_line_chat(data, fn, title='', xlabel='Data Size(log)', ylabel='time(s)'):
    plt.style.use('./tickstyle')
    with plt.style.context(('./tickstyle')):
        fig, ax = plt.subplots()
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        x = [0, 5, 6, 7]
        ax.plot(x, [0] + data, 'b-', marker='o')
    plt.subplots_adjust(left=0.05, right=0.98)
    plt.savefig(fn, format=format_f)
        
    
def point_line(data, fn, idx=True):
    plt.style.use('./tickstyle')
    with plt.style.context(('./tickstyle')):
        fig, (ax1, ax2, ax3, ax4)  = plt.subplots(nrows=1, ncols=4, figsize=fig_s)
        autoline(data, ax1, title_q[0], 0, idx, ylabel='time(s)')
        autoline(data, ax2, title_q[1], 1, idx)
        autoline(data, ax3, title_q[2], 2, idx)
        autoline(data, ax4, title_q[3], 3, idx)
    # plt.show()
    plt.savefig(fn, format=format_f)
    

def handle_data_q(datas):
    datas = handle_data(datas, 4, 12)
    ret = []
    for data in datas:
        list_t = [data[i:i+4] for i in range(0, len(data), 4)]
        ret.append(list_t)

    return ret

if __name__ == '__main__':
    query_num = '../../latex/pic/query.' + format_f
    index = '../../latex/pic/index.' + format_f
    baseline = '../../latex/pic/baseline.' + format_f
    time = '../../latex/pic/time.' + format_f
    time_idx = '../../latex/pic/time_idx.' + format_f
    combine = '../../latex/pic/combine.'  + format_f

    ret_line = '../../result_data/ret_line'
    ret_matrix = '../../result_data/ret_matrix'
    ret_matrix_q = '../../result_data/ret_matrix_q'
    ret_matrix_no_index = '../../result_data/ret_matrix_no_index'

    # method1: baseline
    data = import_data(ret_line)
    data = handle_data(data, 4)
    barchar(data, baseline)
    print('baseline plot complete.')

    # method2: time
    data = import_data(ret_matrix)
    data = handle_data(data, 4)
    barchar(data, time)
    print('time no index plot complete.')

    # method3: time index
    data = import_data(ret_matrix_no_index)
    data = handle_data(data, 4)
    barchar(data, time_idx)
    print('time with index plot complete.')

    # method4: combine three methods 
    data1 = import_data(ret_line)
    data1 = handle_data(data1, 4)
    data2 = import_data(ret_matrix_no_index)
    data2 = handle_data(data2, 4)
    data3 = import_data(ret_matrix)
    data3 = handle_data(data3, 4)
    data = [data1, data2, data3]
    point_line(data, combine, False)
    print('combine plot complete.')

    data_q = import_data(ret_matrix_q)
    data_q = handle_data_q(data_q)
    point_line(data_q, query_num)
    print('Number of query data plot complete.')

    # index line bar
    data_idx = import_data(ret_matrix_q, 'run runtime')
    data_idx = data_idx[0::9]
    one_line_chat(data_idx, index)
    print('Index plot complete.')