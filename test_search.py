from search import *

data = [
{
"question": "In which year was Halley's Comet last visible from Earth?",
"answers": ["1986"],
"difficulty": 3
},
{
"question": "Where were the 2016 Summer Olympics held?", 
"answers": ["rio de janeiro", "rio", "brazil"], 
"difficulty": 2
} 
]
# TESTING SECTION
def test_search_questions_found():
    expected = '2) Where were the 2016 Summer Olympics held?'
    actual = search_term(data, 'olympics')
    assert actual == expected

def test_search_questions_not_found():
    expected = 'No results found'
    actual = search_term(data, 'planets')
    assert actual == expected
