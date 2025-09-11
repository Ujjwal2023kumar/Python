# -------------------------------------------
# Imports (core and optional modules for plotting)
# -------------------------------------------
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt        # state-machine (MATLAB-like) API
from matplotlib.figure import Figure   # object-oriented Figure
from matplotlib.axes import Axes       # object-oriented Axes (rarely imported directly)
from mpl_toolkits.mplot3d import Axes3D  # registers 3D projection
from matplotlib.ticker import FuncFormatter, MaxNLocator, MultipleLocator
import matplotlib.gridspec as gridspec
from matplotlib.cm import ScalarMappable
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, CheckButtons, RadioButtons
from matplotlib.colors import LogNorm, Normalize


# -------------------------------------------
# Basic pyplot figure and axes (state-machine style)
# -------------------------------------------
plt.figure(figsize=(6,4))      # create figure
plt.plot([1,2,3],[4,5,6])      # plot to current axes
plt.title("Title")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# -------------------------------------------
# Object-oriented plotting with Figure & Axes
# -------------------------------------------
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, label='line')
ax.set_title("Title")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
fig.tight_layout()
plt.show()


# -------------------------------------------
# Ways to create subplots and axes
# -------------------------------------------
plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False)
plt.figure(), fig.add_subplot(), fig.add_axes([0.1,0.1,0.8,0.8])
plt.gcf(), plt.gca()   # get current figure/axes


# -------------------------------------------
# Common plotting methods
# -------------------------------------------
ax.plot(x, y, color='C0', linestyle='-', linewidth=2, marker='o', markersize=6, label='data')
ax.scatter(x, y, s=50, c=y, cmap='viridis', marker='o', alpha=0.8)
ax.bar(['A','B','C'], [5,7,3], width=0.6, color='tab:blue', edgecolor='k')
ax.barh([0,1,2], [3,6,2])
ax.hist(np.random.randn(1000), bins=30)
ax.boxplot([np.random.randn(50), np.random.randn(50)], notch=True, vert=True, patch_artist=True)
ax.violinplot([np.random.randn(50), np.random.randn(50)], showmeans=False, showmedians=True)
ax.errorbar(x, y, yerr=0.2, fmt='o-', capsize=3)
ax.pie([30,40,30], labels=['A','B','C'], autopct='%1.1f%%', startangle=90, explode=[0,0.1,0])
ax.axis('equal')  # make pie circular


# -------------------------------------------
# Images and colorbars
# -------------------------------------------
image_array = np.random.rand(10,10)
im = ax.imshow(image_array, cmap='gray', interpolation='nearest', origin='upper', vmin=0, vmax=1)
fig.colorbar(im, ax=ax, orientation='vertical')


# -------------------------------------------
# Contour plots
# -------------------------------------------
X, Y = np.meshgrid(np.linspace(-3,3,100), np.linspace(-3,3,100))
Z = np.sin(X**2+Y**2)
CS = ax.contour(X, Y, Z, levels=10, cmap='viridis')
ax.clabel(CS)
cf = ax.contourf(X, Y, Z)
pcm = ax.pcolormesh(X, Y, Z)
fig.colorbar(pcm, ax=ax)


# -------------------------------------------
# Special plot types
# -------------------------------------------
ax.stackplot(x, np.sin(x), np.cos(x), labels=['sin','cos'])
ax.step(x, y, where='mid')
ax.stem(x[:10], y[:10])
ax.set_xscale('log')
ax.set_yscale('log')
ax.semilogy(x, y)
ax.loglog(x, y)


# -------------------------------------------
# Titles, labels, legends, annotations
# -------------------------------------------
ax.set_title("Title", fontsize=14, pad=10)
ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.legend(loc='best', ncol=1, frameon=True, fontsize='small')
ax.text(0.1, 0.9, "Some text", transform=ax.transAxes)
ax.annotate("peak", xy=(3, np.sin(3)), xytext=(4,1),
            arrowprops=dict(arrowstyle='->', color='black'))


# -------------------------------------------
# Axis limits, ticks, grids, spines
# -------------------------------------------
ax.set_xlim(0,10)
ax.set_ylim(-1,1)
ax.set_xticks([0,2,4,6,8,10])
ax.set_xticklabels(['a','b','c','d','e','f'], rotation=45, fontsize=10)
ax.tick_params(axis='x', which='major', labelsize=10, direction='out', length=6)
ax.xaxis.set_major_locator(MaxNLocator(5))
ax.xaxis.set_major_formatter(FuncFormatter(lambda val, pos: f"{val:.2f}"))
ax.grid(True, which='major', linestyle='--', alpha=0.7)
ax.minorticks_on()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


# -------------------------------------------
# Multiple subplots and layout
# -------------------------------------------
fig, axes = plt.subplots(2,2, figsize=(8,6))
fig.tight_layout(pad=1.0)
plt.subplots_adjust(left=0.1, right=0.9, hspace=0.4, wspace=0.4)
gs = gridspec.GridSpec(3,3)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1:, 0])


# -------------------------------------------
# Styles and rcParams
# -------------------------------------------
plt.style.use('default')  # other: 'ggplot','bmh','seaborn'
mpl.rcParams['figure.figsize'] = (6,4)
mpl.rcParams['font.size'] = 12
mpl.rcParams.update({'lines.linewidth':2})
with mpl.rc_context({'lines.linewidth':1}):
    plt.plot(x,y)


# -------------------------------------------
# Colors and colormaps
# -------------------------------------------
ax.plot(x, y, color='tab:blue')
ax.plot(x, y, color='#FF00AA')      # hex
ax.plot(x, y, color=(0.1,0.2,0.5))  # RGB tuple
plt.cm.get_cmap('viridis')(0.5)
sm = ScalarMappable(cmap='viridis', norm=mpl.colors.Normalize(vmin=0, vmax=1))
fig.colorbar(sm, ax=ax)


# -------------------------------------------
# Saving figures
# -------------------------------------------
fig.savefig('figure.png', dpi=300, bbox_inches='tight', transparent=False, facecolor='white')


# -------------------------------------------
# Adding text over images
# -------------------------------------------
matrix = np.random.rand(5,5)
ax.imshow(matrix, cmap='viridis')
for (i,j), val in np.ndenumerate(matrix):
    ax.text(j, i, f"{val:.1f}", ha='center', va='center')


# -------------------------------------------
# Polar, vector fields, streamplots
# -------------------------------------------
theta = np.linspace(0,2*np.pi,100)
r = 1+np.sin(theta)
ax = plt.subplot(projection='polar')
ax.plot(theta, r)
X, Y = np.meshgrid(np.linspace(-2,2,20), np.linspace(-2,2,20))
U, V = -Y, X
ax = plt.subplot()
ax.quiver(X, Y, U, V, scale=50)
ax.streamplot(X, Y, U, V, density=1.0, color=np.sqrt(U**2+V**2), cmap='plasma')


# -------------------------------------------
# 3D plots
# -------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs, ys = np.linspace(-5,5,100), np.linspace(-5,5,100)
zs = np.sin(xs)
ax.plot3D(xs, zs, zs)
ax.scatter3D(xs, ys, zs, c=zs, cmap='viridis')
X, Y = np.meshgrid(xs, ys)
Z = np.sin(X**2+Y**2)
ax.plot_surface(X, Y, Z, cmap='coolwarm')


# -------------------------------------------
# Animation example
# -------------------------------------------
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
def init():
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1,1)
    line.set_data([], [])
    return line,

def update(frame):
    x = np.linspace(0, 2*np.pi, 200)
    y = np.sin(x + 0.1*frame)
    line.set_data(x,y)
    return line,

ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=20)
ani.save('sine_wave.mp4', fps=30, dpi=200)


# -------------------------------------------
# Event handling (mouse clicks, picking)
# -------------------------------------------
def on_click(event):
    print("Mouse button:", event.button, "at", event.xdata, event.ydata)
cid = fig.canvas.mpl_connect('button_press_event', on_click)

line.set_picker(5)  # tolerance in points
def on_pick(event):
    print("Picked:", event.artist)
fig.canvas.mpl_connect('pick_event', on_pick)


# -------------------------------------------
# Interactive widgets (Slider example)
# -------------------------------------------
axcolor = 'lightgoldenrodyellow'
axamp = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=1)

def update(val):
    line.set_ydata(val*np.sin(x))
    fig.canvas.draw_idle()

samp.on_changed(update)


# -------------------------------------------
# LogNorm with color normalization
# -------------------------------------------
pcm = ax.pcolormesh(X, Y, Z, norm=LogNorm(vmin=Z.min()+1e-6, vmax=Z.max()), cmap='viridis')


# -------------------------------------------
# Mixed plot example: line + fill + hist
# -------------------------------------------
x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = np.cos(x)*0.8
fig, axs = plt.subplots(2,1, figsize=(8,6), sharex=True)
axs[0].plot(x, y1, label='sin', marker='o', markevery=20)
axs[0].plot(x, y2, label='0.8 cos', linestyle='--')
axs[0].fill_between(x, y1, y2, where=(y1>y2), alpha=0.2)
axs[0].legend(); axs[0].grid(True)
axs[0].set_title('Line, fill_between, legend')
axs[1].hist(np.random.randn(1000), bins=30)
axs[1].set_title('Histogram')
fig.tight_layout()
plt.savefig('example.png', dpi=150)
plt.show()
