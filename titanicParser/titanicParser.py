import myFileFuncs as fileFuncs
import csv

'''
public dataset: Titanic Passengers: titanic.csv - contains passengers details.
A parser to separate the Name attribute in titanic.csv to Title, First Name, Middle Name, Last Name
output to "titanic_output.csv" in order:
PassengerId, Survived, Pclass, Title, First Name, Middle Name, Last Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked
output file must be closed when running parser.
'''


def getPassengerNames(splitLine):
    '''extracts passenger's title, name, middlename and surname from input data'''
    surname = splitLine[3]
    surname = surname.replace('"','')#remove random speechmark 
     
    otherNames = splitLine[4]      
    otherNames = otherNames.replace('"','')#remove random speechmarks 
    splitOtherNames = otherNames.split(" ")
    title = splitOtherNames[1]
    firstName = splitOtherNames[2]
    firstName = firstName.replace('(','')
    firstName= firstName.replace(')','')
    
    if len(splitOtherNames)>=4:#if not length of 4, middle name is not present in data
        middleName = splitOtherNames[3]
        
        #middle name must not be available if brackets present at position 3 in list:
        if '(' in middleName:
            #middle name not avaiable so set middleName to blank
            middleName = ''
           
    else:
        #middle name not avaiable so set middleName to blank
        middleName = ''  
    middleName= middleName.replace(')','')
    return(title, firstName, middleName, surname)


def mainFunc():
    fileContent = fileFuncs.readFile('titanic.csv')
    del fileContent[0] #delete first entry as it only contains the headers

    #write headers to output file
    with open('titanic_output.csv', mode='w', newline='',encoding='utf-8') as outputFile:
        outputWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        outputWriter.writerow(['PassengerId','Survived', 'Pclass', 'Title', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])

    #iterate through each line of fileContent to extract data   
    for line in fileContent:
        splitLine = line.split(",")
        passengerID = splitLine[0]
        survived = splitLine[1]
        pClass = splitLine[2]
        sex = splitLine[5]
        age = splitLine[6]
        sibSp = splitLine[7]
        parch = splitLine[8]
        ticket = splitLine[9]
        fare = splitLine[10]
        cabin = splitLine[11]
        embarked = splitLine[12][0]#only need first char to avoid new line symbol
        embarked = embarked.replace("\n","")# incase embarked column is empty
        title, firstName, middleName, surname = getPassengerNames(splitLine)#extract title, firstName, middleName and surname

        #append line to output file
        with open('titanic_output.csv', 'a', newline='', encoding='utf-8') as outputFile:
            outputWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            outputWriter.writerow([passengerID, survived, pClass, title, firstName, middleName, surname, sex, age, sibSp, parch, ticket, fare, cabin, embarked])
            
    print("Finished")        
mainFunc()
