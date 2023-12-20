import os
import wave
import time
import threading
import tkinter as tk
import pyaudio
import socket



class VoiceRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.button = tk.Button(text="🎤", font=("Arial", 120, "bold"),
                                command=self.click_handler)

        self.button.pack()
        self.label = tk.Label(text="00:00:00")
        self.label.pack()
        self.recording = False
        self.server_socket = None
        self.client_socket = None
        self.root.mainloop()

    def click_handler(self):
        if self.recording:
            self.recording = False
            self.button.config(fg="black")
            self.stop_server()
        else:
            self.recording = True
            self.button.config(fg="purple")
            threading.Thread(target=self.record).start()
            threading.Thread(target=self.start_server).start()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("0.0.0.0", 12345))
        self.server_socket.listen(1)
        print("Waiting for a connection...")
        self.client_socket, addr = self.server_socket.accept()
        print("Connected to", addr)

    def stop_server(self):
        if self.server_socket:
            self.server_socket.close()

    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        start = time.time()
        
        def update_label():
            passed = time.time() - start
            secs = passed % 60
            mins = passed // 60
            hours = mins // 60
            self.label.config(text=f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")
            if self.recording:
                self.root.after(1000, update_label)  # Schedule the update after 1 second
        
        self.root.after(1000, update_label)  # Start the initial update
        while self.recording:
            data = stream.read(1024)
            frames.append(data)

            if self.client_socket:
                try:
                    self.client_socket.sendall(data)
                except:
                    print("Error sending data to the client")
                    break

        stream.stop_stream()
        stream.close()
        audio.terminate()

        if self.client_socket:
            self.client_socket.close()

        exist = True
        i = 1
        while exist:
            if os.path.exists(f"recording{i}.wav"):
                i += 1
            else:
                exist = False

        sound_file = wave.open(f"recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()


VoiceRecorder()
