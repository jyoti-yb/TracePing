import typer
from cli.trace import trace
from cli.view import view
from cli.graph import graph

app = typer.Typer()

app.command()(trace)
app.command()(view)
app.command()(graph)

if __name__ == "__main__":
    app()
