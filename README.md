# Urban Dictionary API (Unofficial)
A Simple API In Flask 
# Author
Abhimanyu Sharma, https://github.com/N1nja0p
## Usage
```bash
GET
/api?word={word}
```
## Examples
cURL
```bash
curl https://urban-dictionary-api.n1nja0p.repl.co/api?word={word}
```
Python (Requests)
```python
import requests
import json
word="" # Enter A Word
r=requests.get(f"https://urban-dictionary-api.n1nja0p.repl.co/api?word={word}").content
r=json.loads(r)
print(r)
```
Node.js (Axios)
```javascript
const axios = require('axios');
const word=""; // Enter A Word
axios.get(`https://urban-dictionary-api.n1nja0p.repl.co/api?word=${word}`)
.then(res => console.log(res.data))
.catch(err => console.log(err));
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.