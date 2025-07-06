{\rtf1\ansi\ansicpg936\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # File: app.py\
class Calculator:\
    def add(self, a, b):\
        return a + b\
\
    def subtract(self, a, b):\
        return a - b\
\
    def multiply(self, a, b):\
        return a * b\
\
    def divide(self, a, b):\
        if b == 0:\
            raise ValueError("Cannot divide by zero")\
        return a / b\
}