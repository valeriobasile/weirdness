#!/usr/bin/env python

import logging as log
from tqdm import tqdm
import sys

log.basicConfig(format='%(asctime)s %(message)s', level=log.INFO)

def frequencies(words_file, total):
    log.info("reading words from file {0}".format(words_file))
    frequency = dict()
    with open(words_file) as f:
        for line in tqdm(f, total=total):
            word = line.strip()
            if not word in frequency:
                frequency[word] = 0
            frequency[word] += 1
    return frequency

def linecount(filename):
	return sum(1 for line in open(filename))

file_target = sys.argv[1]
total_target = linecount(file_target)
file_control = sys.argv[2]
total_control = linecount(file_control)

frequencies_target = frequencies(file_target, total_target)
frequencies_control = frequencies(file_control, total_control)

for word, fd in frequencies_control.items():
    frd = float(fd)/float(total_control)
    if word in frequencies_target:
        frg = float(frequencies_target[word])/total_target
        weirdness = frg/frd
    else:
        weirdness = 0.0
    print ("{0:.3f}\t{1}".format(weirdness*0.01, word))
