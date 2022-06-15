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
    medalTable = {} # 1. create a medalTable Dictionary
    for result in results: # 2. for each result in results, loop through the podium list
        for country in result['podium']: # 3. for each country & position string in the podium list
            countryName = country[2:] # save the country name and position in variables
            countryPlace = country[0:1]
            if countryName in medalTable: # 4. if the country already exists in medal table
                if countryPlace == '1': # add the correct number of points to that countries key
                    medalTable[countryName] += 3
                elif countryPlace == '2':
                    medalTable[countryName] += 2
                elif countryPlace == '3':
                    medalTable[countryName] += 1
            else: # 5. if the country does not exist in medal table add the country name as a key and then add the correct number of points to the medal table
                if countryPlace == '1':
                    medalTable[countryName] = 3
                elif countryPlace == '2':
                    medalTable[countryName] = 2
                elif countryPlace == '3':
                    medalTable[countryName] = 1

    return medalTable # 6. return medal table

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
