# SharePoint List API
This snippet demonstrates the querying of a SharePoint list over the API for on-prem SharePoint

## SharePoint Data Structure
The included code includes a filter to filter the results down to a single entry from the list. Below I show the data structure for a few entries so that you can see how it's navigated.

```
{
	"d": {
		"results": [
			{
				"__metadata": {
					"id": "374feb03-a354-424a-82c7-6cf23a5cd9e8",
					"uri": "https://sharepoint.lab.martincrothers.com/ExampleSite/_api/Web/Lists/(guid'71277c21-c65e-1aef-a0f5-183fe7aecf8d')/Items(1)",
					"etag": "\"3\"",
					"type": "ExampleSite.Data.SupportTeamContactsListItem"
				},
				"Title": "Network Support Level 1",
				"email_address": "network.team@lab.martincrothers.com",
				"incident_queue": "Network Team Level 1"
			},
			{
				"__metadata": {
					"id": "374feb03-a354-424a-82c7-6cf23a5cd9e8",
					"uri": "https://sharepoint.lab.martincrothers.com/ExampleSite/_api/Web/Lists/(guid'71277c21-c65e-1aef-a0f5-183fe7aecf8d')/Items(2)",
					"etag": "\"2\"",
					"type": "ExampleSite.Data.SupportTeamContactsListItem"
				},
				"Title": "Windows Support Level 1",
				"email_address": "windows.team@lab.martincrothers.com",
				"incident_queue": "Windows Team Level 1"
			},
			{
				"__metadata": {
					"id": "374feb03-a354-424a-82c7-6cf23a5cd9e8",
					"uri": "https://sharepoint.lab.martincrothers.com/ExampleSite/_api/Web/Lists/(guid'71277c21-c65e-1aef-a0f5-183fe7aecf8d')/Items(3)",
					"etag": "\"2\"",
					"type": "ExampleSite.Data.SupportTeamContactsListItem"
				},
				"Title": "Database SQL",
				"email_address": "sql.team@lab.martincrothers.com",
				"incident_queue": "Database SQL"
			}
		],
		"__next": "https://sharepoint.lab.martincrothers.com/ExampleSite/_api/Web/Lists/GetByTitle('SupportTeamContacts')/items?%24skiptoken=Paged%3dTRUE%26p_ID%3d3&%24select=Title%2cemail_address%2cincident_queue&%24top=3"
	}
}
```



## Python

## PowerShell