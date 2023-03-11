# README

# PDF Title Updater

This is a Python script that updates the title property of a PDF file and adds custom properties based on user input.

## Getting Started

To use this script, you will need Python 3 installed on your machine, as well as the following dependencies:

- PyPDF2

You can install the dependencies by running the following command:

```bash
pip install PyPDF2
```

## Usage

To use this script, follow these steps:

1. Clone this repository to your local machine.
2. Open a terminal window and navigate to the directory where you cloned the repository.
3. Run the following command:

```bash
python pdf_title_updater.py
```

4. Follow the prompts to enter the input file path, title, author, and custom properties for the PDF file.

- The input file path should be the path to the PDF file you want to update.
- The title and author should be strings that you want to set for the PDF file.
- The custom properties are optional and you can skip them by leaving the fields empty.

5. The script will update the title property and custom properties of the PDF file, and save the updated file in the same location as the original file.

- If the input file path and output file path are the same, the original file will be overwritten with the updated file.

6. The script will print the file path of the updated PDF.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.

## Project Structure

The project contains the following files:

- `pdf_title_updater.py`: the Python script that updates the title property of a PDF file and adds custom properties based on user input.
- `README.md`: this file, providing an overview of the project and instructions on how to use it.
- `LICENSE`: the license file for the project.

The `pdf_title_updater.py` file contains the following functions:

- `update_pdf_title_property`: updates the title property of a PDF file and adds custom properties.
- `get_pdf_properties_from_user`: prompts the user for necessary and optional inputs to update a PDF file.
- `main`: updates the title property of a PDF file and adds custom properties based on user input.

These functions are documented in the Numpy docstring format, which provides detailed information on the function's name, description, parameters, returns, preconditions, and notes.

## How it Works

The `pdf_title_updater.py` script uses the `PyPDF2` library to read and write PDF files. When the script is run, it prompts the user to enter the input file path, title, author, and custom properties for the PDF file. It then calls the `update_pdf_title_property` function with the input parameters and custom properties to update the title property and custom properties of the PDF file. The function creates a new PDF file with the updated title and custom properties, and saves it in the same location as the original file. Finally, the script prints the file path of the updated PDF.

The `update_pdf_title_property` function updates the title property of a PDF file by adding a metadata object to the PDF writer object. It also adds custom properties to the PDF by setting additional metadata properties in the PDF writer object.

The `get_pdf_properties_from_user` function prompts the user for the necessary and optional inputs to update a PDF file. It returns a tuple containing the input file path, title, author, and custom properties specified by the user.

The `main` function is the entry point of the script. It calls the `get_pdf_properties_from_user` function to get the input parameters and custom properties from the user, and then calls the `update_pdf_title_property` function with the input parameters to update the title property and custom properties of the PDF file. It finally prints the file path of the updated PDF.

## Converting to an Executable

You can convert the `pdf_title_updater.py` script to a standalone executable using PyInstaller. PyInstaller bundles a Python application and all its dependencies into a single package that can be run on any machine without needing to install Python or the dependencies separately.

To convert the script to an executable, follow these steps:

1. Install PyInstaller using pip:

```bash
pip install pyinstaller
```

2. Navigate to the directory containing the `pdf_title_updater.py` script in a terminal window.
3. Run the following command to create a standalone executable:

```bash
pyinstaller pdf_title_updater.py
```

4. PyInstaller will create a `dist` folder containing the standalone executable and any other files required to run it.

- If you want to create a single executable file instead of a folder, use the `--onefile` option:

  ```
  pyinstaller --onefile pdf_title_updater.py
  ```
- If you want to exclude certain files or folders from the package, use the `--exclude` or `--exclude-folder` options.
- For more information on PyInstaller options, see the [documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html).

You can now distribute the standalone executable to users who don't have Python or the dependencies installed.

## Contributing

Contributions to this project are welcome! To contribute, follow these steps:

1. Fork this repository to your own GitHub account and clone it to your local machine.
2. Create a new branch for your feature or bug fix: `git checkout -b my-new-feature`
3. Make your changes and commit them with a descriptive commit message.
4. Push your changes to your fork: `git push origin my-new-feature`
5. Submit a pull request to the `main` branch of this repository, and describe your changes and the problem or feature they address.

Please make sure your code follows the existing code style and passes the automated tests before submitting a pull request.

## Issues

If you encounter any issues while using this script, please report them on the [GitHub issue tracker](https://github.com/your_username/pdf-title-updater/issues).

## Contact

If you have any questions or comments about this project, feel free to contact using the issues tab.
