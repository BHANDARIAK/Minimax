## Starting Writing MinMax Code!!!

rows = 'ABCDEFGHI'
cols = '123456789'
fullstring = '123456789'

def cross (a,b):
    return [s+t for s in a for t in b]

boxes = cross(rows,cols)


row_units = [cross (r,cols) for r in rows ]
column_units = [cross (rows, c) for c in cols]
square_units = [cross(rs,cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123','456','789')]


##print row_units
##print column_units
##print square_units

unitlist = row_units + column_units + square_units

#print unitlist


def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return


def grid_values (grid):
    puzzle = {}
    #print boxes
    x=0
    while x  < len(boxes):
        #print len(boxes)
        #print boxes [x]
        #print puzzleasstring[x]
            puzzle.update({boxes [x] : grid[x]})
            if puzzle[boxes[x]] == '.':
                puzzle.update({boxes[x]: fullstring})
            x=x+1
    return puzzle


def eliminate_singluar_peers(modgrid):
    unitlist = row_units + column_units + square_units
    units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
    peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
    display(units)
    



##    print(units);
    
      
    for value in peers.keys():
        if len(peers[value]) == 1:
            #print(peers[value])
            modgrid.update({value : peerreplace(peers, value)})

    return modgrid
    #x=0
    #while x  < 81:
    #    if len(modgrid[boxes[x]]) == 1:
            #print grid[boxes[x]]
            #print grid[boxes[x-1]]
    #        modgrid.update({boxes[x-1]: peerreplace(modgrid[boxes[x-1]], modgrid[boxes[x]])})
    #        modgrid.update({boxes[x+1]: peerreplace(modgrid[boxes[x+1]], modgrid[boxes[x]])})
    #    x=x+1

