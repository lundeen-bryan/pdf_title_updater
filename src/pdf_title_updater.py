import sys
import os
from pypdf import PdfReader, PdfWriter
import json
import time
import art

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
    input_pdf = PdfReader(open(input_file_path, "rb"))
    num_pages = len(input_pdf.pages)

    # Create a new PDF writer object
    output_pdf = PdfWriter()

    # Set the title and author properties of the output PDF
    output_pdf.add_metadata({"/Title": title, "/Author": author})

    # Set the custom properties of the output PDF if provided
    if "Processed By" in kwargs:
        output_pdf.add_metadata({"/Processed By": kwargs["Processed By"]})
    if "County" in kwargs:
        output_pdf.add_metadata({"/County": kwargs["County"]})
    if "Court Number" in kwargs:
        output_pdf.add_metadata({"/Court Number": kwargs["Court Number"]})

    # Add each page of the input PDF to the output PDF
    for page_num in range(num_pages):
        page = input_pdf.pages[page_num]
        output_pdf.add_page(page)

    # Create the output file path by combining the directory path and original file name
    output_file_path = os.path.join(file_dir, file_name)

    # Write the output PDF to the output file path
    try:
        with open(output_file_path, "wb") as output_file:
            output_pdf.write(output_file)
    except PermissionError:
        print(f"The file {output_file_path} is currently in use. Please close it and try again.")
        while True:
            try:
                with open(output_file_path, "wb") as output_file:
                    output_pdf.write(output_file)
                break
            except PermissionError:
                time.sleep(5) # wait for 5 seconds

    # Return the output file path
    return output_file_path

def save_pdf_properties_to_log_file(file_dir, file_name, data, title):
    """
    Saves the PDF properties to a log file in JSON format.

    Name:
    save_pdf_properties_to_log_file

    Description:
    This function takes a directory path, a file name, and data to save to the log file.
    It saves the data to a JSON file in the specified directory path.

    Parameters:
    file_dir (str): The directory path where the log file will be saved.
    file_name (str): The name of the log file.
    data (dict): The data to save to the log file.
    title (str): The title of the PDF file.

    Returns:
    None.

    Preconditions:
    - The file_dir must be a valid directory path.
    - The file_name must be a non-empty string.
    - The data must be a dictionary with non-empty string keys and values.
    - The title must be a non-empty string.

    Notes:
    - If the log file already exists, the data will be appended to the existing file.
    - The file extension of the log file should be ".json".
    """
    # Remove double slashes in the input PDF file path
    data["Input PDF File Path"] = data["Input PDF File Path"].replace(
        "\\\\", "\\"
    )

    # Create the full file path
    file_path = os.path.join(file_dir, file_name)

    try:
        # Create the log file if it does not exist
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump({title: [data]}, file, indent=4)

        # If the file exists but is empty, write the new data to the file
        elif os.stat(file_path).st_size == 0:
            with open(file_path, "w") as file:
                json.dump({title: [data]}, file, indent=4)

        # If the file exists and has data, append the new data to the file
        else:
            # Load the log file data into a dictionary
            with open(file_path, "r") as file:
                log_data = json.load(file)

            # Append the new data to the log file dictionary
            if title in log_data:
                log_data[title].append(data)
            else:
                log_data[title] = [data]

            # Write the updated log file dictionary to the log file
            with open(file_path, "w") as file:
                json.dump(log_data, file, indent=4)

    except PermissionError:
        print(f"The file {file_name} is currently in use. Please close it and try again.")
        while True:
            try:
                with open(file_path, "w") as file:
                    json.dump(log_data, file, indent=4)
                break
            except PermissionError:
                time.sleep(5)  # wait for 5 seconds

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
    dict: A dictionary containing the input file path (str), title (str), author (str),
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

    quit_instructions = "(Type \"quit\" to exit the program)"
    mandatory_msg = "Mandatory field: Please enter a value to continue."
    abort_msg = "Aborting process..."
    print(art.logo)
    opening_msg = '''
    Welcome to the PDF Title Updater for EZ Logger!
    ---

    This app will let you change the properties in a PDF file such as the
    title, author, etc., that help identify meta data about the report
    in the PDF document.

    Answer the questions below, and if you want to quit at any time,
    enter the word "quit" and press the ENTER key to exit the app.

    '''
    print()
    while True:
        # Prompt the user for the necessary input
        print(f"Enter the input PDF file path.{quit_instructions}")
        user_input = input("> ").strip()
        if user_input != "":
            if user_input.isdigit():
                print("You can only enter text as the path to a file.")
            elif user_input.lower() == "quit":
                print(f"{abort_msg}")
                sys.exit(0) # exit program w/o displaying error.
        elif user_input == "":
            print(f"{mandatory_msg}")
        input_file_path = (
            user_input
            .replace("'", "")
            .replace('"', "")
        )
        print(f"Enter the PDF title: {quit_instructions}")
        user_input = input("> ").strip()
        if user_input != "":
            if user_input.isdigit():
                print("You can only enter text.")
            elif user_input.lower() == "quit":
                print(f"{abort_msg}")
                sys.exit(0) # exit program w/o displaying error.
        elif user_input == "":
            print(f"{mandatory_msg}")
        title = (
            user_input
            .replace("'", "")
            .replace('"', "")
        )
        print(f"Enter the PDF author/evaluator: {quit_instructions}")
        user_input = input("> ").strip()
        if user_input != "":
            if user_input.isdigit():
                print("You can only enter text.")
            elif user_input.lower() == "quit":
                print(f"{abort_msg}")
                sys.exit(0) # exit program w/o displaying error.
        elif user_input == "":
            print(f"{mandatory_msg}")
        author = (
            user_input
            .replace("'", "")
            .replace('"', "")
        )

        # Prompt the user for the optional inputs
        print(f"Enter the 'Processed By' custom property (optional): {quit_instructions}")
        user_input = input("> ").strip()
        if user_input != "":
            if user_input.isdigit():
                print("You can only enter text.")
            elif user_input.lower() == "quit":
                print(f"{abort_msg}")
                sys.exit(0) # exit program w/o displaying error.
        processed_by = (
            user_input
            .replace("'", "")
            .replace('"', "")
        )
        print(f"Enter the 'County' custom property (optional): {quit_instructions}")
        user_input = input("> ").strip()
        if user_input != "":
            if user_input.isdigit():
                print("You can only enter text.")
            elif user_input.lower() == "quit":
                print(f"{abort_msg}")
                sys.exit(0) # exit program w/o displaying error.
        county = (
            user_input
            .replace("'", "")
            .replace('"', "")
            .upper()
        )
        print(f"Enter the 'Court Number' custom property (optional): {quit_instructions}")
        user_input = input("> ").strip()
        if user_input != "":
            if user_input.isdigit():
                print("You can only enter text.")
            elif user_input.lower() == "quit":
                print(f"{abort_msg}")
                sys.exit(0) # exit program w/o displaying error.
        court_number = (
            user_input
            .replace("'", "")
            .replace('"', "")
        )
        # Check if all required inputs have been provided
        if all(len(value) > 0 for value in [input_file_path, title, author]):
            break

    # Create a dictionary of the optional inputs
    custom_properties = {}
    if processed_by:
        custom_properties["Processed By"] = processed_by
    if county:
        custom_properties["County"] = county
    if court_number:
        custom_properties["Court Number"] = court_number

    # Create a dictionary of all the inputs
    input_dict = {
        "Input PDF File Path": input_file_path,
        "Title": title,
        "Author": author,
        "Custom Properties": custom_properties,
    }

    # Return the dictionary of inputs
    return input_dict


def main():
    """
    Update PDF title and custom properties, and save properties to log file.

    Description:
    This function takes user input for the input PDF file path, the new PDF title, the author, and
    optional custom properties to add to the PDF file. It then updates the title and properties of
    the PDF file and saves a new file with the updated properties. The function also logs the
    properties of the PDF file to a JSON file.

    Preconditions:
    - The input PDF file path must exist and be a valid file path.
    - The PDF title and author must be non-empty strings.
    - The keys and values in the custom properties dictionary must be strings.

    Notes:
    - The function will append the properties of the PDF file to the existing log file if the file
      already exists.
    - The log file name is "_LogThese.json".
    """
    # Get the necessary input from the user
    user_input = get_pdf_properties_from_user()
    input_file_path = user_input["Input PDF File Path"]
    title = user_input["Title"]
    author = user_input["Author"]
    custom_properties = user_input["Custom Properties"]

    # Update the title and properties of the PDF file
    output_file_path = update_pdf_title_property(
        input_file_path, title, author, **custom_properties
    )

    # Log the PDF properties to a JSON file
    log_file_dir = os.path.dirname(output_file_path)
    log_file_name = "_LogThese.json"
    save_pdf_properties_to_log_file(
        log_file_dir, log_file_name, user_input, title
    )

    # Print confirmation message
    print(f"PDF file properties updated and logged to {log_file_name}.")


if __name__ == "__main__":
    main()

"""
To install this in windows
pyinstaller --onefile myscript.py
"""
