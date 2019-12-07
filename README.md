# Download model fasttext here

[WIKI](https://fasttext.cc/docs/en/pretrained-vectors.html) <br>
[VECTOR](https://fasttext.cc/docs/en/crawl-vectors.html)
### Open file vectors_fast_text_to_spacy_model.py and edit
[LANGUAGE] = example: "vi" <br>
[FILE_WORD2VEC] = "./data/word2vec.txt"

## Type in the terminal :
<code> python vectors_fast_text.py </code>

It will take about 10 minutes to finish, depending on the size of the word2vec file. In the script I made the print of the word, so that you can follow.

After that, you must type in the terminal: <br>
<code> python -m spacy package ./models/new_nlp/ ./my_models/ </code><br>
<code> python setup.py sdist </code><br>

And then you will have a "zip" file.

<code> pip install /path/to/vi_spacy_model-1.0.0.tar.gz </code>

## Some model has trained spacy

[Vi Spacy Model Fastai](https://drive.google.com/file/d/1z99svOYplV0iP4IKZjxdg3tVP_TnHDc1/view?usp=sharing) <br>
[Vi Spacy Model Wiki](https://drive.google.com/file/d/1Dq9jbB1f9eYbJUnYl_Y4Xtc5448qu6df/view?usp=sharing) <br>
