# Parts of Speech Comparison

A Python NLP experiment comparing part-of-speech tags produced by NLTK and TextBlob.

## Overview

This project explores how two Python NLP tools, NLTK and TextBlob, tag the same text differently. The script allows a user to choose an NLTK corpus, select a text file from that corpus, and compare the resulting POS tags.

The project began as an investigation into a key NLP issue: different taggers may tokenize or label the same text differently, making direct comparison more complicated than expected.

## Features

- Lists available NLTK corpora
- Lets the user choose a corpus and text
- Tags text using both NLTK and TextBlob
- Compares tagger output lengths
- Identifies whether the two taggers produce directly comparable lists

## Skills Demonstrated

- Python scripting
- Natural language processing
- Corpus exploration with NLTK
- Part-of-speech tagging
- Debugging differences between NLP tools
- Working with tokenization and tagger output

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```
You may also need to download NLTK data:

```python
import nltk
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("brown")
```

## How to Run

```bash
python pos_comparison.py
```

## Notes

This project is exploratory. A major finding is that POS taggers are not always directly comparable because they may tokenize input differently or return slightly different word/tag sequences.

## Future Improvements

* Remove interactive input and add command-line arguments
* Export comparison results to a text or CSV file
* Align tokens before comparing POS tags
* Add support for custom text files
* Add summary statistics for tag disagreements
