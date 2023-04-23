from typing import Any

import yt_dlp


def extract_youtube_id_from_url(url: str) -> str:
    return url.split("v=")[1].split("&")[0]


def get_url_from_youtube_id(id: str) -> str:
    return f"https://www.youtube.com/watch?v={id}"


def validate_id(id: str) -> bool:
    return True


def isAV(s: Any) -> bool:
    return str(s).lower() != "none"


def get_video_info(id: str) -> Any:
    url = get_url_from_youtube_id(id=id)

    with yt_dlp.YoutubeDL() as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except yt_dlp.utils.YoutubeDLError as exc:
            print(exc)  # noqa: T201

            return None

        return info
