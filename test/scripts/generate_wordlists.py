import os
import requests
import random
import sys
import time

TOTAL_COUNT_RANGE = (100, 200)
DUPLICATES_PERCENTAGE_RANGE = (15, 30)

def get_words(max_words=500):
    api_url = f"https://api.datamuse.com/words?ml=technology&max={max_words}"
    response = requests.get(api_url)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch words from Datamuse API")
    
    words = [item['word'] for item in response.json()]
    return words

def generate_wordlist(file_path):
    words = get_words(500)

    total_count = random.randint(*TOTAL_COUNT_RANGE)

    duplicates_percentage = random.randint(*DUPLICATES_PERCENTAGE_RANGE) / 100.0
    duplicates_count = total_count - int(total_count * duplicates_percentage)

    selected_words = random.sample(words, total_count)
    unique_words = selected_words[:total_count - duplicates_count]
    duplicate_words = random.choices(unique_words, k=duplicates_count)

    word_list = unique_words + duplicate_words
    random.shuffle(word_list)

    with open(file_path, "w") as file:
        for word in word_list:
            file.write(word + "\n")

def main(path):
    epoch_time = int(time.time())

    for i in range(5):
        file_name = f"{epoch_time}-{i}.txt"
        file_path = os.path.join(path, file_name)

        generate_wordlist(file_path)

        print(f"Generated file: {file_path}")

if __name__ == "__main__":
    path = sys.argv[1]
    main(path)