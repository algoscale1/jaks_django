
from django.http import HttpResponse
# from app.base import Base
from jaks.app.jaks_model import process_n_get_text
from django.views.generic import View
import os
from django.core.files.base import ContentFile
import json
class TextClassifier(View):
    def post(self,request):
        """

        :return:
        """
        ff = request.FILES

        if len(ff)==0:

            return HttpResponse("{'status':200,'message':'No file was sent'}")

        for fi in ff:

            full_filename = 'jaks/app/test/'+str(ff[fi])

            fout = open(full_filename, 'wb+')
            file_content = ContentFile(ff[fi].read() )


            # Iterate through the chunks.
            for chunk in file_content.chunks():
                fout.write(chunk)
            fout.close()



        extracted_data = process_n_get_text()

        return HttpResponse(json.dumps(extracted_data))

