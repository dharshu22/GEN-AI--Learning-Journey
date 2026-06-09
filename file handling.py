def rat_star():
    f=open('dharshu.txt','w+')
    f.write('RAT STAR\n---------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
rat_star()

def rat_num_row():
    f=open('dharshu.txt','a+')
    f.write('RAT NUM ROW\n---------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
rat_num_row()

def rat_num_col():
    f=open('dharshu.txt','a+')
    f.write('RAT NUM COL\n---------------\n')
    for i in range(1,7):
        for j in range(1,i):
            f.write(str(j))
        f.write('\n')
    f.close()
rat_num_col()

def rat_lower_row():
    f=open('dharshu.txt','a+')
    f.write('RAT LOWER ROW\n---------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(chr(i+96))
            #f.write(str(i))
        f.write('\n')
    f.close()
rat_lower_row()

def rat_lower_col():
    f=open('dharshu.txt','a+')
    f.write('RAT LOWER COL\n---------------\n')
    for i in range(1,6):
        for j in range(1,i):
            f.write(chr(j+96))
            #f.write(str(i))
        f.write('\n')
    f.close()
rat_lower_col()

def rat_upper_row():
    f=open('dharshu.txt','a+')
    f.write('RAT UPPER ROW\n---------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(chr(i+64))
            #f.write(str(i))
        f.write('\n')
    f.close()
rat_upper_row()

def rat_upper_col():
    f=open('dharshu.txt','a+')
    f.write('RAT UPPER COL\n---------------\n')
    for i in range(1,7):
        for j in range(1,i):
            f.write(chr(j+64))
            #f.write(str(i))
        f.write('\n')
    f.close()
rat_upper_col()

def rat_name_row():
    name='priya'
    f=open('dharshu.txt','a+')
    f.write('RAT NAME ROW\n--------------\n')
    for i in range(len(name)):
        for j in range(i+1):
            f.write(name[i])
        f.write('\n')
    f.close()
rat_name_row()

def rat_name_col():
    name='priya'
    f=open('dharshu.txt','a+')
    f.write('RAT NAME COL\n-----------------\n')
    for i in range(len(name)):
        for j in range(i+1):
            f.write(name[j])
        f.write('\n')
    f.close()
rat_name_col()

## IRAT:

def irat_star():
    f=open('dharshu.txt','a+')
    f.write('IRAT STAR\n---------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
irat_star()

def irat_num_row():
    f=open('dharshu.txt','a+')
    f.write('IRAT NUM ROW\n---------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
irat_num_row()

def irat_num_col():
    f=open('dharshu.txt','a+')
    f.write('IRAT NUM COL\n---------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(str(j))
        f.write('\n')
    f.close()
irat_num_col()

def irat_lower_row():
    f=open('dharshu.txt','a+')
    f.write('IRAT LOWER ROW\n---------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(chr(i+96))
            #f.write(str(i))
        f.write('\n')
    f.close()
irat_lower_row()

def irat_lower_col():
    f=open('dharshu.txt','a+')
    f.write('IRAT LOWER COL\n---------------\n')
    for i in range(6,0,-1):
        for j in range(1,i):
            f.write(chr(j+96))
            #f.write(str(i))
        f.write('\n')
    f.close()
irat_lower_col()

def irat_upper_row():
    f=open('dharshu.txt','a+')
    f.write('IRAT UPPER ROW\n---------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(chr(i+64))
            #f.write(str(i))
        f.write('\n')
    f.close()
irat_upper_row()

def irat_upper_col():
    f=open('dharshu.txt','a+')
    f.write('IRAT UPPER COL\n---------------\n')
    for i in range(6,0,-1):
        for j in range(1,i):
            f.write(chr(j+64))
            #f.write(str(i))
        f.write('\n')
    f.close()
irat_upper_col()

def irat_name_row():
    name='priya'
    f=open('dharshu.txt','a+')
    f.write('IRAT NAME ROW\n--------------\n')
    for i in range(4,-1,-1):
        for j in range(0,i+1):
            f.write(name[i])
        f.write('\n')
    f.close()
irat_name_row()

def irat_name_col():
    name='priya'
    f=open('dharshu.txt','a+')
    f.write('IRAT NAME COL\n-----------------\n')
    for i in range(4,-1,-1):
        for j in range(0,i+1):
            f.write(name[j])
        f.write('\n')
    f.close()
irat_name_col()



