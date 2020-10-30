# Predicting ClinVar Classifications Through Bioinformatic Methods
The National Institutes of Health (NIH) maintains a public database of human genetic variants called [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/). The variants are generally classified on a scale that ranges benign, likely benign, uncertain, likely pathogenic, and pathogenic. The clinical classifications are usually manually curated.

This project sought to see if it is possible to replicate the clinical classifications with purely bioinformatic methods. To achieve this, the project ensembles various bioinformatic indicators of protein function and convervation, as well as the frequency of the variants in the general population. For the training and testing of the model, I narrowed down the datasets to those who have a review status that indicates high reliability of the classification ([reference](https://www.ncbi.nlm.nih.gov/clinvar/docs/review_status/)).

# Organization
This repository is organized into four parts.

1. The [Cleanup folder]
2. The [Models folder]
3. The [Evaluations folder]
4. The [Presentations folder]

This repository is organized into four parts.
1. The [WebScraper folder](https://github.com/jcpark376/project2-wikipedia/tree/master/WebScraper), which contains the [code](https://github.com/jcpark376/project2-wikipedia/blob/master/WebScraper/webscraper.ipynb) used to scrape Wikipedia html documents using the Random Article feature on Wikipedia. There is also [code](https://github.com/jcpark376/project2-wikipedia/blob/master/WebScraper/articledateget.ipynb) to collect the date of a given article's first creation.

2. The [Models folder](https://github.com/jcpark376/project2-wikipedia/tree/master/Models). There are three interrelated (but meant to be run sequentially) approaches and their corresponding code.
    * Modeling using 10 select features.
        * [code](https://github.com/jcpark376/project2-wikipedia/blob/master/Models/TenFeatures/features2.ipynb)
    * Modeling using Natural Language Processing (NLP).
        * [code for data_extracting](https://github.com/jcpark376/project2-wikipedia/blob/master/Models/NLP/nlp_dataextract.ipynb)
        * [code for modeling](https://github.com/jcpark376/project2-wikipedia/blob/master/Models/NLP/nlp_model.ipynb)
    * A combination of the two approaches.
        * [code](https://github.com/jcpark376/project2-wikipedia/blob/master/Models/FinalModel/final_model.ipynb)

3. The [Conclusions folder](https://github.com/jcpark376/project2-wikipedia/tree/master/Conclusions). This contains the [presentation](https://github.com/jcpark376/project2-wikipedia/blob/master/Conclusions/Presentation-Revised.pdf) that summarizes the findings as well as [select figures](https://github.com/jcpark376/project2-wikipedia/tree/master/Conclusions/FIgures). 

4. The [wikiarticles folder](https://github.com/jcpark376/project2-wikipedia/tree/master/wikiarticles), which has the html files that the WebScraper module scraped.

# Conclusion

# Acknowledgements
This project is largely inspired by Kevin Arvai's [Kaggle Dataset](https://www.kaggle.com/kevinarvai/clinvar-conflicting). I used some of his code during the cleanup as well as his raw vcf annotated file, but since this project ended up answering a different research question I did not use his cleaned-up csv file.

Thanks so much, Kevin!