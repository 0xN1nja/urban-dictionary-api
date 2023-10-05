# Urban Dictionary API
An API For Urban Dictionary Written In Flask

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
curl "https://urban-dictionary-api.0xN1nja.repl.co/api?word={word}"
```
Python (requests)
```python
import requests
import json
word = "" # Enter A Word
res = requests.get(f"https://urban-dictionary-api.0xN1nja.repl.co/api?word={word}").content
res = json.loads(res)
print(res)
```
Node.js (axios)
```javascript
const axios = require('axios');
const word = ""; // Enter A Word
axios.get(`https://urban-dictionary-api.0xN1nja.repl.co/api?word=${word}`)
.then(res=>console.log(res.data))
.catch(err=>console.log(err));
```

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# License
[MIT](https://github.com/0xN1nja/urban-dictionary-api/blob/master/LICENCE.txt)
