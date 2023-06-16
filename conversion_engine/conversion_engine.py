import os
import sys
import tabula


def pdf_master_converter(file_name: str, target_file_type: str) -> None:

    """
    Entire File Conversion Process: Reads PDF and converts to user specified file type
    :param file_name: The PDF file to be read / converted
    :param target_file_type: The resulting file extension in the form of a user generated string
    :return: None
    """

    print('\n\tReading your PDF file...')

    try:

        source_file_data_frame = tabula.read_pdf(input_path=resource_path(f"../{file_name}"), pages="all")[0]

        print(f'\n\tConverting your pdf file to a/an {target_file_type} file type...')

        # Converting to an EXCEL file
        if target_file_type == 'xlsx':
            source_file_data_frame.to_excel(resource_path('../'+os.path.splitext(file_name)[0])
                                            + f'.{target_file_type}')
            print('\n\t\tSUCCESS! Your excel file has been successfully created!')

        # Converting to a CSV / JSON / TSV file
        elif target_file_type == 'csv' or target_file_type == 'json' or target_file_type == 'tsv':
            tabula.convert_into(input_path=resource_path(f"../{file_name}"),
                                output_path=resource_path(f"../{os.path.splitext(file_name)[0]}.{target_file_type}"),
                                output_format=target_file_type,
                                pages="all")
            print(f'\n\t\tSUCCESS! Your {target_file_type} file has been successfully created!')

        # Converting to an XML file
        elif target_file_type == 'xml':
            try:
                source_file_data_frame.to_xml(resource_path('../'+os.path.splitext(file_name)[0]) +
                                              f'.{target_file_type}')
            except Exception as xml_err:
                print('\n\tERROR: ', str(xml_err))
                input('\nPress Enter to Exit: ')
                sys.exit(1)
            print('\n\t\tSUCCESS! Your xml file has been successfully created!')

        # Converting to an HTML file
        elif target_file_type == 'html':
            source_file_data_frame.to_html(resource_path('../'+os.path.splitext(file_name)[0]) + f'.{target_file_type}')
            print('\n\t\tSUCCESS! Your html file has been successfully created!')

        # Converting to a TXT file
        elif target_file_type == 'txt':
            source_file_data_frame.to_string(resource_path('../'+os.path.splitext(file_name)[0]) +
                                             f'.{target_file_type}')
            print('\n\t\tSUCCESS! Your text file has been successfully created!')

        else:
            print(f'\n\tERROR! Something went wrong!')
            input('\nPress Enter & Exit to Try Again: ')
            sys.exit(1)

    except Exception and FileNotFoundError:
        if FileNotFoundError:
            print(f'\n\tERROR: Unable to locate your file "{file_name}". Please provide a valid file name within this '
                  f'folder.')
        else:
            raise


def resource_path(relative_path) -> [str, bytes]:

    """
    For managing file resources.
    :param: relative_path: The relative path (relative to the script file) of the target file as a string
    :return: A list of bytes (file content) and string (file path)
    """

    base_path: [] = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
