# -*- coding: utf-8 -*-

import numpy as np

def axisFmtDollarsMillions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fM' % (x*1e-6)

def axisFmtDollarsThousands(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fK' % (x*1e-3)

def axisFmtThousands(x, pos):
    'The two args are the value and tick position'
    return '%1.2fK' % (x*1e-3)    

def ecdfPlot(ax,x,y,x_axis_units=None,y_axis_units=None,perc=None,**kwargs):
    '''
    Return a plot axes object ecdf data plotted
    Parameters:
            ax: Axes object
            x: 
            y:
            perc: a list of percentages of percentile to graph. Format .#f
    
    '''
    ax.plot(x,y,marker='.',ls='None')
    if not perc is None:
        for per in perc:
            val = np.percentile(x,per*100)
            ax.hlines(y=per,xmin= 0,xmax=val,color='red',alpha=.5)
            ax.vlines(x=val,ymin= 0,ymax=per,color='red',alpha=.5)
            
            ax.annotate(
                    s='{:.0f}% of {:} had less\nthan {:,.0f} {:}'.format(per*100, x_axis_units, val, y_axis_units),
                    xy=(val*1.1,per-.1),
                    color='#ff3333',
                    alpha=.85
                    )   

def text_box(ax, s, position = 'middle', color='#000000'):
          
    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height 
    
    positions = {
        'middle':{
                'horizontalalignment':'center',
                'verticalalignment':'center',
                'x':0.5*(left+right),
                'y':0.5*(bottom+top),
                }        

    }
        
    p = positions[position]
    
    ax.text(x=p['x'], y=p['y'], s=s,
            horizontalalignment=p['horizontalalignment'],
            verticalalignment=p['verticalalignment'],
            fontsize=20, color=color,
            transform=ax.transAxes)
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    return ax

def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.