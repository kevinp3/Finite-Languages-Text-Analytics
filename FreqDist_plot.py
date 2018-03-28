#Define plot to be used for Frequency Distribution
def plot_freqdist_freq(fd, max_num=None, cumulative=False, title='Frequency plot', linewidth=2):
        tmp = fd.copy()
        norm = fd.N()
        for key in tmp.keys():
                tmp[key] = float(fd[key]) / norm * 100

        if max_num:
                tmp.plot(max_num, cumulative=cumulative,
                        title=title, linewidth=linewidth)
        else:
                tmp.plot(cumulative=cumulative, 
                        title=title, 
                        linewidth=linewidth)

        return
