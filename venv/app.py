from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for demonstration
books = [
    {"id": 1, "title": "Book A", "author": "Author A"},
    {"id": 2, "title": "Book B", "author": "Author B"}
]

borrow_requests = []
users = []

# Route: Home
@app.route('/')
def home():
    return "Welcome to the Library Management System!"

# Admin Routes
@app.route('/admin/create_user', methods=['POST'])
def create_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User created successfully", "user": data}), 201

@app.route('/admin/view_requests', methods=['GET'])
def view_requests():
    return jsonify({"borrow_requests": borrow_requests}), 200

@app.route('/admin/approve_request/<int:request_id>', methods=['PUT'])
def approve_request(request_id):
    for req in borrow_requests:
        if req["id"] == request_id:
            req["status"] = "Approved"
            return jsonify({"message": f"Request {request_id} approved"}), 200
    return jsonify({"error": "Request not found"}), 404

# User Routes
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify({"books": books}), 200

@app.route('/user/borrow', methods=['POST'])
def borrow_book():
    data = request.json
    borrow_requests.append(data)
    return jsonify({"message": "Borrow request submitted", "request": data}), 201

@app.route('/user/borrow_history', methods=['GET'])
def borrow_history():
    user_id = request.args.get('user_id')
    history = [req for req in borrow_requests if req['user_id'] == int(user_id)]
    return jsonify({"borrow_history": history}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)



