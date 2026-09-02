# Spam Email Classification Assignment

## Files Included
- `spam_classifier.py`: Python script implementing spam classification using Scikit-learn
- `spambase.data`: Dataset downloaded from UCI Machine Learning Repository
- `analysis.txt`: 300-word analysis covering the problem solved, model performance, and ethical considerations
- `readme.md`: Original assignment description

## How to Run
1. Ensure Python 3.x and required packages are installed (scikit-learn, pandas, numpy)
2. Run: `python spam_classifier.py`
3. The script will:
   - Download the Spambase dataset (if not already present)
   - Train a Naive Bayes classifier
   - Evaluate performance using accuracy, precision, recall, and F1-score
   - Display results including a confusion matrix

## Dataset Source
Spambase dataset from UCI Machine Learning Repository:
https://archive.ics.uci.edu/ml/datasets/Spambase
- 4601 emails with 57 features each
- Features include word frequencies, character frequencies, and capital letter sequences
- Target variable: 0 = not spam, 1 = spam

## Model Used
Gaussian Naive Bayes classifier from Scikit-learn
- Chosen for its simplicity and effectiveness with this type of data
- Assumes features follow a normal distribution
- Works well for text classification tasks

## Performance Results
As shown in analysis.txt:
- Accuracy: 83.39%
- Precision: 71.78%
- Recall: 95.32%
- F1-Score: 0.8189

The model shows strong ability to detect spam (high recall) with moderate precision, indicating it errs on the side of caution by flagging potential spam rather than missing it.

## Ethical Considerations
As discussed in analysis.txt:
- Dataset may be outdated (1999) and not reflect modern spam techniques
- False positives could lead to missing important communications
- Potential bias against certain writing styles or demographics
- Transparency concerns with automated filtering decisions
- Broader societal impact of content moderation

## References
- Scikit-learn documentation: https://scikit-learn.org/
- UCI Machine Learning Repository: https://archive.ics.uci.edu/