# the special storage setup needs to be imported first to make sure
# the tests run on top of a `BlobStorage`...
from plone.app.blob.tests import db
db  # make pyflakes happy...
