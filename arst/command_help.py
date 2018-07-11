import sys

from .program_arguments import ProgramArguments
from .color_functions import red
from .project_reader import read_project_definition


def show_project_help(projects_folder: str,
                      args: ProgramArguments) -> None:
    if not args.parameter or len(args.parameter) < 1:
        print(red("Invalid number of parameters sent to tree. Specify project."))
        sys.exit(1)

    project_name = args.parameter[0]

    read_project_definition(projects_folder=projects_folder,
                            project_name=project_name)
