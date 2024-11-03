import shodan
import time

# Function to print text in red
def print_red(text):
    print("\033[91m" + text + "\033[0m")

# Function to print text in green
def print_green(text):
    print("\033[92m" + text + "\033[0m")

# Function to display the welcome message
def welcome_message():
    print_red(r""" 
    /$$                 /$$            /$$$$$$
    | $$                | $$           /$$__  $$
    | $$       /$$   /$$| $$ /$$$$$$$$| $$  \__/  /$$$$$$   /$$$$$$$
    | $$      | $$  | $$| $$|____ /$$/|  $$$$$$  /$$__  $$ /$$_____/
    | $$      | $$  | $$| $$   /$$$$/  \____  $$| $$$$$$$$| $$
    | $$      | $$  | $$| $$  /$$__/   /$$  \ $$| $$_____/| $$
    | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$.$
    |________/ \______/ |__/|________/ \______/  \_______/ \_______/
                              //Laughing at your security since 2011!
    """)
    time.sleep(2)
    print_green("ZeroDayX")
    time.sleep(2)

# Function to get IPs from Shodan search with rate limiting
def get_ips(api_key, search_query, pages):
    api = shodan.Shodan(api_key)
    ips = []

    for page in range(1, pages + 1):
        print(f"Retrieving page {page}...")
        try:
            results = api.search(search_query, page=page)
            for result in results['matches']:
                ip_address = result['ip_str']
                ips.append(ip_address)
                print(f"Found IP: {ip_address}")
                
            # Sleep for a short duration to avoid hitting rate limits
            time.sleep(1)  # Adjust the sleep duration as necessary
        except shodan.APIError as e:
            print(f"API Error: {e}")
            break  # Exit the loop on error
        except Exception as e:
            print(f"Unexpected error: {e}")
            break  # Exit the loop on unexpected error

    return ips

def main():
    welcome_message()

    # Input API key
    api_key = input("Enter your Shodan API key: ")

    # Input search query
    search_query = input("Enter your search query: ")

    # Input number of pages to retrieve
    pages = int(input("How many pages to open? "))

    # Retrieve IPs
    ips = get_ips(api_key, search_query, pages)

    # Write IPs to ips.txt
    with open("ips.txt", "w") as f:
        for ip in ips:
            f.write(ip + "\n")

    print(f"Retrieved {len(ips)} IPs and saved to ips.txt.")

if __name__ == "__main__":
    main()
