"""Build dark photographic stand-ins for public/photos/1.jpg..6.jpg.

Replace those files with real Vindam Fitness Gym photos. Keep the names.
"""

from __future__ import annotations

import random
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parents[1] / "public" / "photos"
W, H = 1600, 1100


def grain(seed: int, blur: float) -> Image.Image:
    rng = random.Random(seed)
    raw = rng.randbytes(W * H)
    img = Image.frombytes("L", (W, H), raw)
    return img.filter(ImageFilter.GaussianBlur(blur))


def glow(box: tuple[int, int, int, int], blur: float, strength: float) -> Image.Image:
    img = Image.new("L", (W, H), 0)
    ImageDraw.Draw(img).ellipse(box, fill=255)
    img = img.filter(ImageFilter.GaussianBlur(blur))
    return img.point(lambda p, s=strength: min(255, int(p * s)))


def build(seed: int, lights: list[dict], grade: tuple[int, int, int], blur: float, amp: float) -> Image.Image:
    base = grain(seed, blur).point(lambda p, a=amp: min(255, int(p * a)))
    for spec in lights:
        base = ImageChops.add(base, glow(spec["box"], spec["blur"], spec["strength"]))
    r, g, b = grade
    rgb = Image.merge(
        "RGB",
        (
            base.point(lambda p, c=r: min(255, c + p)),
            base.point(lambda p, c=g: min(255, c + int(p * 0.94))),
            base.point(lambda p, c=b: min(255, c + int(p * 0.82))),
        ),
    )
    vig = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vig).ellipse((-280, -220, W + 280, H + 260), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(90))
    vig = ImageOps.autocontrast(vig)
    shade = Image.merge("RGB", (vig, vig, vig))
    rgb = ImageChops.multiply(rgb, shade)
    rgb = ImageEnhance.Contrast(rgb).enhance(1.18)
    return rgb


VARIANTS = [
    dict(
        seed=11,
        blur=0.85,
        amp=0.42,
        grade=(5, 4, 3),
        lights=[
            {"box": (260, 160, 1360, 940), "blur": 70, "strength": 0.38},
            {"box": (980, 80, 1620, 760), "blur": 48, "strength": 0.22},
        ],
        brightness=0.78,
    ),
    dict(
        seed=29,
        blur=0.8,
        amp=0.28,
        grade=(8, 9, 11),
        lights=[
            {"box": (-300, -100, 700, 900), "blur": 80, "strength": 0.66},
            {"box": (900, 500, 1800, 1300), "blur": 60, "strength": 0.22},
        ],
    ),
    dict(
        seed=47,
        blur=1.6,
        amp=0.2,
        grade=(12, 9, 6),
        lights=[
            {"box": (200, -400, 1400, 500), "blur": 100, "strength": 0.8},
            {"box": (0, 700, 1600, 1300), "blur": 40, "strength": 0.35},
        ],
    ),
    dict(
        seed=83,
        blur=0.55,
        amp=0.34,
        grade=(7, 7, 7),
        lights=[
            {"box": (150, 80, 780, 700), "blur": 55, "strength": 0.55},
            {"box": (860, 40, 1500, 640), "blur": 55, "strength": 0.42},
        ],
    ),
    dict(
        seed=101,
        blur=1.3,
        amp=0.18,
        grade=(14, 10, 7),
        lights=[
            {"box": (-100, 500, 1700, 1400), "blur": 50, "strength": 0.7},
            {"box": (1000, -200, 1900, 600), "blur": 80, "strength": 0.3},
        ],
    ),
    dict(
        seed=157,
        blur=0.9,
        amp=0.24,
        grade=(6, 7, 8),
        lights=[
            {"box": (-400, -100, 500, 1200), "blur": 70, "strength": 0.75},
            {"box": (600, 200, 1500, 1000), "blur": 90, "strength": 0.25},
        ],
    ),
]


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for index, spec in enumerate(VARIANTS, start=1):
        img = build(spec["seed"], spec["lights"], spec["grade"], spec["blur"], spec["amp"])
        if spec.get("brightness"):
            img = ImageEnhance.Brightness(img).enhance(spec["brightness"])
        path = ROOT / f"{index}.jpg"
        img.save(path, "JPEG", quality=78, optimize=True, progressive=True)
        print(f"{path.name} {path.stat().st_size}")


if __name__ == "__main__":
    main()
