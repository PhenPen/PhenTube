# PhenTube

A simple, interactive command-line tool for downloading YouTube videos and playlists with flexible format selection and subtitle support.

## Features

- **Video & Playlist Downloads** - Download single videos or entire playlists from YouTube
- **Flexible Quality Selection** - Choose automatic best quality or manually select video/audio format
- **Subtitle Support** - Download subtitles in default or custom languages
- **Custom Download Locations** - Configure where your downloads are saved
- **Interactive CLI** - User-friendly command-line interface with clear prompts
- **Format Control** - Choose between combined files (video+audio) or separate streams

## Prerequisites

- Python 3.x
- `yt-dlp` - YouTube downloader library
- Internet connection

## Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd phenTube
   ```

2. **Install dependencies**
   ```bash
   pip install yt-dlp
   ```

3. **Run the application**
   ```bash
   python yT.py
   ```

## Usage

### Quick Start

```bash
python yT.py
```

Follow the prompts:
1. Enter **V** for Video or **P** for Playlist
2. Paste the YouTube URL
3. Select quality option:
   - **B** for best quality (automatic)
   - **S** to manually select format
4. Choose subtitle preferences

### Download Examples

**Download a single video in best quality:**
```
Enter V for Video and P for Playlist: V
Enter Youtube Video URL: https://www.youtube.com/watch?v=...
Download best quality format(B) or select for format personally(S): B
Do you want subtitles (y/n): Y
```

**Download a playlist with custom format:**
```
Enter V for Video and P for Playlist: P
Enter Youtube Playlist URL: https://www.youtube.com/playlist?list=...
Download best quality for all playlist videos(B) or select format personally(S): S
Download video and audio file together or a single file: T
Select a video and audio file using ID: 247+250
```

**Download with subtitles in multiple languages:**
```
Do you want subtitles (y/n): Y
Enter D for default subs and A for another language: A
[List of available subtitles displayed]
Enter language from options: en,fr,es
```

## Project Structure

```
phenTube/
├── yT.py                          # Main entry point
│
├── contentSelect/                 # Content type selection logic
│   ├── __init__.py
│   ├── video.py                   # Single video handling
│   └── playlist.py                # Playlist handling
│
├── downloadSelect/                # Download execution logic
│   ├── __init__.py
│   ├── downloaderVideo.py         # Downloads individual videos
│   └── downloaderPlaylist.py      # Downloads entire playlists
│
├── configSelect/                  # Configuration management
│   ├── __init__.py
│   └── config.py                  # Download location configuration
│
├── subtitleSelect/                # Subtitle handling
│   ├── __init__.py
│   ├── subsVideo.py               # Subtitles for videos
│   └── subsPlaylist.py            # Subtitles for playlists
│
├── metaDataSelect/                # Metadata features (coming soon)
│   ├── __init__.py
│   └── metaData.py
│
└── README.md                       # This file
```

## Configuration

### First Time Setup
On first run, you'll be prompted to enter your default download location:
```
Enter default location for downloads: C:\Users\YourUsername\Downloads
```

### Configuration File
The configuration is stored at:
```
C:\Users\HP\AppData\Roaming\yt-dlp\config.txt
```

**Example config.txt:**
```
# Save downloads to Downloads folder
-o "C:\Users\HP\Downloads\%(title)s.%(ext)s"
```

To change the download location, simply delete this file and run the application again.

## Format Selection

When you choose to manually select format (**S** option), the tool displays available formats using `yt-dlp -F`.

**Format Selection Tips:**
- **Best Combined Format:** Single file with video and audio merged (larger file, easier to use)
- **Separate Streams:** Video and audio as separate files (more control, requires merging)
- **Format IDs:** Use the ID numbers shown (e.g., `247` or `247+250` for video+audio)

## Requirements

```
yt-dlp>=2023.0.0
```

Install with:
```bash
pip install yt-dlp
```

## Troubleshooting

**Q: "yt-dlp command not found"**
- A: Install yt-dlp: `pip install yt-dlp`

**Q: Downloads not saving to the right location**
- A: Delete the config file at `C:\Users\HP\AppData\Roaming\yt-dlp\config.txt` and run again to reconfigure

**Q: "Invalid URL" error**
- A: Make sure you're using a valid YouTube video or playlist URL

**Q: Subtitle download fails**
- A: Some videos may not have subtitles available. Try manually checking on YouTube first.

## License

[Unlicensed for Now]

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) before submitting a pull request.

---

**Note:** This tool is designed for personal use. Always respect copyright and usage rights when downloading content from YouTube.
