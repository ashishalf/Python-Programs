from langdetect import detect

txt = input("enter any text in any language: ")
print(detect(txt))