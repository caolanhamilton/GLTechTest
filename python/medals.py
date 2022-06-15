from pyparsing import stringStart


medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):

1. create a medalTable Dictionary
2. for each result in results, loop through the podium list
3. for each country & position string in the podium list, save the position and country name as seprate variables
4. if the country already exists in medal table add the correct number of points to that countries key, e.g 3 points for 1st, 2 points for 2nd, 1 point for 3rd
5. if the country does not exist in medal table add the country name as a key and then add the correct number of points to the medal table
6. return medal table

    # medalTable = {}
    # for result in results:
    #     if result['sport'] == 'high jump':
    #         medalTable['Countries'] = result['podium']
        
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    return medalTable

print(createMedalTable(medalResults))

# def test_function():
#     #This it the test function, please don't change me
#     medalTable = createMedalTable(medalResults)
#     expectedTable = {
#         "Italy": 4,
#         "France": 4,
#         "ROC": 4,
#         "USA": 3,
#         "Qatar": 3,
#         "China": 3,
#         "Germany": 2,
#         "Brazil": 1,
#         "Belarus": 1,
#     }
#     assert medalTable == expectedTable
