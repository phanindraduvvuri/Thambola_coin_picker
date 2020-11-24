from playsound import playsound
import os
import random


def speak_number(number):
    audio_path = "audio-numbers/" + str(number) + '.wav'

    playsound(audio_path)


def play():
    os.system('clear')

    picked_numbers = []
    numbers = [i for i in range(1, 91)]
    random.shuffle(numbers)

    while len(picked_numbers) < 90:
        rand_num = numbers.pop()

        if rand_num not in numbers:
            picked_numbers.append(rand_num)
            print("Your Number is:", rand_num)
            speak_number(rand_num)
            input()


print("""
Welcome!! Let's play Thambola. Hit 'Enter' to start.
""")

input()
play()
