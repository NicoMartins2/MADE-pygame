from cx_Freeze import setup, Executable

setup(
    name="MADE",
    version="1.0",
    description="MADE - A 2D Platformer Game",
    executables=[Executable("main.py")],
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["asset/"]
        }
    }
)