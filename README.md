# CharShift CLI Tool

Welcome to the CharShift CLI Tool! This tool allows you to interact easily with the CharShift API. Follow the steps below to get started.

## 1. Acquiring the API URL and Authentication Key

Before you can use this tool, you need two pieces of information:
1. **API URL**: The endpoint where the CharShift API is hosted.
2. **Authentication Key**: A secret key that grants you access to use the API.

If you don't have these details, please contact your system administrator or the person who provided you with this tool.

## 2. Setting Up the CLI Tool

### On MacOS:

1. **Open the Terminal**:
   - You can find the Terminal application in the Applications > Utilities folder, or search for it using Spotlight.
  
2. **Navigate to the CLI Tool Directory**:
   - If you've downloaded the tool and it's in your Downloads folder inside a `charcli` directory, use the following command:
     ```
     cd ~/Downloads/charcli
     ```

### On Windows:

1. **Open the Command Prompt**:
   - You can search for "cmd" or "Command Prompt" in the Start menu.

2. **Navigate to the CLI Tool Directory**:
   - If you've placed the tool on your Desktop in a `charcli` directory, use the following command:
     ```
     cd %USERPROFILE%\Desktop\charcli
     ```

## 3. Using the CLI Tool

Once you're in the correct directory:

1. **Run the CLI Tool**:
   ```
   ./cli_script_binary --url YOUR_API_URL --key YOUR_AUTH_KEY
   ```
   - Replace `YOUR_API_URL` with the API URL you've received.
   - Replace `YOUR_AUTH_KEY` with the authentication key you've received.

2. **Enter Your Query**:
   - Once the tool starts, you'll see a prompt asking you to enter your request/query. Type your question or command and hit enter.

3. **View the Response**:
   - After submitting your query, you'll receive a streamed response from the API. This response will display directly in your terminal or command prompt window.

4. **Exit**:
   - To exit the CLI tool, simply type `quit` and hit enter.

## 4. Need Help?

If you encounter any issues or have questions, please refer back to this README or contact the person who provided you with this tool.
