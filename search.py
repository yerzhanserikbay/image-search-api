from descriptor import RGBHistogram
from image_search.searcher import Searcher
import numpy as np
import argparse
import os
import pickle
import cv2


# ap = argparse.ArgumentParser()
#
# ap.add_argument("-d", "--dataset", required=True,
#                 help="Path to the directory that contains the images we just indexed")
# ap.add_argument("-i", "--index", required=True,
#                 help="Path  to where we stored our index")

# args = vars(ap.parse_args())

class Search:
    def search(image):
        args = {'dataset': 'images', 'index': 'index.cpickle'}

        queryImage = image

        # cv2.imshow("Query", queryImage)
        # print("query: {}".format(args["query"]))

        desc = RGBHistogram([8, 8, 8])
        queryFeatures = desc.describe(queryImage)

        index = pickle.loads(open(args["index"], "rb").read())
        searcher = Searcher(index)
        results = searcher.search(queryFeatures)

        # montageA = np.zeros((166 * 5, 400, 3), dtype="uint8")
        # montageB = np.zeros((166 * 5, 400, 3), dtype="uint8")

        for j in range(0, 1):
            (score, imageName) = results[j]
            path = os.path.join(args["dataset"], imageName)
            result = cv2.imread(path)
            print("\t{}. {} : {:.3f}".format(j + 1, imageName, score))

        #     if j < 1:
        #         montageA[j * 166:(j + 1) * 166, :] = result
        #
        #     else:
        #         montageB[(j - 5) * 166:((j - 5) + 1) * 166, :] = result
        #
        # cv2.imshow("Results 1-5", montageA)
        # cv2.imshow("Results 6-10", montageB)
        # cv2.waitKey(0)
