'''
#p6-1
tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原長"]
for i in tozai:
    for j in nanboku:
        cross = i+j
        print(cross)
'''
'''
#p6-2
tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原長"]
cross_table = [["","",""], ["","",""], ["","",""]]
for i in range(len(tozai)):
    for j in range(len(nanboku)):
        cross = tozai[i]+nanboku[j]
        cross_table[i][j] = cross
        print(cross)
'''
#p6-3
tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原長"]
cross_table = []
for i in range(len(tozai)):
    street = []
    for j in range(len(nanboku)):
        cross = tozai[i]+nanboku[j]
        street.append(cross)
        cross_table.append(street)
        print(street)