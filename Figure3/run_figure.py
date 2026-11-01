from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(root/"scripts"/"reproduce.py"),"figure3",*sys.argv[1:]],check=True)
