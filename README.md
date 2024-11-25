# dnllzc-rat: Educational Remote Administration Tool (RAT)

![ASCII Logo](https://i.imgur.com/JpotY5O.png)  

**dnllzc-rat** is a lightweight Remote Administration Tool (RAT) designed for educational purposes only. This project demonstrates the basics of distributed command execution using Python and ZeroMQ.

⚠️ **DISCLAIMER**  
This software is intended for **educational purposes only**. The misuse of this tool in any unauthorized or malicious activities is strictly prohibited and could lead to severe legal consequences. The authors assume no responsibility for any misuse of this software.

---

## Features

- **Centralized Command Execution**: 
  The `server.py` script acts as the master, broadcasting shell commands to multiple agents.  
- **Response Handling**: 
  Agents execute commands and send their responses back to the master for review.
- **Dynamic Agent Tracking**: 
  A count of connected agents is displayed in real-time.
- **Interactive Master Console**:
  Includes support for custom commands like `clear` to reset the interface while retaining key information.

---

## Architecture Overview

The system consists of the following components:

1. **Master Server (`server.py`)**  
   - Sends commands to agents via a PUB socket (`tcp://*:9292`).  
   - Manages the master console for user interaction.

2. **Response and Agent Manager (`response.py`)**  
   - Tracks connected agents using a REP socket (`tcp://*:9294`).  
   - Receives responses from agents via a PULL socket (`tcp://*:9293`).  

3. **Agent Script (`agent.py`)**  
   - Connects to the master server.  
   - Executes received commands locally and sends the output back to the master.

---

## Usage Instructions

### Prerequisites
- Python 3.8+  
- ZeroMQ library (`pyzmq`)  

Install dependencies with:  
```bash
pip install pyzmq
```

### Running the Project

1. **Start the Response and Agent Manager**:
   ```bash
   python response.py
   ```

2. **Start the Master Server**:
   ```bash
   python server.py
   ```

3. **Deploy Agents**:
   Run `agent.py` on any number of machines:  
   ```bash
   python agent.py
   ```

⚠️ Replace `<MASTER_IP>` with the IP address of the master server in agent.py file.

### Master Commands
- **`clear`**: Clears the terminal.  
- **`exit`**: Terminates the server and all agents. 

---

## Code Example

Here’s how the master sends a command and processes responses:  
```python
# Sending a command from server.py
socket.send_string("ls -l")

# Example response format
[Response]
Agent: agent-1
Output: 
drwxr-xr-x  2 user group 4096 Nov 17 10:00 example-folder
```

---

## Ethical Usage Policy

By using this project, you agree to the following:
- You will only use this software for learning and research purposes.
- You will not use this software in environments where you do not have explicit permission.  

⚠️ **Unauthorized use of this software is illegal.** Ensure compliance with all local laws and regulations before deploying.

---

## License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use the code for educational purposes, but respect the ethical guidelines.

---
