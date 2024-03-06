import subprocess # allows me to call 'pip' command
from pkg_resources import working_set

#Function to list the libraries with their numbers
def list_installed_libraries():
    # retrieves a list of all intalled libraries
    installed_libraries = list(working_set) 

    for index, lib in enumerate(installed_libraries, start=1):
        print(f"{index}. {lib}")

#Function to get the library number and uninstall it
def uninstall_library(library_number):
    # retrieves a list of all intalled libraries
    installed_libraries = list(working_set) 
    
    if 1 <= library_number <= len(installed_libraries):
        library_to_install = installed_libraries[library_number - 1]
        subprocess.call(['pip', 'uninstall', '-y', library_to_install.key])
        print(f"{library_to_install} uninstalled successfully." )
    else:
        print("Invalid library number")

def main():
    while True:
        print("\n--------------------------------------")
        print("| List of installed Python libraries |")
        print("--------------------------------------")
        list_installed_libraries()

        try:
            library_number = int(input("\nEnter the number of the library you want to uninstall (enter 0 to exit): "))
            if library_number == 0:
                print("Exiting program...")
                break
            uninstall_library(library_number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()