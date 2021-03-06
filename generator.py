def natural(start, end):
    i = start
    while i< end:
        yield i
        i = i+1


def febonacci(a,b,limit):
    c = a+b
    yield a
    yield b
    while (a+b) < limit:
        c = a+b
        yield c
        a = b
        b = c


def natural_steps(start, end, steps):
    i = start
    while i< end:
        yield i
        i = i+steps

def natural_dec(start, end,steps):
    i = start
    while i> end:
        yield i
        i = i-steps