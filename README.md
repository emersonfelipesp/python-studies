# python-studies
My studies related to the Python Language

## Independent example checks

The public source keeps the original FastAPI Hello World example and standalone SQLModel/SQLite playground. CI does not replace these examples or import a different source history.

The read-only workflow runs separate Python 3.10 and Python 3.12 rows for pushes and pull requests targeting `main` or `develop`. Each row records its real interpreter, compiles both authored tutorial modules, checks the original route in-process and verifies that all tutorial and SQLite bytes remain unchanged. The matrix keeps both rows running after a failure, and `Public study checks complete` fails unless both rows succeed. Only obsolete runs within one pull request can supersede each other; main and develop executions remain independent.

`requirements-ci.txt` pins only the dependencies needed by this test profile. It does not declare a new application dependency floor. The test command explicitly disables external telemetry and uses an in-process client; it never imports or executes `database.py`. These checks validate tutorial syntax and the original route, not database migrations or the runtime behavior of the standalone SQLModel playground.

Each row retains interpreter, installed-package, source-digest and JUnit evidence. Artifacts do not include SQLite databases, credentials or the wider environment. The workflow cannot deploy, publish a package or write source.

To reproduce one row in an isolated environment, install the CI requirements with that interpreter and run:

```bash
STUDY_EXPECTED_PYTHON=3.10 OTEL_SDK_DISABLED=true python -m pytest tests/ -v
```

Use an actual Python 3.12 interpreter and set `STUDY_EXPECTED_PYTHON=3.12` for the other row. Passing one runtime does not qualify the other.
