import pyrealsense2 as rs
import numpy as np
import cv2
import torch

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

#YOLOのモデルをロード
model = torch.hub.load('ultralytics/yolov5', 'yolov5s') 


#YOLOを使った物体検出
def output_distance(predict_result, depth_frame):
    name = ""
    distance = 0
    #推論結果を取得
    obj = predict_result.pandas().xyxy[0]

    #バウンディングボックスの情報を取得
    for  i in range(len(obj)):
        name = obj.name[i]
        xmin = obj.xmin[i]
        ymin = obj.ymin[i]
        xmax = obj.xmax[i]
        ymax = obj.ymax[i]

        #中央座標計算
        x_length = xmax - xmin #バウンディングボックス長さ
        y_length = ymax - ymin #バウンティングボックス高さ

        x_center = xmin + (x_length / 2) #中央X座標
        y_center = ymin + (y_length / 2) #中央y座標

        #距離を取得
        distance = depth_frame.get_distance(int(x_center), int(y_center))
        print(name + "," + str(distance))
        return (name, distance)
    return ("None", 0)

#人を認識した際の距離による処理
def personCheck (nm, dis):
    if nm == "person":
        print ("人間を確認しました")
        print ("ゴミ箱と人間の距離は" + str(dis) + "cmです。")
        if (dis <= 0.75) and (dis != 0.0):
            print("距離が近くなってきたので停止します")



#メイン処理
def main():
    # Start streaming
    pipeline.start(config)

    try:
        while True:

            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()
            if not depth_frame or not color_frame:
                continue

            # Convert images to numpy arrays
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())

            #推論実行
            #color_image = predict(color_image)
            result = model(color_image)
            result.render()
            color_image = result.ims[0]

            #距離を出力
            (nam, dist) = output_distance(result, depth_frame)
            
            #人を認識した際の処理
            personCheck (nam, dist)
            

            # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)


            # Stack both images horizontally
            images = np.hstack((color_image, depth_colormap))

            # Show images
            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RealSense', images)
            cv2.waitKey(1)

    finally:

        # Stop streaming
        pipeline.stop()

if __name__ == '__main__':

    main()
