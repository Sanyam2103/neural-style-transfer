# Neural Style Transfer

## Project Overview
This project implements Neural Style Transfer (NST) using TensorFlow and provides a user-friendly interface using Streamlit. Neural Style Transfer is a deep learning technique that allows blending the content of one image with the style of another image, resulting in visually appealing artworks.

The core idea behind NST is to separate and then recombine the content and style of two input images using a pre-trained convolutional neural network, typically VGG19.

## Installation Instructions
To set up the environment and run the project, follow these steps:

1. **Clone the Repository:** Clone the repository to your local machine using Git.
   
2. **Navigate to the Project Directory:** Move into the project directory: cd neural-style-transfer

3. **Install Dependencies:** Install the required Python packages listed in `requirements.txt`: pip install -r requirements.txt


## Usage
To use the code, follow these steps:

1. **Run the Streamlit App:** Launch the Streamlit app by executing the following command: streamlit run Code/app.py
   
2. **Upload Images:** Once the app is running, open the provided URL in your web browser. Use the file upload buttons to upload a content image and a style image.

3. **Apply Neural Style Transfer:** After uploading both images, click the "Style" button to apply Neural Style Transfer.

4. **View Results:** Wait for the process to complete. The styled image will be displayed in the app interface.

5. **Download Styled Image:** Optionally, you can download the styled image by clicking the "Download Styled Image" button.

## Dependencies
The project relies on the following Python libraries and dependencies:

- [Streamlit](https://streamlit.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [NumPy](https://numpy.org/)
- [PIL (Python Imaging Library)](https://pillow.readthedocs.io/en/stable/)
- [Matplotlib](https://matplotlib.org/)

These dependencies are listed in the `requirements.txt` file and can be installed using `pip`.

## Example
Here's an example of how to use the code:

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies.
4. Run the Streamlit app.
5. Upload a content image and a style image.
6. Click "Style" to apply NST.
7. View and download the styled image.

## References
- https://www.tensorflow.org/tutorials/generative/style_transfer
- Gatys, Leon A., et al. "A Neural Algorithm of Artistic Style." arXiv preprint arXiv:1508.06576 (2015).
- Streamlit Documentation: https://docs.streamlit.io/
- TensorFlow Documentation: https://www.tensorflow.org/guide





