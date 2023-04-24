from enum import Enum

from pydantic import BaseModel, validator

from youtube_downloader.utils import (
    get_url_from_youtube_id,
    get_video_info,
    validate_id,
)


class VideoInfo(BaseModel):
    id: str
    title: str
    # formats: List[Any]
    thumbnail: str
    description: str
    # channel_id: str
    # channel_url: str
    ext: str


def get_video_info_model(id: str) -> VideoInfo:
    result_json = get_video_info(id=id)

    return VideoInfo(
        id=result_json["id"],
        title=result_json["title"],
        thumbnail=result_json["thumbnail"],
        description=result_json["description"],
        # formats=[],
        # formats=result_json["formats"],
        ext=result_json["ext"],
    )


class Category(Enum):
    """Category of an item"""

    UNCATEGORIZED = "uncategorized"
    MOVIE = "movie"
    TVSHOW = "tvshow"


class Item(BaseModel):
    """Representation of an item in the system."""

    id: str
    # id: str = Field(description="Unique string that specifies this item.")
    info: VideoInfo
    category: Category = Category.UNCATEGORIZED

    @validator("id")
    def valid_youtube_id(cls, v):
        is_valid = validate_id(id=v)

        if not is_valid:
            raise ValueError("id is not valid")

        return v

    @property
    def url(self) -> str:
        return get_url_from_youtube_id(id=self.id)
