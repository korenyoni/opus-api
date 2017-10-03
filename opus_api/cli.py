# -*- coding: utf-8 -*-

"""Console script for opus_api."""


import click
import opus_api


@click.group()
def main(args=None):
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
def title():
    """
     Get OPUS title
    """
    click.echo(opus_api.get_title())

if __name__ == "__main__":
    main()
