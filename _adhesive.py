import germanium_py_exe  # type: ignore


germanium_py_exe.pipeline({
    "repo": "git@github.com:bmustiata/ars-py.git",
    "binaries": {
        "name": "Python 3.7 on Linux x64",
        "platform": "python:3.7",
        "docker_tag": "arst",
        "publish_pypi": "sdist",
    }
})

