import numpy as np
import matplotlib.pyplot as plt

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

def import_data(fn):
    ret = []
    with open(fn,  'r') as data_out:
        tmp_l = list()           
        for line in data_out.readlines():
            if 'query' in line:
                time = line.strip().split(':')[-1]
                time = float(time.strip())
                ret.append(time)
    return ret

def handle_data(data, step):
    ret = []
    for i in range(len(data)):
        if len(data) > i + step + step:
            ret.append(data[i::step])
    return ret

def autoax(ax, title, data, labelx=''):
    print(data)
    rects1 = ax.bar(ind, data, width, align='edge', color='green')

    # add some text for labels, title and axes ticks
    ax.set_ylabel(labelx)
    ax.set_xlabel('Data(log)')
    ax.set_title(title)
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(('1', '2', '3'))

def autolabel(ax, rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

def barchar(data):
    fig, (ax1, ax2, ax3, ax4)  = plt.subplots(nrows=1, ncols=4, figsize=(18,4))
    autoax(ax1, 'HT', data[0], 'time(s)')
    autoax(ax2, 'REL', data[1])
    autoax(ax3, 'HR', data[2])
    autoax(ax4, 'HRT', data[3])
    # autolabel(rects1)
    # autolabel(rects2)

    plt.show()

def autoline(data, ax, title, i):
    x = [0, 1, 2, 3]
    y = data
    print(y)
    group_labels = ['0', '1', '2', '3']  

    ax.set_title(title)
    ax.set_xlabel('Data size(log)')
    ax.set_ylabel('Time(x)')
    ax.plot(x, [0] + data[0][i], 'g-', label='baseline', marker='o')
    ax.plot(x, [0] + data[1][i], 'r-', label='no-time-idx', marker='*')
    ax.plot(x, [0] + data[2][i], 'b--', label='time-idx', marker='+')
    ax.set_xticks(x, group_labels)
    ax.legend(bbox_to_anchor=[0.5, 1]) 
    
    

def point_line(data):
    fig, (ax1, ax2, ax3, ax4)  = plt.subplots(nrows=1, ncols=4, figsize=(18,4))
    autoline(data, ax1, 'HT', 0)
    autoline(data, ax2, 'REL', 1)
    autoline(data, ax3, 'HR', 2)
    autoline(data, ax4, 'HRT', 3)
    plt.show()
    


if __name__ == '__main__':
    data = import_data('../../result_data/ret_line')
    data = handle_data(data, 4)
    barchar(data)

    data = import_data('../../result_data/ret_matrix')
    data = handle_data(data, 4)
    barchar(data)

    data = import_data('../../result_data/ret_matrix_no_index')
    data = handle_data(data, 4)
    barchar(data)

    data1 = import_data('../../result_data/ret_line')
    data1 = handle_data(data1, 4)
    data2 = import_data('../../result_data/ret_matrix_no_index')
    data2 = handle_data(data2, 4)
    data3 = import_data('../../result_data/ret_matrix')
    data3 = handle_data(data3, 4)
    data = [data1, data2, data3]
    point_line(data)