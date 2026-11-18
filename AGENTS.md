# Public tutorial CI guidance

- Preserve the original tutorial module and SQLite bytes. Parse `database.py` for syntax, but never import or execute its database side effects during CI.
- Run the complete public test profile on actual Python 3.10 and Python 3.12 independently. The test must verify its declared runtime; one row cannot qualify the other.
- Use CI-only pinned dependencies and an in-process route client with external telemetry disabled. Do not replace application examples or import another provider's application/history.
- Retain both matrix rows after failures and require the complete status to fail when either row fails, is cancelled or is skipped. Keep main/develop admission and independent main executions.
- Upload only bounded source/interpreter/JUnit evidence. Do not upload databases, credentials or the broader environment. This repository has no deployment or publisher.
- Read README.md for the scope limit: syntax and Hello World checks do not validate the standalone SQLModel database runtime.
