import os
import time
import subprocess
import threading
#ffmpeg -y -i rtsp://admin:admin@192.168.2.249:554/1/1 -vcodec copy -f mp4 '/image-%4d.mp4'
t=time.localtime()
t_name=str(t.tm_year)+'-'+str(t.tm_mon)+"-"+str(t.tm_mday)
def save_video_from_rtsp(rtsp_path, save_dir):
    print(rtsp_path)
    print(save_dir)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    ffm_shell= 'ffmpeg  -i '+rtsp_path+' -c:v copy  -f segment -segment_time 60 -reset_timestamps 1 -strftime 1 '+ save_dir+'/output_%Y-%m-%d-%H-%M-%S.mp4'
    print(ffm_shell)
    os.system(ffm_shell)


rtsp_list=["rtsp://admin:12345678@192.168.1.4:10554/udp/av0_0","rtsp://admin:12345678@192.168.1.4:10554/udp/av0_0","rtsp://admin:12345678@192.168.1.4:10554/udp/av0_0"]

for i in range(len(rtsp_list)):
    save_dir = r'D:/0_2022/rtsp/'+t_name
    start_time_func = time.time()
    save_dir=save_dir+"/"+str(i)
    threading.Thread(target=save_video_from_rtsp, args=(rtsp_list[i], save_dir)).start()
    endtime_fun = time.time()
    elapsed_fun = endtime_fun - start_time_func
    print(" elapsed_fun : ", elapsed_fun)
