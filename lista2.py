# zadanie 1

def is_text_valid(text, alphabet):
    for sign in text:
        if sign not in alphabet:
            return False
    return True


alphabet = ["0", "1"]
text = str(input("Enter text: "))
while not is_text_valid(text, alphabet):
    print("incorrect input, enter again: ")
    text = str(input("Enter text: "))

state = "q0"
checked = []

for sign in text:
    while sign not in checked:
        output_info = f"current sign: {sign}, previous state: "
        if sign == "0":
            match state:
                case "q0":
                    output_info += f"{state}"
                    state = "q1"
                    output_info += f"next state: {state}"
                    checked.append(sign)
                case "q1":
                    output_info += f"{state}"
                    state = "q3"
                    output_info += f"next state: {state}"
                    checked.append(sign)
                case "q2":
                    output_info += f"{state}"
                    state = "q2"
                    output_info += f"next state: {state}"
                    checked.append(sign)
                case "q3":
                    output_info += f"{state}"
                    state = "q2"
                    output_info += f"next state: {state}"
                    checked.append(sign)
        elif sign == "1":
            match state:
                case "q0":
                    output_info += f"{state}"
                    state = "q0"
                    output_info += f"next state: {state}"
                    checked.append(sign)
                case "q1":
                    output_info += f"{state}"
                    state = "q2"
                    output_info += f"next state: {state}"
                    checked.append(sign)
                case "q2":
                    output_info += f"{state}"
                    state = "q0"
                    output_info += f"next state: {state}"
                    checked.append(sign)
                case "q3":
                    output_info += f"{state}"
                    state = "q1"
                    output_info += f"next state: {state}"
                    checked.append(sign)
        if state == "q3":
            print("text accepted")
        else:
            print("text not accepted")