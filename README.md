# AlfabetoCode
Code from my dissertation

contact: Daniel Tompkins, tompkinsguitar@gmail.com

In general, the .py files contain the functions, and the ipynb files are where those functions are used to produce graphics.

Necessary modules: hmmlearn, networkx, ipyparallel, music21, scikit-learn, numpy, scipy, matplotlib, pygraphviz (requires GraphViz to be installed)

Here is a breakdown of the files:

## Corpus:

The Alfabeto song corpus can be found in Alfabeto/alfabeto_sources/. Each .py file is associated with a composer. Each book of songs is a dictionary that holds a dictionary. Each song has three items: continuo, alfabeto, and data: the continuo numbers are pitch-class integers (C = 0) of the bass line, the alfabeto letters are the alfabeto guitar chords (nb: NOT harmonic chords but fingerings), and the data shows the key signature ('n' for no sharps or flats, 'f' for one flat (B flat)) and final bass note. 

Some books do not contain bass notes (such as Abbatessa) and will not work with some of the code.

**The "all_sources.py" file allows you to retrieve any or all alfabeto sources.**

## Converter:

The Alfabeto/alfabeto_code/ directory contains AlfabetoConverter.py, which converts the corpus data into different musical representations such as chords (with and without bass notes), chord roots, roman numerals, and pitch class sets.

The other files include experimental code not included in the dissertation such as a Markov chain composer that produces a chord progression based on n-gram chords of a given collection of alfabeto songs. 

## Producing Data and Images

Most of the images and data are produced from Alfabeto/alfabeto_data. The best starting place may be dissertation_images.py, which brings most of the other code together and can produce most of the images from the dissertation. 

Data regarding notes and chords of all corpora are stored as either pickle files or scikit-learn's .pkl files in the Alfabeto/alfabeto_data/pickles/ directory and can be accessed through in Alfabeto/alfabeto_data/pickled_data.py. Most of the corpora are not currently on GitHub due to size. However, they can be produced by the process described below:

## Working with your own corpora (or testing mine)

Music21 can work with many different file types, including music xml and krn files, and comes with large corpora of its own. Additional corpora can be found in various places, especially through the humdrum project (http://kern.humdrum.org/) and the Yale classical archives corpus (http://ycac.yale.edu/). These can be processed through the "Alfabeto/Continuo Parser.ipynb" notebook. The result will store two types of data: one that has the key profile of each song in the corpus along with its notated key signature, and one that is a list of every chord in every song along with notated key signatures. The note and chord data can be used for all clustering algorithms, graphing, hidden Markov model, etc.

## The ipython notebook files (.ipynb)

Most of these were used for brainstorming (and still look like it!), but you may find them useful. However, a few were used for the dissertation: "Continuo Parser.ipynb", described above, creates data from digital music corpora; "Cluster Centroids and Continuo Kmeans.ipynb" creates the k-means graphs with numbered centroids and extracts the key profile and mode from each cluster center; the various HMM notebooks create the hidden Markov model graphs and run the Monte Carlo method in parallel. 

## Conclusion
If you have any questions about the code, please feel free to contact me at tompkinsguitar@gmail.com. If you find it useful, I'd love to see what you were able to do. And if you use it for a publication or presentation, please let me know what you did, and you may site my dissertation or this webpage. Thanks!
