import tkinter as tk

window = tk.Tk()
window.title(".........`")  #choosing the window title
window.geometry("1280x800")
label = tk.Label(window,text="welcom please enter your name: ")
label.pack()
entry = tk.Entry(window) #taking the name 
entry.pack(pady=20,padx=30) #putting it and a specified place
def click(): #making the function here
    window_2 = tk.Toplevel(window) #creating another window
    window_2.title("......") #choosing the title
    window_2.geometry("1280x800") #choosing the geimetry
    text_box = tk.Text(window_2)
    text_box.pack(pady=50,padx=30)
    name = entry.get() #taking the name
    labell = tk.Label(window_2,text="enter your text here ")
    labell.place(x = 580,y = 10)
    def second():        #choosing the second function 
      
       text = text_box.get("1.0","end")
       words = text.lower()
       words = words.replace(".","")
       words = words.replace("!","")
       words = words.replace("?","")
       words = words.split()
       len_words = len(words)
       length = len(text)
       sentences = 0
       for char in text:
         if char == "?" or char == "!" or char == ".":
             sentences += 1
        
            
       from collections import Counter

       unique = 0
       count = Counter(words)
       most_repeated = count.most_common(1)[0][0]
       for words,num in count.items():
         if num == 1:
              unique += 1
         else:
                continue          
       final = tk.Label(window_2,text=f"length: {length}\n"
       f"words: {len_words}\n"
       f"sentences: {sentences}\n"
       f"most_repeated: {most_repeated}\n"
       f"unique: {unique}\n")
       final.pack()

    button = tk.Button(window_2,text="analyze",command=second)
    button.pack()

button = tk.Button(window,text="please click here",command=click) #putting the button and when pushing it the function happens
button.pack(pady=120,padx=200)







window.mainloop()