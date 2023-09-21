#Flip a Coin

#import the random library
import random

#define a function for coin flip
def coin_flip():
    output = random.choice(["Heads", "Tails"])
    return output

print(coin_flip())