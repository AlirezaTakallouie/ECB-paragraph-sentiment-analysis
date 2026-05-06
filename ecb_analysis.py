import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd

# ECB press conference URL
url = "https://www.ecb.europa.eu/press/press_conference/monetary-policy-statement/2024/html/ecb.is241212~ce143b3bc8.en.html"

# Download webpage
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find main content
main_content = soup.find("main")

# Extract paragraphs
paragraphs_html = main_content.find_all("p")

# Create clean text
clean_text = "\n\n".join(
    paragraph.get_text(strip=True)
    for paragraph in paragraphs_html
)

# Save cleaned text
with open("Data/ecb_press_conference.txt", "w", encoding="utf-8") as file:
    file.write(clean_text)

print("Clean ECB press conference text saved successfully")

# Read cleaned text file
with open("Data/ecb_press_conference.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split text into paragraphs
paragraphs = text.split("\n\n")

# Remove empty paragraphs
paragraphs = [p for p in paragraphs if p.strip()]

# Print number of paragraphs
print("Number of paragraphs:", len(paragraphs))

# Paragraph-level sentiment analysis
results = []

for i, paragraph in enumerate(paragraphs, start=1):

    # Sentiment score
    sentiment_score = TextBlob(paragraph).sentiment.polarity

    # Store results
    results.append({
        "paragraph_number": i,
        "paragraph_text": paragraph,
        "sentiment_score": sentiment_score
    })

# Convert results into DataFrame
df_sentiment = pd.DataFrame(results)

# Save CSV file
df_sentiment.to_csv(
    "Output/paragraph_sentiment.csv",
    index=False,
    encoding="utf-8"
)

print("Paragraph sentiment CSV saved successfully")
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# Combine all paragraphs into one text
full_text = " ".join(paragraphs)

# Convert to lowercase
full_text = full_text.lower()

# Remove punctuation and numbers
full_text = re.sub(r"[^a-zA-Z\s]", "", full_text)

# Split into words
words = full_text.split()

# Define stop words
stop_words = {
    "the", "and", "to", "of", "in", "a", "for", "on",
    "is", "we", "our", "will", "that", "are", "be",
    "with", "by", "as", "at", "have", "has", "this",
    "it", "from", "their", "they", "an"
}

# Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# Count word frequencies
word_counts = Counter(filtered_words)

# Convert to DataFrame
df_words = pd.DataFrame(
    word_counts.items(),
    columns=["word", "frequency"]
)

# Sort by frequency
df_words = df_words.sort_values(
    by="frequency",
    ascending=False
)

# Save frequent words CSV
df_words.to_csv(
    "Output/word_frequencies.csv",
    index=False,
    encoding="utf-8"
)

print("Word frequency CSV saved successfully")

# Generate word cloud
wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color="white"
).generate(" ".join(filtered_words))

# Create figure
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

# Save word cloud image
plt.savefig("Output/wordcloud.png")

print("Word cloud image saved successfully")