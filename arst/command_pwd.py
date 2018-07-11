import sys
import os.path

from .program_arguments import ProgramArguments
from .color_functions import red


def display_project_location(projects_folder: str,
                             args: ProgramArguments) -> None:
    if not args.parameter or len(args.parameter) < 1:
        print(red("Invalid number of parameters sent to tree. Specify project."))
        sys.exit(1)

    project_name = args.parameter[0]

    print(os.path.join(projects_folder, project_name))