from pathlib import Path

from fastapi import FastAPI, File, UploadFile
import subprocess
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# Directory where the tiles will be stored
tile_base_path = "/tiles"

# Ensure the directory exists
os.makedirs(tile_base_path, exist_ok=True)
# Mount the static file directory for tiles
app.mount("/tiles", StaticFiles(directory=tile_base_path), name="tiles")


@app.post("/upload/")
async def process_image(file: UploadFile = File(...)):
    filename = Path(file.filename).stem
    file_location = f"/tmp/{filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())

    # Output directory for tiles
    output_dir = f"{tile_base_path}/{filename}"
    os.makedirs(output_dir, exist_ok=True)

    # Run gdal2tiles.py
    subprocess.run(["python3",
                    "/gdal2tiles-server/gdal2tiles.py",
                    "--leaflet",
                    "-p", "raster",
                    "-z", "0-4",
                    "-w", "none", file_location, output_dir], check=True)

    # For simplicity, just returning a message
    # Ideally, you might want to return a ZIP of the output directory or URLs to access the tiles
    # http://localhost:8000/tiles/image-name/{zoom}/{x}/{y}.png

    return {"message": "Tiles processed", "tile_directory": output_dir}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
