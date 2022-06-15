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
    medalTable = {} # 1. Create a medalTable dictionary
    for result in results: # 2. For each result in results, loop through the podium list
        for country in result['podium']: # 3. For each country & position string in the podium list
            countryName = country[2:] # save the country name and position in variables
            countryPlace = country[0:1]
            if countryPlace == '1':  # 4. Check the country position and add the correct number of points to that countries key e.g 3 points for 1st, 2 points for 2nd, 1 point for 3rd.
                medalTable[countryName] = medalTable.get(countryName, 0) + 3  # get method checks the medalTable to see if countryName is a key, if it is it return the value, else it returns 0 allowing us to add correct points to that country key even if it is not yet in the medalTable
            elif countryPlace == '2':
                medalTable[countryName] = medalTable.get(countryName, 0) + 2  
            elif countryPlace == '3':
                medalTable[countryName] = medalTable.get(countryName, 0) + 1 
    return medalTable # 5. Return medal table

# print(createMedalTable(medalResults))

def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4, 
        "France": 4,
        "ROC": 4, 
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
