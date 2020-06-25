# Find permutations using recursion:
# Idea from Chapter 7: Optimize & Solve Technique #4: Base case and Build


def permute(s):
    if len(s) == 1:  # basecase
        return [s]
    last_char = s[len(s)-1:]  # e
    subproblem = s[0:len(s)-1]  # abcd
    solutionToSubproblem = permute(subproblem)
    return addChar(solutionToSubproblem=solutionToSubproblem, last_char=last_char)


def addChar(solutionToSubproblem, last_char):
    finalSolution = list()
    print("Calculating permutation for: subproblem: {} || last_char: {}".format(solutionToSubproblem, last_char))
    for permutation in solutionToSubproblem:
        for i in range(0, len(permutation)):
            finalSolution.append(permutation[:i] + last_char + permutation[i:])
        finalSolution.append(permutation + last_char)
    print("finalSolution: {}".format(finalSolution))
    return finalSolution


if __name__ == "__main__":
    s = "abcd"
    permutations = permute(s=s)
    print("Permutations are: {}".format(permutations))
