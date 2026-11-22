from pathlib import Path
import pandas.core.generic as generic

if not hasattr(generic, "FilePath"):
    generic.FilePath = Path
