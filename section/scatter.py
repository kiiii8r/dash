
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np  # 乱数を生成するため
import plotly.graph_objs as go  # ダッシュの裏側で使用されているライブラリ

np.random.seed(1)  # 乱数の基準を設定する
x1 = np.random.randint(0, 100, 50)  # 0~100の間で50個ランダム生成
y1 = np.random.randint(0, 100, 50)

np.random.seed(2)
x2 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(
        id='sample-scatter',
        figure={
            'data': [
                go.Scatter(
                    x=x1,
                    y=y1,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15
                    },
                    name='グループ１'
                ),
                go.Scatter(
                    x=x2,
                    y=y2,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15
                    },
                    name='グループ２'
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'x軸'},
                yaxis={'title': 'y軸'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
