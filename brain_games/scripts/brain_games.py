#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')


if __name__ == '__main__':
    main()  # Выводит на экран приветствие в игре
    welcome_user()  # Спрашивает имя, приветствует пользователя по имени
