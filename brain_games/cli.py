#!/usr/bin/env python3
import prompt


name=''
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
