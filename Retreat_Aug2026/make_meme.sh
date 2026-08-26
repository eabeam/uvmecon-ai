#!/bin/zsh
# Usage: ./make_meme.sh <screenshot.png|jpg> ["caption text"] [out.png]
# Impact-style meme caption at the bottom of the image.
IN="$1"
TEXT="${2:-COULD REALLY GET ME OUT OF A COUPLE OF JAMS}"
OUT="${3:-meme_ranch.png}"
FONT="/System/Library/Fonts/Supplemental/Impact.ttf"
W=$(magick identify -format "%w" "$IN")
PT=$(( W / 18 ))
magick "$IN" \
  \( -background none -fill white -stroke black -strokewidth $(( PT / 14 )) \
     -font "$FONT" -pointsize $PT -size "$(( W - 40 ))x" -gravity center caption:"$TEXT" \) \
  -gravity south -geometry +0+25 -composite "$OUT"
echo "wrote $PWD/$OUT"
