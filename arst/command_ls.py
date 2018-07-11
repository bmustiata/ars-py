import sys

from .program_arguments import ProgramArguments
from .color_functions import red, green, blue, gray
from .project_reader import read_project_definition
from .file_resolver import FileResolver


def list_project_folder(projects_folder: str,
                        args: ProgramArguments) -> None:
    if not args.parameter or len(args.parameter) < 1:
        folder_name = "."
    else:
        folder_name = args.parameter[0]

    project_definition = read_project_definition(projects_folder=projects_folder,
                                                 project_name=folder_name)
    file_resolver = project_definition.file_resolver()
    list_folder(file_resolver)


def list_folder(file_resolver: FileResolver) -> None:
    for entry in file_resolver.listdir():
        if entry.is_dir:
            print(blue(entry.name) + gray(f" ({entry.owning_project})"))
        elif entry.is_exe:
            print(green(entry.name) + gray(f" ({entry.owning_project})"))
        else:
            print(entry.name + gray(f" ({entry.owning_project})"))
