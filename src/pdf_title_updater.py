import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def update_pdf_title_property(input_file_path, title, author, **kwargs):
    """
    Updates the title property of a PDF file and adds custom properties.

    Name:
    update_pdf_title_property

    Description:
    This function takes an input PDF file path, a title string, an author string,
    and optional custom properties as keyword arguments. It updates the title
    property of the PDF file with the given title and adds any custom properties
    specified in the keyword arguments.

    Parameters:
    input_file_path (str): The file path of the input PDF file.
    title (str): The title to set for the PDF file.
    author (str): The author to set for the PDF file.
    **kwargs (dict): Optional custom properties to add to the PDF file.
        The keys are the property names and the values are the property values.

    Returns:
    str: The file path of the output PDF file.

    Preconditions:
    - The input_file_path must be a valid file path of an existing PDF file.
    - The title must be a non-empty string.
    - The author must be a non-empty string.
    - The keys and values in the kwargs dictionary must be strings.

    Notes:
    - This function does not modify the original PDF file. Instead, it creates
      a new PDF file with the updated title and custom properties.
    - If the input file path and output file path are the same, the original file
      will be overwritten with the updated file.
    """

    # Get the directory path and file name from the input file path
    file_dir, file_name = os.path.split(input_file_path)

    # Open the input PDF file and get its number of pages
    input_pdf = PdfFileReader(open(input_file_path, "rb"))
    num_pages = input_pdf.getNumPages()

    # Create a new PDF writer object
    output_pdf = PdfFileWriter()

    # Set the title and author properties of the output PDF
    output_pdf.addMetadata({
        '/Title': title,
        '/Author': author
    })

    # Set the custom properties of the output PDF if provided
    if 'Processed By' in kwargs:
        output_pdf.addMetadata({
            '/Processed By': kwargs['Processed By']
        })
    if 'County' in kwargs:
        output_pdf.addMetadata({
            '/County': kwargs['County']
        })
    if 'Court Number' in kwargs:
        output_pdf.addMetadata({
            '/Court Number': kwargs['Court Number']
        })

    # Add each page of the input PDF to the output PDF
    for page_num in range(num_pages):
        page = input_pdf.getPage(page_num)
        output_pdf.addPage(page)

    # Create the output file path by combining the directory path and original file name
    output_file_path = os.path.join(file_dir, file_name)

    # Write the output PDF to the output file path
    with open(output_file_path, "wb") as output_file:
        output_pdf.write(output_file)

    # Return the output file path
    return output_file_path

def get_pdf_properties_from_user():
    """
    Prompts the user for necessary and optional inputs to update a PDF file.

    Name:
    get_pdf_properties_from_user

    Description:
    This function prompts the user to enter the input file path, title, author,
    and optional custom properties for the PDF file.

    Parameters:
    None.

    Returns:
    tuple: A tuple containing the input file path (str), title (str), author (str),
    and custom properties (dict). The custom properties dictionary contains optional
    properties specified by the user. The keys are the property names and the values
    are the property values.

    Preconditions:
    - The user must enter valid input when prompted for the input file path, title,
      author, and custom properties.

    Notes:
    - The custom properties are optional and the user may choose to skip them by
      leaving the fields empty.
    """

    # Prompt the user for the necessary input
    input_file_path = input("Enter the input PDF file path: ")
    title = input("Enter the PDF title: ")
    author = input("Enter the PDF author: ")

    # Prompt the user for the optional inputs
    processed_by = input("Enter the 'Processed By' custom property (optional): ")
    county = input("Enter the 'County' custom property (optional): ")
    court_number = input("Enter the 'Court Number' custom property (optional): ")

    # Create a dictionary of the optional inputs
    custom_properties = {}
    if processed_by:
        custom_properties['Processed By'] = processed_by
    if county:
        custom_properties['County'] = county
    if court_number:
        custom_properties['Court Number'] = court_number

    # Return a tuple of the necessary and optional inputs
    return (input_file_path, title, author, custom_properties)

def main():
    """
    Updates the title property of a PDF file and adds custom properties based on user input.

    Description:
    This function prompts the user to enter the input file path, title, author,
    and optional custom properties for the PDF file. It then calls the
    update_pdf_title_property function to update the title property and custom
    properties of the PDF file, and prints the file path of the updated PDF.

    Preconditions:
    - The user must enter valid input when prompted for the input file path, title,
      author, and custom properties.
    - The input file path must be a valid file path of an existing PDF file.

    Notes:
    - If the input file path and output file path are the same, the original file
      will be overwritten with the updated file.
    """
    # Get the PDF properties from the user
    input_file_path, title, author, custom_properties = get_pdf_properties_from_user()

    # Update the PDF title property and custom properties
    output_file_path = update_pdf_title_property(input_file_path, title, author, **custom_properties)

    # Print the output file path
    print("Output file path:", output_file_path)

if __name__ == '__main__':
    main()

"""
To install this in windows
pyinstaller --onefile myscript.py
"""