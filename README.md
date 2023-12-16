# Computational Literacy course, autumn 2023 (LDA-H305)

This is my final project for the course "Computational Literacy". The topic of this project is **the sentiment analysis of the wall inscriptions found in Casa delle Nozze d'Argento**, a house in the ancient city of Pompeii. 

My plan was to do a case study to test could lexicon-based sentiment analysis be used to analyse the wall inscriptions, and what the results can tell us. I chose Casa delle Nozze d'Argento since it has a good number of wall inscriptions but and especially because some of them are considered invectives which I already know to be negative in their sentiment. I will use this information to test that the invectives are detected correctly.

**The research questions of this project were:**
-	Can sentiment analysis be used in the context of ancient wall inscriptions and the Latin language?
-	What sentiments are most common in the wall inscriptions of Casa delle Nozze d'Argento?
-	Do the sentiments of the wall inscriptions of Casa delle Nozze d'Argento and their location correlate to each other? Are there specific places where specific sentiments are located?

![cdnda_pic](https://github.com/lisja/LDA-H305/assets/93824007/5a639190-3088-4488-ac11-b3c7d240f89c)


###### <div align="center">A picture from Casa delle Nozze d'Argento (Photograph © Parco Archeologico di Pompei.)</div>


# Background
There has been quite a lot of research about the wall inscriptions of Pompeii. The most central studies considering this project are Polly Lohmann’s book _Graffiti als Interaktionsform: Geritzte Inschriften in den Wohnhäusern Pompejis_ (2018) and Joonas Vanhala’s Master’s thesis titled _Imanis metula es : herjaukset Pompejin seinäkirjoituksissa_ (2019). Lohmann’s book analyses the wall inscriptions as an everyday form of interaction and focuses on the wall inscriptions of six Pompeian houses. One of these is the topic of this project: Casa delle Nozze d'Argento. In his study Vanhala focuses on the invectives found in the wall inscriptions of Pompeii and he also has listed invective wall inscriptions of Casa delle Nozze d'Argento. This is one of the reasons why I chose this specific house as the topic of my case study. Both Vanhala and Lohmann have listed the wall inscriptions found in the house in question and I used these lists as the basis of my dataset. 

Even though the wall inscriptions of Pompeii have been studied quite extensively using the methods and tools from the field of humanities, there has been little research using sentiment analysis. In _Extending and Using a Sentiment Lexicon for Latin in a Linked Data Framework_ Sprugnoli _et al._ (2021) tested sentiment analysis methods on the works of Dante Alighieri. The latest research on the subject is _The Sentiment of Latin Poetry. Annotation and Automatic Analysis of the Odes of Horace_ by Sprugnoli _et al._ (2023) where the sentiment analysis methods are used in the analysis of Odes of Horace, a collection of poems by the poet Horace. In the past couple of years there has been some testing of the sentiment analysis methods, but they have all been focusing on longer Latin literary works that have been written by the freeborn elite men of the ancient Roman society. The language used in these works is completely different from the “vulgar Latin” that the regular people of the Roman society used. Thus, the sentiment analysis of the wall inscriptions can give us important information of the emotions of the everyday Roman citizen that are usually dismissed in the literary works of the elite.

# The Data
As mentioned above I used the listing of wall inscriptions of Casa delle Nozze d'Argento found both in Vanhala’s and Lohmann’s studies, 51 inscriptions in total. I also used the wall inscriptions listed by Vanhala because their sentiment polarity is already known to be negative since they are recognised as invectives. I wanted to test if they are detected correctly as such in the analysis. 

The data gathered can be viewed by downloading the _cdnda_graffiti.xlsx_ file. There are 3 sheets: 
-	**Lohmann_Vanhala**
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
 
I wanted to visualize the results so I used _Palladio_ (https://hdlab.stanford.edu/palladio/) to create some graphs that can be seen below in the **Results and analysis** section. I used _OpenRefine_ (https://openrefine.org/) to clean the dataset a bit to delete empty rows that I had added to the dataset to make it more reader friendly. I also converted the dataset to .csv file because that is necessary for Palladio to work. I also made some donut graphs (using https://graphmaker.imageonline.co/donutchart.php) to visualize the distribution of the sentiment which can also be seen below. 

# Results and analysis

The results of the sentiment analysis shows that it can indeed be used in the context of the ancient wall inscriptions. However, it does require quite a lot of effort because there is still a lot of work to be done to get the methods and tools for this kind of research to work. The only proper sentiment lexicon at this time is _LatinAffectus_ that contains a bit over 6 000 Latin adjectives and nouns. However, it does not contain any verbs and the 6 000 words it has ended up not being enough and thus I had to add some myself. 

A bit surprisingly, when summed up together the total sentiment score of all of the wall inscriptions was 0,5 and the sentiment polarity was positive. I assumed that the neutral sentiments would be dominant because many of the words in the wall inscriptions were not in LatinAffectus but my first intuition was that the sentiments would be more in the negative direction. 

The distribution of the sentiments was as such: from the total 51 of the wall inscriptions in the dataset 24 (47.1 %) were recognized as neutral, 14 (27.5 %) as positive and 13 (25.5 %) as negative. These results can also be viewed in the donut graphs below.

&nbsp;
&nbsp;

### **<div align="center">The donut graphs for the distribution of the wall inscriptions of Casa delle Nozze d'Argento (total amount 51 wall inscriptions):</div>**

<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/09f867e4-d5d4-4b57-ad99-8fef5e59ba1a" width="600" height="350"></div>

<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/ea7cb0b7-08d4-4f87-b5e8-4a98f8d2a3a4" width="600" height="350"></div>

&nbsp;
&nbsp;

The sentiment scores were between -1.5 and 3.5, most of the scores being neutral (0). There is one wall inscription (4160) that is both neutral (0) and negative (-1). This can be seen also in the graph below. The reason for this is mentioned above in the **The Process** section: the dataset had it 3 times because there were 3 different interpretations of the wall inscription. 2 of these interpretations were detected as negative and 1 as neutral. 

&nbsp;
&nbsp;

### **<div align="center">The sentiment scores & the wall inscription marked with CIL IV number:</div>**

<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/1f6de594-672e-4d0c-8daf-2ef443f4d3ee" width="800" height="500"></div>

&nbsp;
&nbsp;

About the locations of the wall inscriptions and the sentiments they describe there seems not to be a clear correlation as seen in the graph below. There is no specific location where a certain sentiment would appear especially often. This could indicate that the location didn’t play a big part of the decision where a person would write their negative or positive opinions about someone. However, the most popular place to scribble some wall inscriptions in general seemed to have been the **peristyle** of the house and then the **“Room y”** in the southern part of the building. I would like to point out that there is also mentioned one negative wall inscription as simply _“Peristyle”_. This is because that wall inscription was only mentioned in Vanhala’s listings where the locations were not mentioned as with so much detail than in Lohmann’s book. 

&nbsp;
&nbsp;

### **<div align="center">The sentiment polarity & the different locations of the wall inscriptions:</div>**

<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/5584a2c7-d301-4372-a598-ce4322f6f7f8" width="800" height="500"></div>

&nbsp;
&nbsp;


Most of the wall inscriptions in the dataset are located in the peristyle of Casa delle Nozze d'Argento, a covered porch consisting of rows of columns, and it typically surrounds a garden or central courtyard. The Casa delle Nozze d'Argento’s peristyle is the rectangular area in the middle of the house marked in the layout below with the letter **“r”**. Even though the house was a private house, most likely owned lastly by Lucius Albucius Celsus, a member of the aristocracy of Pompeii (http://pompeiisites.org/en/archaeological-site/house-of-the-silver-wedding), there would’ve been quite a lot of people inside the house walls. The ancient Roman society depended heavily on slaves, and they would’ve been an important part in running the household in such a big house as Casa delle Nozze d'Argento that would need multiple slaves to do different chores and duties. An important social structure in the ancient Roman society was **the Patronage**: a relationship between a high-ranking aristocrat called patron and his clients. The patron would give protection to the client and their family as well as help with other possible problems, such as giving legal advice and financial help, in exchange of different services, and most importantly, the loyalty of their clients. The clients would regularly visit their patron and such adding to the amount of people roaming around the house. There would’ve been also numerous other people such as family members, relatives and visiting friends. This can explain the wall inscriptions found **inside** Casa delle Nozze d'Argento and might suggest that the writers were either the habitants or invited visitors of the house spending time in the middle area of the house enjoying the garden surrounded by columns. This seems a bit contradictory to our modern idea that graffiti or wall inscriptions are done by outsiders often to the outer parts of the buildings. Considering this, I find it especially interesting and quite funny that someone wrote “Lucio Albucio fellatori” (“To Lucius Albucius cocksucker”) inside Lucius Albucius Celsus’ own house. This makes me ponder the identity of the writer: could it be an unhappy slave or a client that was not pleased with their patron? 


<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/af9c30d8-992d-4718-82ee-3588e4135663"></div>

###### <div align="center">The layout of Casa delle Nozze d'Argento with the wall inscriptions numbered (Lohmann, 2018)</div>


# Problems, biases & alternative solutions

I faced some problems while doing this project. Since there was not a ready dataset openly available online of the wall inscriptions of Casa delle Nozze d'Argento I had to collect such myself manually. This was quite a tiresome part of the project and there is always some possibility of an error in this kind of manual work. The sentiment lexicon I used, _LatinAffectus_, is still lacking quite a lot of Latin words and this of course makes detecting some sentiments harder or impossible. The lemmatizer I used, _Collatinus_, was not my first choice. I wanted to use the Python version of it called _PyCollatinus_- (https://github.com/PonteIneptique/collatinus-python) and thus integrate the lemmatizing in the Python code. I however ran into some problems with this, such as having “a too new” version of Python installed. After a while I decided not to spend any more time battling with _PyCollatinus_ and decided to manually paste the wall inscriptions in the _Collatinus_ application I had downloaded and installed. This new manual part of the project was quite time consuming but necessary to be able to use _LatinAffectus_. _Collatinus_ **_should_** have an English version but still some of the buttons and even the results were in French or sometimes mysteriously in Spanish. Some of the words were not recognized at all and to find their lemmas I once again turned to _philolog.us_ for help. All of this makes it possible that the lemmatized wall inscriptions have some errors. As said this part of the project was time consuming which led to keeping my Python code quite simple. I was planning to create a file containing all of the information of each wall inscription in the dataset as well as make the program go through the file and printing the results in one go. Now the lemmatized wall inscriptions need to be manually pasted in the program one by one but considering the circumstances I am quite pleased with the result. 

Most of the sentiments of the wall inscriptions are detected as neutral (0) but I was quite expecting this. This result could however change if, and when, the _LatinAffectus_ lexicon would be updated with more Latin words and their sentiments. Some of the wall inscriptions are actually names of people and some of them are marked as neutral but some as positive. The reason for this is that many of the names also mean something else, such as _“Augustus”_ which is a name but also means _“majestic”_. These names would be more likely detected as positive sentiments. I do not have a proper idea of how to escape this conundrum. One might delete names completely from the dataset but sometimes it can be difficult to recognise which are names and which are for example meant as an adjective. Of course, the deletion would also take away some of the context of the wall inscriptions which I do not find to be appealing. There is also the question of repetition of words in the wall inscriptions. I didn’t delete the words that were repeated, for example in CIL IV 4197 (“Serene  / Serene / Serene vale”), and this resulted in it getting the highest positive score of the dataset +3.5 because Serenus is an +1 positive adjective in LatinAffectus. I was thinking about how the deletion of repeated words could affect the results but as my primary goal of this project was to test that can sentiment analysis be used in the context of wall inscriptions, I decided to not do anything about them. This could however be something to consider if such research would be done in the future. 

# About the reproducibility of the results

My goal was to make this project and its process as open as possible. This is why I have, hopefully, explained in great detail what I did and why. I have also added the relevant files here in GitHub, such as the _LatinAffectus_ I’ve modified myself, the Python code used in the sentiment analysis and of course the complete dataset. All of these files can contain a lot of “irrelevant” information, but I wanted to leave these because they would shed some light on the decisions I’ve made and the steps I took. Such information is for example Lohmann’s own numbering of the wall inscriptions in their book. I wanted to keep this information so that one could go see for themselves the wall inscriptions in question, if so wanted or needed. 

# References

Lohmann, P. (2018) _Graffiti als Interaktionsform: Geritzte Inschriften in den Wohnhäusern Pompejis_, Berlin, Boston: De Gruyter, 2018. https://doi.org/10.1515/9783110574289

Rose, A. (2018) _Database for The Scratched Voices Begging to be Heard: The Graffiti of Pompeii and Today._ Tempe, AZ: Barrett, the Honors College. 2018 ( tDAR id: 445837) ; https://doi.org/10.6067/XCV8TH8QJ5 

Sprugnoli, Rachele; Passarotti, Marco; Corbetta, Daniela and Peverelli, Andrea. (2020). _LatinAffectus_, ILC-CNR for CLARIN-IT repository hosted at Institute for Computational Linguistics "A. Zampolli", National Research Council, in Pisa. http://hdl.handle.net/20.500.11752/OPEN-527

Sprugnoli, R., Passarotti, M. C., Testori, M., Moretti, G. (2021). _Extending and Using a Sentiment Lexicon for Latin in a Linked Data Framework_, in Proceedings of the Workshops and Tutorials - Language Data and Knowledge 2021 (LDK 2021). Zaragoza, Spain, September 1-4, CEUR Workshop Proceedings, 2021, (Zaragoza, 01-01 September 2021), CEUR Workshop Proceedings (CEUR-WS.org), Zaragoza 2021: 151-164. [10.5281/zenodo.6303164] [http://hdl.handle.net/10807/196024]

Sprugnoli, R., Mambrini, F., Passarotti, M. C., & Moretti, G. (2023). _The Sentiment of Latin Poetry. Annotation and Automatic Analysis of the Odes of Horace._ IJCOL, 9, 53-71.

Vanhala, J. (2019). _Imanis metula es : herjaukset Pompejin seinäkirjoituksissa._ [Master’s thesis, University of Turku]

