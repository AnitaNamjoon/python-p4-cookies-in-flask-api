from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
app.json.compact = False


app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

   
    response_data = {
        'cookies': [{'mouse': request.cookies.get('mouse', 'Cookie')}],
        'session': {
            'session_accessed': session.accessed,
            'session_key': key,
            'session_value': session.get(key),
        },
    }

    response = make_response(jsonify(response_data), 200)
    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    app.run(port=5555)
