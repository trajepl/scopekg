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

def autoax(ax, title, data):
    print(data)
    rects1 = ax.bar(ind, data, width, color='lightblue')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Time/s')
    ax.set_xlabel('Data/log')
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
    autoax(ax1, 'HT', data[0])
    autoax(ax2, 'REL', data[1])
    autoax(ax3, 'HR', data[2])
    autoax(ax4, 'HRT', data[3])
    # autolabel(rects1)
    # autolabel(rects2)

    plt.show()

if __name__ == '__main__':
    data = import_data('../../result_data/ret_matrix')
    data = handle_data(data, 4)
    barchar(data)