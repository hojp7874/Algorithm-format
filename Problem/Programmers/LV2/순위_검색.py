import pandas as pd


def solution(info, query):
    applicants = []
    for args in info:
        applicant = args.split()
        applicant[-1] = int(applicant[-1])
        applicants.append(applicant)
    applicants = pd.DataFrame(applicants, columns=[
        'language', 'position', 'level', 'food', 'score'])
    result = []
    for args in query:
        args = args.split()
        language, position, level, food, score = (
            arg for arg in args if arg != 'and')
        fit = applicants[((language == '-') | (applicants.language == language))
                         & ((position == '-') | (applicants.position == position))
                         & ((level == '-') | (applicants.level == level))
                         & ((food == '-') | (applicants.food == food))
                         & (applicants.score >= int(score))]
        result.append(len(fit))
    return result


if __name__ == "__main__":
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"]

    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]

    result = [1, 1, 1, 1, 2, 4]
    print(solution(info, query) == result)
