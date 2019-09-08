import os
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import threading

def calc(name):

    l2 = Label(window, text='Running...')
    l2.grid(column=0, row=1)
    l2.configure(background='white', font=("Arial Bold", 20))

    element_words = []    

    for w in words:
        eword = ''
        c = 0
        complete = False
        while not complete:
            found = False
            c2 = w[c:c+2]
            for e in elements2:
                if c2 == e.lower():
                    found = True
                    c += 2
                    eword += e
                    break       

            if not found:    
                c1 = w[c:c+1]
                for e in elements1:
                    if c1 == e.lower():      
                        found = True
                        c += 1
                        eword += e
                        break          
                    
            if not found:
                complete = True

            if found and c == len(w):
                complete = True
                element_words.append(eword)

    l2.configure(text='Pass 1 complete')

    element_words2 = []

    for w in words:
        eword = ''
        c = 0
        complete = False
        while not complete:
            found = False
            c1 = w[c:c+1]
            for e in elements1:
                if c1 == e.lower():      
                    found = True
                    c += 1
                    eword += e
                    break

            if not found:
                c2 = w[c:c+2]
                for e in elements2:
                    if c2 == e.lower():
                        found = True
                        c += 2
                        eword += e
                        break
                          
                    
            if not found:
                complete = True

            if found and c == len(w):
                complete = True
                element_words2.append(eword)

    l2.configure(text='Pass 2 complete. Sorting...')


    infirst = set(element_words)
    insecond = set(element_words2)

    diff = insecond - infirst

    element_words = element_words + list(diff)

    def order(e):
        return words.index(e.lower())
    def alph(e):
        return e.lower()

    element_words.sort(key = order)

    l2b = Label(window, text='Finished')
    l2b.grid(column=0, row=3)
    l2b.configure(background='white', font=("Arial Bold", 20))

    elemlen1 = 'Words that can be written using'
    l3 = Label(window, text=elemlen1)
    l3.grid(column=0, row=4)
    l3.configure(background='white', font=("Arial Bold", 20))

    ewL = []
    for w in element_words:
        ewL.append(w.lower())
    ewset = set(ewL)

    elemlen2 = 'only element symbols: ' + str(len(ewset))
    l4 = Label(window, text=elemlen2)
    l4.grid(column=0, row=5)
    l4.configure(background='white', font=("Arial Bold", 20))

    with open('element_words.txt', 'w') as savefile:
        for w in element_words:
            savefile.write('%s\n' % w)

    os.startfile('element_words.txt')
    
#----------------------------------------------------------------
    
window = Tk()
window.title("Element Writer")
window.geometry('500x300')
window.configure(background='white')

r = threading.Thread(target=calc, args=(1,), daemon=True)

def run():
    r.start()

def begin(): 
    wfile = filedialog.askopenfilename()
    load(wfile)

def load_words(file):
    with open(file) as word_file:
        valid_words = list(word_file.read().split())
    return valid_words

def load(wfile):
    global words
    words = load_words(wfile)
    global elements
    elements = load_words('elements.txt')

    dictlen = 'Words in dictionary: ' + str(len(words))
    l1 = Label(window, text=dictlen)
    l1.grid(column=0, row=0)
    l1.configure(background='white', font=("Arial Bold", 20))

    global elements1
    elements1 = []
    global elements2
    elements2 = []

    for e in elements:
        if(len(e)==1):
            elements1.append(e)
        if(len(e)==2):
            elements2.append(e)

    btn = Button(window, text="Run", command=run) 
    btn.grid(column=0, row=1)
    

sbtn = Button(window, text="Choose dictionary", command=begin) 
sbtn.grid(column=0, row=0)


window.mainloop()

