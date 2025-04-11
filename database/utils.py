from validate_email import validate_email

class Utils:
    def is_Valid_Email(self,email):
        valid_email = validate_email(
            email_address=email,
            check_format=True,
            check_blacklist=True,
            check_dns=True,
            dns_timeout=10,
            check_smtp=True,
            smtp_timeout=10,
            smtp_skip_tls=False,
            smtp_tls_context=None,
            smtp_debug=False,
        )
        return valid_email