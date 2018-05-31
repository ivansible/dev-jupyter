#  Use '*' to allow any origin to access your server.
#c.NotebookApp.allow_origin = ''
#  Leading and trailing slashes can be omitted, and will automatically be added.
#c.NotebookApp.base_url = '/'
## The default URL to redirect to from `/`
c.NotebookApp.default_url = '/tree/jupyter/stepik-algos'
## The IP address the notebook server will listen on.
c.NotebookApp.ip = '0.0.0.0'
## The port the notebook server will listen on.
c.NotebookApp.port = {{ jupyter_port }}
## Whether to open in a browser after starting.
c.NotebookApp.open_browser = False
## Hashed password to use for web authentication.
#    from notebook.auth import passwd; passwd()
#  The string should be of the form type:salt:hashed-password.
c.NotebookApp.password = 'sha1:9ef5d6e7310a:584266fbb2942271941b43c03a847fdc503c4e2f'
## Forces users to use a password for the Notebook server.
#c.NotebookApp.password_required = False
## Token used for authenticating first-time connections to the server.
#  When no password is enabled, the default is to generate a new, random token.
#  Setting to an empty string disables authentication altogether
#c.NotebookApp.token = '<generated>'
## Allow access to hidden files
#c.ContentsManager.allow_hidden = False
