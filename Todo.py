from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# -----------------------------
# MongoDB Connection
# -----------------------------
<<<<<<< HEAD
MONGO_URI = "mongodb+srv://shaktig101101_db_user:C1yoWqhkEj5muHcL@cluster0.sofmx8o.mongodb.net/"
# Replace <db_password> with your actual password
=======
# MongoDB Atlas Configuration
# -----------------------------
MONGO_URI = "mongodb+srv://shaktig101101_db_user:C1yoWqhkEj5muHcL@cluster0.sofmx8o.mongodb.net/"
  # Replace <db_password> with your actual password

>>>>>>> master_1

# Connect to Atlas
client = MongoClient(MONGO_URI)

db = client["todo_db"]
collection = db["items"]

@app.route("/")
def home():
    return render_template("todo.html")


# -----------------------------
<<<<<<< HEAD
# Get To-Do Items Route
# -----------------------------
@app.route("/gettodoitems", methods=["GET"])
def get_todo_items():
    try:
        items = list(collection.find({}, {"_id": 0}))  # _id हटाया ताकि साफ JSON मिले
        return jsonify(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
=======
>>>>>>> master_1
# Submit To-Do Item Route
# -----------------------------
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description")

        todo_item = {
            "itemName": item_name,
            "itemDescription": item_description
        }

        collection.insert_one(todo_item)

        return jsonify({"message": "To-Do item added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

<<<<<<< HEAD

=======
>>>>>>> master_1
# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> master_1
