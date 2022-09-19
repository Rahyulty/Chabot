import AI as Zimmy


Bot_Name = "Zimmy"


# var = input("You: ")

# if var:
#     if Zimmy.IsInInput(var, Zimmy.GetPossibleGreetings()):
#         print(Bot_Name + ": " + Zimmy.GenerateResponse())


while True:
    var = Zimmy.GetUserInput()

    if Zimmy.GenerateResponse(var) != False:
        Zimmy.DisplayBotResponse(Bot_Name, Zimmy.GenerateResponse(var))
    elif Zimmy.GenerateResponse(var) == "Response":
        Zimmy.DisplayBotResponse(Bot_Name, Zimmy.GenerateResponse(var))

