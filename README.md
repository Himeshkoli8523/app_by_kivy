
# VoiceRecorder

VoiceRecorder is a Python app that allows you to record and stream audio from your microphone using a graphical user interface (GUI). You can use it to create audio files or broadcast your voice to other devices.

## Features

- Record audio from your microphone and save it as a WAV file
- Stream audio data to a client socket over TCP/IP
- Display the elapsed time of the recording
- Control the recording state with a button

## Installation

To run VoiceRecorder, you need to have Python 3 and the following modules installed:

- os
- wave
- time
- threading
- tkinter
- pyaudio
- socket

You can install these modules using pip:

```bash
pip install os wave time threading tkinter pyaudio socket
```

Alternatively, you can use the requirements.txt file provided in the repository:

```bash
pip install -r requirements.txt
```

## Usage

To start VoiceRecorder, run the following command in your terminal:

```bash
python VoiceRecorder.py
```

This will open a GUI window with a button and a label. To start recording, click on the button. The button will turn purple and the label will show the elapsed time. To stop recording, click on the button again. The button will turn black and the label will reset. The recorded audio will be saved as a WAV file in the same directory as the script.

To stream audio data to a client socket, you need to run another script on the client device that can receive and play the audio data. You can use the VoicePlayer.py script provided in the repository for this purpose. You also need to know the IP address and port number of the server device running VoiceRecorder.

To start VoicePlayer, run the following command in your terminal:

```bash
python VoicePlayer.py <server_ip> <server_port>
```

Replace `<server_ip>` and `<server_port>` with the actual values of the server device. For example, if the server device has the IP address 192.168.0.1 and the port number 12345, run:

```bash
python VoicePlayer.py 192.168.0.1 12345
```

This will connect to the server socket and start playing the audio data received from the microphone. To stop playing, press Ctrl+C in the terminal.

