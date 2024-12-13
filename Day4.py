import numpy as np

def day4_1(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    # Load all into big numpy array
    x = []
    for line in lines:
        x.append(list(line.strip()))
    nump = np.array(x)

    found = 0
    found += count_goods(nump) # right
    found += count_goods(nump.transpose()) # down
    found += count_goods(nump[:, ::-1]) # left
    found += count_goods(nump[::-1,:].transpose()) # up

    # get diagonals
    down_right = get_all_diags(nump)
    down_left = get_all_diags(nump[:,::-1])

    found += count_goods(down_left) # downLeft
    found += count_goods(down_right) # downRight
    found += count_goods(down_right[:, ::-1]) #upLeft
    found += count_goods(down_left[:, ::-1]) #upRight
    print(found)

def get_all_diags(array):
    row_size = len(array[0])
    diags = []
    diags.append(get_diag(array, 0))
    for i in range(1, row_size):
        diags.append(get_diag(array, i))
        diags.append(get_diag(array, -i))
    diags = np.asarray(diags)
    return diags


def get_diag(array, offset):
    temp = np.diagonal(array, offset=offset)
    return list(np.pad(temp, (0,abs(offset))))


def count_goods(array):
    # array = np.pad(array, ((0,3)))
    Xs = array=='X'
    Xs = Xs[:, :-3]
    Ms = array=='M'
    Ms = Ms[:,1:-2]
    As = array=='A'
    As = As[:,2:-1]
    Ss = array=='S'
    Ss = Ss[:,3:]
    collect = np.logical_and(np.logical_and(Xs, As), np.logical_and(Ms, Ss))
    print(np.sum(collect))
    return np.sum(collect)


def is_xmas(t_l, t_r, b_l, b_r):
    if t_l in ('S', 'M') and b_r in ('S', 'M'):
        if (t_l == t_r and b_l == b_r) or (t_l == b_l and b_r == t_r):
            return t_l != b_r
    return False

def day4_2(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    # Load all into big numpy array
    x = []
    for line in lines:
        x.append(list(line.strip()))
    nump = np.array(x)
    xmases = 0

    A_spots = np.transpose(np.where(nump=='A'))
    for i,j in A_spots:
        if max(i, j) == len(nump[0])-1 or min(i,j) == 0:
            continue
        # These are the locations to be checked. Need MM and SS in corners
        top_l = nump[i-1, j-1]
        top_r = nump[i-1, j+1]
        bot_l = nump[i+1, j-1]
        bot_r = nump[i+1, j+1]
        if is_xmas(top_l, top_r, bot_l, bot_r):
            xmases += 1
            print(nump[i-1:i+2,j-1:j+2])
    print(xmases)

day = "4"
testFile = "InputFiles/day" + day + "test.txt"
testFile2 = "InputFiles/day" + day + "test2.txt"
realFile = "InputFiles/day" + day + "real.txt"
moreTests = "InputFiles/day" + day + "moretests.txt"

# day4_1(testFile)
# day4_1(realFile)
#
# day4_2(testFile)
day4_2(realFile)



