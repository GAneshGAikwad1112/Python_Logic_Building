# Crating a Rest API using flask and Jsonify in python.....

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/arm/<int:number>')


def arm(number):
    sum = 0
    order = len(str(number))
    copy_number = number
    while(number>0):
        digit = number % 10
        sum += digit ** order
        number = number // 10

    if (sum == copy_number):
        print(f"\nThis number is Armstrong number! {copy_number}\n")
        result = {
            "Number": copy_number,
            "Armstrong": True,
            "Server_IP": "172.16.1.3"
        }
    else:   
        print(f"\nThis number is not a Armstrong number! {copy_number}\n")
        result = {
            "Number": copy_number,
            "Armstrong": False,
            "Server_IP": "172.16.1.4"}

    return jsonify(result)
    
    

if __name__=="__main__":
    app.run(debug = True)