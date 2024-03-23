def Whisper(nr_of_participants):
    First_whisper = input("Start by saying something:")
    Subsequent_whispers = First_whisper
    for i in range(nr_of_participants - 1):
        print("* " + Subsequent_whispers + " *")
        Subsequent_whispers = input("What did you hear?")
        print("Ok, next player...")
    print("* " + Subsequent_whispers + " *")
    Subsequent_whispers = input("What did you hear?")
    if Subsequent_whispers == First_whisper:
        print("Oh wow, that's exactly what was said :O")
    else:
        print(f"Hmmm that wasn't quite it. The correct whisper is: {First_whisper}")

nr_of_participants = int(input("How many players are we?"))
Whisper(nr_of_participants)
