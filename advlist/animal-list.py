#!/usr/bin/env python3

def main():
    animals = ['fox', 'bee', 'hen', 'cow', 'dog']
    print(animals[1])
    animals2 = ['cow', 'dogs']
    animals.append(animals2[1])
    print(animals)
main()