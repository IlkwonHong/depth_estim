img = imread('kinect_read_data.png');
for x = 1 : tmp(1)
  for y = 1 : tmp(2)
    if(img(x,y) == 0)
      img(x,y) = img(x,y) + 2000;
      endif
    endfor
  endfor
figure(1)

image(img,'CDataMapping','scaled')
colorbar