# Had to search up how to tackle this type of problem.
# Ended up using a dictionary to record the numbers already done.

u = {}


def play(p1p, p2p, p1s=0, p2s=0):  # I should use more default parameters, they look cool.
    k = (p1p, p2p, p1s, p2s)
    if k in u:  # This is very cool.
        return u[k]
    c = [0, 0]
    for i in [x + y + z for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3]]:  # Again some cool list stuff with for loops.
        p1p_ = ((p1p + i - 1) % 10 + 1)
        p1s_ = p1s + p1p_
        if p1s_ >= 21:
            c[0] += 1
        else:
            a, b = play(p2p, p1p_, p2s, p1s_)  # Swap the outputs to process the next turn for the next player. pretty smart O-O
            c[0] += b
            c[1] += a
    u[k] = c  # Stores the record of the number of universes.
    return c  # :D


print(max(play(6, 8)))
