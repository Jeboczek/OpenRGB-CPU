from OpenRGBCpu.openrgbcpu import OpenRGBCPU

if __name__ == "__main__":
    cl = OpenRGBCPU()
    cl.connect()

    try:
        while True:
            cl.update_color()
    except KeyboardInterrupt:
        print("Stopping...")
        cl.disconnect()