fileIP = open( "100.in", "r" )
fileOP = open( "100.out", "w" )

cases = int( fileIP.readline() )
dif1 = 0
dif2 = 0
dif = 0

# print cases

while cases > 0 :
    inputCount =  int( fileIP.readline() )
    inp = map( int, fileIP.readline().split() )
    # print inp

    dif1 = inp[1] - inp[0]
    dif2 = inp[2] - inp[1]

    if dif1 == dif2:
        dif = dif1
        num = inp[2]
        j = 3
        while j < inputCount:
            num = num + dif
            if ( num != inp[j] ):
                print inp[j]
                fileOP.write( str( inp[j] ) + "\n" )
                break
            j += 1

    else:
        if ( dif1 ==  inp[3] - inp[2] ):
            print inp[2]
            fileOP.write( str( inp[2] ) + "\n" )
        elif ( dif2 == inp[3] - inp[2] ):
            print inp[0]
            fileOP.write( str( inp[0] ) + "\n" )
        else:
            print inp[1]
            fileOP.write( str( inp[1] ) + "\n" )

    dif1 = 0
    dif2 = 0
    dif = 0

    cases -= 1

fileIP.close()
fileOP.close()