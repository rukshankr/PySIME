# coding=utf8
 
import tkinter as tk
#import pygame

root = tk.Tk()
root.geometry("400x200")
root.title("Sinhala IME")

sinhala_vols = {"a": "අ", "aa": "ආ", "ae": "ඇ", "aee": "ඈ", "i": "ඉ", "ii": "ඊ", "u": "උ", "uu": "ඌ",
                "Ru": "ඍ", "Ruu": "ඎ", "Lu": "ඏ", "e": "එ", "ee": "ඒ", "ai": "ඓ", "o": "ඔ", "oo": "ඕ", "au": "ඖ" }

sinhala_consa ={"k": "ක", "kh": "ඛ", "g": "ග", "gh": "ඝ", "'g": "ඟ", "ng" : "න්‍ග",
                "ch": "ච", "chh": "ඡ", "j": "ජ", "jh": "ඣ", "jn": "ඤ", "gn": "ඥ", "'j":"ඦ",
                "t": "ට", "tc": "ඨ", "d": "ඩ", "dh": "ඪ", "nh": "ණ", "'d": "ඬ",
                "th": "ත", "thc": "ථ", "z": "ද", "zh": "ධ", "n": "න", "'z": "ඳ",
                "p": "ප", "ph": "ඵ", "b": "බ", "bh": "භ", "m": "ම", "'b":"ඹ",
                "y": "ය", "r": "ර", "l": "ල", "v": "ව", "w": "ව",
                "x": "ශ", "sh": "ෂ", "s": "ස", "h": "හ", "lh": "ළ", "f": "ෆ" }

sinhala_cons = {"k": "ක්‍", "kh": "ඛ්‍", "g": "ග්‍", "gh": "ඝ්‍", "'g": "ඟ්‍", "ng": "ං", "q":"ඃ",
                "ch": "ච්", "chh": "ඡ්", "j": "ජ්", "jh": "ඣ්", "jn": "ඤ්", "gn": "ඥ්", "'j":"ඦ්",
                "t": "ට්‍", "tc": "ඨ්‍", "d": "ඩ්‍", "dh": "ඪ්‍", "nh": "ණ්‍", "'d": "ඬ්‍",
                "th": "ත්‍", "thc": "ථ්‍", "z": "ද්‍", "zh": "ධ්‍", "n": "න්‍", "'z": "ඳ්‍",
                "p": "ප්‍", "ph": "ඵ්‍", "b": "බ්‍", "bh": "භ්‍", "m": "ම්‍", "'b":"ඹ්‍",
                "y": "ය්‍", "r": "ර්", "l": "ල්‍", "v": "ව්‍", "w": "ව්‍",
                "x": "ශ්‍", "sh": "ෂ්‍", "s": "ස්‍", "h": "හ්‍", "lh": "ළ්‍", "f": "ෆ්‍"}

sinhala_diacs = {"a": "", "aa": "ා", "ae": "ැ", "aee": "ෑ", "i": "ි", "ii": "ී", "u": "ු", "uu": "ූ",
                "Ru": "ෘ", "Ruu": "ෲ", "Lu":"ෟ", "Luu":"ෳ", "e": "ෙ", "ee": "ේ", "ai": "ෛ", "o": "ො", "oo": "ෝ",
                "au": "ෞ"}

def check_vowels (i, n, input_text):
    while n > 0:
        if input_text[i:i+n] in sinhala_vols:
                return n
        n -= 1
    return False

def check_consonants (i, n, input_text):
    while n > 0:
        if input_text[i:i+n] in sinhala_cons:
                return n
        n -= 1
    return False

def convert_to_sinhala(input_text):
    print(input_text)
    output_text = ""
    i = 0
    while i < len(input_text):
        if i+1 < len(input_text):
            if (check_consonants(i, 3, input_text)):
                n = check_consonants(i, 3, input_text)
                print("consonant part:"+ input_text[i:i+n])
                m = check_vowels(i+n, 3, input_text)
                print("vowel part:"+ input_text[i+n:i+m+n])
                if (n and m):
                    output_text += sinhala_consa[input_text[i:i+n]]
                    output_text += sinhala_diacs[input_text[i+n:i+n+m]]
                    i += (n+m-1)
                else:
                    output_text += sinhala_cons[input_text[i:i+n]]
                    i += (n-1)
            elif (check_vowels(i, 3, input_text)):
                n = check_vowels(i, 3, input_text)
                output_text += sinhala_vols[input_text[i:i+n]]
                i += (n-1)
            else:
                output_text += input_text[i]
            i += 1
        else:
            if input_text[i] in sinhala_vols:
                output_text += sinhala_vols[input_text[i]]
            elif input_text[i] in sinhala_cons:
                output_text += sinhala_cons[input_text[i]]
            else:
                output_text += input_text[i]
            i += 1
    print("returning "+ output_text)
    return output_text

text_widget = tk.Text(root, font=("Iskoola Pota", 20), height=10, width=50)
text_widget.pack()

def handle_keypress(event):
    input_text = text_widget.get("1.0", tk.END).strip()
    print("inputting "+ input_text)
    if len(input_text) > 0 and input_text[-1] == ' ':
        # Remove the trailing space from the input text
        input_text = input_text[:-1]
    output_text = convert_to_sinhala(input_text)
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, output_text)


#text_widget.bind('<Key>', handle_keypress)
text_widget.bind("<space>", handle_keypress)

root.mainloop()
