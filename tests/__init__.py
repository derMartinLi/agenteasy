import sys
import pathlib

cur_folder = pathlib.Path(__file__).parent.parent / "src"
sys.path.append(str(cur_folder))
