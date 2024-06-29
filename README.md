This Python script is intended to act as the interface for Azure Cosmos DB in which it will delete items from inside of a specific Cosmos DB Account.

Bulk deletion of items in a Cosmos DB used to be somewhat difficult and couldn't be done through SQL queries, it was required to either delete items programmatically in bulk or through Stored Procedures. Now, they have started to implement native support through the portal by allowing the user to select which database entries to delete 1 by 1 using the mouse but there is still no support for deleting items in bulk through SQL queries in the portal. This is why I made a script to be able to delete items in bulk.

Below are pictures of where the connection credentials which need to be modified in the Python file are located in the portal as the documentation used to be somewhat confusing on what values need to be associated with certain parameters

![image](https://github.com/AllenShap/AzPythonDBdeletionScript/assets/164272261/4e27f86c-481d-4e33-a4a2-b6153258ed0f)


Below picture showcases where values for the SQL queries are located within the actual Cosmos DB Container itself.
![image](https://github.com/AllenShap/AzPythonDBdeletionScript/assets/164272261/44ad04d0-76d2-464e-8a05-3add0591455a)


To ensure the script functions correctly, the following Python libraries need to be installed:
 - azure.cosmos
 - azure.identity

There are also comments inside the Python file going into a little more detail if the pictures are not enough.
