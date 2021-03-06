from app import create_app,db
from flask_script import Manager,Server
from app.auth.v1.models.user_models import User,Restaurant,Food,Review,Order,Delivery
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)
@manager.command
def test():
    """Run init tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Restaurant = Restaurant, Food = Food, Review = Review, Order = Order, Delivery = Delivery)

if __name__ == '__main__':
    manager.run()