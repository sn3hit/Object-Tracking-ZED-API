import pyzed.sl as sl

# Create a ZED camera object
zed = sl.Camera()

# Set configuration parameters
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.AUTO # Use HD720 opr HD1200 video mode, depending on camera type.
init_params.camera_fps = 30 # Set fps at 30

# Open the camera
err = zed.open(init_params)
if (err != sl.ERROR_CODE.SUCCESS) :
    exit(-1)

image = sl.Mat()
runtime_parameters = sl.RuntimeParameters()
if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
    # A new image is available if grab() returns SUCCESS
    zed.retrieve_image(image, sl.VIEW.LEFT) # Retrieve the left image

print("Image resolution: ", image.get_width(), " x ", image.get_height())	