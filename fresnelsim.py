from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons
from scipy.special import fresnel
from scipy import *

ax = subplot(111)
subplots_adjust(left=0.25, bottom=0.25)
s = linspace(-10,10,1000)
#I = (fresnel(s)[1]+0.5)**2+(fresnel(s)[0]+0.5)**2
C = fresnel(s)[1]
S = fresnel(s)[0]
l, = plot(C,S, lw=2, color='red')
axis([-1, 1, -1.5, 1.5])
g, = plot([-0.5,0.5],[-0.5,0.5], lw=2)
axs = axes([0.25, 0.1, 0.65, 0.03])

ss = Slider(axs, 's', -2.5, 2.5, valinit=-2.5)

rax = axes([0.7, 0.4, 0.15+0., 0.15+0.])
axis([-3.0,3.0,0.0,3.0])

def update(val):
    s = ss.val
    x=linspace(-2.5,s,1000)
    g.set_data([-0.5,fresnel(s)[1]],[-0.5,fresnel(s)[0]])
   # vec=ax.quiver(-0.5,-0.5,fresnel(s)[1]+0.5,fresnel(s)[0]+0.5,angles='xy',scale_units='xy',scale=1)
    cla()
    I = (fresnel(x)[1]+0.5)**2+(fresnel(x)[0]+0.5)**2
    cla()
    axis([-3.0,3.0,0.0,3.0])
    rax.plot(x,I,lw=2)

    draw()
ss.on_changed(update)

show()
#resetax = axes([0.8, 0.025, 0.1, 0.04])
#button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
#def reset(event):
#    sfreq.reset()
#    samp.reset()
#button.on_clicked(reset)

#radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
#def colorfunc(label):
#    l.set_color(label)
#    draw()
#radio.on_clicked(colorfunc)
