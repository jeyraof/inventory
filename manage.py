# -*- coding: utf-8 -*-
__author__ = 'Jaeyoung'


import click


@click.group()
def cli():
    """
    Group for commands
    """
    pass


@cli.command()
@click.option('--host', '-h', default='0.0.0.0', help='runserver with specific host', show_default=True)
@click.option('--port', '-p', default=8001, help='runserver with specific port', show_default=True)
@click.option('--debug', '-d', is_flag=True, help='runserver with debug mode', default=False, show_default=True)
def runserver(host, port, debug):
    """
    Run server using flask
    """
    try:
        from inventory import app
        app.run(host=str(host),
                port=int(port),
                debug=bool(debug))
    except Exception as msg:
        print 'Failed to run server:'
        print '====================='
        print msg


@cli.command()
def init_db():
    """
    Initialize tables you defined via model.
    """
    from inventory import db
    db.create_all()


@cli.command()
def drop_db():
    """
    Drop all of tables you defined via model.
    """
    from inventory import db
    db.drop_all()


@cli.command()
def reload_db():
    """
    Just do drop_db() after init_db().
    """
    from inventory import db
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    cli()
