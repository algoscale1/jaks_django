
from django.http import HttpResponse
# from app.base import Base
from jaks.app.jaks_model import process_n_get_text
from django.views.generic import View
import os
from django.core.files.base import ContentFile
import json
from jaks.services import sql_service


class TextClassifier(View):
    def post(self,request):
        """

        :return:
        """
        images = request.FILES

        if 'api_key' not in request.POST:
            return  HttpResponse("{'status_code':400,'message':api_key must be in the request}")
        key = request.POST["api_key"]
        if sql_service.check_api_key_validity(key)=="True":

            sql_service.increase_hit_count(key)
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


            return HttpResponse(json.dumps(extracted_data))

        else:
            return HttpResponse("{'status_code':401,'message':Invalid api key}")

