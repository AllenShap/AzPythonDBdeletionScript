from azure.cosmos import CosmosClient, PartitionKey
from azure.identity import DefaultAzureCredential



#Modify the following 4 variables to match the connection details of the CosmosDB, they are used to connect to the cosmos DB container which items will be deleted from.
endpoint = "https://AzureCosmosDBAccountName.documents.azure.com:443/"  
databaseName = "USNYTPythonTwitterBot"                                  #This value will be the actual database name which is made IN the Comos DB Account (It is NOT the Azure Cosmos DB Account name in the top left corner of the portal).
containerName = "USNYTPythonTwitterBotContainer"                        #This value will be the ID associated with the database name (databaseName variable).
credential = "Loremipsumdolorsitametconsecteturadipiscingelitseddoeiusmodtemporincididuntutlaboraaaa==" #This value will be the PRIMARY KEY of the whole Azure Cosmos DB ACCOUNT.


def deleteSpecificCosmosDBItems():
    client = CosmosClient(url=endpoint, credential=credential)
    database = client.create_database_if_not_exists(id=databaseName)
    partitionKeyPath = PartitionKey(path="/id")                                                                     #Replace the path variable value with the unique key of the DB entries.
    container = database.create_container_if_not_exists(id=containerName, partition_key=partitionKeyPath)

    cosmosDBQuery = "SELECT * FROM AzureCosmosDBAccountName p WHERE p.id LIKE @id"                              #Modify query to replace AzureCosmosDBAccountName with the Cosmos Database ACCOUNT name
    id = "2024-04-26%"                                                                                          #In my case, I made the unique key to be the timestamp of when the item was inserted into the database. So I always had true unique entries. The % sign is a wildcard so I could delete all items inserted on a specific day.
    params = [dict(name="@id", value=id)]
    results = container.query_items(query=cosmosDBQuery, parameters=params, enable_cross_partition_query=True)
    items = [item for item in results]
    for i in items:
        container.delete_item(i, "61dba35b-xxxx-xxxx-xxxx-xxxxxxxx")                                        #Replace the string with the partition key associated with the item(s) which will be deleted.

deleteSpecificCosmosDBItems()
