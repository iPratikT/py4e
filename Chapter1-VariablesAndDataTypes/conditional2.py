"""
in this program we will learn about conditional statements
the condition is related to the color if traffic light
"""

light = input("light color: ")
if light == "red":
    print("stop")
elif light == "yellow":
    print("look")
elif light == "green":
    print("go")
else:
    print("traffic signal is broken")