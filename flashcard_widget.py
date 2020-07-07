import ui
import csv
import random
import webbrowser

filename = 'wordlist.csv'
current_word_id = 0
defidx = 2
wordsdb = []
done_cnt = 0

def read_csv_wordlist(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            if len(row) <= defidx+1:
                row.append(False)
            wordsdb.append(row)

def random_next_word():
    allow_disp_done_word = random.random() < 0.1
    current_word_id = random.choice(range(len(wordsdb)))
    while wordsdb[current_word_id][defidx] == True and allow_disp_done_word == False:
        current_word_id = random.choice(range(len(wordsdb)))

    disp_flashcard(wordsdb[current_word_id])

def disp_flashcard(defines):
    print(defines[0] + "\n" + defines[1] + "\n" + defines[2])

def invoke_genius(word):
    open_url = 'mkg5:///search?text=' + word
    webbrowser.open(open_url)

read_csv_wordlist(filename)
random_next_word()
