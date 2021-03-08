import cv2,numpy as np,pyscreenshot as pss,time

Screen_record = cv2.VideoWriter('ss_record.avi', cv2.VideoWriter_fourcc(*'XVID'), 1.0, (1920,  1080))
time.sleep(5)
while (True):
	frame= pss.grab()
	frame_array=np.array(frame)
	cv2.imshow('Screen', frame_array)
	
	Screen_record.write(frame_array)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

Screen_record.release()
cv2.destroyAllWindows()