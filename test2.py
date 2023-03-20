import http.server
import socketserver
import urllib.parse
import re

def ask_question(question, options):
    # Display question and options on website
    html = f"<p>{question}</p>"
    for i, option in enumerate(options):
        html += f'<p><input type="radio" name="answer" value="{i+1}">{option}</p>'
    return html





def run_expert_system(rules):
    # Initialize current rule to first rule
    current_rule = 1

    # Set up HTTP server to receive user input
    class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            # If the request method is GET, display the initial question
            html = run_expert_system_helper(rules)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))

        def do_POST(self):
            # If the request method is POST, get the user's answer and display the next question or answer
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            answer = params['answer'][0]

            # Determine the next rule based on the user's answer
            next_rule = rules[int(answer)][answer.lower()]

            # Update the current rule
            nonlocal current_rule
            current_rule = next_rule

            # Display the next question or answer
            html = run_expert_system_helper(rules)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))

    # Helper function to run the expert system
    def run_expert_system_helper(rules):
        # Get the current rule and its information
        rule_info = rules[current_rule]

        # If the rule is a question, ask it and update the current rule based on the user's answer
        if rule_info['type'] == 'question':
            # Call ask_question function to display the question and options and get user input
            question_html = ask_question(rule_info['question'], rule_info['options'])

            # Add a submit button to the HTML form
            html = f"<form method='post'>{question_html}<input type='submit' value='Submit'></form>"

            # Return the HTML to display on website
            return html

        # If the rule is an answer, print it and exit the loop
        elif rule_info['type'] == 'answer':
            # Display the answer on the website
            html = f"<p>{rule_info['answer']}</p>"

            # Return the HTML to display on website
            return html

    # Set up HTTP server
    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()

# Define the expert system rules
rules = {
    1: {'type': 'question', 'question': 'Is the car engine turning over?', 'options': ['Yes', 'No'], 'yes': 2, 'no': 6},
    2: {'type': 'question', 'question': 'Is the engine receiving fuel?', 'options': ['Yes', 'No'], 'yes': 3, 'no': 4},
    3: {'type': 'question', 'question': 'Is the fuel filter clogged?', 'options': ['Yes', 'No'], 'yes': 4, 'no': 5},
    4: {'type': 'answer', 'answer': 'Clean or replace the fuel filter.'},
    5: {'type': 'answer', 'answer': 'Check the fuel pump and fuel lines.'},
    6: {'type': 'question', 'question': 'Is the battery charged?', 'options': ['Yes', 'No'], 'yes': 7, 'no': 8},
    7: {'type': 'question', 'question': 'Are the spark plugs firing?', 'options': ['Yes', 'No'], 'yes': 8, 'no': 9},
    8: {'type': 'answer', 'answer': 'Check the starter and ignition system.'},
    9: {'type': 'answer', 'answer': 'Check the battery and charging system.'},
}

# Run the expert system
run_expert_system(rules)

