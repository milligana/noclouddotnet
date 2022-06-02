#
#  This file is part of NoCloud.Net.
#
#  Copyright (C) 2022 Last Bastion Network Pty Ltd
#
#  NoCloud.Net is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later version.
#
#  NoCloud.Net is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#  PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along with
#  NoCloud.Net. If not, see <https://www.gnu.org/licenses/>. 
#


import os
from dynaconf import FlaskDynaconf
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# environment variables for settings
# eg NOCLOUD_NET_FOO=1
ENVVAR_PREFIX_DYNACONF = 'NOCLOUD_NET'

# dynaconf config path
# eg NOCLOUD_NET_SETTINGS=./settings.yaml
#
# default:
#  foo: 1
ENVVAR_FOR_DYNACONF = 'NOCLOUD_NET_SETTINGS'

# hmmm - not sure if we can configure this ...
INSTANCE_PATH = '/var/lib/noclouddotnet'

def create_app():
    app = Flask(__name__, instance_path=INSTANCE_PATH)

    # ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    initialize_extensions(app)
    register_blueprints(app)

    return app



##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)

    FlaskDynaconf(app,
                  ENVVAR_PREFIX_DYNACONF=ENVVAR_PREFIX_DYNACONF,
                  ENVVAR_FOR_DYNACONF=ENVVAR_FOR_DYNACONF)

    db.init_app(app)


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from noclouddotnet.instance import instance_blueprint

    app.register_blueprint(instance_blueprint)
