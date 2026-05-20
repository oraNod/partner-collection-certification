from __future__ import annotations

import subprocess

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
def llms_txt_check(session: nox.Session):
    """
    Check that docs/llms-full.txt is updated when docs/*.md files change.
    This session requires git history and is intended for CI only.
    """
    log_result = subprocess.run(
        ["git", "log", "--format=%B", "origin/main..HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    if "[skip llms-check]" in log_result.stdout:
        session.log("Skipping: [skip llms-check] found in commit messages.")
        return

    diff_result = subprocess.run(
        ["git", "diff", "--name-only", "origin/main..HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    changed = diff_result.stdout.strip().splitlines()
    md_changed = any(f.startswith("docs/") and f.endswith(".md") for f in changed)
    llms_changed = "docs/llms-full.txt" in changed
    if md_changed and not llms_changed:
        session.error(
            "docs/*.md files changed but docs/llms-full.txt was not updated. "
            "Review the changes and update llms-full.txt to reflect them, "
            "or include [skip llms-check] in a commit message to bypass."
        )


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
