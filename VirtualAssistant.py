from speech import Speech
from interpreter import Interpreter

def main():
    interpreter = Interpreter()
    speech = Speech()
    speech.initialSpeech()
    while True:
        interpreter.wait_for_siri()       

if __name__ == "__main__":
    main()

#ctrl+C to stop listening