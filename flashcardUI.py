import ui
import sys
import csv
import random
import argparse
import io
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

def write_csv_wordlist(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(['Word','Pronunciation','Definition'])
        
        for row in wordsdb:
            writer.writerow(row)

def random_next_word():
    allow_disp_done_word = random.random() < 0.1
    current_word_id = random.choice(range(len(wordsdb)))
    while wordsdb[current_word_id][defidx] == True and allow_disp_done_word == False:
        current_word_id = random.choice(range(len(wordsdb)))

    disp_flashcard(wordsdb[current_word_id])

def done_tapped(sender):
    global wordsdb, done_cnt
    '@type sender: ui.Button'
    t = sender.title
    if t == 'Done':
        wordsdb[current_word_id][defidx+1] = True
        random_next_word()
        done_cnt += 1
        if done_cnt > 10:
            write_csv_wordlist(filename)
            done_cnt = 0
    elif t == 'Yet':
        wordsdb[current_word_id][defidx+1] = False
        random_next_word()
    elif t == 'Genius':
        invoke_genius(wordsdb[current_word_id][0])
    else:
        print('dontknow')

def disp_flashcard(defines):
    word_lbl.text = defines[0]
    pron_lbl.text = defines[1]
    define_lbl.text = defines[defidx]

def invoke_genius(word):
    open_url = 'mkg5:///search?text=' + word
    webbrowser.open(open_url)

v = ui.load_view()
v.present('sheet')

word_lbl = v['wordlabel']
pron_lbl = v['pronlabel']
define_lbl = v['deflabel']
done_btn = v['donebutton']
yet_btn = v['yetbutton']
done_btn.action = done_tapped
yet_btn.action = done_tapped


read_csv_wordlist(filename)
random_next_word()

"""
print(wordsdb[current_word_id])
wordsdb[current_word_id][3] = True
print(wordsdb[current_word_id])
"""

