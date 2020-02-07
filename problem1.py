time = 8

if time < 9:
    print("Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.")
elif time <= 16:
    print("Working hard or hardly working?")
elif time < 20:
    print("How did it get so late so soon?")
elif time < 22:
    print("A day without sunshine is like, you know, night.")
elif time >= 25:
    raise ValueError("Please enter a valid time")
else:
    print("Burning the midnight oil!")