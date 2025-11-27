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

        # self.soup = BeautifulSoup(chapters, "html.parser")

    #Thanks Kimi
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

    def to_html(self, save_path, style_name, title, author):
        save_path = Path(save_path)

        style = """
            h1, h2, h3 {
                display: block;
                width: fit-content;
                margin: 0 auto;
            }
            div {
                margin: 0% 6%;
            }
            img {
                display: block;
                margin-left: auto;
                margin-right: auto;
                max-width: 100%;   
                max-height: 80vh; 
                height: auto;     
                width: auto;      
            }
        """

        match style_name:
            case Styles.HTML.antique:
                style += """
                body {
                    background-color: rgb(175, 146, 109);
                    color: #52331e
                }
                """
            case Styles.HTML.midnight:
                style += """
                body {
                    background-color: rgb(26, 26, 26);
                    color: gray;
                }
                """
            case Styles.HTML.light:
                style += """
                body {
                    background-color: rgb(255, 255, 255);
                    color: rgb(0, 0, 0);
                }
                """
            case Styles.HTML.dark:
                style += """
                body {
                    background-color: rgb(19, 19, 19);
                    color: rgb(207, 207, 207);
                }
                """

        content = f"""
        <h1>{title}</h1>
        <h2>By {author}</h2>
        <br><br><br>
        """

        # chapter_id, fiction_id, url, date, title, content 
        for chap in self.all_chapters:
            content += f"<h2>{chap[4]}</h2>\n"
            content += f"<h3>{chap[3]}</h3>\n"

            content += chap[5]
            content += "<br><br><br>\n"

        with open(save_path, "w") as file:
            file.write(f"""
                        <html>
                            <head>
                                <title>{title} - RoyalRoad</title>
                                <style>{style}</style>
                            </head>
                            <body>
                                {content}
                            </body>
                        </html>
                        """)


if __name__ == "__main__":
    from downloader import Downloader

    d = Downloader('https://www.royalroad.com/fiction/114710/engineering-magic-and-kitsune')

    chapters = d.get_chapters()

    r = Renderer(chapters)

    r.to_html("/home/naiker303/Code/Python/rr_downloader_rework/test.html", Styles.HTML.midnight, d.fiction_title, d.author_name)

