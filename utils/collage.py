import asyncio
import io
from typing import List, Tuple, Union

from aiogram import Bot
from aiogram.types import BufferedInputFile, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageOps

import config


# Build inline button linking to the bot for posting announcements
BOT_URL = f"https://t.me/{getattr(config, 'BOT_USERNAME', 'demo_bot_2022Bot')}"
elon_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✍️ ЭЪЛОН БЕРИШ", url=BOT_URL)]
    ]
)


def create_collage(
    images: List[Image.Image],
    width: int = 1200,
    padding: int = 10,
    bg_color: Tuple[int, int, int] = (255, 255, 255),
) -> Image.Image:
    """
    Arranges 2 to 10 images logically into a clean collage with thin borders.
    For 3 images, matches standard layout: top row = 2 images, bottom row = 1 full-width image.
    """
    n = len(images)
    if n == 0:
        raise ValueError("Kamida bitta rasm kerak.")
    if n == 1:
        return images[0]

    # Logical layouts (row_counts, row_heights) for 2 to 10 images
    layouts = {
        2: ([2], [500]),
        3: ([2, 1], [460, 460]),
        4: ([2, 2], [440, 440]),
        5: ([2, 3], [390, 390]),
        6: ([3, 3], [360, 360]),
        7: ([2, 3, 2], [290, 290, 290]),
        8: ([4, 4], [320, 320]),
        9: ([3, 3, 3], [290, 290, 290]),
        10: ([3, 4, 3], [270, 270, 270]),
    }

    row_counts, row_heights = layouts.get(n, ([n], [400]))
    total_height = sum(row_heights) + padding * (len(row_heights) + 1)
    collage = Image.new("RGB", (width, total_height), color=bg_color)

    img_idx = 0
    y_offset = padding

    for r, count in enumerate(row_counts):
        h = row_heights[r]
        total_gaps = (count + 1) * padding
        avail_w = width - total_gaps
        cell_w = avail_w // count
        rem = avail_w % count

        x_offset = padding
        for c in range(count):
            extra = 1 if c < rem else 0
            w = cell_w + extra
            # Scale and center-crop each image to fit the cell exactly without distortion
            fitted = ImageOps.fit(images[img_idx], (w, h), method=Image.Resampling.LANCZOS)
            collage.paste(fitted, (x_offset, y_offset))
            x_offset += w + padding
            img_idx += 1
        y_offset += h + padding

    return collage


async def build_collage_or_photo(
    bot: Bot,
    photo_ids: List[str],
) -> Union[str, BufferedInputFile]:
    """
    If 1 photo_id is passed, returns the original photo_id directly (zero processing/download overhead).
    If 2 or more photo_ids are passed, downloads them and builds a high-res JPEG collage BufferedInputFile.
    """
    if not photo_ids:
        raise ValueError("Kamida bitta rasm kerak.")

    if len(photo_ids) == 1:
        return photo_ids[0]

    async def _fetch_photo(fid: str) -> Image.Image:
        bio = io.BytesIO()
        await bot.download(fid, destination=bio)
        bio.seek(0)
        return Image.open(bio).convert("RGB")

    # Download images concurrently (up to 10)
    images = await asyncio.gather(*[_fetch_photo(fid) for fid in photo_ids[:10]])
    collage = create_collage(images)

    output = io.BytesIO()
    collage.save(output, format="JPEG", quality=92, optimize=True)
    output.seek(0)
    return BufferedInputFile(output.getvalue(), filename="collage.jpg")
