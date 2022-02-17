from cdev.resources.simple.table import Table, AttributeDefinition, KeyDefinition, key_type, attribute_type

myAttributes = [
  AttributeDefinition("email", attribute_type.S),
  AttributeDefinition("date_created", attribute_type.S)
]

myKeys = [
  KeyDefinition("email", key_type.HASH),
  KeyDefinition("date_created", key_type.RANGE)
]


EmailTable = Table("EmailRegistryTable", myAttributes, myKeys)