
from django.http import HttpResponse
# from app.base import Base
from jaks.app.jaks_model import process_n_get_text
from django.views.generic import View
import os
from django.core.files.base import ContentFile
import json
from jaks.services import sql_service
from django.http import HttpResponseRedirect


class TextClassifier(View):

    @staticmethod
    def post(request):
        """

        :param request:
        :param api_key:
        :return:
        """

        api_key = request.GET['api_key']
        user_id = request.user.id
        images = request.FILES
        extracted_data = None
        if len(images)==0:

            return HttpResponse("{'status':401,'message':'No file was sent'}")

        if len(api_key) == 16:

            if sql_service.check_api_key_validity(api_key) == "True":
                extracted_data = TextClassifier.find_subject(images)
            else:
                return HttpResponse("{'status_code':401,'message':Invalid api key}")

        elif user_id is not None:
            api_key = sql_service.get_api_key(user_id)
            if api_key:
                if sql_service.check_api_key_validity(api_key)=="True":
                    extracted_data = TextClassifier.find_subject(images)
                else:
                    return HttpResponse("{'status_code':401,'message':Invalid api key}")
            else:
                return HttpResponse("Please renew the api key")
        elif len(api_key) >0 and len(api_key) !=16:
            return HttpResponse("Invalid api key")
        else:
            return HttpResponse("Either login or api key is required to use this service.")

        sql_service.increase_hit_count(api_key)

        return HttpResponse(json.dumps(extracted_data))

    @staticmethod
    def find_subject(images):
        """

        :param images:
        :return:
        """



        for img in images:

            full_filename = 'jaks/app/test/'+str(images[img])

            fout = open(full_filename, 'wb+')
            file_content = ContentFile(images[img].read() )

            # Iterate through the chunks.
            for chunk in file_content.chunks():
                fout.write(chunk)
            fout.close()

        extracted_data = process_n_get_text()

        return extracted_data
