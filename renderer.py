from pathlib import Path
from bs4 import BeautifulSoup
import re


class Styles:
    class HTML:
        antique = 1
        midnight = 2
        light = 3
        dark = 4
    class PDF:
        antique = 1
        midnight = 2
        light = 3
        dark = 4

class Renderer:
    """
    Give it all chaptes and then choose how to save them
    """
    def __init__(self, chapters):
        self.all_chapters = chapters

        self.soup = BeautifulSoup(chapters)

    def _safe_name(name: str) -> str:
        """Return a filesystem-safe version of *name*."""
        name = name.strip(' .')
        # drop every character that is NOT letter, digit, space, dash or underscore
        name = re.sub(r'[^\w\s-]', '', name)
        # collapse runs of spaces into a single underscore
        name = re.sub(r'\s+', '_', name)
        # guarantee we never return an empty or Windows-reserved name
        if not name or name.upper() in {'CON', 'PRN', 'AUX', 'NUL'}:
            name = '_'
        return name

    def to_html(self, save_path, style, title):
        save_path = Path(save_path)

        match style:
            case Styles.HTML.antique:
                pass
            case Styles.HTML.midnight:
                pass
            case Styles.HTML.light:
                pass
            case Styles.HTML.dark:
                pass


        with open(save_path, "w") as file:
            pass            


if __name__ == "__main__":
    from downloader import Downloader

    d = Downloader('https://www.royalroad.com/fiction/114710/engineering-magic-and-kitsune')

    chapters = [d.get_chapter(chap) for chap in d.get_url_list()]

    r = Renderer(chapters)

    r.to_txt("/home/naiker303/Code/Python/rr_downloader_rework/")

