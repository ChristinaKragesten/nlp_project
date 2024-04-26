import click

from nlp.setup_data import SetUpData
from nlp.src_code.summary import TextSummary

@click.group()
@click.option(
    "--cfg_filepath",
    default="/workspaces/healthcare_nlp/nlp/config/config.yaml",
    help="path to configuration yaml file"
)
@click.option(
    "--txt_filepath",
    default="/workspaces/healthcare_nlp/nlp/src_data/semantics_text.txt",
    help="path to csv with text"
)

@click.pass_context
def cli(ctx, cfg_filepath: str, txt_filepath: str):
    ctx.obj = SetUpData(config_filepath=cfg_filepath, text_filepath=txt_filepath)

@cli.command()
@click.option("--above_avg_factor", default=1.2)
@click.pass_context
def summarize(ctx, above_avg_factor):
    print(TextSummary(ctx.obj.text, above_avg_factor).summarize())
