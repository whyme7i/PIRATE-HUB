import os
import json

banners_folder = "static/banners"
output_file = "games.json"

games = []

# List all image files
for idx, filename in enumerate(sorted(os.listdir(banners_folder)), start=1):
    if filename.lower().endswith(('.jpg', '.png')):
        game_entry = {
            "id": idx,
            "title": os.path.splitext(filename)[0],  # filename without extension
            "description": "Description for " + os.path.splitext(filename)[0],
            "banner": filename,
            "download": "#"
        }
        games.append(game_entry)

# Save to JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(games, f, indent=4, ensure_ascii=False)

print(f"{len(games)} games added to {output_file}")
