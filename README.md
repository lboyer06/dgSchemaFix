
DataGrips DB Force Feeder 6000


<h1>What this do</h1>
This quickly adds many DB and associates a schema by using excel and updating the xml file DataGrips uses in project folder
<h1> Why DataGrapes only works well for tiny business </h1>
DataGrapes does not work well with large amount of databases and you cannot force feed it a single schema for all. You have to enable the correct schema each one for possibly 100s or 1000s of DB one after another.

<h1>How to use</h1>

<h3>You must have at least one schema enabled for one DB and have data source set up. </h3>

<ol>
  <li>Go to your project folder and retrieve the dataSources.local.xml file</li>
  <li>Extract it into the venv directory with the main.py file, leave the name alone!!!</li>
  <li>Make an excel sheet with two columns >> db_name | Schema </li>
  <li>Populate the db names and the schemas you want to use e.g. dbo</li>
</ol>
File Names:
    excel_path = "schema_map.xlsx"
    xml_path = "dataSources.local.xml"

This should trigger DG to introspect all of these DB automatically instead of having to go thru each one.


