from flask import Flask, jsonify, request,render_template
from py2neo import Graph, Node, Relationship
import json

app = Flask(__name__)
graph = Graph("bolt://localhost:7687", auth=("python", "123123"))

@app.route("/")
def index():
    return render_template("index.html")



@app.route('/get_person_data', methods=['POST'])

def get_person_data():

    # получаем ФИО из запроса
    fio = request.json['name']
    print(fio)

    # запрашиваем данные о персоне из графа по ФИО
    query = """
       MATCH (Manager {name:$fio})--(Events:Event)--(Persons2:Person2)
       RETURN Events.id, Persons2.name
       LIMIT 100
       """
    result = graph.run(query, fio=fio).data()
    print(result)
    # возвращаем данные в формате JSON
#    data = json.loads(result)
    data = result

    # возвращаем данные в формате JSON
    return render_template('index.html', events=data)


@app.route('/api/get_person_data_py', methods=['POST'])

def get_person_data_py():

    # получаем ФИО из запроса
    fio = request.json['name']
    print(fio)

    # запрашиваем данные о персоне из графа по ФИО
    query = """
       MATCH (Manager {name:$fio})--(Events:Event)--(Persons2:Person2)
       RETURN Events.id, Persons2.name
       LIMIT 100
       """
    result = graph.run(query, fio=fio).data()
    print(result)

    # возвращаем данные в формате JSON
    return result



@app.route('/api', methods=['POST'])
def export_graph():
    fio = "data"

    # запрашиваем данные о персоне из графа по ФИО
    query = """
        MATCH (Person)--()--()
        WITH Person.name AS name, count(*) AS count
        WHERE count > 1
        RETURN name, count
        """

    # экспортируем данные в формате graphml
    result = graph.run(query, fio=fio).data()
    print(result)

    posts = result

    return render_template('index.html', posts=posts)

@app.route('/api_py', methods=['POST'])
def export_graph_py():
    fio = "data"

    # запрашиваем данные о персоне из графа по ФИО
    query = """
        MATCH (Person)--()--()
        WITH Person.name AS name, count(*) AS count
        WHERE count > 1
        RETURN name, count
        """

    # экспортируем данные в формате graphml
    result = graph.run(query, fio=fio).data()
    print(result)

    return result


if __name__ == '__main__':
    app.run(debug=True)