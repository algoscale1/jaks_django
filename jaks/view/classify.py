
from django.http import HttpResponse
# from app.base import Base
from jaks.app.jaks_model import process_n_get_text
from django.views.generic import View
import os
from django.core.files.base import ContentFile
import json
from jaks.services import sql_service


class TextClassifier(View):

    @staticmethod
    def post(request):
        """

        :param request:
        :param api_key:
        :return:
        """
        if(request.GET['api_key'] is None):
            # user_id = request.user
            user_id = 1
            api_key = sql_service.get_api_key(user_id)
        else:
            api_key = request.GET['api_key']

        images = request.FILES

        # if 'api_key' not in request.POST:
        #     return  HttpResponse("{'status_code':400,'message':api_key must be in the request}")
        # key = request.POST["api_key"]
        if sql_service.check_api_key_validity(api_key)=="True":
            print("kkkkkkk")
            exit()

            # sql_service.increase_hit_count(api_key)
            if len(images)==0:

                return HttpResponse("{'status':200,'message':'No file was sent'}")

            for img in images:

                full_filename = 'jaks/app/test/'+str(images[img])

                fout = open(full_filename, 'wb+')
                file_content = ContentFile(images[img].read() )

                # Iterate through the chunks.
                for chunk in file_content.chunks():
                    fout.write(chunk)
                fout.close()

            extracted_data = process_n_get_text()

            sql_service.increase_hit_count(api_key)

            return HttpResponse(json.dumps(extracted_data))

        else:
            return HttpResponse("{'status_code':401,'message':Invalid api key}")

