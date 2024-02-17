#!/usr/bin/env python3

from brain_games.cli import welcome_user


def greating():
    print('Welcome to the Brain Games!')
    welcome_user()


def main():
    greating()


if __name__ == '__main__':
    main()
