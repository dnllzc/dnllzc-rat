import zmq
import subprocess
import socket

def register_with_master():
    """Register the agent with the master server."""
    context = zmq.Context()
    reg_socket = context.socket(zmq.REQ)  # REQ to register
    reg_socket.connect("tcp://<MASTER_IP>:9294")  # connect to master registration
    agent_id = socket.gethostname()
    reg_socket.send_string(agent_id)
    ack = reg_socket.recv_string()
    print(f"Registration status: {ack}")

def main():
    context = zmq.Context()
    # SUB for receiving commands
    command_socket = context.socket(zmq.SUB)
    command_socket.connect("tcp://<MASTER_IP>:9292")
    command_socket.setsockopt_string(zmq.SUBSCRIBE, "")

    # PUSH for sending response
    response_socket = context.socket(zmq.PUSH)
    response_socket.connect("tcp://<MASTER_IP>:9293")

    register_with_master()

    print("Agent is ready.")
    while True:
        command = command_socket.recv_string()
        if command.lower() == "exit":
            print("Agent exiting.")
            break
        print(f"Executing command: {command}")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout.strip()
            error = result.stderr.strip()
            response = f"Agent: {socket.gethostname()}\nCommand: {command}\nOutput: {output}\nError: {error}"
        except Exception as e:
            response = f"Agent: {socket.gethostname()}\nCommand: {command}\nError: {str(e)}"
        response_socket.send_string(response)

if __name__ == "__main__":
    main()
