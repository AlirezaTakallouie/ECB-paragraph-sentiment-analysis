# ECB Text Analysis Project

In this project, I analyzed an ECB monetary policy press conference from December 12, 2024.

First, I scraped the text from the ECB website using Python. Then I cleaned the text and saved it into a TXT file.

After that, I split the text into paragraphs and analyzed each paragraph separately using TextBlob to get a sentiment score.

I also counted the most frequent words and created a word cloud.

## Tools used
- Python
- requests
- BeautifulSoup
- pandas
- TextBlob

## Output
- paragraph_sentiment.csv
- word_frequencies.csv
- wordcloud.png

## Summary
The text is mostly neutral, which makes sense because it is a formal central bank communication. Some parts are slightly positive or negative depending on the economic outlook and policy discussion.