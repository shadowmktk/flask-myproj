from OpenSSL import crypto
from datetime import datetime
from pytz import timezone


def load_certificate_date(date_string: str):
    utc = timezone("UTC")
    shanghai = timezone("Asia/Shanghai")
    
    format_date = datetime.strptime(date_string, "%Y%m%d%H%M%SZ")
    new_date = utc.localize(format_date)
    
    return new_date.astimezone(tz=shanghai)


class GetCertificateDate:
    def __init__(self, certificate: str):
        self.cert = crypto.load_certificate(crypto.FILETYPE_PEM, certificate)

    def get_begin_date(self):
        self.begin_date = load_certificate_date(self.cert.get_notBefore().decode("utf-8"))
        self.begin_date = self.begin_date.strftime("%Y-%m-%d %H:%M:%S")
        
        return self.begin_date

    def get_expire_date(self):
        self.expire_date = load_certificate_date(self.cert.get_notAfter().decode("utf-8"))
        self.expire_date = self.expire_date.strftime("%Y-%m-%d %H:%M:%S")

        return self.expire_date

    def has_expired(self):
        return self.cert.has_expired()
      
