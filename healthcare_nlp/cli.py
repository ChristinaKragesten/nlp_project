import click
from pathlib import Path

@click.group()
@click.option(
    "--cfg_filepath",
    default="/workspaces/healthcare_nlp/healthcare_nlp/config/config.yaml",
    help="path to configuration yaml file"
)

@click.pass_context
def cli(ctx, cfg_filepath: str):
    ctx.cfg_filepath = cfg_filepath

@cli.command()
@click.option("--val", default=1)
@click.pass_context
def squared(ctx, val):
    print(val**2)