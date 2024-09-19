from mangum import Mangum

import api

app = api.create_app()

handler = Mangum(app)
