from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from langchain import LLMChain, OpenAI
from search import BabyAGI, vectorstore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('generate')
def generate_response(data):
    input_string = data['objective']
    llm = OpenAI(temperature=0)
    baby_agi = BabyAGI.from_llm(llm=llm, vectorstore=vectorstore,max_iterations=3)
    
    # Send the response to the client using websockets
    emit('generated', {'response': str(baby_agi({"objective": input_string}))}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
