# -*- coding: utf-8 -*-

"""Console script for opus_api."""


import click
import opus_api
import pkg_resources


@click.group()
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

    if (version):
        version = pkg_resources.require("opus_api")[0].version
        click.echo(version)


@main.command()
@click.argument('src')
@click.argument('target')
def get(src, target):
    """
    Get src-target corpora
    """
    click.echo(src + ' ' + target)


@main.command()
@click.option('--pp', is_flag=True, help='Use pretty-printing', default=True)
def langs(pp):
    """
    Get list of available languages
    """
    click.echo(opus_api.langs(pp))

if __name__ == "__main__":
    main(False)
