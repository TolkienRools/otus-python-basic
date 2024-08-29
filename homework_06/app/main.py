from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from database_connection import db
from views.task import task_router
from config import DB_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(task_router, url_prefix='/tasks')


@app.route("/", endpoint='home')
def index():
    return redirect(url_for('tasks.tasks'))


# export PYTHONPATH=$PYTHONPATH:/path/to/your/project

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5050,
    )
