import re

from .program_arguments import ProgramArguments
from .color_functions import green, blue, gray
from .project_reader import read_project_definition
from .file_resolver import FileResolver


LS_PARSER = re.compile(r'^(.+?)(/(.*))?$')


def list_project_folder(projects_folder: str,
                        args: ProgramArguments) -> None:
    if not args.parameter or len(args.parameter) < 1:
        project_name = "."
        folder_path = ""
    else:
        m = LS_PARSER.match(args.parameter[0])

        assert m

        project_name = m.group(1)
        folder_path = m.group(3)

    project_definition = read_project_definition(projects_folder=projects_folder,
                                                 project_name=project_name)
    file_resolver = project_definition.file_resolver()

    if folder_path:
        file_resolver = file_resolver.subentry(path=folder_path)

    list_folder(file_resolver)


def list_folder(file_resolver: FileResolver) -> None:
    for entry in file_resolver.listdir():
        if entry.is_dir:
            print(blue(entry.name, bold=True) + gray(f" ({entry.owning_project})", bold=True))
        elif entry.is_exe:
            print(green(entry.name, bold=True) + gray(f" ({entry.owning_project})", bold=True))
        else:
            print(entry.name + gray(f" ({entry.owning_project})", bold=True))
