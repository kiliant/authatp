"""
Example demo server to use a supported web browser to call the WebAuthn APIs
to register and use a credential.

See the file README.adoc in this directory for details.

Navigate to https://localhost:5000 in a supported web browser.
"""
from __future__ import absolute_import, print_function, unicode_literals

from app import create_app, db

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == "__main__":
    print(__doc__)
    app.run(ssl_context="adhoc")
