#!/usr/bin/env python3

import click
import yt_dlp
from rich.console import Console

cls = Console()


class Functions:
    @click.command()
    @click.argument("channel_name")
    @click.option("--js-runtimes", default="node")
    @click.option("--item", default=1)
    @staticmethod
    def prompt_channel(channel_name, js_runtimes, item):
        channel = f"https://www.youtube.com/@{channel_name}/videos"
        opts = {
            "playlist_items": str(item),
            "extract_flat": "in-playlist",
            "skip_download": True,
            "js_runtimes": {"node": {}},
            "remote_components": ["ejs:github"],
            "quiet": True,
            "no_warnings": True,
            "lazy_playlist": True,
        }

        with yt_dlp.YoutubeDL(opts) as ydl:
            with cls.status("[bold cyan]Extracting...[/]"):
                info = ydl.extract_info(channel, download=False)
                latest = info["entries"][0]
                data = {
                    "uploader": latest.get("uploader"),
                    "title": latest.get("title"),
                    "original_url": latest.get("original_url"),
                    "duration": latest.get("duration"),
                }

                raw_date = latest.get("upload_date")
                formatted_date = f"{raw_date[-2:]}.{raw_date[-4:-2]}.{raw_date[-8:-4]}"
                minutes = data["duration"] // 60
                seconds = data["duration"] % 60
                data["duration"] = f"{minutes}:{seconds:02d}"

                cls.print(f"\n[bold green]Channel:[/] {data['uploader']}")
                cls.print(f"[bold green]Title:[/] {data['title']}")
                cls.print(f"[bold green]URL:[/] {data['original_url']}")
                cls.print(f"[bold green]Duration:[/] {data['duration']}")
                cls.print(f"[bold green]Upload Date:[/] {formatted_date}")

                return data


if __name__ == "__main__":
    Functions.prompt_channel()
