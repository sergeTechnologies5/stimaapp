from flask_migrate import Migrate, MigrateCommand
from app import create_app, db


app = create_app()

migrate = Migrate(app, db)
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host='192.168.0.195',port='5000')
