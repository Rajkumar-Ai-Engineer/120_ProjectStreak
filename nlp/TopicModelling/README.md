# TopicModelling — LDA Topic Discovery with Gensim

**Domain:** NLP. **Entry point:** topic_modelling.py.

## Purpose and pipeline
A small LDA example using five hard-coded sports and technology sentences. It tokenizes and lowercases text, removes stopwords, builds a Gensim dictionary and bag-of-words corpus, trains an LdaModel with two topics and prints four words per topic.

## Findings
- The file contains notebook-only !pip commands and is not directly executable as a standard Python script.
- The alphabetic-token filter is assigned to misspelled variable tokems and never used; returned tokens are not filtered as intended.
- Five short documents are insufficient for meaningful topic discovery or validation.
- No random seed, coherence evaluation, topic visualisation, saved model or external corpus loader is present.
- NLTK downloads happen at runtime.

## Next steps
Move installation commands out of the script, fix token filtering, use a representative corpus, tune topic count, calculate coherence and persist model/preprocessing metadata. Static inspection only; no run performed.
