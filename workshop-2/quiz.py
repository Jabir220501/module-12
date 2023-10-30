def stel_vraag(vraag, juist_antwoord):
    print(vraag)
    antwoord = input("Wat is je antwoord? ")

    if antwoord.lower() == juist_antwoord.lower():
        print("Goed antwoord!")
        return True
    else:
        print(f"Fout! Het juiste antwoord was: {juist_antwoord}")
        return False

def speel_quiz():
    vraag = "Wat is de hoofdstad van Frankrijk?"
    juist_antwoord = "Parijs"
    
    if stel_vraag(vraag, juist_antwoord):
        print("Gefeliciteerd, je hebt de vraag correct beantwoord!")
    else:
        print("Helaas, probeer het opnieuw.")

if __name__ == "__main__":
    speel_quiz()
