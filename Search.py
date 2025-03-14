import tkinter as tk
from tkinter import scrolledtext, messagebox
from exa_py import Exa  

  
API_KEY = 'a0dbf29d-1450-45e5-b8c3-28ab795b2b18'  
exa = Exa(API_KEY)  

  
domains = [
    # Wikipedia and Research Papers  
    "https://en.wikipedia.org", "https://www.ncbi.nlm.nih.gov", "https://arxiv.org",
    "https://www.researchgate.net", "https://www.jstor.org", "https://www.nature.com",
    "https://www.sciencedirect.com", "https://ieeexplore.ieee.org", "https://www.academia.edu",

    # Coding Documentation  
    "https://docs.python.org", "https://developer.mozilla.org", "https://devdocs.io",
    "https://stackoverflow.com", "https://www.w3schools.com", "https://docs.oracle.com",
    "https://learn.microsoft.com", "https://www.geeksforgeeks.org", "https://www.tutorialspoint.com",
    "https://github.com", "https://gitlab.com",

    # News & Media Sources  
    "https://www.bbc.com", "https://www.cnn.com", "https://www.nytimes.com", "https://www.forbes.com",
    "https://www.theguardian.com", "https://www.reuters.com", "https://www.aljazeera.com",
    "https://www.wsj.com", "https://www.bloomberg.com",

    # Social Media & Tweets  
    "https://twitter.com", "https://www.linkedin.com", "https://www.instagram.com",
    "https://www.reddit.com", "https://www.facebook.com",

    # Other useful sources  
    "https://medium.com", "https://www.quora.com", "https://www.producthunt.com"
]

  
def perform_search():
    query = search_entry.get()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a search term!")
        return

    result_text.delete("1.0", tk.END)  # Clear previous results  

    try:
        response = exa.search(query, include_domains=domains)

        if hasattr(response, "results") and isinstance(response.results, list):
            for result in response.results:
                title = getattr(result, "title", "No Title")
                url = getattr(result, "url", "No URL")
                result_text.insert(tk.END, f"Title: {title}\nURL: {url}\n\n")
        else:
            result_text.insert(tk.END, "No results found.\n")

    except Exception as e:
        messagebox.showerror("Search Error", f"Error: {e}")

  
root = tk.Tk()
root.title("Exa Search GUI")
root.geometry("700x450")

 
tk.Label(root, text="Enter Search Query:").pack(pady=5)
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=5)

  
search_button = tk.Button(root, text="Search", command=perform_search)
search_button.pack(pady=5)

  
result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.pack(pady=10)

  
root.mainloop()
