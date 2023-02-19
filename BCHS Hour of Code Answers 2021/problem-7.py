MORSE_CODE = ['.-',"-...",'-.-.',"-..",'.',"..-.",'--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
action = input("What would you like to do? (encode/decode)")
message = input("Enter your message: ")
output = ""
if action == "encode":
    for character in message:
        if character in letters:
            output += morse_code[letters.index(character)] + " "
        elif character == " ":
            output += " "
    print("\n"+output)
elif action == "decode":
    morse_list = message.split(" ")
    for character in morse_list:
        if character == "":
            output += " "
        else:
            output += letters[morse_code.index(character)]
    print("\n"+output)
