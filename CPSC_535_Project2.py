#!/usr/bin/python3

import sys
#takes list of word frequencies and list of pairs of synonyms
#returns dicitonary of first word of each connected synonm group as the key adn the frequency of the synonyms as the value
# -*- coding: utf-8 -*-
def synonym_freq(wf, syn):
    comb = []
    while syn:
       comb = combine(syn, comb)
    syn = comb
    freq = {}
   
    
    for i in syn:
        freq[i[0]] = 0
        for j in i:
            freq[i[0]] += wf[j]  
                
    return freq

#adds arr2 to arr element by elment, removes duplicates, does inplace
def add(arr, arr2):
    
    for x in arr2:
        if x not in arr:
           arr.append((x)) 
   

#combines all synonyms for the two words at space index into one list
def combine(syn, comb):
    
    comb.append([])
    

    add(comb[-1], list(syn.pop(0)))
    arr = comb[-1]
    
    i = 0
    if syn:
        j = 0
        while j < len(arr):
        
            
          
            index = 0
            for i in range(len(syn)):
                if  arr[j] in syn[index]:
                    add(arr, list(syn.pop(index)))
                else:
                    index+= 1
                i += 1
                    
            j += 1
            
        arr.sort() 
    return  comb        



if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise("Error", "No iput file detected")
    wf = {}
    syn = []
    with open(sys.argv[1], 'r', encoding='utf8')  as input: #parses file for inputs, removes any whites spaces from words
                                                                #takes file as command line argument
        
        line  = input.readline()
        example_num = 1
        while line != '':
            if '=' in line:
                end = False                
                  
                while not end:
                    wf_text = line.split('(', 1)[1] #everythng after the first open parenthese
                    tempk = wf_text.split(',', 1)[0]
                    tempv = wf_text.split(',', 1)[1].split(')')[0]
                    key = ''
                    value = ''
                    for i in tempk:

                        if i.isalpha():
                            key += i
                    for i in tempv:
                        if i.isdigit():
                            value += i
                    wf[key] = int(value)
                    line = line.split(')', 1)[1]
                    if '(' not  in line :
                        end =True
                              
                line = input.readline()
                while '=' not in line:
                   
                    line = input.readline()
                    if line == '':
                        raise('EOF', "error didn't find synonym list")
                        
                end = False
                                
                while not end:
                    sy_text = line.split('(', 1)[1] #everythng after the first open parenthese
                    tempk = sy_text.split(',', 1)[0]
                    tempv = sy_text.split(',', 1)[1].split(')')[0]
                    key = ''
                    value = ''
                    for i in tempk:
                        if i.isalpha():
                            key =key + i
                    for i in tempv:
                        if i.isalpha():
                            value += i
                    syn.append((key, value))
                    line = line.split(')', 1)[1]
                    if '(' not  in line :
                        end =True
                print('example#',example_num )
                print('wf = ', wf)
                print('sys = ', syn)
                print('output = ', synonym_freq(wf, syn))
                example_num +=1
            line  = input.readline()
        if example_num == 1:
            raise('EOF', "error didn't find input")
