from __future__ import annotations

import nox

nox.options.sessions = ("spelling", "build")


@nox.session
def spelling(session: nox.Session):
    """
    Spell check documentation
    """
    session.install("-r", "requirements/spelling.in", "-c", "requirements/spelling.txt")
    session.run(
        "codespell",
        "docs",
        *session.posargs,
    )


@nox.session
def formatters_check(session: nox.Session):
    """
    Check Python file formatting without making changes
    """
    session.install(
        "-r", "requirements/formatters.in", "-c", "requirements/formatters.txt"
    )
    session.run("black", "--check", *session.posargs, "noxfile.py")


@nox.session
def commitlint(session: nox.Session):
    """
    Check commit messages against conventional commits format.
    This session requires git history and is intended for CI only.
    """
    session.install(
        "-r", "requirements/commitlint.in", "-c", "requirements/commitlint.txt"
    )
    session.run("cz", "check", "--rev-range", "origin/main..HEAD", *session.posargs)


@nox.session
def build(session: nox.Session):
    """
    Build the docsite with mkdocs
    """
    session.install(
        "-r", "requirements/requirements.in", "-c", "requirements/requirements.txt"
    )
    session.run(
        "mkdocs",
        "build",
        "--strict",
        *session.posargs,
    )
