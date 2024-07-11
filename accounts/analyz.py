
import requests
from bs4 import BeautifulSoup
import time
from django.shortcuts import render

# Print the paragraphs

def math_decide(keywordlist):
    horrible_crimes = ["murder", "murders", "killing", "killed", "shooting", "shootings", "rape", "firearm"]
    
    total_count1 = sum(keywordlist[word] for word in keywordlist if word in horrible_crimes)
    total_count2 = sum(keywordlist.values())
    
    print(f"Total count of horrible crimes: {total_count1}")
    print(f"Total count of all crimes: {total_count2}")
    
    if total_count2 == 0:
        print("No data available.")
        return
    
    percentage = (total_count1 / total_count2) * 100
    
    if percentage > 51:
        print("Not safe at all")
    elif percentage < 18:
        print("Safe")
    elif 18 <= percentage <= 30:
        print("Somewhere in the middle")
    else:
        print("Not enough data to process")
    
    for word, count in keywordlist.items():
        if count > 0:
            print(f"{word}: {count} occurrences")

    return 'name'


def contains_crime(paragraph):
    crime_words = [
        "theft", "robbery", "criminal", "burglary", "firearm", "fraud", "embezzlement", "extortion",
        "kidnapping", "assault", "murder", "manslaughter", "arson", "forgery",
        "hijacking", "ransom", "vandalism", "blackmail", "smuggling", "counterfeiting",
        "money laundering", "drug trafficking", "cybercrime", "identity theft",
        "carjacking", "terrorism", "Sommelier", "Fourie", "bribery", "corruption", "perjury", "money laundering"
    ]

    # Initialize a dictionary to store counts of each crime word
    word_count = {word: 0 for word in crime_words}

    # Split paragraph into words
    words = paragraph.lower().split()

    # Count occurrences of each crime word
    for word in words:
        if word in word_count:
            word_count[word] += 1

    # Print out the counts
    for word, count in word_count.items():
        if count > 0:
            print(f"{word}: {count}")

    # Call math_decide function to compute total count of horrible crimes
    return word_count



key_paragraphs = []



import random

def scrape_paragraphs_from_multiple_urls(urls):
    try:
        all_paragraphs = []
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        ]
        headers = {'User-Agent': ''}
        
        for url in urls:
            print("Processing URL 1 <@:", url)  # Moved this print statement inside the loop
            headers['User-Agent'] = user_agents[len(all_paragraphs) % len(user_agents)]
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            content = response.content.decode('utf-8', errors='ignore')
            soup = BeautifulSoup(content, 'html.parser')
            paragraphs = soup.find_all('p')
            
            for paragraph in paragraphs:
                paragraph_text = paragraph.get_text()
                all_paragraphs.append(paragraph_text)
                
            time.sleep(1)
        
        print("Paragraphs scraped successfully.")  # Moved this print statement outside the loop
       
    except Exception as e: 
       pass

    string_of_words = " "
    for i, paragraph in enumerate(all_paragraphs, start=1):
         strings = str(paragraph)
         string_of_words += strings
         key_paragraphs.append(strings)

    print(string_of_words +" "+ "add30")
    contains_crime(string_of_words)
    
urls = []
print('new',urls)

print(key_paragraphs)

from googlesearch import search

def get_google_links(query, num_results=10,country="ZA"):

    time.sleep(20)
    try:
        # Perform the Google search
        search_results = search(query)
        
        # Return the links
        return search_results
    except Exception as e:
        print("An error occurred:", e)
        return []

import requests

def ignore_tripadvisor(sentence):
    count = 0
    tripadvisor_string = ""
    for i in sentence:
        tripadvisor_string+=i
        count+=1
        if count == 23:
            break
    return tripadvisor_string

def count_words_in_link(sentence, url):
        tripadvisor_string = ignore_tripadvisor(url)
        print(tripadvisor_string)
        if tripadvisor_string == "https://www.tripadvisor":
         pass
        else:
         
         response = requests.get(url)
        
        # Convert response text to lowercase for case-insensitive comparison
         url_text = response.text.lower()
        
        # Split the sentence into individual words
         words = sentence.split()

        # Initialize a dictionary to store word counts
         word_counts = {word.lower(): 0 for word in words}
        
        # Count how many times each word appears in the URL text
         for word in words:
             word_counts[word.lower()] += url_text.count(word.lower())
        
         return {
            "url": url,
            "word_counts": word_counts
         }
   
province_or_state = "cape town"
place = "khayelitsha"
query =f"crime in {place} {province_or_state}"
num_results = 1  # Number of results you want to retrieve
links = get_google_links(query, num_results)
count = 0
for i, link in enumerate(links, start=1):
    count += 1
    if count < 40:
     
      urls.append(link)
      print(f"{i}. {link}")
    else:
        
         break

sentence = query
urls_ = urls

for url in urls_:
    try:   
        tripadvisor_string = ignore_tripadvisor(url)

        details = count_words_in_link(sentence, url)
        print(tripadvisor_string)

        if details:
            print(f"Details for URL: {details['url']}")
            for word, count in details['word_counts'].items():
                if word.lower() == place.lower():
                    if count >= 1:
                        pass
                    #print(url)
                    else:
                        urls = [ele for ele in urls if ele != url]
                        print("Removed URL:", url)  # Add this print statement
                        print("Remaining URLs:", urls)  # Add this print statement

                elif word.lower() == province_or_state.lower():
                    print('CA')

                print(f"'{word}' appears {count} times in the URL text.")
            print()
        else:
            print(f"No details available for URL: {url}")
            if tripadvisor_string == "https://www.tripadvisor":
                urls = [ele for ele in urls if ele != url]
                print('removed ',url)
    except Exception as e:
       
        print("An exception occurred: 8", e)  # Add this print statement
        print("Exception occurred for URL 4:", url)  # Add this print statement
