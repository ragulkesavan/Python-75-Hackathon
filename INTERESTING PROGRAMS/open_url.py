#OPENING A WEBPAGE IN NEW TAB IN BROWSER OF GIVEN URL
'''
The webbrowser module in Python provides an interface to display Web-based documents.
webbrowser.open_new_tab(url)
Open url in a new page (“tab”) of the default browser, if possible, 
otherwise equivalent to open_new().
'''
import webbrowser
webbrowser.open_new_tab("https://www.pythonforbeginners.com/code-snippets-source-code/python-webbrowser")
