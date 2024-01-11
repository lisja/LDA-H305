# The code for the sentiment analysis using the LatinAffectus v.4 sentiment lexicon

# HOW TO USE: add manually the lemmatized text in Latin in the latin_text variable. It will print the tokens as well as the sentiment polarity and the total sentiment score.


from cltk.tokenizers.lat.lat import LatinWordTokenizer
import csv

# Load the Latin tokenizer
word_tokenizer = LatinWordTokenizer()

# Load the sentiment analysis lexicon from the TSV file
sentiment_lexicon = {}
with open('added_LatinAffectusv4.tsv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        word = row[0]
        score = 0
        if row[2] in ['-1', '-0.5', '0', '0.5', '1']:
            score = float(row[2])
        sentiment_lexicon[word] = score

# Add lemmatized Latin text
latin_text = "Meroe fututor"

# Tokenize the text & convert to lowercase letters
words = word_tokenizer.tokenize(latin_text.lower())

print(words)

# The sentiment score
total_sentiment_score = 0

# Calculate the total sentiment score
for word in words:
    if word in sentiment_lexicon:
        total_sentiment_score += sentiment_lexicon[word]

# Return the sentiment based on the total sentiment score
if total_sentiment_score > 0:
    print("Positive sentiment")
elif total_sentiment_score < 0:
    print("Negative sentiment")
else:
    print("Neutral sentiment")

print(total_sentiment_score)
