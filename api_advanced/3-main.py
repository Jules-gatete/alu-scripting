#!/usr/bin/python3
"""
3-main
"""
import sys

if __name__ == '__main__':
    count_words = __import__('3-count').count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        original_keywords = sys.argv[2].split()
        keywords = [x.lower() for x in original_keywords]  # Convert keywords to lowercase
        result = count_words(subreddit, keywords)

        # Print the result using original keyword casing
        for original_keyword, count in result.items():
            print(f"{original_keyword}: {count}")

