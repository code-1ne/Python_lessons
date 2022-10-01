import webbrowser


def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Неверный юрл!")
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)

open_url("https://github.com/code-1ne/Python_lessons")