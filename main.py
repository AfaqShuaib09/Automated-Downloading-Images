#Automating Downloading picture in the Desired directory
# Modules Required
# 1. Mechancical Soup for web scraping
# 2. os for creating the directory
# 3. w.get to download the file
import mechanicalsoup
import os
import wget

# obj to allow to enter command without creating new variables
webbrowser = mechanicalsoup.StatefulBrowser()
url = 'https://www.google.com.pk/imghp'
webbrowser.open(url)
#print(webbrowser.get_url())

# to get html of page
#print(webbrowser.get_current_page())

# target search input
webbrowser.select_form()
#webbrowser.get_current_form().print_summary()

# search for a term
search_term = input("Enter the search term to download Images: ")
webbrowser['q'] = search_term

# submit search
webbrowser.launch_browser()
results = webbrowser.submit_selected()
#print(results.text)

# open search result url
new_url = webbrowser.get_url()
webbrowser.open(new_url)

web_page = webbrowser.get_current_page()
images = web_page.find_all('img')

img_src = [image.get('src') for image in images if image.get('src').startswith('https')]
#print(img_src)

# Making a directory to store images
file_storage_path = os.getcwd()
path = 'C:\\Users\\Afaq\\PycharmProjects\\Mechanical soup\\'
file_storage_path = os.path.join(path, search_term)
try:
    os.mkdir(file_storage_path)
    print(f'Images saved to: {file_storage_path}')

    # Now download images using wget module
    counter = 0
    for img in img_src:
        save_path = os.path.join(file_storage_path, f'{search_term}{str(counter)}.jpg')
        wget.download(img, save_path)
        counter += 1
except Exception as e:
    print('Exception Occurred: Folder Already Exists')
