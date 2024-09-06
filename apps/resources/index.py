from flask import Blueprint, request, current_app
from flask_restful import Api, Resource
from ..services.index import GetCertificateDate
import ssl
        

indexbp = Blueprint("index", __name__)
api = Api(indexbp)


class IndexResource(Resource):
    def get(self):
        try:
            domain = request.args.get("domain", None)
            if domain is not None:
                port = request.args.get("port", 443)
                certificate = ssl.get_server_certificate((domain, port), timeout=1)
                result = GetCertificateDate(certificate)
                to_dict = {
                    "域名": domain,
                    "证书创建时间": result.get_begin_date(),
                    "证书到期时间": result.get_expire_date(),
                    "证书是否过期": result.has_expired(),
                    "证书内容": certificate
                }
                return to_dict
            else:
                return {"error": "内容有误 缺少domain参数"}, 400

        except ConnectionError as e:
            current_app.logger.error(e)
            return {"error": "异常 请检查domain或port参数"}, 400

        except OSError as e:
            current_app.logger.error(e)
            return {"error": "异常 请检查domain或port参数"}, 400

        except Exception as e:
            current_app.logger.error(e)
            return {"error": "未知异常 你干了些什么"}, 400

        
api.add_resource(IndexResource, '/')

