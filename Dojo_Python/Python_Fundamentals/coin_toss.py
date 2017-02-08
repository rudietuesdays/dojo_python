import random

def coin_toss(attempt):
    coin = ''
    heads_tally = 0
    tails_tally = 0
    i=1
    while (i <= attempt):
        toss = round(random.random())
        # print toss
        if (toss == 0):
            coin = 'head'
            heads_tally += 1
        else:
            coin = 'tail'
            tails_tally += 1
        print 'Attempt #', i, ": Throwing a coin... it's a", coin, "! Got ", heads_tally, "head(s) so far and", tails_tally, "tail(s) so far."
        i += 1
    print "No tosses left. Thanks for playing!"

print coin_toss(100)
