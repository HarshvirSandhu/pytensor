from setuptools.errors import CompileError as BaseCompileError


class MissingGXX(Exception):
    """This error is raised when we try to generate c code, but g++ is not available."""


class CompileError(BaseCompileError):  # pyright: ignore
    """Custom `Exception` prints compilation errors with their original formatting."""

    def __str__(self):
        return self.args[0]
