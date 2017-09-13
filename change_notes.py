#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:20:24 2017

@author: jesusvergaratemprado
"""

import numpy as np

notes_name=['do',]

notes_name=['DO','DO#','RE','RE#','MI','FA','FA#','SOL','SOL#','LA','LA#','SI',
            'DO+','DO#+','RE+','RE#+','MI+','FA+','FA#+','SOL+','SOL#+','LA+','LA#+','SI+']
#notes_number=np.linspace(0,len(notes_name),len(notes_name)+1).tolist()
n_notes=len(notes_name)
notes_dict={}
for i in range(len(notes_name)):
#    print 
    notes_dict[notes_name[i]]=i
print notes_dict


text='Sol re# re mi fa \
Sol re# re mi fa \
Sol la'

t='''
Fa do fa sol sol# sib
Sol# sol fa 
Re# do# sol# sol#

Sol# re# Sol# re# Sol# re# 
Sol# sib sol


Fa do fa sol sol# sib
Sol# sol fa 
Re# do# sol# sol# 

Sol# re# Sol# re# Sol# re# 
Sol# sib sol


Fa fa fa sol sol# sol sol# sol sol# sol fa
Fa fa fa sol sol# sol sol# sol sol# sol re#
Re# re# re# sol# re# sol# re# sol#  sib sib sol

Fa fa fa sol sol# sol sol# sol sol# sol fa
Fa fa fa sol sol# sol sol# sol sol# sol re#
Re# re# re# sol# re# sol# re# sol#  sib sib sol




Sol# sol fa fa
Do do do do do do 
Fa fa fa fa   fa 
Re# fa do

Do do do do do do
Fa fa fa sol sol# re#
Re# Re# Re# Re# 
Sol# sol# sol# sol# sol# sol#
 sib sib sol

Sol# sol fa fa
Do do do do do do 
Fa fa fa fa   fa 
Re# fa do

Do do do do do do
Fa fa fa sol sol# re#
Re# Re# Re# Re# 
Sol# sol# sol# sol# sol# sol#
 sib sib sol

Do# sib Do# sib Do# sib Do# sib Do# sib do# 
Re re sol




'''
t='''
Mi mi fa# sol mi do+ si do sol fa#

Fa# sol la si si la si fa# mi 



mi fa# sol mi do+ si do sol fa#



fa# sol la la si sol 
'''


t='''
Si la si do si la sol si
La si do si la sol si

Do la si sol
Fa# fa# fa# fa# fa#'''



t='''
Fa# sol# sol# sol# la sol# fa# mi fa#
Fa# fa# sol# fa# mi re# mi
Mi mi la re# do#

'''
t='''
FA, SOL, LA 
SOL, LA, SOL, FA, SOL, DO’ 
SIB, LA, FA, RE, DO 
MI, SOL, SOL, LA 
SIB, LA, SOL, FA, SOL,DO’ 
LA, DO’, RE’, DO’, SOL 


 FA, FA, FA, FA, MI, FA 
FA, MI, FA 
SOL, LA, SOL 

FA, FA, FA, FA,MI, FA 
FA, DO

FA SOL 
DO DO’ SIB LA SOL 
LA SIB LA SOL FA MI FA 
MI RE DO 

FA SOL 
DO DO’ SIB LA SOL 
LA SIB LA SOL FA MI FA 
MI MI FA SOL LA SOL 

MI SOL SOL LA 
SIB LA SOL FA SOL DO’ 
LA DO’ DO’ RE’ DO’ SOL 

FA, FA, FA, FA, MI, FA 
FA, MI, FA 
SOL, LA, SIB, LA, SOL 

FA, FA, FA, FA,MI, FA 
FA, DO

FA SOL 
DO DO’ SIB LA SOL 
LA SIB LA SOL 
LA SIB LA SOL FA MI FA 
MI RE DO 

FA SOL 
DO DO’ SIB LA SOL 
LA SIB LA SOL FA MI FA 
MI MI FA SOL LA 
SIB LA SOL 

FA SOL LA 
SOL LA SOL FA SOL DO’ 
SIB LA FA RE DO 

MI SOL SOL LA 
SIB LA SOL FA SOL DO’ 
LA DO’ RE’ 
MI’ FA’ SOL’ 

LA si 
Mi mi’ re’ do#’ si 
Do#’ re’ do#’ si la sol# la 
Sol# fa# mi 

La si 
Mi mi’ re’ do#’ si 
Do#’ re’ do#’ si la sol# la 
Re’ do#’ si la 
Si do# re’ do#’ si la la sol# la 
Si do#’ re’ do#’ si la la

'''
t='''
LA RE fa sol la re 
Fa sol mi
Sol do fa mi sol do 
FA MI RE


La re fa sol la re 
Fa sol mi 

Sol do fa mi sol do 
Fa mi re


La re fa sol la re 
Fa sol mi 

Sol do 
Mi fa mi do re

La sib do re 
DO RE DO 
Sib la sib re SOL SIB LA
La sol fa sib 
FA SOL LA

La sib do re 
DO RE DO 
Sib la sib re SOL SIB LA
La sol fa sib 
FA MI RE

RE LA 
Sib do RE LA 
Sib do RE LA 
Sib do RE LA 
Sib do RE LA 

'''
t='''
La do do do la sib
Do do do do 
Sib la 
Sol sol la 


Fa fa sol la 
Fa sib la 
La la la sol

Re fa fa fa fa 
Re fa sol la
Re fa 
Re fa fa fa fa 
Fa la re do

Re fa fa fa fa 
Re fa
Sol la 
Fa fa do la sol 
Sol la 
Sol do fa 
Fa do la 
Sol sol la sol do fa 

Do re fa sol sol 
Do re fa sol sol 
La


Fa do la sol sol la 
Sol do fa 
Fa do la sol sol la
Sol do fa
'''

def identify(note):
    note=note.upper()
    if note[-1]=='B':
           return notes_dict[note[:-1]]-1
    else:
        return notes_dict[note]


for text in t.split('\n'):
    if text=='':
        print '\n'
        continue
        

    text_note=text.replace(' ',',').replace("\xe2\x80\x99",'').split(',')
    
    
    text_notes_number=np.array([identify(note) for note in text_note if note!=''])
    
    semitones_to_add=2

    
    text_notes_number_changed=text_notes_number+semitones_to_add
    
    text_notes_number_changed[text_notes_number_changed>n_notes]=text_notes_number_changed[text_notes_number_changed>n_notes]-n_notes
    new_text=[notes_name[i] for i in text_notes_number_changed]
    print ' '.join(new_text)
    
#    for note in new_text:
#        print 
#    print '\n'





