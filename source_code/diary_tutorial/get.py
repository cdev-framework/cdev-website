def entries_serializer(obj_list):
    data = []
    for object in obj_list:
        dictionary = {
            'id':object.id,
            'title':object.title,
            'content':object.content
        }
        data.append(dictionary)
    print("data complete")
    return data

@ServerlessFunction("get_entries_function", events=[get_entries_route.event()], 
environment={"CLUSTER_ARN": myDB.output.cluster_arn, "SECRET_ARN": myDB.output.secret_arn, "DB_NAME": myDB.database_name}, 
permissions=[myDB.available_permissions.DATABASE_ACCESS, myDB.available_permissions.SECRET_ACCESS])
def get_entriess(event, context):
    print('Hello from inside your get entriess Function!')

    session = Session(engine)
    try:
        entries: Entry = session.query(Entry).order_by('id').all()
        data = entries_serializer(entries)
        return Response(200, body=json.dumps(data))
    except Exception as e:
        return Response(400, body=json.dumps({"message": str(e)}))