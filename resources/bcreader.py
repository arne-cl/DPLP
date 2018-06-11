## bcreader.py
## Author: Yangfeng Ji
## Date: 01-27-2015
## Time-stamp: <yangfeng 01/30/2015 22:16:26>

from cPickle import dump, load
import gzip

def reader(fname):
    bcvocab = {}
    with open(fname, 'r') as fin:
        for line in fin:
            items = line.strip().split('\t')
            bcvocab[items[1]] = items[0]
    return bcvocab


def savevocab(vocab, fname):
    with gzip.open(fname, 'w') as fout:
        dump(vocab, fout)
    print 'Done'

def loadvocab(vocab_pickle_file):
    """reverse engineering: the resulting vocab dict maps from a token
    to a stringified binary number, e.g. ('unsupportable', '10111101010111').
    """
    with gzip.open(vocab_pickle_file) as infile:
        vocab = load(infile)
    return vocab

if __name__ == '__main__':
    vocab = reader("./bc-3200.txt")
    savevocab(vocab, "./bc3200.pickle.gz")
