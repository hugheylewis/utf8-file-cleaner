def remove_character_from_file(input_file, output_file, character_to_remove):
    try:
        # Open the input file in read mode
        with open(input_file, 'r', encoding='utf-8') as file:
            # Read the file content
            file_content = file.read()

        # Remove the specified character from the file content
        updated_content = file_content.replace(character_to_remove, '')

        # Open the output file in write mode
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write the updated content to the output file
            file.write(updated_content)

        print(f"All instances of '{character_to_remove}' have been removed from {input_file} and saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input file, output file, and character to remove
input_file = 'input.txt'
output_file = 'output.txt'
character_to_remove = ' '

# Call the function to remove the character
remove_character_from_file('ENTER_INPUT_FILE_PATH_HERE', 'ENTER_OUTPUT_FILE_PATH_HERE', character_to_remove)
