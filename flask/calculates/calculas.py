from flask import Flask, request, render_template, redirect, url_for, session
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from typing import Set, List

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  

def download_page(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

def count_word_occurrences(page: str, word: str) -> int:

    soup = BeautifulSoup(page, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
    text = soup.get_text(separator=" ")
    text = re.sub(r"\s+", " ", text).strip()
    word_pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)
    matches = word_pattern.findall(text)
    return len(matches)

def get_links_in_page(page: str, base_url: str) -> Set[str]:
    soup = BeautifulSoup(page, "html.parser")
    links = set()
    for a_tag in soup.find_all("a", href=True):
        link = urljoin(base_url, a_tag["href"])
        links.add(link)
    return links

def process_page(url: str, word: str, visited_urls: Set[str], total_occurrences: List[int], max_pages: int = 100) -> None:
    if len(visited_urls) >= max_pages:
        return
    if url in visited_urls:
        return
    visited_urls.add(url)

    print(f"Processing: {url}")
    html_content = download_page(url)
    if not html_content:
        return

    occurrences = count_word_occurrences(html_content, word)
    total_occurrences[0] += occurrences
    print(f"Occurrences of '{word}' in {url}: {occurrences}")

    links = get_links_in_page(html_content, url)
    for link in links:
        process_page(link, word, visited_urls, total_occurrences, max_pages)

@app.route("/", methods=["GET", "POST"])
def step1():
    if request.method == "POST":
        session["start_url"] = request.form.get("url")
        session["word"] = request.form.get("word")
        return redirect(url_for("step2"))
    return render_template("step1.html")

@app.route("/step2")
def step2():
    start_url = session.get("start_url")
    word = session.get("word")
    if not start_url or not word:
        return redirect(url_for("step1"))

    # Step 2: Count word occurrences in the starting page
    html_content = download_page(start_url)
    if not html_content:
        return "Error: Unable to fetch the starting page."

    occurrences = count_word_occurrences(html_content, word)
    session["starting_page_occurrences"] = occurrences
    return render_template("step2.html", occurrences=occurrences, word=word)

@app.route("/step3")
def step3():
    start_url = session.get("start_url")
    word = session.get("word")
    if not start_url or not word:
        return redirect(url_for("step1"))

    # Step 3: Find all links in the starting page
    html_content = download_page(start_url)
    if not html_content:
        return "Error: Unable to fetch the starting page."

    links = get_links_in_page(html_content, start_url)
    session["links"] = list(links)  # Store links in session
    return render_template("step3.html", links=links)

@app.route("/step4")
def step4():
    start_url = session.get("start_url")
    word = session.get("word")
    if not start_url or not word:
        return redirect(url_for("step1"))

    # Step 4: Accumulate word occurrences from all linked pages
    visited_urls = set()
    total_occurrences = [0]
    links = session.get("links", [])
    for link in links:
        process_page(link, word, visited_urls, total_occurrences)

    # Add starting page occurrences to the total
    total_occurrences[0] += session.get("starting_page_occurrences", 0)
    return render_template("step4.html", total_occurrences=total_occurrences[0], word=word)

@app.route("/show_html", methods=["GET", "POST"])
def show_html():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            return "Please provide a URL."

        try:
            html_content = download_page(url)
            if not html_content:
                return "Error: Unable to fetch the HTML content."

            return render_template("show_html.html", html_content=html_content, url=url)
        except Exception as e:
            return f"An error occurred while fetching the HTML content: {str(e)}"

    return redirect(url_for("step1"))


if __name__ == "__main__":
    app.run(debug=True) 