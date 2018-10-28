from flask import *
import api

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/create', methods=['POST'])
def create_lead():
    return api.save_lead(request)


if __name__ == '__main__':
    app.run()
