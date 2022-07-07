@simple_function_annotation("create_entry_function", events=[create_entries_route.event()], 
environment={"CLUSTER_ARN": myDB.output.cluster_arn, "SECRET_ARN": myDB.output.secret_arn, "DB_NAME": myDB.database_name}, 
permissions=[myDB.available_permissions.DATABASE_ACCESS, myDB.available_permissions.SECRET_ACCESS])
def create_entry(event, context):
    print('Hello from inside your entry creation Function!')

    session = Session(engine)
    data = json.loads(event.get("body"))
    try:
        session.add(Entry(title=data.get("title"), content=data.get("content")))
        session.commit()
        return Response(200, body = json.dumps({"message": "Created entry"}))
    except Exception as e:
        print(str(e))
        return Response(400, body = json.dumps({"message":"entry creation failed"}))