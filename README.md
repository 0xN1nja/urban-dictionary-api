# Urban Dictionary API (Unofficial)
A Simple API In Flask 
# Author
Abhimanyu Sharma, https://github.com/0xN1nja
# Usage
```
GET
/api?word={word}
```
# Examples
cURL
```
curl https://urban-dictionary-api.n1nja0p.repl.co/api?word={word}
```
Python (Requests)
```python
import requests
import json
word = "" # Enter A Word
res = requests.get(f"https://urban-dictionary-api.n1nja0p.repl.co/api?word={word}").content
res = json.loads(res)
print(res)
```
Node.js (Axios)
```javascript
const axios = require('axios');
const word = ""; // Enter A Word
axios.get(`https://urban-dictionary-api.n1nja0p.repl.co/api?word=${word}`)
.then(res=>console.log(res.data))
.catch(err=>console.log(err));
```
C# (WebClient)
```csharp
WebClient client = new WebClient();
var word = ""; // Enter A Word
string reply = client.DownloadString($"https://urban-dictionary-api.n1nja0p.repl.co/api?word={word}");
Console.WriteLine(reply);
```
Java (java.net.http)
```java
HttpRequest request = HttpRequest.newBuilder()
     .uri(URI.create("https://urban-dictionary-api.n1nja0p.repl.co/api?word={word}")) // Enter A Word
     .method("GET", HttpRequest.BodyPublishers.noBody())
     .build();
HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```
Kotlin (OkHttp)
```kotlin
val client = OkHttpClient()
val request = Request.Builder()
	.url("https://urban-dictionary-api.n1nja0p.repl.co/api?word={word}") // Enter A Word
	.get()
	.build()
val response = client.newCall(request).execute()
```
# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
# License
[MIT](https://github.com/0xN1nja/Urban-Dictionary-API-Unofficial/blob/master/LICENCE.txt)
