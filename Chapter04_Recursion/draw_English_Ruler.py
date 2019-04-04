def draw_Line(tick_length,tick_label=''):
    """
    Draw one line with given tick length (followed by optional label).
    """
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print (line)
    
def draw_Interval(central_length):
    """
    Draw tick interval based upon a central tick length
    """
    if central_length > 0:                   # stop when length drops to 0
        draw_Interval(central_length-1)      # recursively draw top ticks
        draw_Line(central_length)            # draw center tick
        draw_Interval(central_length-1)      # recursively draw bottom ticks
        
def draw_Euler(num_inches,major_length):
    """
    Draw English ruler with given number of inches, major tick length
    """
    draw_Line(major_length,'O')              # draw inch 0 line
    for j in range(1,1+num_inches):
        draw_Interval(major_length-1)        # draw interior ticks for inch
        draw_Line(major_length,str(j))       # draw inch j line and label
        
        
#Code Fragment 4.2: A recursive implementation of a function that draws a ruler