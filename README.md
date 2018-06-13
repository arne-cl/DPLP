# RST Parser #

## 1. Required Package ##

scipy, numpy, sklearn, nltk, python-tk 

The last two packages are required to draw the RST tree structure in the PostScript format. It is highly recommended to install these two packages for visualization. Otherwise, you have to read the bracketing results and to imagine what the tree looks like :-)

## 2. RST Parsing with Raw Documents ##

To do RST parsing on raw documents, you will need syntactic parses and also the discourse segmentations on the documents. Let's start with preparing data

First, we need to collect all the documents into one folder, as all the following commands will scan this folder and process the documents in the same way. Let's assume the directory is **./data**

All the following commands will be run in a batch fasion, which means every command will scan will the documents in the data folder and process them once.

### 2.1 Data Processing ###

1. Run the Stanford CoreNLP with the given bash script **corenlp.sh** with the command "*./corenlp.sh path_to_dplp/data*"
    - This is a little awkward, as I am not sure how to call the Stanford parser from any other directory.

2. Convert the XML file into CoNLL-like format with command "*python convert.py ./data*"
    - Now, we can come back to the DPLP folder to run this command

### 2.2 Segmentation and Parsing ###

1. Segment each document into EDUs with command "*python segmenter ./data*"

2. Finally, run RST parser with command "*python rstparser ./data*"
    - The RST parser will generate the bracketing file for each document, which can be used for evaluation
    - It will also generate the PostScript file of the RST structure. Generating (and saving) these PS files will slow down the parsing procedure a little. You can turn it off with "*python rstparser ./data* False"


## 3. Training Your Own RST Parser ##

TODO

## 4. Repository Structure

```
.
├── code
│   ├── buildtree.py # test() shows how to extract shift-reduce actions from a .dis file
│   ├── data.py # test() shows how to build a 'vocab' and a 'matrix' file from training data
        - Data.builddata() needs a .merge file in addition to a .dis file to create an RSTTree
        - a .merge file is a .conll file (converted output from CoreNLP with added EDU column)
        - to create .merge files, we would first need to train a discourse segmenter (or use an existing one)
│   ├── datastructure.py
│   ├── docreader.py
│   ├── evalparser.py
│   ├── evaluation.py
│   ├── featselection.py
│   ├── feature.py
│   ├── learn.py # only contains empty class 'Learn'
│   ├── model.py
│   ├── parser.py
│   ├── readdoc.py
│   ├── tree.py
│   └── util.py
├── convert.py # converts CoreNLP's XML output into .conll files
├── corenlp.sh
├── discoseg
│   ├── buildedu.py
│   ├── buildmodel.py
│   ├── buildsample.py
│   ├── buildvocab.py
│   ├── main.py # calls methods in the other modules of that package to train / run discourse segmentation
        - we need .merge files for discoseg training, so we'll have to extract EDUs from the corpus beforehand
│   ├── model
│   │   ├── classifier.py
│   │   ├── datastruct.py
│   │   ├── docreader.py
│   │   ├── example.txt
│   │   ├── feature.py
│   │   ├── sample.py
│   │   ├── util.py
│   │   └── vocab.py
│   └── pretrained
│       ├── model.pickle.gz
│       └── vocab.pickle.gz
├── doc # 5 page description of this parser incl. some code layout description
│   ├── ...
├── main.py # contains out-commented code for training in __name__
    - createtrndata() can train/create a vocab.pickle.gz from training data (.dis + .merge)
    - trainmodel() can train/create a parsing-model.pickle.gz from training data
├── model
│   └── parsing-model.pickle.gz # estimator LinearSVC from pre-0.18 version of sklearn
├── preprocess
│   └── xmlreader.py # reads XML from CoreNLP and writes CONLL format
├── README.md
├── resources # acc. to main.py, these are Brown clusters
│   ├── bc3200.pickle.gz # dict (ca. 250000 entries), mapping from tokens to binary numbers, e.g. ('unsupportable', '10111101010111')
│   └── bcreader.py  # read bc-3200.txt into 'vocab' dict, write it into 'bc3200.pickle.gz'
├── rstparser.py
├── segmenter.py
├── tmp  # contains some example RST parses
│   ├── ...
```

## Reference ##

Please read the following paper for more technical details

Yangfeng Ji, Jacob Eisenstein. *[Representation Learning for Text-level Discourse Parsing](http://jiyfeng.github.io/papers/ji-acl-2014.pdf)*. ACL 2014
