import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_display = f"{minutes:02d}:{seconds:02d}"
        print(timer_display, end='\r')
        time.sleep(1)
    
    print("专注时间结束！")

# 设置专注时长为25分钟
focus_timer(25)
