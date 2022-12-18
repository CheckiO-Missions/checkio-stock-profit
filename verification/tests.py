"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[2, 3, 4, 5]],
            "answer": 3,
            "explanation": "Buy for $2, Sell for $5"
        },
        {
            "input": [[3, 1, 3, 4, 5, 1]],
            "answer": 4,
            "explanation": "Buy for $1, Sell for $5"
        },
        {
            "input": [[4, 3, 2, 1]],
            "answer": 0,
            "explanation": "It is impossible to get profit."
        },
        {
            "input": [[6, 2, 1, 2, 3, 2, 3, 4, 5, 4, ]],
            "answer": 4,
            "explanation": "Buy for $1, Sell for $5"
        },
        {
            "input": [[1, 1, 1, 2, 1, 1, 1 ]],
            "answer": 1,
            "explanation": "Buy for $1, Sell for $2"
        },
        {
            "input": [[4, 3, 2, 1, 2, 1, 2, 1]],
            "answer": 1,
            "explanation": "Buy for $1, Sell for $2"
        },
        {
            "input": [[1, 1, 1, 1]],
            "answer": 0,
            "explanation": "It is impossible to get profit. Price doesn't move"
        },
    ],
    "Extra": [
        {
            "input": [[22, 10, 4, 4, 1]],
            "answer": 0,
        },
        {
            "input": [[80, 70, 10, 3, 7]],
            "answer": 4,
        },
        {
            "input": [[60, 50, 51, 52, 40]],
            "answer": 2,
        },
    ]
}
