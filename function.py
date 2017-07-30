from utils import *

puzzleasstring = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
sudokupuzzle = grid_values(puzzleasstring)
#display(sudokupuzzle)
modsudokupuzzle = eliminate_singluar_peers(sudokupuzzle)    
print('*********************************************************************************************************************************************')
print('*********************************************************************************************************************************************')  
#display(modsudokupuzzle)
   
    


#print len(puzzle)
#print puzzle
    

##def grid_values (puzzle):
##   return []


##row_units = [cross (r,cols) for r in rows ]
##column_units = [cross (rows, c) for c in cols]
##square_units = [cross(rs,cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123','456','789')]

##print row_units
##print column_units
##print square_units

##unitlist = row_units + column_units + square_units

##print unitlist
