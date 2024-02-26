1   def minimum(vals):
2       mini = vals[0]
3       for val in vals[1:]:
4           if val < mini: mini = val
5       return mini