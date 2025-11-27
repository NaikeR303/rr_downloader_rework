from pathlib import Path


class Renderer:
    """
    Give it all chaptes and then choose how to save them
    """
    def __init__(self, chapters):
        self.all_chapters = chapters

    def to_txt(self, save_path):
        save_path = Path(save_path)
        
        print(save_path.name)


if __name__ == "__main__":
    from downloader import Downloader

    d = Downloader('https://www.royalroad.com/fiction/114710/engineering-magic-and-kitsune')

    r = Renderer()

