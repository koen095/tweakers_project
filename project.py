# TO DO: Import relevant modules
import webbrowser

# TO DO: Get the search url
base_url = "https://tweakers.net/pricewatch/zoeken/?keyword="

# Ask for the user input, add a '+' in case there are whitespaces in the search
user_search_input = input("What would you like to search for in the pricewatch?\n").split()
separator = '+'
search_url = separator.join(user_search_input)
full_url = f"{base_url}{search_url}"


# TO DO: open website and display search results
webbrowser.open(full_url)
# TO DO: Return search results
# TO DO: add html elements so the search results are clickable
# TO DO: Create esthetically pleasing pysimplegui