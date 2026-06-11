def lat_star():
    f=open('priya.txt','w+')
    f.write('LAT STAR\n------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
lat_star()

def lat_num_row():
    f=open('priya.txt','a+')
    f.write('LAT NUM ROW\n------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
lat_num_row()

def lat_num_col():
    f=open('priya.txt','a+')
    f.write('LAT NUM COL\n------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(k))
        f.write('\n')
    f.close()
lat_num_col()

def lat_upper_row():
    f=open('priya.txt','a+')
    f.write('LAT UPPER ROW\n------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(chr(i+64)))
        f.write('\n')
    f.close()
lat_upper_row()

def lat_upper_col():
    f=open('priya.txt','a+')
    f.write('LAT UPPER COL\n------------\n')
    for i in range(1,7):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(chr(k+64)))
        f.write('\n')
    f.close()
lat_upper_col()

def lat_lower_row():
    f=open('priya.txt','a+')
    f.write('LAT LOWER ROW\n------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(chr(i+96)))
        f.write('\n')
    f.close()
lat_lower_row()

def lat_lower_col():
    f=open('priya.txt','a+')
    f.write('LAT LOWER COL\n------------\n')
    for i in range(1,7):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(chr(k+96)))
        f.write('\n')
    f.close()
lat_lower_col()

def lat_nam_row():
    name='vishnu'
    f=open('priya.txt','a+')
    f.write('LAT NAM ROW\n------------\n')
    for i in range(len(name)):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i+1):
            f.write(name[i])
        f.write('\n')
    f.close()
lat_nam_row()

def lat_nam_col():
    name='vishnu'
    f=open('priya.txt','a+')
    f.write('LAT NAM COL\n------------\n')
    for i in range(len(name)):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i+1):
            f.write(name[k])
        f.write('\n')
    f.close()
lat_nam_col()


#ILAT

def ilat_star():
    f=open('priya.txt','a+')
    f.write('ILAT STAR\n--------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
ilat_star()

def ilat_num_row():
    f=open('priya.txt','a+')
    f.write('ILAT NUM ROW\n------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
ilat_num_row()

def ilat_num_col():
    f=open('priya.txt','a+')
    f.write('ILAT NUM COL\n------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(k))
        f.write('\n')
    f.close()
ilat_num_col()

def ilat_upper_row():
    f=open('priya.txt','a+')
    f.write('ILAT UPPER ROW\n------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(chr(i+64)))
        f.write('\n')
    f.close()
ilat_upper_row()

def ilat_upper_col():
    f=open('priya.txt','a+')
    f.write('ILAT UPPER COL\n------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(chr(k+64)))
        f.write('\n')
    f.close()
ilat_upper_col()

def ilat_lower_row():
    f=open('priya.txt','a+')
    f.write('ILAT LOWER ROW\n------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(chr(i+96)))
        f.write('\n')
    f.close()
ilat_lower_row()

def ilat_LOWER_col():
    f=open('priya.txt','a+')
    f.write('ILAT LOWER COL\n------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(chr(k+96)))
        f.write('\n')
    f.close()
ilat_LOWER_col()



