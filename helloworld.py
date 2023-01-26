from influxdb import InfluxDBClient

def get_influxdb(database_name, host='localhost', port=8086):
    client = InfluxDBClient(host, port)
    try:
        client.create_database(database_name)
        print('create ' + database_name)
    except Exception as e:
        print('create except')
        print(e)
        pass
    try:
        client.switch_database(database_name)
        print('switch ' + database_name)
    except Exception as e:
        print('switch except')
        print(e)
        return None
    return client

client = get_influxdb(database_name='ig_test3', host='34.64.88.253', port=8086)
client.get_list_database()
client.get_list_measurements

points = [{'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 8.0 },
     'time': '2019-01-11 06:00:00+09:00'}, # 한국시간 6시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 8.0},
     'time': '2019-01-11 07:00:00+09:00'}, # 한국시간 17시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 9.5},
     'time': '2019-01-11 08:00:00+09:00'}, # 한국시간 18시
     {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 10.0},
     'time': '2019-01-11 09:00:00+09:00'}, # 한국시간 16시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 12.0},
     'time': '2019-01-11 10:00:00+09:00'}, # 한국시간 17시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 14.0},
     'time': '2019-01-11 11:00:00+09:00'}, # 한국시간 18시
     {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 15.0},
     'time': '2019-01-11 12:00:00+09:00'}, # 한국시간 16시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 17.0},
     'time': '2019-01-11 13:00:00+09:00'}, # 한국시간 17시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 17.5},
     'time': '2019-01-11 14:00:00+09:00'}, # 한국시간 18시
     {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 17.0},
     'time': '2019-01-11 15:00:00+09:00'}, # 한국시간 16시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 14.0},
     'time': '2019-01-11 16:00:00+09:00'}, # 한국시간 17시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 13.5},
     'time': '2019-01-11 17:00:00+09:00'}, # 한국시간 18시
     {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 12.0},
     'time': '2019-01-11 18:00:00+09:00'}, # 한국시간 16시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 11.5},
     'time': '2019-01-11 19:00:00+09:00'}, # 한국시간 17시
    {'measurement':'temp', 
     'tags':{'server_id': 'server1'}, 
     'fields':{'v': 10.0},
     'time': '2019-01-11 20:00:00+09:00'}, # 한국시간 18시
     ]

client.write_points(points=points, protocol='json')

rs = client.query("""
    SELECT max(v) as cnt_v
    FROM temp 
    WHERE time >= now() - 12h GROUP BY time(3h)
    """)
for point in rs.get_points():
    print(point)