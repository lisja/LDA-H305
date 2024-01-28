# Computational Literacy course, autumn 2023 (LDA-H305)

[![DOI](https://zenodo.org/badge/731136786.svg)](https://zenodo.org/doi/10.5281/zenodo.10395676)

This is my final project for the course "Computational Literacy". The topic of this project is **the sentiment analysis of the wall inscriptions found in Casa delle Nozze d'Argento**, a house in the ancient city of Pompeii. It was lastly owned by Lucius Albucius Celsus, a member of the Pompeiian aristocracy. (Ormerod 2007) 

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

The results of the sentiment analysis shows that it can indeed be used in the context of the ancient wall inscriptions. However, it does require quite a lot of effort because there is still a lot of work to be done to get the methods and tools for this kind of research to work. The only proper sentiment lexicon at this time is _LatinAffectus_ that contains a bit over 6 000 Latin adjectives and nouns. However, it does not contain any verbs and the 6 000 words it has, ended up not being enough and thus I had to add some myself. These added words can be seen below. 

### **<div align="center">The words added to _LatinAffectus_:</div>**

<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/ff41e310-b864-4d7e-89a8-7a19d7178de2"></div>

&nbsp;
&nbsp;

A bit surprisingly, when summed up together, the total sentiment score of all of the wall inscriptions was 0,5 and the sentiment polarity was positive. I assumed that the neutral sentiments would be dominant because many of the words in the wall inscriptions were not in LatinAffectus but my first intuition was that the sentiments would be more in the negative direction.


The distribution of the sentiments was as such: from the total 51 of the wall inscriptions in the dataset 24 (47.1 %) were recognized as neutral, 14 (27.5 %) as positive and 13 (25.5 %) as negative. These results can also be viewed in the donut graphs below. It seems that the words that were found in _LatinAffectus_ were all detected correctly, as were also all of the invectives gathered from Vanhala’s work. The large amount of the neutral wall inscriptions can be explained partly by the fact that they were not in _LatinAffectus_ and thus they were automatically detected as neutral. If we would be able to add more words in _LatinAffectus_ the result might be different.

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

Three locations can be distinguished from Casa delle nozze d'argento, where only positive or negative wall inscriptions were present, as can be seen from the figure below. Locations where only positive polarities occurred are the garden ("_Garden 05 Western wall_") and the _cubiculum_ ("_Room x Southern wall_"), both of which have one wall inscription. The garden wall inscription (CIL IV 4219) had a sentiment score of 1 and the _cubiculum_ wall inscription (CIL IV 4215) 0.5. In the _fauces_ corridor ("_Corridor p Western wall_") there is one wall inscription (CIL IV 4158). The sentiment polarity of this is negative and the sentiment score is -1. Since they are only individual wall inscriptions in each of the three locations, no greater generalization can be made based on them regarding the connection between location and emotional contents, but one can still think about the functions of these parts of the house to explain their selection as writing targets.

&nbsp;

### **<div align="center">The sentiment polarity & the different locations of the wall inscriptions:</div>**

<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/5584a2c7-d301-4372-a598-ce4322f6f7f8" width="800" height="500"></div>

&nbsp;
&nbsp;

In order to analyse the locations of the Casa delle nozze d'argento’s wall inscriptions in more detail, one must first focus on the Roman private house in general and its function and operation. Nissinen (2008) describes that a Roman private house was "the center of its owner's social, political and economic life". Unlike in modern times, the Roman private house was partly open to everyone and played an important role in highlighting the host's social status and wealth. (Ormerod 2007) Because private houses were constantly under observation and as objects of visits, the owners were invested in them and specifically wanted to present them to the public. (Simelius 2018)

Wallace-Hadrill (1994) divides the Roman house into different areas according to "grandeur" and accessibility. He also divides the users of the Roman private house into three different groups: the host family (_paterfamilia_), servants and slaves (_servi_), and friends. Wallace-Hadrill has in turn divided the friends into four different groups according to the closeness and the social hierarchy between them and the host family: _familiares_ (closest friends), _amici_ (friends), _clientes_ (clients) and _liberti_ (freed slaves). Only the family and the closest friends had access to the most luxurious and at the same time private parts of the house, while the public areas were often the humblest ones. 

&nbsp;

<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/91611de4-8ac7-4a03-a395-ddff6ecc6d1e"></div>

###### <div align="center">Wallace-Hadrill (1994) & division of the Roman house</div>

The residents of the private house consisted of the family with their servants and slaves. Slaves were an extremely important part of the Roman Empire and without them the entire economic life of the empire would have collapsed. In a large house like Casa delle nozze d'argento, slaves were an important part of the household and everyday life, so logically they also spent time in almost all different parts of the house. (Wallace-Hadrill 1994)

Guests were brought to the private house by the _salutatio_, a morning "greeting visit" related to the old traditions of Roman society. This is based on the hierarchical structure of Roman society and the _patronus_-client tradition that emerged from it. The members of the aristocracy acted as patrons of their lower-status clients and could give them gifts, such as money or goods, in return for example their clients' votes in elections. The relationship between the _patronus_ and the client was considered sacred, indicating its importance and esteem in Roman society. An important part of this tradition was the morning salutation, where the client visited his _patronus_ at his home. (Castren & Andrews 2008) This was a natural opportunity for the _patronus_ to showcase his house and thus his status and wealth. There is no exact information whether the salutation was also used in Pompeii because there was no population of the senatorial class, but considering how important and respected this tradition was in society, it is very possible that it or a similar custom was practiced in Pompeii as well. Besides the salutation and the open nature of the houses, there are other reasons why Roman private houses had many guests: parties and dinners and other social gatherings were held among friends. Both business and public affairs could also be handled in different parts of private houses. (Simelius 2018)


<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/af9c30d8-992d-4718-82ee-3588e4135663"></div>

###### <div align="center">The layout of Casa delle Nozze d'Argento with the wall inscriptions numbered (Lohmann, 2018)</div>

&nbsp;

As mentioned earlier there were three locations with a specific sentiment polarity: **the garden** & **the _cubiculum_** with a positive sentiment polarity and **the _fauces_** with a negative sentiment polarity. Each of the locations have only one wall inscription so a proper generalization or a pattern cannot be drawn based on these but they might still tell us something about the writers of the specific wall inscriptions. 

The gardens of private Roman houses were partially or completely hidden from the public and they functioned as a sort of private relaxation place for the family. (Ormerod 2007) This may have also been the case at Casa delle nozze d'argento’s garden (marked as “05” in the layout) because it is clearly fenced and there is only one entrance from inside the house. Thus, fewer people have had access there, which can tell something about the author of the garden's wall inscription, interpreted as positive. As the garden is placed in the more private area of the house, the writer could be one of the family members, but the content of the wall writing in question says otherwise. The wall inscription found in the garden is CIL IV 4219 "_Albuci bene nos accipis_" (In English: "_Albucius, you received us well_"). This does not seem like something an inhabitant of the house would write and thus the writer is most likely an acquaintance, a client or a friend of the family.

Another location with a completely positive sentiment polarity is "_Room x Southern wall_" (marked as “x” in the layout), which is identified as a _cubiculum_ room. (Ormerod 2007) Cubiculum rooms have generally been considered to be sleeping quarters in a Roman house, but they also had many different functions and they could also be used to receive friends or to take care of other private matters. (Nissinen 2008) Casa delle nozze d'argento’s _cubiculum x_ is in the southernmost part of the house behind the _peristyle_, farthest from the entrance and to get there you have to go through the entire building. This gives me the impression that the room has been used more privately. Only one wall inscription CIL IV has also been found in the room CIL 4215 “_Deli vale_” and has been interpreted as a greeting addressed to a person named Delos. Because there is only one wall inscription found in the _cubiculum_ it suggests that the room was not visited by as many people as other parts of the Casa delle nozze d'argento. The private nature of the _cubiculum_ can indicate that the writer of the wall inscription could be either a family member or a close friend of the family.

A completely negative location in terms of sentiment polarity is Casa delle nozze d'argento’s _fauces_ corridor ("_Corridor p Western wall_"). There is also only one wall inscription CIL IV 4158 "_Pyris fellas_" i.e. "_Pyris, you suck cock_". The corridor’s function has been to connect different parts of the house. (Ormerod 2007) In the case of Casa delle nozze d'argento, the _fauces_ connects the _atrium d_ to the _peristyle r_. Since the _fauces_ corridor has most probably had a good line of sight from both the _atrium_ and the _peristyle_ , I believe it has not been possible to scribble freely or at least completely secretly wall writings there. This may partly explain why only one wall inscription has been found there. Ormerod (2007) sees the _atrium_ as an open space in the Roman house that could be visited by anyone. Thus, there are multiple possibilities for the identity of the writer of the wall inscription in the _fauces_. The residents of the house cannot be ruled out either: Vanhala (2019) interprets the invectives found inside of private houses as part of the mutual slander of the residents. 

In addition to the above-mentioned sentimentally polarized locations, there are clearly visible concentrations of wall inscriptions in Casa delle nozze d'argento. The most popular place for writing wall inscriptions in general seems to have been the _peristyle_ courtyard of the house and its surroundings, where 30 of the 51 wall inscriptions used in this project have been located. This is 58.8% of the entire data. Another clear concentration of wall inscriptions is the _exedra_ ("_Room y_") in the southern part of the building. There are 12 wall inscriptions, which is 23.5% of the material. 


### **<div align="center">The locations of the wall inscriptions:</div>**

<div align="center"><img src="https://github.com/lisja/LDA-H305/assets/93824007/d0abaae6-dffa-45c6-914f-ce6b77199e5a"></div>


Most of the wall inscriptions in the dataset are located in the _peristyle_ of Casa delle Nozze d'Argento, a covered porch consisting of rows of columns, and it typically surrounds a garden or central courtyard. (Simelius 2011) The Casa delle Nozze d'Argento’s _peristyle_ is the rectangular area in the middle of the house marked in the layout above with the letter **“r”**. 

Another concentration of wall inscriptions is the _exedra_ located in the southern part of the house, which is marked on the floor plan with the letter **"y"**. An _exedra_ is an interior space or alcove that is closed on three sides but opens completely on the fourth side, most often into the _peristyle_. It was used, for example, to entertain guests and as a space for conversation. (Castren & Andrews 2008). 

I don't consider it a coincidence that most of the graffiti in the Casa delle nozze d'argento are located in these two places, because both of them have had a social function in entertaining guests and therefore many people have spent time there. 


The open nature of Roman private houses and the large number of people living and visiting them may explain why the wall inscriptions found inside the Casa delle nozze d'argento are so abundant. Their authors were probably either residents of the house (Vanhala 2019) or invited guests who spent time in the central part of the house enjoying the garden surrounded by columns. This seems a bit contradictory to our modern idea that graffiti or wall inscriptions are done by outsiders often to the outer parts of the buildings. Considering this, I find it especially interesting and quite funny that someone wrote “Lucio Albucio fellatori” (“To Lucius Albucius cocksucker”) inside Lucius Albucius Celsus’ own house. This makes me ponder the identity of the writer: could it be an unhappy slave or a client that was not pleased with their patron? 

# Problems, biases & alternative solutions

I faced some problems while doing this project. Since there was not a ready dataset openly available online of the wall inscriptions of Casa delle Nozze d'Argento I had to collect such myself manually. This was quite a tiresome part of the project and there is always some possibility of an error in this kind of manual work. The sentiment lexicon I used, _LatinAffectus_, is still lacking quite a lot of Latin words and this of course makes detecting some sentiments harder or impossible. The lemmatizer I used, _Collatinus_, was not my first choice. I wanted to use the Python version of it called _PyCollatinus_- (https://github.com/PonteIneptique/collatinus-python) and thus integrate the lemmatizing in the Python code. I however ran into some problems with this, such as having “a too new” version of Python installed. After a while I decided not to spend any more time battling with _PyCollatinus_ and decided to manually paste the wall inscriptions in the _Collatinus_ application I had downloaded and installed. This new manual part of the project was quite time consuming but necessary to be able to use _LatinAffectus_. _Collatinus_ **_should_** have an English version but still some of the buttons and even the results were in French or sometimes mysteriously in Spanish. Some of the words were not recognized at all and to find their lemmas I once again turned to _philolog.us_ for help. All of this makes it possible that the lemmatized wall inscriptions have some errors. As said this part of the project was time consuming which led to keeping my Python code quite simple. I was planning to create a file containing all of the information of each wall inscription in the dataset as well as make the program go through the file and printing the results in one go. Now the lemmatized wall inscriptions need to be manually pasted in the program one by one but considering the circumstances I am quite pleased with the result. 

Most of the sentiments of the wall inscriptions are detected as neutral (0) but I was quite expecting this. This result could however change if, and when, the _LatinAffectus_ lexicon would be updated with more Latin words and their sentiments. Some of the wall inscriptions are actually names of people and some of them are marked as neutral but some as positive. The reason for this is that many of the names also mean something else, such as _“Augustus”_ which is a name but also means _“majestic”_. These names would be more likely detected as positive sentiments. I do not have a proper idea of how to escape this conundrum. One might delete names completely from the dataset but sometimes it can be difficult to recognise which are names and which are for example meant as an adjective. Of course, the deletion would also take away some of the context of the wall inscriptions which I do not find to be appealing. There is also the question of repetition of words in the wall inscriptions. I didn’t delete the words that were repeated, for example in CIL IV 4197 (“Serene  / Serene / Serene vale”), and this resulted in it getting the highest positive score of the dataset +3.5 because Serenus is an +1 positive adjective in LatinAffectus. I was thinking about how the deletion of repeated words could affect the results but as my primary goal of this project was to test that can sentiment analysis be used in the context of wall inscriptions, I decided to not do anything about them. This could however be something to consider if such research would be done in the future. 

# About the reproducibility of the results

My goal was to make this project and its process as open as possible. This is why I have, hopefully, explained in great detail what I did and why. I have also added the relevant files here in GitHub, such as the _LatinAffectus_ I’ve modified myself, the Python code used in the sentiment analysis and of course the complete dataset. All of these files can contain a lot of “irrelevant” information, but I wanted to leave these because they would shed some light on the decisions I’ve made and the steps I took. Such information is for example Lohmann’s own numbering of the wall inscriptions in their book. I wanted to keep this information so that one could go see for themselves the wall inscriptions in question, if so wanted or needed. 

# References

Castren, P., & Andrews, J. (Eds.) (2008). Domus Pompeiana: talo Pompejissa : näyttelykirja. Otava

Lohmann, P. (2018) _Graffiti als Interaktionsform: Geritzte Inschriften in den Wohnhäusern Pompejis_, Berlin, Boston: De Gruyter, 2018. https://doi.org/10.1515/9783110574289

Nissinen, L. (2008). Cubicula diurna, nocturna: cubiculum-makuutila latinankielisessä kirjallisuudessa. [Pro gradu -työ / MA thesis, University of Helsinki].

Ormerod, W. J. (2007). Modesty and excess: a comparative analysis of pompeian houses and their relationship to romanitas and luxuria (Master's thesis).

Rose, A. (2018) _Database for The Scratched Voices Begging to be Heard: The Graffiti of Pompeii and Today._ Tempe, AZ: Barrett, the Honors College. 2018 ( tDAR id: 445837) ; https://doi.org/10.6067/XCV8TH8QJ5 

Simelius, S. (2011). Pylväskäytävien suojassa: Pompejilainen peristyylipuutarha sosioekonomisen edustamisen muotona. [Master's thesis, University of Helsinki]. Helsingin yliopisto verkkojulkaisut e-thesis. https://helda.helsinki.fi/items/074ae8f5-c2ca-4e26-9c8c-4f0f6aaff1ad

Simelius, S. (2018). Pompeian peristyle gardens as a means of socioeconomic representation. Helsingin yliopisto.

Sprugnoli, Rachele; Passarotti, Marco; Corbetta, Daniela and Peverelli, Andrea. (2020). _LatinAffectus_, ILC-CNR for CLARIN-IT repository hosted at Institute for Computational Linguistics "A. Zampolli", National Research Council, in Pisa. http://hdl.handle.net/20.500.11752/OPEN-527

Sprugnoli, R., Passarotti, M. C., Testori, M., Moretti, G. (2021). _Extending and Using a Sentiment Lexicon for Latin in a Linked Data Framework_, in Proceedings of the Workshops and Tutorials - Language Data and Knowledge 2021 (LDK 2021). Zaragoza, Spain, September 1-4, CEUR Workshop Proceedings, 2021, (Zaragoza, 01-01 September 2021), CEUR Workshop Proceedings (CEUR-WS.org), Zaragoza 2021: 151-164. [10.5281/zenodo.6303164] [http://hdl.handle.net/10807/196024]

Sprugnoli, R., Mambrini, F., Passarotti, M. C., & Moretti, G. (2023). _The Sentiment of Latin Poetry. Annotation and Automatic Analysis of the Odes of Horace._ IJCOL, 9, 53-71.

Vanhala, J. (2019). _Imanis metula es : herjaukset Pompejin seinäkirjoituksissa._ [Master’s thesis, University of Turku]

Wallace-Hadrill, A. (1994). Houses and Society in Pompeii and Herculaneum. Princeton University Press. https://doi.org/10.2307/j.ctv289dw2n
