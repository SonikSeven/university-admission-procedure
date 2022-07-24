# University Admission Procedure

This project is a Python-based University Admission Procedure that automates the process of sorting and admitting applicants into different departments based on their preferences and scores.

## Description

The script processes a list of applicants along with their scores in different subjects and assigns them to their preferred departments according to the available slots and their scores. The assignment takes into account the applicant's preferences for the department and their combined scores in the relevant subjects for that department.

## Features

- Reads applicants' data from a text file.
- Organizes applicants into departments based on their preferences and scores.
- Generates text files for each department with the list of admitted applicants.

## Departments and Relevant Subjects

- **Biotech:** Considers Biology and Chemistry scores.
- **Chemistry:** Considers Chemistry scores only.
- **Engineering:** Considers Math and Computer Science scores.
- **Mathematics:** Considers Math scores only.
- **Physics:** Considers Physics and Math scores.

## How It Works

1. The script reads the number of available slots in each department from the user.
2. It then reads applicants' details from `applicants.txt` file which includes names and scores among other details.
3. Applicants are sorted and admitted into their preferred departments based on the average score of the subjects relevant to each department.
4. The list of admitted applicants for each department is saved in separate text files named after the departments.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/university-admission-procedure.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## License

This project is licensed under the [MIT License](LICENSE.txt).
