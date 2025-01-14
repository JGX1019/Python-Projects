from datetime import datetime   
import pygame

pygame.mixer.init()

def play_alarm_sound():
    while True:
        pygame.mixer.music.load("strong_alarm.mp3")  
        pygame.mixer.music.play(-1)   
        pygame.time.Clock().tick(10)
        user_input = input("\nEnter to stop the alarm: ").strip().upper() 
        break  

def set_alarm():
    Time = datetime.now().strftime("%H:%M:%S")
    print(f"Time: {Time}")
    print("\nEnter the alarm time in HH:MM:SS format (24-hour clock):")

    while True:
        alarm_time = input("\nAlarm Time: ").strip()
        
        try:
            hours, minutes, seconds = map(int, alarm_time.split(":"))
            
            if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
                return alarm_time
            else:
                print("\nInvalid time. Hours must be 0-23, minutes and seconds must be 0-59.")
        
        except ValueError:
            print("\nInvalid format. Please enter the time in HH:MM:SS format.")

def alarm_clock(alarm_time):
    print(f"\nAlarm set for {alarm_time}. Waiting...")
    
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            play_alarm_sound()
            break
            

if __name__ == "__main__":
    alarm_time = set_alarm()
    alarm_clock(alarm_time)
