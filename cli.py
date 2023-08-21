import requests
import argparse
import time

def call_api(prompt, api_url, auth_secret):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "auth": auth_secret,
        "query": prompt
    }
    response = requests.post(api_url, json=payload, headers=headers, stream=True)

    for chunk in response.iter_content(chunk_size=128):
        cleaned_data = chunk.decode('utf-8').replace("data: ", "").replace("\r\n", "")
        print(cleaned_data, end="", flush=True)
        time.sleep(0.1)
    
    print()

def main():
    parser = argparse.ArgumentParser(description="Program to interact with your CharShift API.")
    parser.add_argument("--url", required=True, help="URL of your API to interact with.")
    parser.add_argument("--key", required=True, help="Authentication key for the API.")
    args = parser.parse_args()


    print("""
.d88b 8               .d88b. 8     w  d8b  w      
8P    8d8b. .d88 8d8b YPwww. 8d8b. w  8'  w8ww    
8b    8P Y8 8  8 8P       d8 8P Y8 8 w8ww  8      
`Y88P 8   8 `Y88 8    `Y88P' 8   8 8  8    Y8P                         
    """)
    print("")
    print("""
   db    888b. 888    88888             8         
  dPYb   8  .8  8       8   .d8b. .d8b. 8         
 dPwwYb  8wwP'  8       8   8' .8 8' .8 8         
dP    Yb 8     888      8   `Y8P' `Y8P' 8         
                                                  
    """)
    # Instructions
    print("\nWelcome to the CharShift API Tool!")
    print("This tool allows you to interact with your CharShift API.")
    print(f"CharShift API configured at: {args.url}")
    print("\nInstructions:")
    print("1. You'll be prompted to enter a request/query.")
    print("2. After submitting, you'll receive a response from the API.")
    print("3. Enter 'quit' anytime to exit the session.\n")
    
    while True:
        prompt = input("Enter your prompt: ")
        
        if prompt.lower() == 'quit':
            break

        call_api(prompt, args.url, args.key)

if __name__ == "__main__":
    main()
