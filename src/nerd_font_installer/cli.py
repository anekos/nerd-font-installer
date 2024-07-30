import subprocess
import time
from pathlib import Path

import click

from .installer import install
from .listing import extract_font_urls

TypePath = click.types.Path(path_type=Path)


@click.group()
@click.pass_context
def main(ctx: click.Context) -> None:
    # ctx.obj = App()
    pass


@main.command("install")
@click.argument("dest", type=TypePath, required=True)
def cmd_install(dest: Path) -> None:
    dest.mkdir(exist_ok=True, parents=True)

    urls = extract_font_urls()

    first = True
    for index, url in enumerate(sorted(urls)):
        if not first:
            time.sleep(2)

        print(f"[{index + 1}/{len(urls)}] Installing {url}")
        if install(url, dest):
            print("  Done")
            first = False
        else:
            print("  Font directory already exists, skipping")

    if not first:
        subprocess.run(["fc-cache", "-fv"])


if __name__ == "__main__":
    main()
