# *********************
# CADA NOTA EN SU SITIO
# *********************


def run(marks: dict) -> tuple:
    passed = {}
    failed = {}
    for student, mark in marks.items():
        if mark >= 5:
            passed[student.upper()] = mark
        else:
            failed[student.lower()] = mark
    return passed, failed


if __name__ == '__main__':
    run({'Ana': 4, 'Domingo': 7, 'Eva': 5, 'Álvaro': 3, 'Juan': 8, 'Belén': 1})

