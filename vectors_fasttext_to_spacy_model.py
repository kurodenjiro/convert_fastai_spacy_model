from __future__ import unicode_literals
import plac
import numpy

import spacy
from spacy.language import Language


@plac.annotations()
def main():
    nlp = spacy.load('[Language]')
    with open("[File Path]", 'rb') as file_:
        header = file_.readline()
        nr_row, nr_dim = header.split()
        nlp.vocab.reset_vectors(width=int(nr_dim))
        count = 0
        for line in file_:
            count += 1
            line = line.rstrip().decode('utf8')
            pieces = line.rsplit(' ', int(nr_dim))
            word = pieces[0]
            print("{} - {}".format(count, word))
            vector = numpy.asarray([float(v) for v in pieces[1:]], dtype='f')
            nlp.vocab.set_vector(word, vector)  # add the vectors to the vocab
    nlp.to_disk("./models/")


if __name__ == '__main__':
    plac.call(main)
