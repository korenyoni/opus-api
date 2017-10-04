# -*- coding: utf-8 -*-

"""Console script for opus_api."""


import click
import opus_api
import pkg_resources
from exceptions import InvalidSrcException, InvalidTrgException


class MainGroup(click.Group):
    def parse_args(self, ctx, args):
        if len(args) == 1 and args[0] == '--version':
            version = pkg_resources.require("opus_api")[0].version
            click.echo(version)
            exit(0)
        else:
            super(MainGroup, self).parse_args(ctx, args)


@click.group(cls=MainGroup)
@click.option('--version', is_flag=True, help="Get version")
def main(version, args=None):
    """
    \b
                /$$$$$$            /$$$$$$$  /$$   /$$  /$$$$$$
               /$$__  $$          | $$__  $$| $$  | $$ /$$__  $$
      /$$$$$$$| $$  \ $$  /$$$$$$ | $$  \ $$| $$  | $$| $$  \__/
     /$$_____/| $$  | $$ /$$__  $$| $$$$$$$/| $$  | $$|  $$$$$$
    | $$      | $$  | $$| $$  \__/| $$____/ | $$  | $$ \____  $$
    | $$      | $$  | $$| $$      | $$      | $$  | $$ /$$  \ $$
    |  $$$$$$$|  $$$$$$/| $$      | $$      |  $$$$$$/|  $$$$$$/
     \_______/ \______/ |__/      |__/       \______/  \______/


    OPUS (opus.lingfil.uu.se) Command Line Interface
    """


@main.command()
@click.argument('src')
@click.argument('target')
def get(src, target):
    """
    Get src-target corpora
    """
    try:
        click.echo(opus_api.get(src, target))
    except InvalidSrcException as e:
        raise(click.UsageError('invalid source: ' + e.lang))
    except InvalidTrgException as e:
        raise(click.UsageError('invalid target: ' + e.lang))


@main.command()
def langs():
    """
    Get list of available languages
    """
    click.echo(opus_api.langs())

if __name__ == "__main__":
    main()
