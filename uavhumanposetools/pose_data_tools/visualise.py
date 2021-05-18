import numpy as np
import matplotlib.pyplot as plt


def visualise(data, graph=None, is_3d=True):
    '''
    Visualise skeleton data using matplotlib
    
    Args:
        data: tensor of shape (B x C x V x T x M)
        graph: graph representation for skeleton
        is_3d: set true for 3d skeletons
    '''
    N, C, T, V, M = data.shape

    plt.ion()
    fig = plt.figure()
    if is_3d:
        from mpl_toolkits.mplot3d import Axes3D
        ax = fig.add_subplot(111, projection='3d')
    else:
        ax = fig.add_subplot(111)

    if graph is None:
        p_type = ['b.', 'g.', 'r.', 'c.', 'm.', 'y.', 'k.', 'k.', 'k.', 'k.']
        pose = [
            ax.plot(np.zeros(V), np.zeros(V), p_type[m])[0] for m in range(M)
        ]
        ax.axis([-1, 1, -1, 1])
        for t in range(T):
            for m in range(M):
                pose[m].set_xdata(data[0, 0, t, :, m])
                pose[m].set_ydata(data[0, 1, t, :, m])
            fig.canvas.draw()
            plt.pause(0.001)
    else:
        p_type = ['b-', 'g-', 'r-', 'c-', 'm-', 'y-', 'k-', 'k-', 'k-', 'k-']
        import sys
        from os import path
        sys.path.append(
            path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
        G = graph
        edge = G.inward
        pose = []
        for m in range(M):
            a = []
            for i in range(len(edge)):
                if is_3d:
                    a.append(ax.plot(np.zeros(3), np.zeros(3), p_type[m])[0])
                else:
                    a.append(ax.plot(np.zeros(2), np.zeros(2), p_type[m])[0])
            pose.append(a)
        ax.axis([-100, 100, -100, 100])
        if is_3d:
            ax.set_zlim3d(-100, 100)
        for t in range(T):
            for m in range(M):
                for i, (v1, v2) in enumerate(edge):
                    x1 = data[0, :2, t, v1, m]
                    x2 = data[0, :2, t, v2, m]
                    if (x1.sum() != 0 and x2.sum() != 0) or v1 == 1 or v2 == 1:
                        pose[m][i].set_xdata(data[0, 0, t, [v1, v2], m])
                        pose[m][i].set_ydata(data[0, 1, t, [v1, v2], m])
                        if is_3d:
                            pose[m][i].set_3d_properties(data[0, 2, t, [v1, v2], m])
            fig.canvas.draw()
            plt.pause(0.01)
