from typing import Union

from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/abe", response_class=HTMLResponse)
def read_root():
    return '''
    <html>
        <script>
            function makeCapital(str) {
                return str.toUpperCase()
            }
        </script>
        <body>
            <input text="inputStr" placeholder="p text"/>
            <button type="button">Click Me!</button>
            hello <h3>abe</h3> da <p>man dfddf df df</p>
            <a href="https://google.com">take me to microsft.com</a>
        </body>
    </html>
    '''

@app.get("/mae" , response_class=HTMLResponse)
def read_root():
    return '''<h1>mae</h1> <b>is</b> better than abe
    <table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
  <tr>
    <td>one</td>
    <td>two</td>
    <td>creative</td>
  </tr>
</table>

'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}