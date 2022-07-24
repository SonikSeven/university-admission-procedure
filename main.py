n = int(input())
with open("applicants.txt") as applicants_file:
    applicants = [x.split() for x in applicants_file.readlines()]
departments = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
subjects = {"Biotech": (3, 2), "Chemistry": (3, 3), "Engineering": (5, 4), "Mathematics": (4, 4), "Physics": (2, 4)}

for i in range(6, 9):
    for subject, j in subjects.items():
        n_1, n_2 = j
        applicants.sort(key=lambda x: (-(float(x[n_1]) + float(x[n_2])) / 2, x[0], x[1]))
        for applicant in applicants.copy():
            if applicant[i] == subject and len(departments[applicant[i]]) < n:
                result = applicant[0], applicant[1], (float(applicant[n_1]) + float(applicant[n_2])) / 2
                departments[applicant[i]].append(result)
                applicants.remove(applicant)

for applicants in departments.values():
    applicants.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

for department, applicants in departments.items():
    with open(department + ".txt", "w") as department_file:
        for applicant in applicants:
            print(*applicant, file=department_file)
