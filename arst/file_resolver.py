from typing import List, Set
import os.path


class FileEntry(object):
    name: str
    absolute_path: str
    is_dir: bool

    def __init__(self,
                 name: str,
                 absolute_path: str,
                 is_dir: bool) -> None:
        self.name = name
        self.absolute_path = absolute_path
        self.is_dir = is_dir


class FileResolver(object):
    def __init__(self,
                 projects_folder: str,
                 search_path: List[str],
                 current_path: str = '.') -> None:
        self.projects_folder = projects_folder
        self.search_path = list(search_path)
        self.current_path = current_path

    def listdir(self) -> List[FileEntry]:
        """
        Lists the current folder, by iterating the search path that
        was provided and aggregating all the files from there.
        """
        current_files: Set[str] = set()
        result: List[FileEntry] = list()

        for searched_folder in self.search_path:
            abs_path = os.path.join(self.projects_folder, searched_folder, self.current_path)

            if not os.path.isdir(abs_path):
                continue

            for found_entry in os.listdir(abs_path):
                if found_entry in current_files:
                    continue

                current_files.add(found_entry)

                abs_entry = os.path.join(abs_path, found_entry)

                result.append(FileEntry(name=found_entry,
                                        absolute_path=abs_entry,
                                        is_dir=os.path.isdir(abs_entry)))

        return result

    def subentry(self, entry: FileEntry) -> 'FileResolver':
        return FileResolver(projects_folder=self.projects_folder,
                            search_path=self.search_path,
                            current_path=os.path.join(self.current_path, entry.name))
