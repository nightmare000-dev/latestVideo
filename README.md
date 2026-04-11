```markdown
# YouTube Latest Video Extractor

A lightweight command-line tool to quickly fetch information about the **latest video** from any YouTube channel using `yt-dlp`.

Built with **Click** for CLI handling and **Rich** for beautiful console output.

## Features

- Extracts the most recent video from a YouTube channel
- Displays: Channel name, Video title, URL, Duration, and Upload date
- Clean and colorful output
- Fast and lightweight (no video download)
- Easy to use via command line

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/youtube-latest-video.git
cd youtube-latest-video
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install click yt-dlp rich
```

## Usage

### Basic command

```bash
python main.py CHANNEL_NAME
```

**Examples:**

```bash
python main.py MrBeast
python main.py PewDiePie
python main.py LinusTechTips
python main.py Veritasium
```

### Options

| Option                | Description                                      | Default     |
|-----------------------|--------------------------------------------------|-------------|
| `channel_name`        | YouTube channel handle (without @)               | Required    |
| `--js-runtimes`       | JavaScript runtime used by yt-dlp                | `node`      |
| `--item`              | Which video to extract (1 = latest)              | `1`         |

### Advanced Examples

```bash
# Get the 3rd latest video
python main.py Veritasium --item 3

# Change JS runtime
python main.py Kurzgesagt --js-runtimes node
```

## Example Output

```
Extracting... ✓

Channel:      MrBeast
Title:        I Spent 50 Hours Buried Alive
URL:          https://www.youtube.com/watch?v=abc123xyz...
Duration:     24:51
Upload Date:  08.04.2026
```

## Project Structure

```
youtube-latest-video/
├── main.py                 # Main script
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.8 or higher
- yt-dlp
- click
- rich

## How It Works

The script constructs a YouTube channel videos URL (`https://www.youtube.com/@channel_name/videos`), extracts playlist information using `yt-dlp`, and displays details of the latest video.

## License

MIT License

---

You can now copy and paste this directly into your `README.md` file.

Would you like me to also create a `requirements.txt` file content and maybe add a "Troubleshooting" section?
```
