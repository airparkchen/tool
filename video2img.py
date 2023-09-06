import cv2
import os

def video_to_frames(video_path, output_folder, interval):
    vid = cv2.VideoCapture(video_path)
    count = 0
    while True:
        ret, frame = vid.read()
        if not ret:
            break
        if count % interval == 0:
            frame_name = os.path.join(output_folder, f"frame_{count}.jpg")
            cv2.imwrite(frame_name, frame)
        count += 1
    vid.release()
    print(f"{video_path} has been split into frames.")

def process_folder(folder_path, interval):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            video_path = os.path.join(folder_path, filename)
            output_folder = os.path.join(folder_path, f"{filename}_frames")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            video_to_frames(video_path, output_folder, interval)

if __name__ == "__main__":
    folder_path = "./video"  # 更資料夾路徑
    interval = 1  # 每x秒一張圖片（以幀為單位 一秒30幀）

    process_folder(folder_path, interval)