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

# Scaling Out the Application

To scale the application across multiple servers or containers, use a **distributed task queue system** like **Celery** with **Redis** or **RabbitMQ** as the message broker.

---

## Steps to Scale Out

1. **Task Distribution**  
   - Break workload into smaller tasks (e.g., process a single URL).  
   - Use a task queue to distribute tasks to worker nodes.

2. **Worker Nodes**  
   - Each worker processes tasks independently:  
     - Downloads pages.  
     - Counts word occurrences.  
     - Extracts new links.  
   - Workers send results (word counts, new links) to a central aggregator.

3. **Central Aggregator**  
   - Aggregates results from workers.  
   - Maintains shared state (e.g., visited URLs, word counts) using **Redis**.

4. **Fault Tolerance**  
   - Retry failed tasks.  
   - Ensure tasks are idempotent (processing the same URL multiple times doesn’t affect results).

5. **Scaling**  
   - Add more worker nodes to handle increased load.  
   - Use **Kubernetes** or **Docker Swarm** to manage and scale worker containers dynamically.

---

## Key Components

- **Celery**: Distributed task management.  
- **Redis**: Task queuing and shared state (visited URLs, word counts).  
- **Flask**: Web interface and task coordination.  

---

This approach enables **horizontal scaling** across multiple servers or containers.

+-------------------+       +-------------------+       +-------------------+
|   Flask Web App   |       |   Task Queue      |       |   Celery Workers  |
| (Task Submission) | ----> | (Redis/RabbitMQ)  | ----> | (Task Processing) |
+-------------------+       +-------------------+       +-------------------+
        |                           |                           |
        |                           |                           |
        v                           v                           v
+-------------------+       +-------------------+       +-------------------+
|   Central Aggregator | <--- |   Redis (Shared State) | <--- |   Results (Word Counts, Links) |
| (Flask + Redis)    |       | (Visited URLs, Counts) |       |   (Sent by Workers)           |
+-------------------+       +-------------------+       +-------------------+

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


