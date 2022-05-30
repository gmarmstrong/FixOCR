import tesserocr
from flask import Flask
from PIL import Image
from tesserocr import PyTessBaseAPI, RIL, iterate_level, PyResultIterator
from typing import List, Tuple

app = Flask(__name__)

SAMPLE_PATH = "static/samples/eurotext.png"
sample = Image.open(SAMPLE_PATH)


@app.route("/")
def main_page() -> str:
    """
    :return: HTML for the main page
    """
    # TODO Use an actual templating language instead of f-strings...
    output = "<h2>Image</h2>"
    output += f"""<img style="max-height: 300px" src="{SAMPLE_PATH}" alt="The image being analyzed"/>"""
    output += "<h2>Analysis</h2>"
    output += "<ul>"
    for text, confidence in analyze(sample):
        output += f"<li>{text} ({round(confidence, 2)}%)</li>"
    output += "</ul>"
    return output


@app.route("/recognize")
def recognize(image: Image = sample) -> str:
    """
    Very basic text recognition. Result cannot
    be used for any deeper inspection. Just
    a demo of the image_to_text function.

    :param image: an Image object to analyze
    :return: text detected in the image
    """
    return tesserocr.image_to_text(image)


def analyze(image: Image) -> List[Tuple[str, float]]:
    """
    :param image: an Image object to analyze
    :returns:
        a list of the words found in the image as (text, confidence)
        tuples, where text should be interpreted as UTF-8 str and
        confidence should be interpreted as a percent
        probability float (from 0.0 to 100.0).
    """
    output: List[Tuple[str, float]] = []
    with PyTessBaseAPI() as api:
        api.SetImage(image)
        api.SetVariable("save_blob_choices", "T")
        api.Recognize()
        level = RIL.WORD
        symbol: PyResultIterator
        for symbol in iterate_level(api.GetIterator(), level):
            text = symbol.GetUTF8Text(level)
            confidence: float = symbol.Confidence(level)
            if text:
                output.append((text, confidence))
    return output


if __name__ == "__main__":
    app.run()
