# Computational Literacy course, autumn 2023 (LDA-H305)

This is my final project for the course "Computational Literacy". The topic of this project is **the sentiment analysis of the wall inscriptions found in Casa delle Nozze d'Argento**, a house in the ancient city of Pompeii. 

My plan was to do a case study to test could lexicon-based sentiment analysis be used to analyse the wall inscriptions, and what the results can tell us.

**The research questions of this project were:**
-	Can sentiment analysis be used in the context of ancient wall inscriptions and the Latin language?
-	What sentiments are most common in the wall inscriptions of Casa delle Nozze d'Argento?
-	Do the sentiments of the wall inscriptions of Casa delle Nozze d'Argento and their location correlate to each other? Are there specific places where specific sentiments are located?

![lohmann_cdnda](https://github.com/lisja/LDA-H305/assets/93824007/af9c30d8-992d-4718-82ee-3588e4135663)

# Background
There has been quite a lot of research about the wall inscriptions of Pompeii. The most central studies considering this project are Polly Lohmann’s book _Graffiti als Interaktionsform: Geritzte Inschriften in den Wohnhäusern Pompejis_ (2018) and Joonas Vanhala’s Master’s thesis titled _Imanis metula es : herjaukset Pompejin seinäkirjoituksissa_ (2019). Lohmann’s book analyses the wall inscriptions as an everyday form of interaction and focuses on the wall inscriptions of six Pompeian houses. One of these is the topic of this project: Casa delle Nozze d'Argento. In his study Vanhala focuses on the invectives found in the wall inscriptions of Pompeii and he also has listed invective wall inscriptions of Casa delle Nozze d'Argento. This is one of the reasons why I chose this specific house as the topic of my case study. Both Vanhala and Lohmann have listed the wall inscriptions found in the house in question and I used these lists as the basis of my dataset. 

Even though the wall inscriptions of Pompeii have been studied quite extensively using the methods and tools from the field of humanities, there has been little research using sentiment analysis. In _Extending and Using a Sentiment Lexicon for Latin in a Linked Data Framework_ Sprugnoli _et al._ (2021) tested sentiment analysis methods on the works of Dante Alighieri. The latest research on the subject is _The Sentiment of Latin Poetry. Annotation and Automatic Analysis of the Odes of Horace_ by Sprugnoli _et al._ (2023) where the sentiment analysis methods are used in the analysis of Odes of Horace, a collection of poems by the poet Horace. In the past couple of years there has been some testing of the sentiment analysis methods, but they have all been focusing on longer Latin literary works that have been written by the freeborn elite men of the ancient Roman society. The language used in these works is completely different from the “vulgar Latin” that the regular people of the Roman society used. Thus, the sentiment analysis of the wall inscriptions can give us important information of the emotions of the everyday Roman citizen that are usually dismissed in the literary works of the elite.

# The Data
As mentioned above I used the listing of wall inscriptions of Casa delle Nozze d'Argento found both in Vanhala’s and Lohmann’s studies, 51 inscriptions in total. I also used the wall inscriptions listed by Vanhala because their sentiment polarity is already known to be negative since they are recognised as invectives. I wanted to test if they are detected correctly as such in the analysis. 

The data gathered can be viewed by downloading the _cdnda_graffiti.xlsx_ file. There are 3 sheets: 
-	**Lohmann_Vanhala**:
    -	The graffiti from Casa delle Nozze d'Argento in Pompeii, gathered from the works of Lohmann and Vanhala
    - A guide to read the cells:
      - **CIL IV:** number assigned to each wall inscription in _Corpus Inscriptionum Latinarum_, a collection of Latin inscriptions.
      - **NOTES:** “VANHALA” = found also in Vanhala’s list, “Has Incomprehensible words” = part of the text needs to be deleted since it is incomprehensible, “Has Greek” = the part in Greek needs to be deleted since the study focuses on Latin
      - **Text:** the wall inscription itself
      - **Lohmann number:** the numbering used by Lohmann in the list of the wall inscriptions of Casa delle Nozze d'Argento
      - **Lohmann location:** the location of each wall inscription by Lohmann
      - **Vanhala's interpretations/notes:** Vanhala’s corrections of grammar or other difference compared to Lohmann’s
      -	**Vanhala's additions:** 1 wall inscription not mentioned by Lohmann and 1 which significantly differs from Lohmann’s
      - **Vanhala Location:** the location of the 2 wall inscriptions in “Vanhala's additions”
-	**Dataset**
    -	The dataset of the lemmatized graffiti of Casa delle Nozze d'Argento with English translations
-	**Sentiments**
    -	The sentiments of the lemmatized graffiti of Casa delle Nozze d'Argento

For translation of the wall inscriptions from Latin to English I used _philolog.us_ (https://philolog.us/) as well as the database by Rose (2018) that has translations on some of the wall inscriptions found in Casa delle Nozze d'Argento. 


# The Process

First, I manually collected the wall inscriptions of Casa delle Nozze d'Argento listed in both Vanhala’s and Lohmann’s studies and saved them to the file _cdnda_graffiti.xlsx_’s sheet named _Lohmann_Vanhala_. There were total of 80 inscriptions listed in Lohmann’s book and 10 invectives listed in Vanhala’s thesis. One of the invectives listed by Vanhala was not found in Lohmann’s listing (CIL IV 4195) so I added this to the dataset. Also, there was a difference in interpretation of the wall inscription CIL IV 4196 (“Meroe” vs. “Miduse”). I ended up using the version by Vanhala (“Meroe”) because his thesis is more recent, and he had added explanations of his interpretation of the wall inscription. There is also a difference in the interpretation of the wall inscription CIL IV 4160: Vanhala lists 3 different possibilities and I have added all of these possibilities in the dataset since there are clear differences in their sentiments. I didn’t add the wall inscriptions to the datasets that were not in Latin or were only Roman numerals and thus would not add anything to the data. I also deleted the totally incomprehensible wall inscriptions completely and deleted the incomprehensible parts of some inscriptions for the same reason. Eventually the total amount of the wall inscriptions in the dataset was set to 51, containing the 3 different interpretations of the wall inscription CIL IV 4160. 

Next, I translated the wall inscriptions in the dataset with the best of my ability. I used _philolog.us_ (https://philolog.us/) and the database by Rose for help in this endeavour. Even though, the translations didn’t bring anything new to the table when it comes to the sentiment analysis, I still wanted to do this because it helps better understand the wall inscriptions, especially if you do not have knowledge of the Latin language. The translations can be found in the file _cdnda_graffiti.xlsx_’s sheet named _Dataset_. 

The next step was to lemmatize the dataset. I used _Collatinus_ application (https://outils.biblissima.fr/en/collatinus/), a Latin lemmatizer and morphological analyzer by Yves Ouvrard and Philippe Verkerk. Some of the words were not recognised at all by _Collatinus_ and thus I again turned to _philolog.us_ to find the lemmas. These lemmas are stored in the file _cdnda_graffiti.xlsx_’s sheet named _Dataset_. 

I used _LatinAffectus_, a set of sentiment lexicons of Latin adjectives and nouns by Sprugnoli _et al._ (2020) as the basis of sentiment analysis. I had to add 14 words myself because they were not listed and were essential to do sentiment analysis on the dataset. These added words are marked as “ADDED” in the end of the file _added_LatinAffectusv4.tsv_ that contains the original _LatinAffectus_ as well as the insertions made by me. 

I wrote the Python code to do the sentiment analysis on the dataset. The code and the instructions to use it can be found in the file _manual_latinaffectus_sentiments.py_. The lemmatized wall inscriptions need to be inputted manually and then the program prints the tokens of the input, the sentiment polarity, and the sentiment score as the output. I manually placed each of the lemmatized wall inscriptions to the code and saved the sentiment polarity and sentiment score to the file _cdnda_graffiti.xlsx_’s sheet named _Sentiments_. 
 
I wanted to visualize the results so I used _Palladio_ (https://hdlab.stanford.edu/palladio/) to create some graphs that can be seen below in the **Results and analysis** section. I also made some donut graphs (using https://graphmaker.imageonline.co/donutchart.php) to visualize the distribution of the sentiment which can also be seen below. 

# Results and analysis

<div align="center">The distribution of the wall inscriptions of Casa delle Nozze d'Argento: in numbers and in percentage</div>

<img src="https://github.com/lisja/LDA-H305/assets/93824007/09f867e4-d5d4-4b57-ad99-8fef5e59ba1a" width="500" height="300">

![sentiments_amount_donut](https://github.com/lisja/LDA-H305/assets/93824007/09f867e4-d5d4-4b57-ad99-8fef5e59ba1a)

![sentiments_donut](https://github.com/lisja/LDA-H305/assets/93824007/ea7cb0b7-08d4-4f87-b5e8-4a98f8d2a3a4)

![cil_and_sentiment_polarity](https://github.com/lisja/LDA-H305/assets/93824007/1f6de594-672e-4d0c-8daf-2ef443f4d3ee)


![location_and_sentiments](https://github.com/lisja/LDA-H305/assets/93824007/f7842371-7631-4f0f-8c28-748c4c17f040)

# Problems, biases, and alternative solutions

# About the reproducibility of the results

# References

Lohmann, P. (2018) Graffiti als Interaktionsform: Geritzte Inschriften in den Wohnhäusern Pompejis, Berlin, Boston: De Gruyter, 2018. https://doi.org/10.1515/9783110574289

Rose, A. (2018) Database for The Scratched Voices Begging to be Heard: The Graffiti of Pompeii and Today. Tempe, AZ: Barrett, the Honors College. 2018 ( tDAR id: 445837) ; https://doi.org/10.6067/XCV8TH8QJ5 

Sprugnoli, Rachele; Passarotti, Marco; Corbetta, Daniela and Peverelli, Andrea. (2020). LatinAffectus, ILC-CNR for CLARIN-IT repository hosted at Institute for Computational Linguistics "A. Zampolli", National Research Council, in Pisa. http://hdl.handle.net/20.500.11752/OPEN-527

Sprugnoli, R., Passarotti, M. C., Testori, M., Moretti, G. (2021). Extending and Using a Sentiment Lexicon for Latin in a Linked Data Framework, in Proceedings of the Workshops and Tutorials - Language Data and Knowledge 2021 (LDK 2021). Zaragoza, Spain, September 1-4, CEUR Workshop Proceedings, 2021, (Zaragoza, 01-01 September 2021), CEUR Workshop Proceedings (CEUR-WS.org), Zaragoza 2021: 151-164. [10.5281/zenodo.6303164] [http://hdl.handle.net/10807/196024]

Sprugnoli, R., Mambrini, F., Passarotti, M. C., & Moretti, G. (2023). The Sentiment of Latin Poetry. Annotation and Automatic Analysis of the Odes of Horace. IJCOL, 9, 53-71.

Vanhala, J. (2019). Imanis metula es : herjaukset Pompejin seinäkirjoituksissa. [Master’s thesis, University of Turku]

