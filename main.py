# # from flask import Flask, render_template,request,send_file,Response
# # from flask_socketio import SocketIO
# # import pickle
# # import numpy as np
# # from typing import Dict, List, Optional, Any
# # import os, string, re
# # # from flask_ngrok import run_with_ngrok
# # from langchain import LLMChain, OpenAI, PromptTemplate
# # from synt_search import BabyAGI, vectorstore, TaskCreationChain, TaskPrioritizationChain, LLMChain, ZeroShotAgent, AgentExecutor, tools, prompt, execute_task, get_next_task, prioritize_tasks, deque

# # app = Flask(__name__)
# # # run_with_ngrok(app)  
# # socketio= SocketIO(app)
# # @app.route("/")
# # def home():
# #     return render_template("home.html")

# # @socketio.on('generate_event')

# # def generate_event(userInput):
# #     output = generate(userInput)
# #     socketio.emit('generated_output', output)

# # def generate(a):
# #     llm = OpenAI(temperature=0)
    
# #     # Logging of LLMChains
# #     verbose=False
# #     # If None, will keep on going forever
# #     max_iterations: Optional[int] = 5
# #     baby_agi = BabyAGI.from_llm(
# #         llm=llm,
# #         vectorstore=vectorstore,
# #         verbose=verbose,
# #         max_iterations=max_iterations
# #     )

# #     return baby_agi({"objective": a})


# # if __name__ == '__main__':
# #     socketio.run(app, port=8000, host='0.0.0.0', debug=True)
# from flask import Flask, render_template,request,send_file,Response
# from flask_socketio import SocketIO, emit
# import pickle
# import numpy as np
# from typing import Dict, List, Optional, Any
# import os, string, re
# from langchain import LLMChain, OpenAI, PromptTemplate
# from synt_search import BabyAGI, vectorstore, TaskCreationChain, TaskPrioritizationChain, LLMChain, ZeroShotAgent, AgentExecutor, tools, prompt, execute_task, get_next_task, prioritize_tasks, deque

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "secret!"
# socketio = SocketIO(app)

# @app.route("/")
# def home():
#     return render_template("home.html")

# @socketio.on('generate_event', namespace='/generate')
# def generate_event(userInput):
#     for output in generate(userInput):
#         socketio.emit('generated_output', output, namespace='/generate')
#     # output = generate(userInput)
#     # emit('generated_output', output)

# def generate(a):
#     llm = OpenAI(temperature=0)
    
#     # Logging of LLMChains
#     verbose=False
#     # If None, will keep on going forever
#     max_iterations: Optional[int] =  2
#     baby_agi = BabyAGI.from_llm(
#         llm=llm,
#         vectorstore=vectorstore,
#         verbose=verbose,
#         max_iterations=max_iterations
#     )

#     return baby_agi({"objective": a})

# if __name__ == '__main__':
#     socketio.run(app, debug=True, port=5000, namespace='/generate')
















# from flask import Flask, render_template, request
# from flask_socketio import SocketIO, emit

# from langchain import LLMChain, OpenAI
# from search import BabyAGI, vectorstore, TaskCreationChain, TaskPrioritizationChain, LLMChain, ZeroShotAgent, AgentExecutor, tools, prompt, execute_task, get_next_task, prioritize_tasks, deque


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @socketio.on('generate_event')
# def generate_event(input_text):
#     output, log = generate(input_text)
#     emit('generated_output', {'output': output, 'log_output': log})

# def generate(a):
#     llm = OpenAI(temperature=0)
#     # Logging of LLMChains
#     verbose = True
#     # If None, will keep on going forever
#     max_iterations = 2
#     baby_agi = BabyAGI.from_llm(
#         llm=llm,
#         vectorstore=vectorstore,
#         verbose=verbose,
#         max_iterations=max_iterations
#     )
#     # output = baby_agi({"objective": a})
#     return socketio.emit('logging_output', {'output': baby_agi({"objective": a})}, namespace='/test')


# if __name__ == '__main__':
#     socketio.run(app, debug=True)















from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from langchain import LLMChain, OpenAI
from search import BabyAGI, vectorstore, TaskCreationChain, TaskPrioritizationChain, LLMChain, ZeroShotAgent, AgentExecutor, tools, prompt, execute_task, get_next_task, prioritize_tasks, deque

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @socketio.on('generate_event')
# def generate_event(data):
#     output = generate(data)
#     emit('generated_output', {'output': output})

# def generate(a):
#     llm = OpenAI(temperature=0)
#     # Logging of LLMChains
#     verbose=False
#     # If None, will keep on going forever
#     max_iterations = 2
#     baby_agi = BabyAGI.from_llm(
#         llm=llm,
#         vectorstore=vectorstore,
#         verbose=verbose,
#         max_iterations=max_iterations
#     )
#     output = baby_agi({"objective": a})
#     return output


# if __name__ == '__main__':
#     socketio.run(app, debug=True)


from flask import Flask, render_template
from flask_socketio import SocketIO

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @socketio.on('connect')
# def test_connect():
#     print('Client connected')

# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')

# @app.route('/')
# def index():
#     return render_template('home.html')

# @app.route('/generate/<objective>')
# def generate(objective):
#     llm = OpenAI(temperature=0)
    
#     # Logging of LLMChains
#     verbose=False
#     # If None, will keep on going forever
#     max_iterations: Optional[int] = 2
#     baby_agi = BabyAGI.from_llm(
#         llm=llm,
#         vectorstore=vectorstore,
#         verbose=verbose,
#         max_iterations=max_iterations
#     )

#     # Generate the task with BabyAGI
#     result = baby_agi({"objective": objective})

#     # Send the output to the client
#     socketio.emit('output', result)

# if __name__ == '__main__':
#     socketio.run(app)





# def generate(OBJECTIVE):
#     llm = OpenAI(temperature=0)
    
#     # Logging of LLMChains
#     verbose=False
#     # If None, will keep on going forever
#     max_iterations: Optional[int] = 1
#     baby_agi = BabyAGI.from_llm(
#         llm=llm,
#         vectorstore=vectorstore,
#         verbose=verbose,
#         max_iterations=max_iterations
#     )
#     baby_agi({"objective": OBJECTIVE})
#     from search import text
#     return text
# generate("Behave as a security resercher, get me all the information you can on Ogundayo femi")


from flask import Flask, request, render_template

def generate(OBJECTIVE):
    llm = OpenAI(temperature=0)
    
    # Logging of LLMChains
    verbose=False
    # If None, will keep on going forever
    max_iterations= 2 
    baby_agi = BabyAGI.from_llm(
        llm=llm,
        vectorstore=vectorstore,
        verbose=verbose,
        max_iterations=max_iterations
    )
    baby_agi({"objective": OBJECTIVE})
    with open('myfile.txt', 'r') as f:
        lines = f.readlines()
    return lines


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from the form
        input_string = request.form['input_string']
        # Call the generate function with the input
        output_list = generate(input_string)
        
        # Render the template with the output list
        return render_template('form.html', input_string=input_string, output_list=output_list)
    else:
        # Render the form
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

