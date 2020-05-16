import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


class Square:
    def __init__(self, amplitude=1, frequency=1):
        self.x = 0
        self.amplitude = amplitude
        self.frequency = frequency
        self.path = []

    def add_data(self):
        Path = mpath.Path
        self.path.append((Path.MOVETO, (self.x, 0)))
        self.path.append((Path.LINETO, (self.x, self.amplitude)))
        self.path.append((Path.LINETO, (self.x + self.frequency, self.amplitude)))
        self.path.append((Path.LINETO, (self.x + self.frequency, 0)))
        self.x = self.x + self.frequency
        self.amplitude *= -1;

    def plot(self):
        fig, ax = plt.subplots()
        codes, verts = zip(*self.path)
        path = mpath.Path(verts, codes)
        patch = mpatches.PathPatch(path, facecolor='g', alpha=0.5)
        ax.add_patch(patch)
        # plot control points and connecting lines
        x, y = zip(*path.vertices)
        line, = ax.plot(x, y, 'go-')

        ax.grid()
        ax.axis('equal')
        plt.show()
