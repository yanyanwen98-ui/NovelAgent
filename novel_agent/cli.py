import typer

app = typer.Typer(help='NovelAgent v0.1 CLI')

@app.command()
def init(path: str):
    '''Initialize a novel project.'''
    typer.echo(f'TODO: initialize project at {path}')

@app.command()
def run(path: str, goal: str):
    '''Run the autonomous novel-agent loop.'''
    typer.echo(f'TODO: run agent for {path}')
    typer.echo(f'Goal: {goal}')

if __name__ == '__main__':
    app()
