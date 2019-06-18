from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import cv2
import os
from search import Search

@csrf_exempt
def find_image(request):
    data = {"success": False}

    if request.method == "POST":
        if request.FILES.get("image", None) is not None:
            image = _grab_image(stream=request.FILES["image"])
        else:
            url = request.POST.get("url", None)

            if url is None:
                data["error"] = "No URL provided."
                return JsonResponse(data)

            image = _grab_image(url=url)

        # work with an image

        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        Search.search(image)

        data.update({"success": True, "image_name": True})

    return JsonResponse(data)


def _grab_image(path=None, stream=None, url=None):
    if path is not None:
        image = cv2.imread(path)

    else:
        if url is not None:
            resp = urllib.request.urlopen(url)
            data = resp.read()

        elif stream is not None:
            data = stream.read()

        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return  image
