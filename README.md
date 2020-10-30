# Predicting ClinVar Classifications Through Bioinformatic Methods
The National Institutes of Health (NIH) maintains a public database of human genetic variants called [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/). The variants are generally classified on a scale that ranges benign, likely benign, uncertain, likely pathogenic, and pathogenic. The clinical classifications are usually manually curated.

This project sought to see if it is possible to replicate the clinical classifications with purely bioinformatic methods. To achieve this, the project ensembles various bioinformatic indicators of protein function and convervation, as well as the frequency of the variants in the general population. For the training and testing of the model, I narrowed down the datasets to those who have a review status that indicates high reliability of the classification ([reference](https://www.ncbi.nlm.nih.gov/clinvar/docs/review_status/)).

# Organization
This repository is organized into four parts.

1. The [Cleanup folder](https://github.com/jcpark376/ClinVar_project/tree/master/Cleanup), which contains the [code](https://github.com/jcpark376/ClinVar_project/blob/master/Cleanup/vc_annot_to_df.ipynb) used to clean up the raw vcf data and exported to a pickled dataframe.
2. The [Models folder](https://github.com/jcpark376/ClinVar_project/tree/master/models), which contains the code for three iterative models as well as the pickled version of the final model.
    * [First Simple Model](https://github.com/jcpark376/ClinVar_project/blob/master/models/first_simple_model.ipynb)
    * [Second Model](https://github.com/jcpark376/ClinVar_project/blob/master/models/second_model.ipynb)
    * [Final Model](https://github.com/jcpark376/ClinVar_project/blob/master/models/third_model.ipynb)
3. The [Evaluations folder](https://github.com/jcpark376/ClinVar_project/tree/master/evaluations), which contains two sub-projects that applies the model, as well as [figures](https://github.com/jcpark376/ClinVar_project/tree/master/evaluations) that well-summarizes the main takeaways from this project.
    * Evaluated data rows with low-confidence targets ([code](https://github.com/jcpark376/ClinVar_project/blob/master/evaluations/evaluate_singles.ipynb))
    * Created a [Streamlit app](https://github.com/jcpark376/ClinVar_project/blob/master/evaluations/stream.py) where users can change the variables to see how it changes chance of DNA variant will be benign vs pathogenic.
4. The [Presentations folder](https://github.com/jcpark376/ClinVar_project/tree/master/Presentation) contains the presentation on this project in PDF and PPTX formats.

# Conclusion
Ensembling many bioinformatic methods is a relatively reliable way to classify DNA variants for their pathogenicity. Also, while majority of manually annotated variants is likley to be accurate, there may be a tendency for truly benign variants to be classified as uncertain.

# Acknowledgements
This project is largely inspired by Kevin Arvai's [Kaggle Dataset](https://www.kaggle.com/kevinarvai/clinvar-conflicting). I used some of his code during the cleanup as well as his raw vcf annotated file, but since this project ended up answering a different research question I did not use his cleaned-up csv file.

Thanks so much, Kevin!