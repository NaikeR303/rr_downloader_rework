from pathlib import Path
from ebooklib import epub
from enum import Enum, auto
import platform
import pdfkit
import re


class Styles(Enum):
    ANTIQUE = auto()
    LIGHT = auto()
    DARK = auto()
    MIDNIGHT = auto()
    SEPIA = auto()

class Renderer:
    """
    Give it all chapters and then choose how to save them
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

    def _create_html(self, style_name: int, title: str, author: str, chapters: list, first: bool = True):
        style = """
            h1, h2, h3 {
                display: block;
                width: fit-content;
                margin: 0 auto;
            }
            div {
                margin: 0% 6%;
            }
            body {
                font-family: "Lexend", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;

                padding: 1cm;
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
            case Styles.ANTIQUE:
                style += """
                body {
                    background-color: rgb(175, 146, 109);
                    color: #52331e
                }
                @page {
                    margin: 0.4in;
                    background-color: rgb(175, 146, 109);
                }
                """
            case Styles.SEPIA:
                style += """
                body {
                    background-color: #E5CFAA;
                    color: #404040
                }
                @page {
                    margin: 0.4in;
                    background-color: #E5CFAA;
                }
                """
            case Styles.MIDNIGHT:
                style += """
                body {
                    background-color: rgb(26, 26, 26);
                    color: gray;
                }
                @page {
                    margin: 0.4in;
                    background-color: rgb(26, 26, 26);
                }
                """
            case Styles.LIGHT:
                style += """
                body {
                    background-color: rgb(255, 255, 255);
                    color: rgb(0, 0, 0);
                }
                @page {
                    margin: 0.4in;
                    background-color: rgb(255, 255, 255);
                }
                """
            case Styles.DARK:
                style += """
                body {
                    background-color: rgb(19, 19, 19);
                    color: rgb(207, 207, 207);
                }
                @page {
                    margin: 0.4in;
                    background-color: rgb(19, 19, 19);
                }
                """

        if first:
            content = f"""
            <h1>{title}</h1>
            <h2>By {author}</h2>
            <br><br><br>
            """
        else: 
            content = ""

        # chapter_id, fiction_id, url, date, title, content 
        for chap in chapters:
            content += f"<h2>{chap[4]}</h2>\n"
            content += f"<p style='font-weight: bold; display: block; width: fit-content; margin: 0 auto;'>{chap[3]}</p>\n"

            content += chap[5]
            content += "<br><br><br>\n"

        template = f"""
                    <html>
                        <head>
                            <title>{title} - RoyalRoad</title>
                            <style>{style}</style>
                        </head>
                        <body>
                            {content}
                        </body>
                    </html>
                    """
        
        return template


    def to_html(self, save_path: str, style_name: int, title: str, author: str):
        if not save_path.endswith(".html"):
            save_path = save_path + ".html"

        save_path = Path(save_path)

        template = self._create_html(style_name, title, author, self.all_chapters)

        with open(save_path, "w") as file:
            file.write(template)

    def to_pdf(self, save_path: str, style_name: int, title: str, author: str):
        if not save_path.endswith(".pdf"):
            save_path = save_path + ".pdf"

        save_path = Path(save_path)

        html = self._create_html(style_name, title, author, self.all_chapters)

        if platform.system() == "Windows":
            wk_path = "wkhtmltopdf/win_bin/wkhtmltopdf.exe"
        else:
            wk_path = "wkhtmltopdf/lin_bin/wkhtmltopdf"

        cfg = pdfkit.configuration(wkhtmltopdf=wk_path)   # or full path

        pdfkit.from_string(html, save_path, configuration=cfg, options={'encoding': 'UTF-8',
                                                                        '--page-size': 'A4',
                                                                        '--margin-top': '0',
                                                                        '--margin-bottom': '0',
                                                                        '--margin-left': '0',
                                                                        '--margin-right': '0'})

    def to_epub(self, save_path: str, title: str, author: str):
        if not save_path.endswith(".epub"):
            save_path = save_path + ".epub"

        save_path = Path(save_path)

        # Setting basic stuff
        book = epub.EpubBook()
        book.set_identifier(Renderer._safe_name(title))
        book.set_title(title)
        book.set_language("en")
        book.add_author(author)

        #Cover
        html = f"""
                <html>
                    <body>
                        <h1>{title}</h1>
                        <h2>By {author}</h2>
                    </body>
                </html>
                """
        cover = epub.EpubHtml(title="Cover", file_name=f'cover.xhtml')
        cover.set_content(html)
        book.add_item(cover)

        chaps = [cover]

        # Adding other chapters
        for chap in self.all_chapters:
            html = f"""
                    <html>
                        <body>
                            <h2>{chap[4]}</h2>
                            <p style='font-weight: bold;'>{chap[3]}</p>
                            <br>
                            {chap[5]}
                        </body>
                    </html>
                    """

            # Creating chapters
            chapter = epub.EpubHtml(title=chap[4], file_name=f'{Renderer._safe_name(chap[4])}.xhtml')
            chapter.set_content(html)

            chaps.append(chapter)

            # Add chapter to the book
            book.add_item(chapter)

        book.spine = ['nav'] + chaps

        book.toc = chaps

        epub.write_epub(save_path, book)

if __name__ == "__main__":
    from downloader import Downloader

    d = Downloader('https://www.royalroad.com/fiction/124235/die-trying-a-roguelite-extraction-litrpg/chapter/2424538/chapter-1')

    chapters = d.get_chapters()

    r = Renderer(chapters)

    r.to_pdf("book.pdf", Styles.MIDNIGHT, d.fiction_title, d.author_name)

    r.to_html("book.html", Styles.MIDNIGHT, d.fiction_title, d.author_name)

