def prt_star():
    f=open('vishnu.txt','w+')
    f.write('PRT STAR\n--------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('* ')
        f.write('\n')
    f.close()
prt_star()

def prt_num_row():
    f=open('vishnu.txt','a+')
    f.write('PRT NUM ROW\n--------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i)+' ')
        f.write('\n')
    f.close()
prt_num_row()

def prt_num_col():
    f=open('vishnu.txt','a+')
    f.write('PRT NUM COL\n--------------\n')
    for i in range(1,7):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(k)+' ')
        f.write('\n')
    f.close()
prt_num_col()

def prt_upper_row():
    f=open('vishnu.txt','a+')
    f.write('PRT UPPER ROW\n--------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64)+' ')
        f.write('\n')
    f.close()
prt_upper_row()

def prt_upper_col():
    f=open('vishnu.txt','a+')
    f.write('PRT UPPER COL\n--------------\n')
    for i in range(0,7):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(chr(k+64)+' ')
        f.write('\n')
    f.close()
prt_upper_col()

def prt_lower_row():
    f=open('vishnu.txt','a+')
    f.write('PRT LOWER ROW\n--------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+96)+' ')
        f.write('\n')
    f.close()
prt_lower_row()

def prt_LOWER_col():
    f=open('vishnu.txt','a+')
    f.write('PRT LOWER COL\n--------------\n')
    for i in range(0,7):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(chr(k+96)+' ')
        f.write('\n')
    f.close()
prt_LOWER_col()

#IPRT

def iprt_star():
    f=open('vishnu.txt','w+')
    f.write('IPRT STAR\n--------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('* ')
        f.write('\n')
    f.close()
iprt_star()

def iprt_num_row():
    f=open('vishnu.txt','a+')
    f.write('IPRT NUM ROW\n--------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i)+' ')
        f.write('\n')
    f.close()
iprt_num_row()

def iprt_num_col():
    f=open('vishnu.txt','a+')
    f.write('IPRT NUM COL\n--------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(k)+' ')
        f.write('\n')
    f.close()
iprt_num_col()

def iprt_upper_row():
    f=open('vishnu.txt','a+')
    f.write('IPRT UPPER ROW\n--------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64)+' ')
        f.write('\n')
    f.close()
iprt_upper_row()


def iprt_upper_col():
    f=open('vishnu.txt','a+')
    f.write('IPRT UPPER COL\n--------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(chr(k+64)+' ')
        f.write('\n')
    f.close()
iprt_upper_col()

def iprt_lower_row():
    f=open('vishnu.txt','a+')
    f.write('IPRT LOWER ROW\n--------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+96)+' ')
        f.write('\n')
    f.close()
iprt_lower_row()


def iprt_lower_col():
    f=open('vishnu.txt','a+')
    f.write('IPRT lowER COL\n--------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(chr(k+96)+' ')
        f.write('\n')
    f.close()
iprt_lower_col()







