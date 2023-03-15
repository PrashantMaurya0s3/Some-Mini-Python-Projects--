lis = [[1,2,3],[4,5,6],[7],[8,9]]
flatlist = [ element for innerList in lis for element in innerList]
print('List',lis)
print('Flat List :',flatlist)