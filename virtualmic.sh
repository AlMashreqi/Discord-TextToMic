#!/usr/bin/bash

pactl load-module module-null-sink sink_name=Source
pactl load-module module-virtual-source source_name=VirtualMic master=Source.monitor