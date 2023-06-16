import os
import sys
from conversion_engine.conversion_engine import pdf_master_converter


def script_summary() -> None:
    print('''
               ***----------------------------------------------------------------------------------------***
         \t***------------------------ DUMELANG means GREETINGS! ~ G-CODE -----------------------***
                     \t***------------------------------------------------------------------------***\n

        \t"PDF_TO --> MASTER CONVERTER" Version 1.0.0\n

        This bot will help you convert a pdf file to either an excel spreadsheet file or a 
        CSV file, or a TSV file or a JSON file or an XML file or an HTML file or a txt 
        (text based) file.
        All you need to do is provide the name of the PDF file you want convert and the type
        of the file you want to convert to.

        Cheers!!
    ''')


def from_pdf_bot(file_name: str, destination_file_type: str) -> None:
    try:
        pdf_master_converter(file_name, destination_file_type)

    except Exception and FileNotFoundError:
        if FileNotFoundError:
            print(
                '\n\t*** Unable to locate your file. Please make sure you provide a valid file name & '
                'file extension within this folder. ***')
        else:
            raise

    input('\nPress Enter to Exit.')
    sys.exit(0)


def main() -> None:
    script_summary()
    file_name: str = input('\nPlease type the name of the file (including the extension) you would like to convert '
                           'and Press Enter: ')

    destination_file_type: str = input(
        '\nPlease type:\n\n\t\t"xlsx" to convert to an excel spreadsheet file\n\t\t"csv" to convert to a CSV '
        'file\n\t\t"tsv" to convert to a TSV file\n\t\t"json" '
        'to convert to a JSON file\n\t\t"xml" to convert to an XML file\n\t\t"html" to convert to an HTML '
        'file\n\t\t"txt" to '
        'convert to a text (TXT) file\n\t\t"X" to quit\n\nType Here & Press Enter: ').lower()

    if len(file_name.strip()) >= 5:
        if not os.path.splitext(file_name)[-1].casefold() == '.pdf':
            input('\nPlease provide a valid pdf file name.')
        if destination_file_type not in ['xlsx', 'csv', 'tsv', 'json', 'xml', 'html', 'txt']:
            print(f'\n\tERROR: Your file type "{destination_file_type}" is not recognised.')
            input('\nPress Enter to Exit & Try Again: ')
            sys.exit(1)
        else:
            from_pdf_bot(file_name, destination_file_type)

    elif len(file_name.strip()) < 5 or os.path.splitext(file_name.strip()[-1]) == '':
        print('\nPlease provide a valid file name.')
        input('\nPress Enter to Exit: ')
        sys.exit(1)


if __name__ == '__main__':
    main()
