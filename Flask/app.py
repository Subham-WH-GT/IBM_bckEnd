from flask import Flask,jsonify,make_response,request
#Since we are running the script as an imported file so __name__=app.py (the current file itself)
app=Flask(__name__)
@app.route("/")


def index():
    return jsonify(message='Hello World')



# Task 1: sending the status code explicitely
#   def index():
#     response=make_response(jsonify(message='Hello World'))
#     response.status_code=200
#     return response


#Task 2:   The client will send in requests in the form of http://localhost:5000?q=first_name. 
#You will create a method that will accept a first_name as the input and return a person with that first name.

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

@app.route('/data')
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": "Data of length "+str(len(data))+" found"},200
        else:
            return {"message":"Data is empty"},500
        
    except NameError:
        return {"message": "Data not found"},404    
    
@app.route('/name_search')
def name_search():
        query=request.args.get('q')

        if not query:
             return jsonify(message="Argument 'q' is missing"),422
        
        for person in data:
             if query.lower() in person['first_name'].lower():
                  return jsonify(person),200
             
        return jsonify(message="Person not found"),404     

#Task 3: You are asked to implement both of these endpoints in this exercise. 
#You will also implement a count method that returns the total number of persons 
#in the data list. This will help confirm that the two methods GET and DELETE work, as required.

@app.route("/count")
def count():
     try:
          return jsonify(data_count=len(data)),200
     
     except NameError:
          return jsonify(message="Data not defined!"),500
     

#task 4:   Implement the GET endpoint to ask for a person by id. and returns detail if exists
@app.route('/person/<uuid:person_id>') #uuid is a data-type which consists of both int and char values 
def find_detail_by_uuid(person_id):
     for person in data:
          if person['id']==str(person_id): #convert the uuid type to string before matching
               return jsonify(person),200
     return jsonify(message="Id not found"),404   


#Task 5: create a Delete endpoint that takes id in uuid type and delete the person detail
# from the data if exists

@app.route('/person/<uuid:person_id>',methods=['DELETE']) #in flask the method is bydefault set to get request
def delete_by_uuid(person_id):
     for person in data:
          if(person['id'])==str(person_id):
               data.remove(person)
               return jsonify(message='Data deleted Successfully'),200

     return jsonify(message="Person doesnot Exist!"),404

#Task 6: post a new data using post request and parse the json data to the data list
  #dont forget to parse the data in a single line in the command promt, else it will give error
@app.route('/person',methods=['POST'])   
def post_data():
     new_entry=request.json #is used to retrieve the json data

     if not new_entry or not isinstance(new_entry,dict):
          return jsonify(message="Invalid Input"),400

     data.append(new_entry)
     return jsonify(message="Person added successfully"),200 

#Task 7: create error handler with json response
# by default flask returns error in html format if user gives invalid endpoit

@app.errorhandler(404)
def api_not_found(error):
     return jsonify(message="Api doesnot Exist!"),404
               