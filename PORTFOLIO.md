# Portfolio copy

## Project title

Gojek Review Sentiment Analysis

## One-sentence summary

Built an Indonesian sentiment-analysis workflow for Gojek app reviews using TF-IDF and machine learning, with a tuned Linear SVM recording 90.13% test accuracy on rating-derived labels.

## Project summary

Developed a Python workflow to analyze Indonesian user reviews of the Gojek Android app collected from Google Play. The recorded experiment starts with 8,000 reviews and produces 5,113 distinct, nonempty preprocessed samples with positive or negative labels derived from star ratings. Applied text cleaning, informal-word normalization, stopword removal, and Sastrawi stemming, then compared Naive Bayes, Logistic Regression, Linear SVM, and Random Forest through TF-IDF pipelines. Tuned Linear SVM with three-fold grid search and recorded 90.13% accuracy on a 1,023-review test split. Presented model comparisons, classification reports, confusion-matrix analysis, and example predictions in Jupyter Notebook.

## Outputs to showcase

| Priority | Output | What it demonstrates |
|---|---|---|
| Lead visual | [Model comparison chart](assets/model-comparison.png) | A consistent comparison of four baseline classifiers. |
| Main result | Notebook sections 14–15: tuned SVM report and final model selection | 90.13% recorded test accuracy, approximately 0.90 F1 for each class, and the selected parameters. |
| Evaluation visual | [Untuned Linear SVM confusion matrix](assets/linear-svm-confusion-matrix.png) | Error analysis for the 89.83% baseline; label it explicitly as untuned. |
| NLP workflow | Notebook section 7: preprocessing functions | Indonesian text cleaning, normalization, stopword removal, and stemming. |
| Prediction demonstration | Notebook section 16: four example reviews and predictions | How the workflow processes new positive and negative text. |
| Supporting visual | [Sentiment distribution](assets/sentiment-distribution.png) | Positive/negative label counts after excluding 3-star reviews, before text deduplication. |
| Supporting visual | [Rating distribution](assets/rating-distribution.png) | The original sample's rating distribution. |
| Reproducibility | Scraper, notebook, and pinned requirements | A documented path from data collection to model evaluation and export. |

## Technologies used

Python; Jupyter Notebook; google-play-scraper; pandas; NumPy; regular expressions; Sastrawi; scikit-learn; TF-IDF; Multinomial Naive Bayes; Logistic Regression; Linear SVM; Random Forest; GridSearchCV; Matplotlib; Seaborn; Joblib.

## Suggested portfolio bullets

- Collected 8,000 Indonesian Google Play reviews and prepared 5,113 cleaned, deduplicated samples for binary sentiment classification.
- Compared four TF-IDF classification pipelines and tuned Linear SVM across 18 parameter combinations using three-fold cross-validation.
- Recorded 90.13% test accuracy and presented class-level metrics, baseline error analysis, and sample predictions.

## How to describe the results accurately

The metrics come from saved notebook outputs and have not been rerun during repository preparation. Labels are rating-based proxies rather than manually annotated sentiment. Keep that qualification next to the result when presenting the project. The saved confusion matrix is for the untuned SVM, and the project has no deployed web app or API.

The model file and cleaned dataset are generated locally by the notebook and are not included in the public repository. Do not showcase raw reviewer identities or claim the serialized model includes raw-text preprocessing.
