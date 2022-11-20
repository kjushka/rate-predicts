from flask import Flask
from flask import request
import pandas as pd
import numpy as np
from pmdarima.arima import auto_arima

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def make_prediction():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        requestData = request.get_json()

        rates = np.array(list(requestData.values()))

        dataset = pd.DataFrame(np.array(rates), columns=['rates'])
        auto_arima_fit = auto_arima(dataset, start_p=1, start_q=1,
                            max_p=3, max_q=3, m=12,
                            start_P=0, seasonal=True,
                            d=1, D=1, trace=True,
                            error_action='ignore',
                            suppress_warnings=True,
                            stepwise=True)
        forecasts = auto_arima_fit.predict(n_periods=30, alpha=0.05)
        result = list(map(lambda x: round(x, 4), forecasts.to_list()))
        return result
    else:
        return 'Content-Type not supported!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
