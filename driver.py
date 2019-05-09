from DataValidator import *






data = {
"title": "Book",
 "author": {
 "name": "Maher",
 "dob": "33-01-1996",
 "email": "maher@birzeit.edu",

  },
"pages": 50,
 "creation_date": "15/12/2015"
  }

rules = {
    "title": "string",
    "author.name": "string",
	"author.dob": "date",
	"author.email" : "email",
    "author.co_authors":"string",
    "pages":"number|max100|min10",
    "salary":"number",
"creation_date":"date"}


cA = {
    "name" : "first name",
    "age" : "old"


}

cE = {
    "age.number" : "Please provide a valid number for the age",
    "author.dob.date":"Please provide valid dob for the author",
	"author.name.string" : "author should be string",
	"dob.date": "dob should be date"
}
d = DataValidator(data,rules,cA,cE)


d.isValidData()
print(d.errorMessages)