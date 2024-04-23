import click
from healthcare_nlp.setup_data import SetUpData

@click.group()
@click.option(
    "--cfg_filepath",
    default="/workspaces/healthcare_nlp/healthcare_nlp/config/config.yaml",
    help="path to configuration yaml file"
)

@click.pass_context
def cli(ctx, cfg_filepath: str):
    ctx.obj = SetUpData(config_filepath=cfg_filepath)

@cli.command()
@click.option("--val", default=1)
@click.pass_context
def squared(ctx, val):
    print(ctx.obj.config["initial_value"] + val**2)