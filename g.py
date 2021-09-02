import sys
import webbrowser

base = "http://www.google.com/search?q="

webbrowser.open(url=f'{base}{"+".join(sys.argv[1:]).replace(" ", "+")}', new=2)
