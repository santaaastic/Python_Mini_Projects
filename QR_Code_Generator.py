# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:10:54 2021
Quick Response Image generator
pip install pyqrcode if not present
@author: Shantanu
"""

import pyqrcode as QR
video_link="https://www.youtube.com/watch?v=CLsSpFd6lYI"
link = QR.create(video_link)
link.svg("Vibin_PlanetPunk.svg", scale = 10) 