# VADER Sentiment Analyzer 

A simple, user-friendly desktop application built with Python to perform sentiment analysis using the VADER (Valence Aware Dictionary and sEntiment Reasoner) library, presented through a clean Tkinter Graphical User Interface (GUI).

## Features

* **Real-time Analysis:** Analyze input text instantaneously upon clicking the "Analyze" button.
* **VADER Integration:** Leverages the robust VADER model for scoring social media and general text.
* **Detailed Scoring:** Displays percentage scores for Positive, Negative, and Neutral components.
* **Clear Classification:** Provides a definitive sentiment label: Positive Sentiment, Negative Sentiment, or Neutral Sentiment.
* **Intuitive GUI:** Uses Tkinter for providing an Interactive Theme.

## Prerequisites

To run this application, you need to have Python 3.x installed.

The following libraries are required:

* tkinter
* vaderSentiment



## Installation

1.  **Clone the repository:**
    ```bash
    git clone [Your Repository URL]
    cd [Your Repository Name]
    ```
2.  **Install dependencies:**
    ```bash
    pip install vaderSentiment
    ```

## Running the Application
Run the Application by the following command:
```bash
python vader_sentiment_analyzer.py
```
## How to Use

​The main window titled "VADER Sentimental Analysis" will appear.   
* Enter the sentence or text you wish to analyze into the large text area.  
* Click the Analyze button.  
* A popup window will display the analysis results, showing the final sentiment classification and the percentage breakdown of Positive, Negative, and Neutral scores.  
* Click Close to dismiss the results and continue analyzing new text.  

## References

Hutto, C., & Gilbert, E. (2014). VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text. Proceedings of the International AAAI Conference on Web and Social Media, 8(1), 216-225. [Link to the paper](https://doi.org/10.1609/icwsm.v8i1.14550)
```bash
