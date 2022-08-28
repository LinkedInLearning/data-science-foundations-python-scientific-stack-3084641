# %%
from sklearn.datasets import fetch_20newsgroups

corpus = fetch_20newsgroups(
    categories=['sci.space'],
    remove=['headers', 'footers'],
)
text = corpus['data'][4]
print(text)

# %%
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
doc

# %%
type(doc)

# %%
sent = list(doc.sents)[1]
print(sent)

# %%
for tok in sent:
    print(f'{tok.text!r} -> {tok.tag_}')

# %%
for ent in doc.ents:
    print(f'{ent.text} ({ent.label_})')
