"""Utils functions to handle the paths
    to save the downloaded and produced
    files"""

from pathlib import Path


def get_project_root() -> Path:
    """Get the absolut project root dir."""
    return Path(
        __file__
    ).parent.parent.parent.parent  # <folder>/src/download_clean_data/utils/paths.py


def get_data_directory() -> Path:
    """Get data directory, if doesn't exist create it"""
    data_dir = get_project_root() / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir
