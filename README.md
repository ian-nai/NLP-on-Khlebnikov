# NLP-on-Khlebnikov
NLP on works by Velimir Khlebnikov. This repository is an outgrowth of the [Non-English NLP Tutorial](https://github.com/ian-nai/Non-English-NLP-Tutorial).
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/f/f6/Chlebnikow.jpg" height="390" width="273"/>
</p>
## Getting Started
Install required dependencies:

```
pip3 install -r requirements.txt
```
## Scope
This repository is a starting point for using NLP to analyze and visualize various aspects of the poetry of Velimir Khlebnikov. Code may be updated and added as necessary while the project progresses.

## What This Repository Contains
#### <span style="text-decoration: underline">CSVs</span>
A collection of .csv files containing data gleaned from analyzing the texts using NLP. The sub-folders in this section contain data for different models that were used to process the texts, the ru_core_news_lg model from spaCy and the Stanza French model from Stanford's Stanza library. There is also a folder for data used in visualizing the texts using graphs.

#### Original Texts
The original texts of Khlebnikov's complete poems:

* Стихотворения 1904-1916
* Стихотворения 1917-1922


#### Pickle Files
These are pickled NLP models (using the ru_core_news_lg spaCy model) of the original texts, broken up into smaller chunks to avoid file size limitations.

#### Python Code
The Python files contained here perform the NLP used to generate the CSVs and visualizations. The files are as follows:
* remove_stopwords.py - 
* ru_core_news_lg.py - Run the spaCy csv_ru_core_news_lg model on the text(s) included in the code and output the results to a CSV file.
* stanza_csv.py - Run Stanford's Stanza library on the text(s) included in the code and output the results to a .csv file.
* stress_detection.py - 
* liv_rix_readability_test.py - Perform the Liv and Rix readability tests on the text(s) included in the code and output the results in the terminal.
* make_pickles.py - Create the pickle files for uploading to GitHub.
* visualizations.py - Code to generate various visualizations of textual data using matplotlib.

#### Tokenized Lines and Sentences
These folders contain text files of the texts tokenized into lines and sentences.

#### Visualizations
Visualizations of textual data in PNG and interactive HTML/JS format. This folder may be added to in the future.
