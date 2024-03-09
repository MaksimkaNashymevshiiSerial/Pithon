import os
import pandas as pd

data = pd.read_csv('D:\\Альбрехт Максим\\word.csv',sep=';')
print(data)
a = data['tag'].value_counts(sort=True).to_list
#print(a)
animal = data[data['tag'] == 'ANIMAL']
print(animal)
animal_words = animal[animal['term'].str.len().between(6,50)]
print(animal_words)
animal_list = animal_words['term'].to_list()
print(animal_list)