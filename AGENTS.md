# AGENTS.md

This is a Python project for converting images to sketches using OpenCV.

## Project Overview
- **Purpose**: Apply sketch effects to images via image processing techniques.
- **Main file**: `Image to sketch.py` - Contains the `make_sketch(image_path)` function.
- **Language**: Python with OpenCV library.

## Setup and Dependencies
- Install Python 3.x if not already available.
- Install required packages: `pip install opencv-python`
- No virtual environment configured; consider using `venv` or `conda` for isolation.

## Running the Project
- Place an input image named `input.jpg` in the project directory.
- Run the script: `python "Image to sketch.py"`
- Output will be saved as `my_sketch.jpg` in the same directory.

## Conventions
- Code is written in English, but comments are in Hindi (e.g., step-by-step explanations).
- Function and variable names follow English conventions.
- Hardcoded values (e.g., blur kernel size 21x21) may need parameterization for flexibility.
- No classes or modules; procedural style.

## Common Pitfalls
- Ensure `opencv-python` is installed; otherwise, `ModuleNotFoundError` on import.
- Input file `input.jpg` must exist; no validation or error handling for missing files.
- Output overwrites `my_sketch.jpg` without confirmation.
- Large images may process slowly due to Gaussian blur; consider optimizations.
- Platform-specific issues: OpenCV setup on Windows may require additional steps.

## Best Practices
- Add input validation and exception handling.
- Make paths configurable via command-line arguments.
- Refactor into a class for better structure.
- Add tests using `pytest` for the `make_sketch` function.
- Create a `README.md` for detailed documentation (link to it once created).

## Links
- [OpenCV Documentation](https://docs.opencv.org/) for image processing details.</content>
<parameter name="filePath">c:\Users\ALI BABA TRAVEL\Desktop\image to sketch\AGENTS.md