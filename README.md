# Download model here

[WIKI](https://fasttext.cc/docs/en/pretrained-vectors.html)
[VECTOR](https://fasttext.cc/docs/en/crawl-vectors.html)
### open file vectors_fast_text_to_spacy_model.py and edit
[LANGUAGE] = example: "vi"
[FILE_WORD2VEC] = "./data/word2vec.txt"

## Type in the terminal :
<code> python vectors_fast_text.py </code>

It will take about 10 minutes to finish, depending on the size of the word2vec file. In the script I made the print of the word, so that you can follow.

After that, you must type in the terminal:
<code> python -m spacy package ./models/new_nlp/ ./my_models/ </code>
<code> python setup.py sdist </code>

And then you will have a "zip" file.

<code> pip install /path/to/pt_example_model-1.0.0.tar.gz </code>

