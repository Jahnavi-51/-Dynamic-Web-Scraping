from rake_nltk import Rake

# Initialize RAKE using English stopwords
r = Rake()

# Sample text to extract keywords from
text = """
Machine learning is a method of data analysis that automates analytical model building.
It is a branch of artificial intelligence based on the idea that systems can learn from data,
identify patterns, and make decisions with minimal human intervention.
"""

# Extract keywords
r.extract_keywords_from_text(text)

# Retrieve keywords with their scores
keywords = r.get_ranked_phrases_with_scores()
print(keywords)
