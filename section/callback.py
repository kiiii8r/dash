
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# htmlを生成
app.layout = html.Div([
    dcc.Input(id='input-div', value='initial value', type='text'),
    html.Div(id='output-div')
])

# コールバック関数で非同期
@app.callback(
    Output(component_id='output-div', component_property='children'),
    [Input(component_id='input-div', component_property='value')]
)

# callback関数で入ってくる変数をformatで出力(Inputの値がinput_valueに入ってくるらしい)
def update(input_value):
    return 'You entered {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
