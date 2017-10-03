# -*- coding: utf-8 -*-

"""Console script for opus_api."""


import click

@click.command()
def main(args=None):
    """
    OPUS (opus.lingfil.uu.se) Command Line Interface
    """
    click.echo(
        """
                    /$$$$$$            /$$$$$$$  /$$   /$$  /$$$$$$
                   /$$__  $$          | $$__  $$| $$  | $$ /$$__  $$
          /$$$$$$$| $$  \ $$  /$$$$$$ | $$  \ $$| $$  | $$| $$  \__/
         /$$_____/| $$  | $$ /$$__  $$| $$$$$$$/| $$  | $$|  $$$$$$
        | $$      | $$  | $$| $$  \__/| $$____/ | $$  | $$ \____  $$
        | $$      | $$  | $$| $$      | $$      | $$  | $$ /$$  \ $$
        |  $$$$$$$|  $$$$$$/| $$      | $$      |  $$$$$$/|  $$$$$$/
        \_______/ \______/ |__/      |__/       \______/  \______/
        """
    )
    with click.Context(main) as ctx:
        click.echo(main.get_help(ctx))

if __name__ == "__main__":
    main()
