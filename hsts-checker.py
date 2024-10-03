import requests

def check_hsts(url):
    try:
        # Ensure the URL starts with HTTPS
        if not url.startswith("https://"):
            url = "https://" + url
        
        # Send a request to the website
        response = requests.get(url)
        
        # Check if the 'Strict-Transport-Security' header is present
        hsts_header = response.headers.get('Strict-Transport-Security')
        
        if hsts_header:
            print(f"[+] HSTS is enabled for {url}")
            print(f"HSTS Header: {hsts_header}")
        else:
            print(f"[-] HSTS is NOT enabled for {url}")
    
    except requests.exceptions.RequestException as e:
        print(f"[!] Error connecting to {url}: {e}")

if __name__ == "__main__":
    # Example: User input for website to check
    website = input("Enter a website URL (without http/https): ").strip()
    check_hsts(website)