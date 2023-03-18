# upload first/oldest image captured on the phone

last_image_uploaded ="" 
daily_upload_imgs = []
images = []
idx_to_start_upload = 0
idx_to_end_upload = 0

def getImages():
	pass
	# find gallery -> 1000 images -> filename.ext and filename(1).ext -> get all iamges into an array-> 
    # images = [img1, img2, img3, ....imgn-1, imgn]
    # get sequence ascending or desc because no new image can be added at before date from current date

for img in images:
	if last_image_uploaded == "" or last_image_uploaded == img:
		idx_to_start_upload = img.indexOf()
		remaining_len = len(images[idx_to_start_upload:])
		if remaining_len > 5:
			idx_to_end_upload = idx_to_start_upload + 5
			daily_upload_imgs = images[idx_to_start_upload:idx_to_end_upload]

# start uploadign daily images
for image in daily_upload_imgs:
	pass
	# upload image one by one