import typer

from string_addition import string_addition

cli_app = typer.Typer()
@cli_app.command()
def string_add(value: str):
    string_value = string_addition(value)
    start = "The strings numeric value is "
    end = typer.style(f"{string_value}", fg=typer.colors.GREEN)
    typer.echo(start + end)
if __name__ == "__main__":
    cli_app()