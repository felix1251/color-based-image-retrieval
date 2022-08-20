import argparse
import cv2
from color.color import ColorDescriptor
from searcher import Searcher

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True, help = "Path to the query image")
ap.add_argument("-c", "--class", required = True, help = "Feature class")
args = vars(ap.parse_args())

if args["class"] == "color":

	if(args["class"] == "color"):
		bins = (8,12,3)
		cd = ColorDescriptor(bins)

		query = cv2.imread(args["query"])
		features = cd.describe(query)

		searcher = Searcher("color/index.csv")
		results = searcher.search(features)

	myWindow = cv2.resize(query,(500,500))
	cv2.imshow("query",myWindow)

	for (score, resultId) in results:
		print("Similarity: ",score)
		result = cv2.imread("../"+resultId)
		myWindow = cv2.resize(result,(480,480))
		cv2.imshow("Result: " +str(score), myWindow)
		print('Result Images: ', resultId)
		ch = cv2.waitKey(0)
		if ch == ord('q'):
			pass

