
import dash
import dash_core_components as dcc
# グラフを作成する
import dash_html_components as html
# htmlを担っている

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# 外部のstylesheetを参照している
# 参照先を増やす場合、List形式で記入

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# 外部のstylesheetをDashで読み込むためのおまじない

colors = {
    'background': 'black',
    'text': 'white'
}

app.layout = html.Div(children=[  # アプリケーションのレイアウト(divでまとめてある)
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'background-color': colors['background']
        }
    ),

    html.Div(children='''
        Dash: A web application framework for Python.
        ''',
             style={
                 'textAlign': 'center',
                 'color': colors['text'],
                 'background-color': colors['background']
             }
             ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [  # グラフのデータ
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                    'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {  # グラフのレイアウト
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],  # グラフの背景
                'paper_bgcolor': colors['background'],  # グラフ周辺の背景
                'font':{
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
# デバッグモード、コードに変更がある度に表示を変更してくれる
