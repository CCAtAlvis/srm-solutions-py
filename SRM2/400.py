fileIP = open( "400.in", "r" )
fileOP = open( "400.out", "w" )

cases = int( fileIP.readline() )

# print cases

while cases > 0:
    inputCount =  int( fileIP.readline() )
    inp = [[0]*inputCount for i in xrange( inputCount )]

    # print inputCount

    i = 0
    while i < inputCount:
        j = 0
        while j < inputCount:
            ch = fileIP.read(1)
            # print ch
            if ch == '#' or ch == '.':
                inp[i][j] = ch
                j += 1
        i += 1
    # print inp
    # print "\n"
    fileIP.readline()

# the main code
    # j:rows
    # print inp
    for j in xrange( inputCount ):
        # first and most important condition
        # if any of diagonal most elements are '.' then break right away
        if "." == inp[0][ inputCount-1 ] or "." ==  inp[ inputCount-1 ][0]:
            inp[ inputCount-1 ][0] = "."
            break

        # k:colms
        for k in xrange( inputCount ):
            # first condition
            # if the element is '.' then skip is right away
            if "." == inp[j][k]:
                continue

            # is first (zeroth) row
            if 0 == j:
                # check elements only to the right

                # is last colm
                if inputCount-1 == k:
                    # check only the top element
                    # but here nothing to check
                    # its the top most element
                    pass
                else:
                    # check all elements i.e to top, right and top-right
                    # but with above constrains, check only the right elements
                    if "." == inp[j][ k+1 ]:
                        inp[j][k] = "."

            else:
                # check all elements i.e to top, right and top-right
                if inputCount-1 == k:        
                    # check only the top element
                    if "." == inp[ j-1 ][k]:
                        inp[j][k] = "."
                else:
                    # check all elements i.e to top, right and top-right
                    if "." == inp[j][ k+1 ] and "." == inp[ j-1 ][k] and "." == inp[ j-1 ][ k+1 ]:            
                        inp[j][k] = "."

    if "." == inp[ inputCount-1 ][0]:
        print "NO"
        fileOP.write("NO\n")
    elif "#" == inp[ inputCount-1 ][0]:
        print "YES"
        fileOP.write("YES\n")

    cases -= 1

fileIP.close()
fileOP.close()