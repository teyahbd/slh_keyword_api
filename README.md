# Word2Vec Keyword Recommendation API (Wikipedia Word Vectors)

This repo contains a previous version of a keyword API for a Northcoders bootcamp project. Please find the current repo with more information [here](https://github.com/teyahbd/ecommerce-keyword-api).

To make use of this repo, you will need to generate your own word vector file as it is too large to host on Github. Our API uses pretrained word vectors from [GLoVe](https://nlp.stanford.edu/projects/glove/) - specifically the Wikipedia 2014 + Gigaword 5 vectors at 50 dimensions. Once you have downloaded this file, you can run the script found in ```model/setup_vectors.py``` to generate a word vector file in the correct Word2Vec format required for this project. Once you have a file called ```wiki-50d.txt``` in your ```model``` folder, you should be able to set up the API in a similar fashion as described in our [current repo](https://github.com/teyahbd/ecommerce-keyword-api).

At the time of writing, this API is hosted [here](https://slh-keyword-api.herokuapp.com/).
