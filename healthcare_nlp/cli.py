import click

from healthcare_nlp.setup_data import SetUpData

@click.group()
@click.option(
    "--cfg_filepath",
    default="/workspaces/healthcare_nlp/healthcare_nlp/config/config.yaml",
    help="path to configuration yaml file"
)
@click.option(
    "--txt_filepath",
    default="/workspaces/healthcare_nlp/healthcare_nlp/src_data/semantics_text.txt",
    help="path to csv with text"
)

@click.pass_context
def cli(ctx, cfg_filepath: str, txt_filepath: str):
    ctx.obj = SetUpData(config_filepath=cfg_filepath, text_filepath=txt_filepath)

@cli.command()
@click.option("--val", default=1)
@click.pass_context
def summarize(ctx, val):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(ctx.obj.text)
 
    frequency_table = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in frequency_table:
            frequency_table[word]+=1
        else:
            frequency_table[word] = 1
    sentences = sent_tokenize(ctx.obj.text)
    sentences_value = dict()
    for sentence in sentences:
        for word, freq in frequency_table.items():
            if word in sentence.lower():
                if sentence in sentences_value:
                    sentences_value[sentence] += freq
                else:
                    sentences_value[sentence] = freq

    sum_values = 0
    for sentence in sentences_value:
        sum_values += sentences_value[sentence]
    
    average = int(sum_values / len(sentences_value))

    summary=""
    for sentence in sentences:
        if (sentence in sentences_value) and (sentences_value[sentence]>(1.2 * average)):
            summary += " " + sentence
    print(summary)


