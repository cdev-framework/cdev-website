from cdev.resources.simple.table import Table, key_type, attribute_type


MyAttributes = [
    {"AttributeName": "email", "AttributeType": attribute_type.S},
    {"AttributeName": "date_created", "AttributeType": attribute_type.S},
]

MyKeys = [
    {"AttributeName": "email", "KeyType": key_type.HASH},
    {"AttributeName": "date_created", "KeyType": key_type.RANGE},
]


EmailTable = Table("EmailRegistryTable", "new_email_registry", MyAttributes, MyKeys)