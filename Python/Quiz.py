def quiz():
    QuesAns = {
        "What is the capital of India?": "Delhi",
        "What is the largest state of India?": "Uttar Pradesh",
        "What is the National Anthem of India?": "Jana Gana Mana",
        "Who is the President of India?": "Draupadi Murmu",
        "Who is the Prime Minister of India?": "Narendra Modi"
    }
    correctAns = 0
    for i in QuesAns.keys():
        print(i)
        user_input = input("Enter you answer: ")
        if user_input==QuesAns.values():
            correctAns+=1
        else:
            print("Error")

quiz()

