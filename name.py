# print name
for row in range(7):
    for column in range(35):
        if column==0 or (column==3 and (row==0 or row==1 or row==2)) or (column==6) or (column==10 and (row!=0 and row!=3)) or (column==12 and (row!=0)) or (column==16 and (row!=0)) or (row==0 and (column>0 and column<3)) or (row==0 and (column>6 and column<10)) or (row==2 and (column>0 and column<3)) or (row==3 and (column>6 and column<10)) or (row==0 and (column>12 and column<16)) or (row==3 and (column>12 and column<16)) or (column==20 and (row!=0)) or (row==0 and (column>17 and column<23)) or (column==26 and (row!=0 and row!=6)) or (row==0 and (column>23 and column<29)) or (row==6 and (column>23 and column<29)) or (column==30) or (row==3 and(column==31)) or (column==32 and (row==2 or row==4)) or (column==33 and (row==1 or row==5)) or (column==34 and (row==0 or row==6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
