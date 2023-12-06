import keyboard
import time

def trigger_key(key, frequency):
    try:
        while True:
            keyboard.press(key)
            time.sleep(1 / frequency)
            keyboard.release(key)
            time.sleep(1 / frequency)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    custom_key = "f"  # 自定义的按键
    custom_frequency = 20  # 自定义的触发频率，单位为Hz

    print(f"按键 {custom_key} 将以 {custom_frequency} Hz 的频率触发。")
    print("按下 Ctrl+C 停止程序。")

    trigger_key(custom_key, custom_frequency)

