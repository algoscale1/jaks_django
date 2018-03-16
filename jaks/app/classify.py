from flask import request, jsonify
from . import routes
from .exceptions import InvalidUsage, DataNotFound, ElasticsearchTimeout
from app.exceptions import InvalidData, ElasticsearchService, DataNotFoundError
import logging
from django.http import HttpResponse
# from app.base import Base
from jaks.app.jaks_model import process_n_get_text
from django.views.generic import View


class TextClassifier(View):
    def post(self,request):
        """

        :return:
        """
        ff = request.FILES
        print("fffffffffffffffffffffffffffff")
        if len(ff)==0:

            return "{'status':200,'message':'No file was sent'}"

        for fi in ff:
            ff[fi].save('test/'+ff[fi].filename)


        extracted_data = process_n_get_text()

        return HttpResponse("done")
        # return jsonify(extracted_data)
