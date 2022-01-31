from selenium import webdriver

webbrowser = webdriver.Firefox()
webbrowser.get('localhost:8000')

assert 'Django' in webbrowser.title
