# Change Log

Check [Keep a Changelog](http://keepachangelog.com/) for recommendations on how to structure this file.

Date each section like release version number [0.1.0] - 2022-11-29 so that we know what version and when. All sections are newest at the top and oldest at the bottom.

Sections should include:

* Added
* Changed
* Depreicated
* Removed
* Fixed
* Security

## [Unreleased]

## Changed

### [1.0.001] 2023-03-10

1. Imported "os", "PdfReader" and "PdfWriter" from the "pypdf" library, "json", and "time" modules.
2. Added a docstring to the "update_pdf_title_property" function.
3. Added a try-except block in the "update_pdf_title_property" function to handle the "PermissionError" exception.
4. Refactored the "save_pdf_properties_to_log_file" function by adding a try-except block to handle the "PermissionError" exception.
5. Added a docstring to the "save_pdf_properties_to_log_file" function.
6. Refactored the "save_pdf_properties_to_log_file" function to remove the unnecessary "else" statement.
7. Added a docstring to the "get_pdf_properties_from_user" function.
8. Refactored the "get_pdf_properties_from_user" function to remove the unnecessary use of replace function.
9. Added a docstring to the "main" function.
10. Refactored the "main" function by using the "get_pdf_properties_from_user" function to get the user input and changed the input variable name to "user_input".
11. Added a confirmation message to the end of the "main" function.
12. Refactored the "main" function by passing the dictionary "user_input" instead of individual variables to the "update_pdf_title_property" function.
13. Refactored the "main" function by changing the "log_file_name" variable from "LogThese.json" to "_LogThese.json".
14. Added a while loop in the "update_pdf_title_property" and "save_pdf_properties_to_log_file" functions to keep trying to access the file after waiting for 5 seconds when a "PermissionError" exception is raised.
15. Changed the file extension of the log file from ".txt" to ".json".
16. Removed the unnecessary "wb" argument from the "with open" statement in the "update_pdf_title_property" function.

