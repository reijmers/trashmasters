import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import youtube_vids_comments 
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import seaborn as sns
import nltk
nltk.download('punkt')
nltk.download('stopwords') 

#opening all files
vid1 = pd.read_csv("comments_0JtoSafhvLM.csv")
vid2 = pd.read_csv("comments_DabP0adyVqw.csv")
vid3 = pd.read_csv("comments_JCyRZA2xA1Q.csv")
vid4 = pd.read_csv("comments_xFcOEZSoGv0.csv") 

#combining all comments into 1 dataframe
dfs = [vid1, vid2, vid3, vid4]
combined_df = pd.concat(dfs, ignore_index=True)

# getting all video ids
#video_ids = youtube_vids_comments.final_ids() ISSUE WITH API SO DOESNRT CURRENTLY WORK
video_ids = ['0JtoSafhvLM', 'DabP0adyVqw', 'JCyRZA2xA1Q', 'xFcOEZSoGv0']

#FOR WORD FREQUENCY
# Tokenize and remove stopwords
languages = ['english', 'dutch']
stop_words = set([word for lang in languages for word in stopwords.words(lang)])
combined_df['tokenized_text'] = combined_df['text'].apply(lambda x: word_tokenize(str(x)))
combined_df['filtered_text'] = combined_df['tokenized_text'].apply(lambda x: [word.lower() for word in x if word.isalpha() and word.lower() not in stop_words])

# Calculate word frequencies
all_words = [word for sublist in combined_df['filtered_text'] for word in sublist]
freq_dist = FreqDist(all_words)

# Create a table showing word frequencies
word_freq_df = pd.DataFrame(list(freq_dist.items()), columns=['Word', 'Frequency'])
word_freq_df = word_freq_df.sort_values(by='Frequency', ascending=False)

# Display the table
csv_filename = 'word_frequences_YT'
word_freq_df.to_csv(csv_filename, index = False)

top_15_word_freq_df = word_freq_df.head(15)
top_15_csv_filename = 'top_15_word_frequencies.csv'
top_15_word_freq_df.to_csv(top_15_csv_filename, index=False)

# Visualize the top 15 word frequencies using a bar plot
plt.figure(figsize=(10, 6))
plt.bar(top_15_word_freq_df['Word'], top_15_word_freq_df['Frequency'], color='skyblue')
plt.title('Top 15 Word Frequencies')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot as an image (optional)
plot_filename = 'top_15_word_frequencies_plot.png'
plt.savefig(plot_filename)

# Show the plot
plt.show()


## Number of comments per video scraped:

#getting nb of comments per video
nb_comments = [len(vid1), len(vid2), len(vid3), len(vid4)]
print(nb_comments)

avg_nb = sum(nb_comments) // len(nb_comments) 

print(avg_nb)

#create figure showeing nb of relevant comments per video
plt.figure(figsize=(12, 6))
plt.bar(video_ids, nb_comments, color = 'skyblue')
plt.title('Number of Relevant Comments Per Video')
plt.xlabel('Video ID')
plt.ylabel('Number of Comments')
plt.xticks(rotation=45, ha='right')
plt.show()



##Creating a table for the most liked comments

sorted_df = combined_df.sort_values(by="like_count", ascending = False)
csv_filename2 = 'most_liked_comments_YT'
sorted_df.to_csv(csv_filename2, index = False)
print(sorted_df['text'].head())