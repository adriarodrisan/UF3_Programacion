import os
fd=open('./document.txt', 'r+')
document=input("nombre del documento: ")
os.rename('document.txt',document)
