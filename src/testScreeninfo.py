from screeninfo import get_monitors


monitor = get_monitors()[0]
screenWidthRatio = round(monitor.width / 1920, 2)
screenHeightRatio = round(monitor.height / 1080, 2)
def calculateWidth(width):
    return round(width * screenWidthRatio,1)

def calculateHeight(height):
    return round(height * screenHeightRatio, 1)

def main():


    print(f"Width: {calculateWidth(586)}, Height: {calculateHeight(586)}")

if __name__ == "__main__":
    main()