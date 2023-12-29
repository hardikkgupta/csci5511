import sat_interface

def tt2():
    # print("-------------------------")
    ttprob = sat_interface.KB(["~A C",
                               "~A A",
                               "~C ~A A",
                               "~B ~C",
                               "C B",
                               "~C B ~A",
                               "C ~B",
                               "A C"])
    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append(False)
        # print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append(True)
        # print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append(False)
        # print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append(True)
        # print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append(False)
        # print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append(True)
    #     print("Cal is a truth-teller")
    return tuple(entailed)

def tt3():
    '''
    Example of how to interact with sat_interface module

    Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller

    return a list containing all entailed propositions or negated propositions
    '''
    ttprob = sat_interface.KB(["~A ~C",
                               "C A",
                               "~B A",
                               "~B C",
                               "~A ~C B",
                               "~C B",
                               "~B C"])

    entailed = []
    if ttprob.test_literal("Amy is a liar") == False:
        entailed.append(False)
        # print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append(True)
        # print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append(False)
        # print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append(True)
        # print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append(False)
        # print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append(True)
        # print("Cal is a truth-teller")

    return tuple(entailed)

def salt():
    '''
    Example of how to interact with sat_interface module

    Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller

    return a list containing all entailed propositions or negated propositions
    '''
    # print("-------------------------")
    ttprob = sat_interface.KB(["D E F",
                               "~D ~E ~F",
                               "C A B",
                               "~C ~A",
                               "~B ~C",
                               "~D B",
                               "~B D",
                               "~E B",
                               "~B E",
                               "~F ~C",
                               "C F",
                               "~B ~A",
                               "~B ~C",
                               "A B C"])
    entailed = {}
    if ttprob.test_literal("A") == False:
        entailed["Caterpillar stole the salt"] = False
        #  entailed.append(False)
        # print("Caterpillar did not steal the salt")
    if ttprob.test_literal("~A") == False:
        entailed["Caterpillar stole the salt"] = True
        # entailed.append(True)
        # print("Caterpillar stole the salt")
    if ttprob.test_literal("B") == False:
        entailed["Bill the Lizard stole the salt"] = False
        #  entailed.append(False)
        # print("Bill the Lizard did not steal the salt")
    if ttprob.test_literal("~B") == False:
        entailed["Bill the Lizard stole the salt"] = True
        #  entailed.append(True)
        # print("Bill the Lizard stole the salt")
    if ttprob.test_literal("C") == False:
        entailed["Cheshire Cat stole the salt"] = False
        # entailed.append(False)
        # print("Cheshire Cat did not steal the salt")
    if ttprob.test_literal("~C") == False:
        entailed["Cheshire Cat stole the salt"] = True
        # entailed.append(True)
        # print("Cheshire Cat stole the salt")
    if ttprob.test_literal("D") == False:
        entailed["Caterpillar is Truthful"] = False
        # entailed.append(False)
        # print("Caterpillar is a liar")
    if ttprob.test_literal("~D") == False:
        entailed["Caterpillar is Truthful"] = True
        # entailed.append(True)
        # print("Caterpillar is a truth-teller")
    if ttprob.test_literal("E") == False:
        entailed["Bill the Lizard is Truthful"] = False
        # entailed.append(False)
        # print("Bill the Lizard is a liar")
    if ttprob.test_literal("~E") == False:
        entailed["Bill the Lizard is Truthful"] = True
        #  entailed.append(True)
        # print("Bill the Lizard is a truth-teller")
    if ttprob.test_literal("F") == False:
        entailed["Cheshire Cat is Truthful"] = False
        #  entailed.append(False)
        # print("Cheshire Cat is a liar")
    if ttprob.test_literal("~F") == False:
        entailed["Cheshire Cat is Truthful"] = True
        # entailed.append(True)
        # print("Cheshire Cat is a truth-teller")
    return entailed

def golf():
    '''
    Example of how to interact with sat_interface module

    Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller

    return a list containing all entailed propositions or negated propositions
    '''
    # print("-------------------------")
    ttprob = sat_interface.KB(["T",
                               "~H",
                               "~T1 ~T H2",
                               "~T1 T ~H2",
                               "~D1 ~D H2",
                               "~D1 D ~H2",
                               "~H1 ~H H2",
                               "~H1 H ~H2",
                               "~T2 ~T D2",
                               "~T2 T ~D2",
                               "~D2 ~D D2",
                               "~D2 D ~D2",
                               "~H2 ~H D2",
                               "~H2 H ~D2",
                               "~T3 ~T T2",
                               "~T3 T ~T2",
                               "~D3 ~D T2",
                               "~D3 D ~T2",
                               "~H3 ~H T2",
                               "~H3 H ~T2",
                               "~T1 ~T2",
                               "~T1 ~T3",
                               "~T1 ~H1",
                               "~T1 ~D1",
                               "~T2 ~T3",
                               "~T2 ~H2",
                               "~T2 ~D2",
                               "~T3 ~H3",
                               "~T3 ~D3",
                               "~H1 ~H2",
                               "~H1 ~H3",
                               "~H1 ~D1",
                               "~H2 ~H3",
                               "~H2 ~D2",
                               "~H3 ~D3",
                               "~D1 ~D2",
                               "~D1 ~D3",
                               "~D2 ~D3",
                               "T2 T3 H1 D1 T1",
                               "T1 T3 H2 D2 T2",
                               "T1 T2 T3 H3 D3",
                               "H1 H2 H3 D1 T1",
                               "H1 H2 H3 D2 T2",
                               "H1 H2 H3 T3 D3",
                               "D1 D2 D3 T1 H1",
                               "D1 D2 D3 H2 T2",
                               "D1 D2 D3 H3 T3"
                               ])
    entailed = {}
    if ttprob.test_literal("T1") == False:
        entailed["Tom is in 1st place"] = False
    if ttprob.test_literal("~T1") == False:
        entailed["Tom is in 1st place"] = True
    if ttprob.test_literal("T2") == False:
        entailed["Tom is in 2nd place"] = False
    if ttprob.test_literal("~T2") == False:
        entailed["Tom is in 2nd place"] = True
    if ttprob.test_literal("T3") == False:
        entailed["Tom is in 3rd place"] = False
    if ttprob.test_literal("~T3") == False:
        entailed["Tom is in 3rd place"] = True

    if ttprob.test_literal("H1") == False:
        entailed["Harry is in 1st place"] = False
    if ttprob.test_literal("~H1") == False:
        entailed["Harry is in 1st place"] = True
    if ttprob.test_literal("H2") == False:
        entailed["Harry is in 2nd place"] = False
    if ttprob.test_literal("~H2") == False:
        entailed["Harry is in 2nd place"] = True
    if ttprob.test_literal("H3") == False:
        entailed["Harry is in 3rd place"] = False
    if ttprob.test_literal("~H3") == False:
        entailed["Harry is in 3rd place"] = True

    if ttprob.test_literal("D1") == False:
        entailed["Dick is in 1st place"] = False
    if ttprob.test_literal("~D1") == False:
        entailed["Dick is in 1st place"] = True
    if ttprob.test_literal("D2") == False:
        entailed["Dick is in 2nd place"] = False
    if ttprob.test_literal("~D2") == False:
        entailed["Dick is in 2nd place"] = True
    if ttprob.test_literal("D3") == False:
        entailed["Dick is in 3rd place"] = False
    if ttprob.test_literal("~D3") == False:
        entailed["Dick is in 3rd place"] = True


    return entailed

def main():
    print("Liars and Truth-tellers II")
    print(tt2())
    print("-------------------------")
    print("Liars and Truth-tellers III")
    print(tt3())
    print("-------------------------")
    print("Robbery and a Salt")
    print(salt())
    print("-------------------------")
    print("An honest name")
    print(golf())

if __name__ == '__main__':
    main()