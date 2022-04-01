from cdev.resources.simple.table import Table, AttributeDefinition, KeyDefinition, key_type, attribute_type

from .link_service import TABLE_VAR_NAME

myAttributes = [
  AttributeDefinition("PK", attribute_type.S),
  AttributeDefinition("timestamp", attribute_type.S),
]

myKeys = [
  KeyDefinition("PK", key_type.HASH),
  KeyDefinition("timestamp", key_type.RANGE),
 
]


LinkTable = Table("RecentLinkTable", myAttributes, myKeys)


link_table_permissions = [LinkTable.available_permissions.READ_AND_WRITE_TABLE]
link_table_env_var = {
    TABLE_VAR_NAME: LinkTable.output.table_name,
}