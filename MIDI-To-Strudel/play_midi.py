
import mido
import time
import rtmidi

# Load your MIDI file
mid = mido.MidiFile('ClubbedToDeath.midi')
port_name = "FLUID Synth (37792):Synth input port (37792:0) 128:0"  # adjust to the correct name
with mido.open_output(port_name) as outport:
    for msg in mid.play():
        if not msg.is_meta:
            outport.send(msg)
'''
# Initialize RtMidi output
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("Virtual MIDI Output")

# Start FluidSynth in a separate terminal using a high-quality SoundFont:
# fluidsynth -a alsa /path/to/GeneralUserGS.sf2

# Play the MIDI file
for msg in mid.play():
    if not msg.is_meta:
        midiout.send_message(msg.bytes())
'''
