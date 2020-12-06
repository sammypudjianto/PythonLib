import os
import sys
from pathlib import Path

parent_path = Path(os.path.dirname(os.path.realpath(__file__))).parent
# print(parent_path)

sys.path.append(str(parent_path))
