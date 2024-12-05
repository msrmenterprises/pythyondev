from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text

app = Flask(__name__)
CORS(app)

# Connect to SQLite database
engine = create_engine('sqlite:///example.db')

@app.route('/text-to-sql', methods=['POST'])
def text_to_sql():
    user_input = request.json.get('query').lower()  # Convert to lowercase for consistency

    # Map user input to SQL queries
    if "list all emails" in user_input:
        sql_query = "SELECT email FROM users"
    elif "list all users" in user_input:
        sql_query = "SELECT * FROM users"
    else:
        # Default fallback query (this will likely not match anything)
        sql_query = "SELECT * FROM users WHERE name LIKE '%{}%'".format(user_input)

    print("Executing Query:", sql_query)    

    try:
        # Execute query
        with engine.connect() as connection:
            result = connection.execute(text(sql_query))
            rows = [dict(row._mapping) for row in result]  # Safe conversion using _mapping
        return jsonify({"success": True, "data": rows, "query": sql_query})
    except Exception as e:
        return jsonify({"success": False, "error": str(e), "query": sql_query})



if __name__ == '__main__':
    app.run(debug=True)
