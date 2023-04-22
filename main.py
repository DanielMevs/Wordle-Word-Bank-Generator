from selenium import webdriver
from selenium.webdriver.common.by import By
from timer import decorator_timer
chrome_path = "<your_chrome_path>"

driver = webdriver.Chrome(executable_path=chrome_path)


START = 63
END = 72
URL = 'https://www.merriam-webster.com/browse/dictionary/b/'


@decorator_timer
def generate_wordbank(page):
    while page < END:
        driver.get(f'{URL}{page}')

        words_in_section = [word.text.lower() for word in driver.find_elements(By.CSS_SELECTOR, 'ul.d-flex.flex-wrap li')]
        for word in words_in_section:
            if len(word) == 5 and word[1] != 'r' and 'a' not in word[1:3] and '-' not in word:
                with open('words.txt', mode='a+') as word_file:
                    word_file.write(word + '\n')
        page += 1


exec_time = generate_wordbank(START)
print(f"Prints after {exec_time} seconds")


