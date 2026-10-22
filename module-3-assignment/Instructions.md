## In this assignment we will going to fix all the errors and make a basic coding assistant similar to claude-code/codex

#### Terminal.py is the main source file for interacting agent through CLI.

Try running the terminal.py file `python3 module-3-assignment/invoke/terminal.py`

Make sure your local llama server is up and running.

### Instructions -

1. Start fixing TODO - 1 in local_agent.py

- Try running the terminal.py file `python3 module-3-assignment/invoke/terminal.py` 

- And try to enter prompt like `Who are you ?`

2. Since our aim is to build coding assistant, agent needs an ability to read and write to a file.

- Address TODO - 2,3 in module-3-assignment/tools/file_tool.py

- Test the changes by promting agent to read and write something into file.

3. Test the agents memory, whether it can remember previous messages in same session

- Fix TODO - 4.a and TODO - 4.b

4. Lets try to ask `Whats current time now ?` to our agent and see the response.

- It won't give you the current time. We already have mcp client ready and initialised client in module-3-assignment/tools/mcp_tools.py. Extend your tools with tools provided by mcp.

- Complete TODO - 5

5. Now add human in the loop 

- Fix TODO - 6