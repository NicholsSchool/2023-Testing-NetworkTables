from _pynetworktables import NetworkTables

ip = "10.1.21.122"
NetworkTables.initialize()

table = NetworkTables.getTable("mahogany")

while True:
    response = input( "Happy? " )
    if response == "quit":
        break
    table.putString( "camden_status", "Camden happy? " + response )
    print( table.getString("camden_status", ""))