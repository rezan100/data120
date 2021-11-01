#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:46:22 2021

@author: rezanmoustafa
"""

class Question:
    def __init__(self, text, choices, correctNum):
        self.text = text
        self.choices = choices
        self.correctNum = correctNum
    
    def __str__(self):
        text = "\n" + self.text + "\n"
        for i, alt in enumerate(self.choices):
            text += (str(i) + ": " + alt + "\n")

        return f"{text}"

    def check(self, answer):
        if answer == self.correctNum:
            print("CORRECT")
        else:
            print("WRONG")

if __name__ == "__main__":


    q1 = Question("Capital of Norway", ["Stavanger", "Oslo", "Bergen", "Trondheim"], 1)
    print(q1)
    answ = int(input("answer: "))
    q1.check(answ)

    q2 = Question("most common color of a banana", ["Green", "Red", "Blue", "Yellow"], 3)
    print(q2)
    answ = int(input("answer: "))
    q2.check(answ)