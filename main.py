import pymongo

client = pymongo.MongoClient("mongodb+srv://user:12345@cluster0.yezzjjp.mongodb.net/?retryWrites=true&w=majority")
db = client.list

  
workers_list = [{"_id": 1,'worker_name': 'Фараон Ірина Олександрівна', 'date_of_birth': '14.01.1985', 'date_of_servece': '10.09.2020', 'email': 'personal_gmail1@gmail.com', 'adress': 'м. Миколаїв вул. Куліша 12', 'telephone_number': '1631963568', 'salary': 17500},
    {"_id": 2,'worker_name': 'Мельник Ірина Іванівна', 'date_of_birth': '24.03.1991', 'date_of_servece': '10.09.2021', 'email': 'personal_gmail2@gmail.com', 'adress': 'м. Херсон вул. 10-та лінія 64', 'telephone_number': '2631963568', 'salary': 16500},
    {"_id": 3,'worker_name': 'Дуб Володимир Олексійович', 'date_of_birth': '21.01.2001', 'date_of_servece': '10.09.2020', 'email': 'personal_gmail3@gmail.com', 'adress': 'м. Одеса вул. Біловодська 12', 'telephone_number': '3631963568', 'salary': 17000},
    {"_id": 4,'worker_name': 'Лев Олесь Олександрович', 'date_of_birth': '30.11.1975', 'date_of_servece': '10.09.2020', 'email': 'personal_gmail4@gmail.com', 'adress': 'м. Миколаїв вул. Шестидесятників 86', 'telephone_number': '4631963568', 'salary': 15500},
    {"_id": 5,'worker_name': 'Леопольд Іван Олегович', 'date_of_birth': '09.10.1988', 'date_of_servece': '10.02.2018', 'email': 'personal_gmail5@gmail.com', 'adress': 'м. Миколаїв вул. Шестидесятників 80', 'telephone_number': '5631963568', 'salary': 25500},
    {"_id": 6,'worker_name': 'Джері Микита Вальдемарович', 'date_of_birth': '17.05.1989', 'date_of_servece': '10.09.2020', 'email': 'personal_gmail6@gmail.com', 'adress': 'м. Київ вул. Народна 32', 'telephone_number': '6631963568', 'salary': 14500},
    {"_id": 7,'worker_name': 'Джентрі Максим Евгенович', 'date_of_birth': '11.04.2002', 'date_of_servece': '10.09.2020', 'email': 'personal_gmail7@gmail.com', 'adress': 'м. Одеса вул. Виговського 22', 'telephone_number': '7631963568', 'salary': 17800},
    {"_id": 8,'worker_name': 'Чорна Анна Володимірівна', 'date_of_birth': '22.07.1985', 'date_of_servece': '25.08.2016', 'email': 'personal_gmail8@gmail.com', 'adress': 'м. Одеса вул. Франка 19', 'telephone_number': '8631963568', 'salary': 17500}]

workers = Worker.select()

subdivision_list = [
        {"_id": 1,'organization_name': 'Національна поліція', 'subdivision_name': 'Департамент Національної поліції',  'number_of_workers': 5231},
        {"_id": 2,'organization_name': 'Національна поліція', 'subdivision_name': 'Управління Національної поліції',  'number_of_workers': 2131},
        {"_id": 3,'organization_name': 'Національна поліція', 'subdivision_name': 'Секретаріат Національної поліції', 'number_of_workers': 3231},
        {"_id": 4,'organization_name': 'Національна поліція', 'subdivision_name': 'Директорат Національної поліції', 'number_of_workers': 5000},
        {"_id": 5,'organization_name': 'Державна фіскальна служба', 'subdivision_name': 'Департамент Державної фіскальної служби',  'number_of_workers': 2280},
        {"_id": 6,'organization_name': 'Державна фіскальна служба', 'subdivision_name': 'Управління Державної фіскальної служби',  'number_of_workers': 1234},
        {"_id": 7,'organization_name': 'Державна фіскальна служба', 'subdivision_name': 'Секретаріат Державної фіскальної служби',  'number_of_workers': 6546},
        {"_id": 8,'organization_name': 'Державна фіскальна служба', 'subdivision_name': 'Директорат Державної фіскальної служби',  'number_of_workers': 5451}
    ]

db.subdivision_list.insert_many(subdivision_list)
db.workers_list.insert_many(workers_list)
