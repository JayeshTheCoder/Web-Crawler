import requests
from bs4 import BeautifulSoup

def crawl_website(url):
  """Crawls a website and extracts links.

  Args:
      url: The URL of the website to crawl.

  Returns:
      A list of links found on the website.
  """
  # Send an HTTP GET request to the URL
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags (<a>) containing links
    links = []
    for link in soup.find_all('a'):
      # Extract the href attribute (URL) from the anchor tag
      href = link.get('href')
      if href and href.startswith('http'):  # Only consider absolute URLs
        links.append(href)

    return links
  else:
    print(f"Error: Failed to crawl {url} (Status code: {response.status_code})")
    return []

# Example usage
seed_url = "https://hianime.to/home"  # Replace with the starting URL
crawled_links = crawl_website(seed_url)

# Print the extracted links
print("Extracted Links:")
for link in crawled_links:
  print(link)