# AI_AutomobileExpertSystem

**Expert System for Car Troubleshooting**
This Python application is an Expert System designed to diagnose car issues. It operates as a web server, which takes user input through a web interface and provides recommendations based on the inputs.

**Dependencies**
This application is based on Python's built-in modules, including:

http.server
socketserver
urllib.parse
re

**How it Works**
This expert system uses a simple rule-based approach to diagnose issues. A set of rules is defined in the form of questions and corresponding answers. These rules guide the diagnostic process, similar to how a human expert would ask a series of questions to identify the problem.

The rules are represented as a Python dictionary, with the rule number as the key and rule details as the value. Rule details include the rule type (question or answer), the actual question or answer, the options for questions, and the next rule number corresponding to each option.

The system starts by asking the user the first question. Based on the user's response, it determines the next rule (either question or answer) to present. This continues until it reaches an answer, at which point the diagnosis is complete.

**How to Run**
To run this expert system, just run the Python script. This will start the HTTP server at localhost and the port 8000.

**Interacting with the System**
You interact with the system through your web browser by visiting http://localhost:8000.

The system will present a question with a list of options. Click the radio button for your choice, then click the Submit button to send your answer to the system. The system will process your answer and either present the next question or provide a final diagnosis based on the rules.

**Customizing the System**
You can customize the system by modifying the set of rules. For example, you can add new questions and answers, or change the order in which questions are asked. The rules are defined in the rules dictionary in the script.

Note: The order of questions is determined by the "yes" and "no" keys in each rule. These keys correspond to the next rule number to follow if the user selects "yes" or "no" for the question.

**Limitations**
This expert system is a simple rule-based system and does not incorporate any machine learning or probabilistic reasoning. As a result, its diagnostic capabilities are limited to the rules that are explicitly defined in the system. It may not provide accurate diagnoses for complex or unusual issues.
