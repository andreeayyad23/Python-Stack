# Web Page Word Counter Application

## Overview
This application is a Flask-based web tool that analyzes the content of web pages to count occurrences of a specific word. It traverses through links on a given web page, recursively processing linked pages to provide a total word count.

The program combines **I/O-bound** and **CPU-bound** tasks. While the dominant bottleneck lies in the I/O operations (downloading pages from the internet), it also performs computationally expensive tasks like parsing HTML and counting word occurrences.

---

## Key Features
1. **Page Downloading**:
   - Fetches HTML pages using the `requests` library.
   - Handles errors gracefully during network requests.

2. **Word Counting**:
   - Parses HTML content using `BeautifulSoup` to extract text.
   - Cleans and preprocesses text by removing scripts and styles.
   - Uses regex to find case-insensitive occurrences of the target word.

3. **Recursive Link Processing**:
   - Extracts links from the starting page and processes them recursively.
   - Accumulates word counts from linked pages.

4. **User Interface**:
   - Simple Flask web interface to input the URL and word.
   - Displays word count results and found links step-by-step.

---

## Performance Analysis

### I/O-Bound Operations
The program is primarily **I/O-bound**, as most of its time is spent downloading web pages using `requests.get()`. The performance is highly dependent on:
- Network speed
- Server response times

Downloading multiple pages and waiting for external server responses dominates the execution time, especially when processing many links.

### CPU-Bound Operations
The program also contains **CPU-bound** tasks, such as:
- Parsing HTML with `BeautifulSoup`.
- Cleaning text by removing unnecessary tags and white spaces.
- Counting word occurrences using regex.

These tasks involve significant computation but are secondary to the I/O operations. The CPU-bound components only become a bottleneck when pages download quickly and processing large amounts of text.

---

## Technologies Used
- **Flask**: Web framework for building the interface.
- **BeautifulSoup**: For parsing and cleaning HTML content.
- **Regex**: For efficient word matching.
- **Requests**: For HTTP requests to fetch web pages.

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-name/web-word-counter.git
   ```

2. Navigate to the project directory:
   ```bash
   cd web-word-counter
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

---


