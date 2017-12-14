from faceReplacement import faceReplacement
import cv2
import numpy as np

def faceReplacementForVideo(video1, video2):
    # process the video here, convert into frames of images
    # assuming that 'rawVideo' is a video path
    cap1 = cv2.VideoCapture(video1)
    # ie, test with rawVideo = 'Data/Easy/TheMartian.mp4'
    frame_width1 = int(cap1.get(3))
    frame_height1 = int(cap1.get(4))
    num_frames1 = int(cap1.get(7))
    # create an array that holds all the frames in the video, format: frame_number x width x height
    frames1 = np.zeros([num_frames1, frame_height1, frame_width1, 3], np.uint8)
    f = 0

    while (cap1.isOpened()):
        ret, frame = cap1.read()
        # cv2.imshow('fr ame')
        frames1[f, :, :, :] = frame

        f += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if f == num_frames1 - 1:
            break

    cap1.release()
    cv2.destroyAllWindows()

    cap2 = cv2.VideoCapture(video2)
    # ie, test with rawVideo = 'Data/Easy/TheMartian.mp4'
    frame_width2 = int(cap1.get(3))
    frame_height2 = int(cap1.get(4))
    num_frames2 = int(cap1.get(7))
    # create an array that holds all the frames in the video, format: frame_number x width x height
    frames2 = np.zeros([num_frames2, frame_height2, frame_width2, 3], np.uint8)
    f = 0

    while (cap2.isOpened()):
        ret, frame = cap2.read()
        # cv2.imshow('fr ame')
        frames2[f, :, :, :] = frame

        f += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if f == num_frames2 - 1:
            break

    cap2.release()
    cv2.destroyAllWindows()


