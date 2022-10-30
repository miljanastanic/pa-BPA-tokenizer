#pip install wikipedia

import wikipedia
from functools import reduce
from itertools import starmap
import random
import multiprocessing as mp
import numpy as np
#import functools import partial

#-------------1-zadatak----------------------------------------

wikipedia.set_lang("en")  
_
def get_pages(query, results=25):

  titles = wikipedia.search(query, results=results)
  pages = []
  pages.clear()

  for title in titles:
    try:
      page = wikipedia.page(title)
      page =  wikipedia.summary(page, sentences = 5)
      pages.append((title, page))
    except wikipedia.DisambiguationError as e:
      print(e.options)
    except wikipedia.exceptions.PageError as e:
      print(e)

  return pages

keys =  ['Beograd', 'Prvi svetski rat', 'Protein', 'Mikroprocesor', 'Stefan Nemanja', 'Košarka']

def keysMap(keys):
  return (keys, get_pages(keys))

def funreduce(array, tuples):
  key, value = tuples
  return array + value


pool = mp.Pool(mp.cpu_count())
solutions = pool.map(keysMap, keys)
solutions2 = list(reduce(funreduce, solutions, []))

#print('Solutions', solutions)
print('Solutions2, kraj 1 zadatka', solutions2)

#-------------2-zadatak----------------------------------------

def reduceSplitString(array, tuple):
  niz = []
  key, value = tuple
  niz.append((key, list(value)))
  return array + niz


def removeSym(array, c):
  if (c == '!' or c == '?' or c == '=' or c == '-' or c == ',' or c == '.' or c == '$' or  c == '(' or c == ')' or c == '[' or c == ']'):
    return array
  else:
    return array + c

def removeSpace(array, c):
  if(c == ' ' or c == "\n" or c == "\t"):
    #if c and array[-1] != '$':
    return array + '$'  
  else:
    return array + c

def reduceArr(array, c): 
  if len(array) < 100000:
    return array + c
  else: 
    return array

def allFour(niz):

  if (niz == []):
    return []
  outputNiz = []
  outputNiz = list(map(lambda x: x.lower(), niz))
  #print(outputNiz)

  outputReduce = []
  outputReduce = list(reduce(removeSym, outputNiz))

  outputReduce2 = []
  outputReduce2 = list(reduce(removeSpace, outputReduce) + '$')

  outputReduce3 = []
  outputReduce3 = list(reduce(reduceArr, outputReduce2))
  return outputReduce3


def funmaps(tuple):
  key, value = tuple
  text = allFour(value)
  return key, text

splitArr = list(reduce(reduceSplitString, solutions2, []))
solutions3 = list(map(funmaps, splitArr))
print('Resenje 2 zadatka', solutions3)

#-------------3-zadatak----------------------------------------

#1 zahtev
def randomreduce(array, tuples):
  key, value = tuples
  if len(array) < 5:
    return array + [value]
  else: 
    return array 

#zahtev2
def funZahtev2(array,x):
  pomoc = []
  if array:
    pomoc = array[-1]
    duzina = len(array)
    if(pomoc[len(pomoc)-1] == '$'):
      zup = x + x
      array.append(zup)
    else:
      pomocna = []
      pomocna = list(pomoc)
      zup = pomocna[len(pomoc)-1] + x 
      array.append(zup)               
                                      
  else:
    array.append(x)
  return array

#zahtev3
def mapZahtev3(token):
  return token, 1

def reduceZatev3(array, value):
  if array and array[-1][0] == value[0]:
    array[-1] = array[-1][0], array[-1][1] + value[1]
  else:
    array.append(value)
  return array

#zahtev4
def getToken():
  return zahtev3[0][0]

def get_num_tokens():
  return len(list(zahtev3[0][0]))

def getTokenElement(token,i):
  return token[i]  
  

counter = 0
w = ''

def funkcija(array,curr):
  token = getToken()
  #print(token)
  global counter
  global w
  if token[counter] == curr:
    counter += 1
    w += curr
    if counter == len(token):
      array.append(w)
      counter = 0
      w = ''
    
  else:
    if counter > 0:
      counter = 0
      for ch in w:
        array.append(ch)
      w = ''
    array.append(curr)
  return array          


zahtev1 = list(reduce(randomreduce, solutions3, []))
zahtev1 = [rez for red in zahtev1 for rez in red]

for i in range(50):
 
  zahtev2 = list(reduce(funZahtev2,zahtev1,[]))

  zahtev3a = list(map(mapZahtev3, zahtev2))
  z_sort = sorted(zahtev3a, key=lambda x: x[0])
  zahtev3 = list(reduce(reduceZatev3, z_sort, []))
  zahtev3 = sorted(zahtev3, key=lambda x: x[1], reverse=True)

  zahtev4 = list(reduce(funkcija,zahtev1,[]))

  zahtev1 = zahtev4

def Sorting(lst):
    lst2 = list(reversed(sorted(lst, key=len)))
    return lst2

zahtev5 = Sorting(zahtev1)
print('Kraj 3 zadatka', zahtev5)

#-------------4-zadatak----------------------------------------


