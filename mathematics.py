import math


def squared(sample):
    """Return squared sample"""
    return [x**2 for x in sample]
    

def avg(sample):
    return float(sum(sample)) / len(sample)
    

def std(sample):
    return math.sqrt(var(sample))

    
def var(sample):
    return avg(squared(sample)) - avg(sample)**2


def mult(a, sample):
    return "\n".join("%s" % (a * x) for x in sample)
    

def div(sample, a):
    return "\n".join("%s" % (x / a) for x in sample)
    

