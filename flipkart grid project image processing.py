import cv2

vid=cv2.VideoCapture(0)
bot1,bot2,bot3,bot4=0,0,0,0
while True:
    isTrue,frame=vid.read()
    frame=cv2.resize(frame,(900,450))
    # frame croping for diff positions
    s1=frame[0:75,300:375]
    s2=frame[0:75,375:450]
    s3=frame[0:75,450:525]
    s4=frame[0:75,525:600]
    d1=frame[300:375,0:75]
    d2=frame[375:450,0:75]
    d3=frame[375:450,825:900]
    d4=frame[300:375,825:900]
    s1d1=frame[300:375,300:375]
    s2d2=frame[375:450,375:450]
    s3d3=frame[375:450,450:525]
    s4d4=frame[300:375,525:600]
    # display all the windows
    cv2.imshow("main frame",frame)
    cv2.imshow("s1",s1)
    cv2.imshow("s2", s2)
    cv2.imshow("s3", s3)
    cv2.imshow("s4", s4)
    cv2.imshow("d1", d1)
    cv2.imshow("d2", d2)
    cv2.imshow("d3", d3)
    cv2.imshow("d4", d4)
    cv2.imshow("s1d1", s1d1)
    cv2.imshow("s2d2", s2d2)
    cv2.imshow("s3d3", s3d3)
    cv2.imshow("s4d4", s4d4)
    # taking the colors of diff frames
    #for bot1
    s1_color = s1[35,35,2]
    s1d1_color = s1d1[35, 35, 2]
    d1_color = d1[35, 35, 2]
    # for bot2
    s2_color = s2[35, 35, 2]
    s2d2_color = s2d2[35, 35, 2]
    d2_color = d2[35, 35, 2]
    # for bot3
    s3_color = s3[35, 35, 2]
    s3d3_color = s3d3[35, 35, 2]
    d3_color = d3[35, 35, 2]
    # for bot4
    s4_color = s4[35, 35, 2]
    s4d4_color = s4d4[35, 35, 2]
    d4_color = d4[35, 35, 2]
    # control statements--->
    if bot1<=4:
         if s1_color<50 and s1d1_color>100 and d1_color>100 and bot1==0:
            bot1=bot1+1
         if s1d1_color<50 and s1_color>100 and d1_color>100 and bot1==1:
            bot1 = bot1 + 1
         if d1_color<50 and s1d1_color>100 and s1_color>100 and bot1==2:
            bot1 = bot1 + 1
         if s1d1_color < 50 and s1_color > 100 and d1_color > 100 and bot1==3:
            bot1 = bot1 + 1
         if s1_color < 50 and s1d1_color > 100 and d1_color > 100 and bot1==4:
            bot1 = bot1 + 1
    if bot2<=4 and bot1==5:
        if s2_color < 50 and s2d2_color > 100 and d2_color > 100 and bot2==0:
            bot2 = bot2 + 1
        if s2d2_color < 50 and s2_color > 100 and d2_color > 100 and bot2==1:
            bot2 = bot2 + 1
        if d2_color < 50 and s2d2_color > 100 and s2_color > 100 and bot2==2:
            bot2 = bot2 + 1
        if s2d2_color < 50 and s2_color > 100 and d2_color > 100 and bot2==3:
            bot2 = bot2 + 1
        if s2_color < 50 and s2d2_color > 100 and d2_color > 100 and bot2==4:
            bot2 = bot2 + 1
    if bot3 <= 4 and bot2 == 5:
        if s3_color < 50 and s3d3_color > 100 and d3_color > 100 and bot3==0:
            bot3 = bot3 + 1
        if s3d3_color < 50 and s3_color > 100 and d3_color > 100 and bot3==1:
            bot3 = bot3 + 1
        if d3_color < 50 and s3d3_color > 100 and s3_color > 100 and bot3==2:
            bot3 = bot3 + 1
        if s3d3_color < 50 and s3_color > 100 and d3_color > 100 and bot3==3:
            bot3 = bot3 + 1
        if s3_color < 50 and s3d3_color > 100 and d3_color > 100 and bot3==4:
            bot3 = bot3 + 1
    if bot4 <= 4 and bot3 == 5:
        if s4_color < 50 and s4d4_color > 100 and d4_color > 100 and bot4==0:
            bot4 = bot4 + 1
        if s4d4_color < 50 and s4_color > 100 and d4_color > 100 and bot4==1:
            bot4 = bot4 + 1
        if d4_color < 50 and s4d4_color > 100 and s4_color > 100 and bot4==2:
            bot4 = bot4 + 1
        if s4d4_color < 50 and s4_color > 100 and d4_color > 100 and bot4==3:
            bot4 = bot4 + 1
        if s4_color < 50 and s4d4_color > 100 and d4_color > 100 and bot4==4:
            bot4 = bot4 + 1

    print(bot1 ,bot2 ,bot3 ,bot4)

    # print(frame.shape)
    #print(s1d1.shape)
    if cv2.waitKey(1)==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()

