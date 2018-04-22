# -*- coding: utf-8 -*-

"""Console script for opus_api."""


from opus_api.util import minint, maxint
import click
import opus_api.opus_api as base
import pkg_resources
from opus_api.exceptions import InvalidSrcException, InvalidTrgException, InvalidFormException
from opus_api.cache import clearCache


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


    OPUS (opus.nlpl.eu) Command Line Interface
    """


@main.command()
@click.argument('src')
@click.argument('target')
@click.option('--minimum', default=minint(),
              help="Minimum sentences (src + target tokens) in millions")
@click.option('--maximum', default=maxint(),
              help="Maximum sentences (src + target tokens) in millions")
@click.option('--form', default='moses',
              help="Format of parallel corpora (default: MOSES)")
def get(src, target, minimum, maximum, form):
    """
    Get src-target corpora
    """
    if minimum < 0 and minimum != minint():
        raise click.UsageError('minimum cannot be negative')
    if maximum < 0:
        raise click.UsageError('maximum cannot be negative')
    if minimum > maximum:
        raise click.UsageError('minimum cannot be greater than maximum')
    try:
        click.echo(base.get(src, target, minimum, maximum, form))
    except InvalidSrcException as e:
        raise(click.UsageError('invalid source: ' + e.lang))
    except InvalidTrgException as e:
        raise(click.UsageError('invalid target: ' + e.lang))
    except InvalidFormException as e:
        raise(click.UsageError('invalid form: ' + e.form))


@main.command()
def langs():
    """
    Get list of available languages
    """
    click.echo(base.langs())


@main.command()
def clear():
    """
    Clear the JSON and HTML cache
    """
    clearCache()
    click.echo("Cache cleared.")


if __name__ == "__main__":
    main()
