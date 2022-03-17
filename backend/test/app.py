from flask import Flask,jsonify

app = Flask(__name__)


employees = [{
    'firstname': 'Silvia',
    'lastname': 'Njoki',
    'email': 'silvianjoki@gmail.com',
    'job_id': '3232',
    'education': 'Degree',
    'jobgroup': 'JobGroup B',
    'position': 'Manager',
    'photo_url': 'http://'},

    {
    'firstname': 'Hawa',
    'lastname': 'Evakali',
    'email': 'ailabeyqute@gmail.com',
    'job_id': '8367',
    'education': 'PhD',
    'jobgroup': 'JobGroup A',
    'position': 'CEO',
    'photo_url': 'http://'},

    {
    'firstname': 'Felix',
    'lastname': 'Kibet',
    'email': 'kenya1@gmail.com',
    'job_id': '6888',
    'education': 'KCSE',
    'jobgroup': 'JobGroup D',
    'position': 'Cook',
    'photo_url': 'http://'},


    {
    'firstname': 'Brian',
    'lastname': 'Otieno',
    'email': 'ot@gmail.com',
    'job_id': '1027',
    'education': 'Masters',
    'jobgroup': 'JobGroup B',
    'position': 'Financial Manager',
    'photo_url': 'http://'},


     {
    'firstname': 'Isaac',
    'lastname': 'Ndirangu',
    'email': 'kimoda@gmail.com',
    'job_id': '4560',
    'education': 'KCSE',
    'jobgroup': 'JobGroup B',
    'position': 'Security Officer',
    'photo_url': 'http://'},

     {
    'firstname': 'Daniel',
    'lastname': 'Njoroge',
    'email': 'dan@gmail.com',
    'job_id': '3345',
    'education': 'Dagree',
    'jobgroup': 'JobGroup C',
    'position': 'Clerk',
    'photo_url': 'http://'},
    
    
    
]



@app.route('/')
def index():
    return 'Welcome Here'



@app.route('/employees', methods=['GET'])
def get():
    return jsonify({'Employees':employees})


@app.route('/employees/<int:job_id>', methods=['GET'])
def get_course_id(job_id):
    return jsonify({'employees': employees[job_id]})




@app.route('/employees', methods=['POST'])
def create():
    employee = {
    'firstname': 'John',
    'lastname': 'Njoroge',
    'email': 'john@gmail.com',
    'job_id': '3345',
    'education': 'Masters',
    'jobgroup': 'JobGroup B',
    'position': 'IT officer',
    'photo_url': 'http://'}
    employees.append(employee)

    return jsonify ({'Created': employee})


# used for updating existing info
@app.route('/employees/<int:job_id>', methods=['PUT'])
def course_update(job_id):
    employees[job_id]['firstname']= "James"
    return jsonify({'course':employees[job_id]})




if __name__ == '__main__':
        app.run(debug=True)