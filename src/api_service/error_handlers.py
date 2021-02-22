# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


def register_error_handlers(webapp):
    """
    Register error handlers in the flask application
    Args:
        webapp: flask application

    """

    @webapp.errorhandler(404)
    def error_404(e):
        """
        Process a 400 error
        Args:
            e:

        Returns:

        """
        return {'status': 'ERROR 404'}, 200

    @webapp.errorhandler(500)
    def error_500(e):
        """
        Process a 500 error
        Args:
            e:

        Returns:

        """
        return {'status': 'ERROR 500'}, 500
