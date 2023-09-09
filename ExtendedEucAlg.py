def ExtendedEucAlg(a,b):
    
    """Modified GCD Function"""
    s = [a,b] # the list contains a,b and all remainders
    q = [] # the contains all quotients

    while s[-1] > 0:
        quo = s[-2] // s[-1]
        rem = s[-2] % s[-1]

        s += [rem]
        q += [quo]



    """Table Method"""
    # Step 1: create table

    row_1 = [0,1]
    row_2 = [1,0]

    # Step 2: fill the table

    for i in q:
        row_1.append(i*row_1[-1]+row_1[-2])
        row_2.append(i*row_2[-1]+row_2[-2])

    # Step 3: determine positive and negative v and u

    if q[-2] // 2 == 0: # if the 2nd to last row is even # quotient, then -v and u
        v = (-1) * row_1[-2]
        u = row_2[-2]
    
    else: # odd # quotient, then v and -u
        v = row_1[-2]
        u = (-1) * row_2[-2]

    
    #Test
    """
    print('a: ', a)
    print('b: ', b)
    print('v: ', v)
    print('u: ', u)
    print('au + bv = ', a*u + b*v) 
    """

    return q # Return the list of all quotients 

print(ExtendedEucAlg(838222375530069915492642196190885036047883190728079417794092457259839019813001503512115583750669531327,303161543779443155549396275568937917645581190482587926550743982097205250817215142071462212547531051703))
