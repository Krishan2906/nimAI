from nim import train, play

ai = train(5000)
n=input("numer of games you want to play : ")
for i in range(n):
    print(f"play {i+1}")
    play(ai)