# RoyalRoad Downloader with UI
A download utility for archiving content from [RoyalRoad](https://www.royalroad.com/).

Exports stories and books in three formats (HTML, PDF, EPUB) with four color theme choices (Light, Dark, Midnight, Sepia). All with its own UI.

## Supported Formats
- `.html` - Web page
- `.pdf` - Portable Document Format
- `.epub` - Electronic Publication

Other formats may be added in the future if requested.

## Color Themes
- **Light** - Standard light theme
- **Dark** - RoyalRoad's dark theme
- **Midnight** - Dark theme with low contrast (recommended for reading)
- **Sepia** - Sepia/old paper theme

Other themes may be added in the future if requested.

## Requirements
- Python 3.10 or higher
- Required Python packages:
  - BeautifulSoup4
  - WeasyPrint
  - Ebooklib
  - Requests
  - PySide6 (Qt for Python)

[View the full list in requirements.txt](req.txt)

## Installation

### Option 1: Executables
Look for Linux and Windows executables in [releases](https://github.com/NaikeR303/rr_downloader_rework/releases).

These executables should work without any additional packages or libraries.

### Option 2: From Source

#### Linux
Install Python if not installed already
```bash
sudo apt update
sudo apt install python3 python3-pip
```
Clone or download the project files
```bash
git clone https://github.com/NaikeR303/rr_downloader_rework.git
cd royalroad-downloader
```
Create virtual environment and activate it
```bash 
python3 -m venv venv
source venv/bin/activate
```
Install requirements
```bash
pip install -r req.txt
```
Run the application
```bash
python main.py
```

#### Windows
- Install [Python](https://www.python.org/) if not installed already
- Clone or download the project files

Create virtual environment and activate it
```bash
python3 -m venv venv
.\venv\Scripts\activate
```
Install requirements
```bash
pip install -r req.txt
```
Run the application
```bash
python main.py
```
## Usage
1. **Enter URL**: Paste the RoyalRoad story URL in the input field
2. **Select Theme**: Choose from one of the four color themes
3. **Choose Format**: Click your preferred download format button
4. **Wait for Completion**: A popup will notify you when download finishes
5. **Find File**: Check the directory with `main.py` or executable for your exported file

## License
MIT License

Do whatever you want, just don't forget to mention me

And please, for personal use only. **Respect authors of the books you archive**