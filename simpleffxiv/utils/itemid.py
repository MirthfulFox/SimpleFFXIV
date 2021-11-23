def getitemid(client, name, indexes=["Item"], columns=["ID"]):
    id = client.index_search(name=name, indexes=indexes, columns=columns)
    return id