import sys
import re
import os
import math

#this terrible code is written by red hot dogs---
#convert brainfuck to pyfun

if len(sys.argv)<3:
    print(os.path.basename(sys.argv[0])+" [input file] [output file]")
    sys.exit()

input_file=open(sys.argv[1],"r")
output_file=open(sys.argv[2],"w")

def list_rindex(a,b):
    for i in range(len(a)-1,-1,-1):
        if a[i]==b:
            return i

def pyf_number(x):
    if x<4:
        t=["[[]<[]][[]<[]]","[[]<[[]]][[]<[]]","[[]<[[]]][[]<[]]+[[]<[[]]][[]<[]]","[[]<[[]]][[]<[]]+[[]<[[]]][[]<[]]+[[]<[[]]][[]<[]]"][x]
    else:
        b=x
        a=0
        while not b&1:
            a+=1
            b>>=1
        if a>0:
            t='['+pyf_number(b)+"<<"+pyf_number(a)+"][[]<[]]"
        else:
            a,b=x&3,x-(x&3)
            t=pyf_number(b)+'+'+pyf_number(a)
    return t

def pyf_number_w(x,w):
    if x<4:
        a=[1,1,0,0][x]
    else:
        a=not x&1
    if a==w:
        return pyf_number(x)
    if w==0 and a==1:
        return pyf_number(x)[1:-8]
    if w==1 and a==0:
        return '['+pyf_number(x)+'][[]<[]]'

def pyf_remove_numbers(s):
    g=re.split("([0-9]+)",s)
    for i in range(len(g)):
        if g[i].isnumeric():
            w=not (g[i-1][-1]=='[' and g[i+1][0]==']')
            g[i]=pyf_number_w(int(g[i]),w)
    return "".join(g)

def bf_to_pyf(s):
    a=re.findall("(\\++|\\-+|\\<|\\>|\\[|\\]|\\.|\\,)",s)
    t=[]
    for i in a:
        if i[0]=='+':
            t+=[0,len(i)%256]
        elif i[0]=='-':
            t+=[0,-len(i)%256]
        elif i==',':
            t+=[6,1]
        elif i=='.':
            t+=[7,1]
        elif i=='<':
            t+=[2]
        elif i=='>':
            t+=[3]
        elif i=='[':
            t+=[4,'n']
        elif i==']':
            b=list_rindex(t,'n')
            t+=[5,b-1]
            t[b]=len(t)-2
    t+=[8,8]
    b=[0]*9
    b[0]="[a[0]]+[["+"+".join('['+str(i%256)+']' for i in range(511))+"][0][a[[[0]+[1]][0][0<a[0]]]+[[[[[[]]+[0]]+[a[[[0]+[5]][0][0<a[0]]]]][0][0<a[0]][a[[[0]+[4]][0][0<a[0]]]+1]]+[0]][0][0<[[[0]]+[a[[[0]+[5]][0][0<a[0]]]]][0][0<a[0]][a[[[0]+[4]][0][0<a[0]]]]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[a[[[0]+[4]][0][0<a[0]]]+2]+[a[[[0]+[5]][0][0<a[0]]]]"
    b[1]="[4]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]"
    b[2]="[a[0]]+[[[[0]]+[a[[[0]+[2]][0][0<a[0]]]]][0][0<a[0]][0]]+[[[[0]+[0]]+[a[[[0]+[2]][0][0<a[0]]]]][0][0<a[0]][1]]+[[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]"
    b[3]="[a[0]]+[[[[0]]+[a[[[0]+[3]][0][0<a[0]]]]][0][[[0]+[[]]][0][0<a[0]]<a[[[0]+[3]][0][0<a[0]]]][0]]+[[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]]+[[[[[]]+[[]]]+[a[[[0]+[3]][0][0<a[0]]]]][0][[[0]+[[]]][0][0<a[0]]<a[[[0]+[3]][0][0<a[0]]]][1]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]"
    b[4]="[a[0]]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[[[[[[[]]+[0]]+[a[[[0]+[5]][0][0<a[0]]]]][0][0<a[0]][a[[[0]+[4]][0][0<a[0]]]+1]]+[a[[[0]+[4]][0][0<a[0]]]]][0][0<a[[[0]+[1]][0][0<a[0]]]]+2]+[a[[[0]+[5]][0][0<a[0]]]]"
    b[5]="[a[0]]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[[[a[[[0]+[4]][0][0<a[0]]]]+[[[[[]]+[0]]+[a[[[0]+[5]][0][0<a[0]]]]][0][0<a[0]][a[[[0]+[4]][0][0<a[0]]]+1]]][0][0<a[[[0]+[1]][0][0<a[0]]]]+2]+[a[[[0]+[5]][0][0<a[0]]]]"
    b[6]="[1]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]"
    b[7]="[2]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]"
    b[8]="[3]"
    r="["+"+".join('['+str(i)+']' for i in t)+"][0]"
    pyf="[[[4]+[0]+[[0]+[[]]]+[[]]+[0]+["+r+"]]+[[[%s]+[%s]+[%s]+[%s]+[%s]+[%s]+[%s]+[%s]+[%s]][0][[[[0]]+[a[[[0]+[5]][0][0<a[0]]]]][0][0<a[0]][a[[[0]+[4]][0][0<a[0]]]]]]][0][0<a[0]]"%tuple(b)
    pyf=pyf_remove_numbers(pyf)
    return pyf

#some important stuff
#[a[0]]+[[i%256 for i in range(511)][a[[[0]+[1]][0][0<a[0]]]+[[[[[[]]+[0]]+[a[[[0]+[5]][0][0<a[0]]]]][0][0<a[0]][a[[[0]+[4]][0][0<a[0]]]+1]]+[0]][0][0<[[[0]]+[a[[[0]+[5]][0][0<a[0]]]]][0][0<a[0]][a[[[0]+[4]][0][0<a[0]]]]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[a[[[0]+[4]][0][0<a[0]]]+2]+[a[[[0]+[5]][0][0<a[0]]]]
#[4]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]
#[a[0]]+[[[[0]]+[a[[[0]+[2]][0][0<a[0]]]]][0][0<a[0]][0]]+[[[[0]+[0]]+[a[[[0]+[2]][0][0<a[0]]]]][0][0<a[0]][1]]+[[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]
#[a[0]]+[[[[0]]+[a[[[0]+[3]][0][0<a[0]]]]][0][[[0]+[[]]][0][0<a[0]]<a[[[0]+[3]][0][0<a[0]]]][0]]+[[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]]+[[[[[]]+[[]]]+[a[[[0]+[3]][0][0<a[0]]]]][0][[[0]+[[]]][0][0<a[0]]<a[[[0]+[3]][0][0<a[0]]]][1]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]
#[a[0]]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[[[[[[[]]+[0]]+[a[[[0]+[5]][0][0<a[0]]]]][0][0<a[0]][a[[[0]+[4]][0][0<a[0]]]+1]]+[a[[[0]+[4]][0][0<a[0]]]]][0][0<a[[[0]+[1]][0][0<a[0]]]]+2]+[a[[[0]+[5]][0][0<a[0]]]]
#[a[0]]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[[[a[[[0]+[4]][0][0<a[0]]]]+[[[[[]]+[0]]+[a[[[0]+[5]][0][0<a[0]]]]][0][0<a[0]][a[[[0]+[4]][0][0<a[0]]]+1]]][0][0<a[[[0]+[1]][0][0<a[0]]]]+2]+[a[[[0]+[5]][0][0<a[0]]]]
#[1]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]
#[2]+[a[[[0]+[1]][0][0<a[0]]]]+[a[[[0]+[2]][0][0<a[0]]]]+[a[[[0]+[3]][0][0<a[0]]]]+[a[[[0]+[4]][0][0<a[0]]]+1]+[a[[[0]+[5]][0][0<a[0]]]]
#[3]
output_file.write(bf_to_pyf(input_file.read()))
input_file.close()
output_file.close()
