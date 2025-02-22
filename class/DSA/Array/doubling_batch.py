import sys # provides getsizeof function
data = [ ]
for k in range(1000,2000): # NOTE: must fix choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    print( "Length: {0:3d}; Size in bytes: {1:4d} increment of {2:4d}" .format(a, b, b-56))
    data.extend([None,None,None,None])
print(data)


# Length:   0; Size in bytes:   56 increment of    0

# Length:   4; Size in bytes:   88 increment of   32

# Length:   8; Size in bytes:  152 increment of   96
# Length:  12; Size in bytes:  152 increment of   96

# Length:  16; Size in bytes:  248 increment of  192
# Length:  20; Size in bytes:  248 increment of  192
# Length:  24; Size in bytes:  248 increment of  192

# Length:  28; Size in bytes:  344 increment of  288
# Length:  32; Size in bytes:  344 increment of  288
# Length:  36; Size in bytes:  344 increment of  288

# Length:  40; Size in bytes:  440 increment of  384
# Length:  44; Size in bytes:  440 increment of  384
# Length:  48; Size in bytes:  440 increment of  384

# Length:  52; Size in bytes:  568 increment of  512
# Length:  56; Size in bytes:  568 increment of  512
# Length:  60; Size in bytes:  568 increment of  512
# Length:  64; Size in bytes:  568 increment of  512

# Length:  68; Size in bytes:  696 increment of  640
# Length:  72; Size in bytes:  696 increment of  640
# Length:  76; Size in bytes:  696 increment of  640
# Length:  80; Size in bytes:  696 increment of  640

# Length:  84; Size in bytes:  856 increment of  800
# Length:  88; Size in bytes:  856 increment of  800
# Length:  92; Size in bytes:  856 increment of  800
# Length:  96; Size in bytes:  856 increment of  800
# Length: 100; Size in bytes:  856 increment of  800

# Length: 104; Size in bytes: 1016 increment of  960
# Length: 108; Size in bytes: 1016 increment of  960
# Length: 112; Size in bytes: 1016 increment of  960
# Length: 116; Size in bytes: 1016 increment of  960
# Length: 120; Size in bytes: 1016 increment of  960

# Length: 124; Size in bytes: 1208 increment of 1152
# Length: 128; Size in bytes: 1208 increment of 1152
# Length: 132; Size in bytes: 1208 increment of 1152
# Length: 136; Size in bytes: 1208 increment of 1152
# Length: 140; Size in bytes: 1208 increment of 1152
# Length: 144; Size in bytes: 1208 increment of 1152

# Length: 148; Size in bytes: 1432 increment of 1376
# Length: 152; Size in bytes: 1432 increment of 1376
# Length: 156; Size in bytes: 1432 increment of 1376
# Length: 160; Size in bytes: 1432 increment of 1376
# Length: 164; Size in bytes: 1432 increment of 1376
# Length: 168; Size in bytes: 1432 increment of 1376
# Length: 172; Size in bytes: 1432 increment of 1376

# Length: 176; Size in bytes: 1688 increment of 1632
# Length: 180; Size in bytes: 1688 increment of 1632
# Length: 184; Size in bytes: 1688 increment of 1632
# Length: 188; Size in bytes: 1688 increment of 1632
# Length: 192; Size in bytes: 1688 increment of 1632
# Length: 196; Size in bytes: 1688 increment of 1632
# Length: 200; Size in bytes: 1688 increment of 1632
# Length: 204; Size in bytes: 1688 increment of 1632

# Length: 208; Size in bytes: 1976 increment of 1920
# Length: 212; Size in bytes: 1976 increment of 1920
# Length: 216; Size in bytes: 1976 increment of 1920
# Length: 220; Size in bytes: 1976 increment of 1920
# Length: 224; Size in bytes: 1976 increment of 1920
# Length: 228; Size in bytes: 1976 increment of 1920
# Length: 232; Size in bytes: 1976 increment of 1920
# Length: 236; Size in bytes: 1976 increment of 1920
# Length: 240; Size in bytes: 1976 increment of 1920

# Length: 244; Size in bytes: 2296 increment of 2240
# Length: 248; Size in bytes: 2296 increment of 2240
# Length: 252; Size in bytes: 2296 increment of 2240
# Length: 256; Size in bytes: 2296 increment of 2240
# Length: 260; Size in bytes: 2296 increment of 2240
# Length: 264; Size in bytes: 2296 increment of 2240
# Length: 268; Size in bytes: 2296 increment of 2240
# Length: 272; Size in bytes: 2296 increment of 2240
# Length: 276; Size in bytes: 2296 increment of 2240
# Length: 280; Size in bytes: 2296 increment of 2240

# Length: 284; Size in bytes: 2648 increment of 2592
# Length: 288; Size in bytes: 2648 increment of 2592
# Length: 292; Size in bytes: 2648 increment of 2592
# Length: 296; Size in bytes: 2648 increment of 2592
# Length: 300; Size in bytes: 2648 increment of 2592
# Length: 304; Size in bytes: 2648 increment of 2592
# Length: 308; Size in bytes: 2648 increment of 2592
# Length: 312; Size in bytes: 2648 increment of 2592
# Length: 316; Size in bytes: 2648 increment of 2592
# Length: 320; Size in bytes: 2648 increment of 2592
# Length: 324; Size in bytes: 2648 increment of 2592

# Length: 328; Size in bytes: 3032 increment of 2976
# Length: 332; Size in bytes: 3032 increment of 2976
# Length: 336; Size in bytes: 3032 increment of 2976
# Length: 340; Size in bytes: 3032 increment of 2976
# Length: 344; Size in bytes: 3032 increment of 2976
# Length: 348; Size in bytes: 3032 increment of 2976
# Length: 352; Size in bytes: 3032 increment of 2976
# Length: 356; Size in bytes: 3032 increment of 2976
# Length: 360; Size in bytes: 3032 increment of 2976
# Length: 364; Size in bytes: 3032 increment of 2976
# Length: 368; Size in bytes: 3032 increment of 2976
# Length: 372; Size in bytes: 3032 increment of 2976

# Length: 376; Size in bytes: 3480 increment of 3424
# Length: 380; Size in bytes: 3480 increment of 3424
# Length: 384; Size in bytes: 3480 increment of 3424
# Length: 388; Size in bytes: 3480 increment of 3424
# Length: 392; Size in bytes: 3480 increment of 3424
# Length: 396; Size in bytes: 3480 increment of 3424
# Length: 400; Size in bytes: 3480 increment of 3424
# Length: 404; Size in bytes: 3480 increment of 3424
# Length: 408; Size in bytes: 3480 increment of 3424
# Length: 412; Size in bytes: 3480 increment of 3424
# Length: 416; Size in bytes: 3480 increment of 3424
# Length: 420; Size in bytes: 3480 increment of 3424
# Length: 424; Size in bytes: 3480 increment of 3424
# Length: 428; Size in bytes: 3480 increment of 3424

# Length: 432; Size in bytes: 3992 increment of 3936
# Length: 436; Size in bytes: 3992 increment of 3936
# Length: 440; Size in bytes: 3992 increment of 3936
# Length: 444; Size in bytes: 3992 increment of 3936
# Length: 448; Size in bytes: 3992 increment of 3936
# Length: 452; Size in bytes: 3992 increment of 3936
# Length: 456; Size in bytes: 3992 increment of 3936
# Length: 460; Size in bytes: 3992 increment of 3936
# Length: 464; Size in bytes: 3992 increment of 3936
# Length: 468; Size in bytes: 3992 increment of 3936
# Length: 472; Size in bytes: 3992 increment of 3936
# Length: 476; Size in bytes: 3992 increment of 3936
# Length: 480; Size in bytes: 3992 increment of 3936
# Length: 484; Size in bytes: 3992 increment of 3936
# Length: 488; Size in bytes: 3992 increment of 3936
# Length: 492; Size in bytes: 3992 increment of 3936

# Length: 496; Size in bytes: 4568 increment of 4512
# Length: 500; Size in bytes: 4568 increment of 4512
# Length: 504; Size in bytes: 4568 increment of 4512
# Length: 508; Size in bytes: 4568 increment of 4512
# Length: 512; Size in bytes: 4568 increment of 4512
# Length: 516; Size in bytes: 4568 increment of 4512
# Length: 520; Size in bytes: 4568 increment of 4512
# Length: 524; Size in bytes: 4568 increment of 4512
# Length: 528; Size in bytes: 4568 increment of 4512
# Length: 532; Size in bytes: 4568 increment of 4512
# Length: 536; Size in bytes: 4568 increment of 4512
# Length: 540; Size in bytes: 4568 increment of 4512
# Length: 544; Size in bytes: 4568 increment of 4512
# Length: 548; Size in bytes: 4568 increment of 4512
# Length: 552; Size in bytes: 4568 increment of 4512
# Length: 556; Size in bytes: 4568 increment of 4512
# Length: 560; Size in bytes: 4568 increment of 4512
# Length: 564; Size in bytes: 4568 increment of 4512
# Length: 568; Size in bytes: 5208 increment of 5152
# Length: 572; Size in bytes: 5208 increment of 5152
# Length: 576; Size in bytes: 5208 increment of 5152
# Length: 580; Size in bytes: 5208 increment of 5152
# Length: 584; Size in bytes: 5208 increment of 5152
# Length: 588; Size in bytes: 5208 increment of 5152
# Length: 592; Size in bytes: 5208 increment of 5152
# Length: 596; Size in bytes: 5208 increment of 5152
# Length: 600; Size in bytes: 5208 increment of 5152
# Length: 604; Size in bytes: 5208 increment of 5152
# Length: 608; Size in bytes: 5208 increment of 5152
# Length: 612; Size in bytes: 5208 increment of 5152
# Length: 616; Size in bytes: 5208 increment of 5152
# Length: 620; Size in bytes: 5208 increment of 5152
# Length: 624; Size in bytes: 5208 increment of 5152
# Length: 628; Size in bytes: 5208 increment of 5152
# Length: 632; Size in bytes: 5208 increment of 5152
# Length: 636; Size in bytes: 5208 increment of 5152
# Length: 640; Size in bytes: 5208 increment of 5152
# Length: 644; Size in bytes: 5208 increment of 5152
# Length: 648; Size in bytes: 5912 increment of 5856
# Length: 652; Size in bytes: 5912 increment of 5856
# Length: 656; Size in bytes: 5912 increment of 5856
# Length: 660; Size in bytes: 5912 increment of 5856
# Length: 664; Size in bytes: 5912 increment of 5856
# Length: 668; Size in bytes: 5912 increment of 5856
# Length: 672; Size in bytes: 5912 increment of 5856
# Length: 676; Size in bytes: 5912 increment of 5856
# Length: 680; Size in bytes: 5912 increment of 5856
# Length: 684; Size in bytes: 5912 increment of 5856
# Length: 688; Size in bytes: 5912 increment of 5856
# Length: 692; Size in bytes: 5912 increment of 5856
# Length: 696; Size in bytes: 5912 increment of 5856
# Length: 700; Size in bytes: 5912 increment of 5856
# Length: 704; Size in bytes: 5912 increment of 5856
# Length: 708; Size in bytes: 5912 increment of 5856
# Length: 712; Size in bytes: 5912 increment of 5856
# Length: 716; Size in bytes: 5912 increment of 5856
# Length: 720; Size in bytes: 5912 increment of 5856
# Length: 724; Size in bytes: 5912 increment of 5856
# Length: 728; Size in bytes: 5912 increment of 5856
# Length: 732; Size in bytes: 5912 increment of 5856
# Length: 736; Size in bytes: 6712 increment of 6656
# Length: 740; Size in bytes: 6712 increment of 6656
# Length: 744; Size in bytes: 6712 increment of 6656
# Length: 748; Size in bytes: 6712 increment of 6656
# Length: 752; Size in bytes: 6712 increment of 6656
# Length: 756; Size in bytes: 6712 increment of 6656
# Length: 760; Size in bytes: 6712 increment of 6656
# Length: 764; Size in bytes: 6712 increment of 6656
# Length: 768; Size in bytes: 6712 increment of 6656
# Length: 772; Size in bytes: 6712 increment of 6656
# Length: 776; Size in bytes: 6712 increment of 6656
# Length: 780; Size in bytes: 6712 increment of 6656
# Length: 784; Size in bytes: 6712 increment of 6656
# Length: 788; Size in bytes: 6712 increment of 6656
# Length: 792; Size in bytes: 6712 increment of 6656
# Length: 796; Size in bytes: 6712 increment of 6656
# Length: 800; Size in bytes: 6712 increment of 6656
# Length: 804; Size in bytes: 6712 increment of 6656
# Length: 808; Size in bytes: 6712 increment of 6656
# Length: 812; Size in bytes: 6712 increment of 6656
# Length: 816; Size in bytes: 6712 increment of 6656
# Length: 820; Size in bytes: 6712 increment of 6656
# Length: 824; Size in bytes: 6712 increment of 6656
# Length: 828; Size in bytes: 6712 increment of 6656
# Length: 832; Size in bytes: 6712 increment of 6656
# Length: 836; Size in bytes: 7608 increment of 7552
# Length: 840; Size in bytes: 7608 increment of 7552
# Length: 844; Size in bytes: 7608 increment of 7552
# Length: 848; Size in bytes: 7608 increment of 7552
# Length: 852; Size in bytes: 7608 increment of 7552
# Length: 856; Size in bytes: 7608 increment of 7552
# Length: 860; Size in bytes: 7608 increment of 7552
# Length: 864; Size in bytes: 7608 increment of 7552
# Length: 868; Size in bytes: 7608 increment of 7552
# Length: 872; Size in bytes: 7608 increment of 7552
# Length: 876; Size in bytes: 7608 increment of 7552
# Length: 880; Size in bytes: 7608 increment of 7552
# Length: 884; Size in bytes: 7608 increment of 7552
# Length: 888; Size in bytes: 7608 increment of 7552
# Length: 892; Size in bytes: 7608 increment of 7552
# Length: 896; Size in bytes: 7608 increment of 7552
# Length: 900; Size in bytes: 7608 increment of 7552
# Length: 904; Size in bytes: 7608 increment of 7552
# Length: 908; Size in bytes: 7608 increment of 7552
# Length: 912; Size in bytes: 7608 increment of 7552
# Length: 916; Size in bytes: 7608 increment of 7552
# Length: 920; Size in bytes: 7608 increment of 7552
# Length: 924; Size in bytes: 7608 increment of 7552
# Length: 928; Size in bytes: 7608 increment of 7552
# Length: 932; Size in bytes: 7608 increment of 7552
# Length: 936; Size in bytes: 7608 increment of 7552
# Length: 940; Size in bytes: 7608 increment of 7552
# Length: 944; Size in bytes: 7608 increment of 7552
# Length: 948; Size in bytes: 8632 increment of 8576
# Length: 952; Size in bytes: 8632 increment of 8576
# Length: 956; Size in bytes: 8632 increment of 8576
# Length: 960; Size in bytes: 8632 increment of 8576
# Length: 964; Size in bytes: 8632 increment of 8576
# Length: 968; Size in bytes: 8632 increment of 8576
# Length: 972; Size in bytes: 8632 increment of 8576
# Length: 976; Size in bytes: 8632 increment of 8576
# Length: 980; Size in bytes: 8632 increment of 8576
# Length: 984; Size in bytes: 8632 increment of 8576
# Length: 988; Size in bytes: 8632 increment of 8576
# Length: 992; Size in bytes: 8632 increment of 8576
# Length: 996; Size in bytes: 8632 increment of 8576

# 20
# Length: 1000; Size in bytes: 8632 increment of 8576
# Length: 1004; Size in bytes: 8632 increment of 8576
# Length: 1008; Size in bytes: 8632 increment of 8576
# Length: 1012; Size in bytes: 8632 increment of 8576
# Length: 1016; Size in bytes: 8632 increment of 8576
# Length: 1020; Size in bytes: 8632 increment of 8576
# Length: 1024; Size in bytes: 8632 increment of 8576
# Length: 1028; Size in bytes: 8632 increment of 8576
# Length: 1032; Size in bytes: 8632 increment of 8576
# Length: 1036; Size in bytes: 8632 increment of 8576
# Length: 1040; Size in bytes: 8632 increment of 8576
# Length: 1044; Size in bytes: 8632 increment of 8576
# Length: 1048; Size in bytes: 8632 increment of 8576
# Length: 1052; Size in bytes: 8632 increment of 8576
# Length: 1056; Size in bytes: 8632 increment of 8576
# Length: 1060; Size in bytes: 8632 increment of 8576
# Length: 1064; Size in bytes: 8632 increment of 8576
# Length: 1068; Size in bytes: 8632 increment of 8576
# Length: 1072; Size in bytes: 8632 increment of 8576

# 36
# Length: 1076; Size in bytes: 9784 increment of 9728
# Length: 1080; Size in bytes: 9784 increment of 9728
# Length: 1084; Size in bytes: 9784 increment of 9728
# Length: 1088; Size in bytes: 9784 increment of 9728
# Length: 1092; Size in bytes: 9784 increment of 9728
# Length: 1096; Size in bytes: 9784 increment of 9728
# Length: 1100; Size in bytes: 9784 increment of 9728
# Length: 1104; Size in bytes: 9784 increment of 9728
# Length: 1108; Size in bytes: 9784 increment of 9728
# Length: 1112; Size in bytes: 9784 increment of 9728
# Length: 1116; Size in bytes: 9784 increment of 9728
# Length: 1120; Size in bytes: 9784 increment of 9728
# Length: 1124; Size in bytes: 9784 increment of 9728
# Length: 1128; Size in bytes: 9784 increment of 9728
# Length: 1132; Size in bytes: 9784 increment of 9728
# Length: 1136; Size in bytes: 9784 increment of 9728
# Length: 1140; Size in bytes: 9784 increment of 9728
# Length: 1144; Size in bytes: 9784 increment of 9728
# Length: 1148; Size in bytes: 9784 increment of 9728
# Length: 1152; Size in bytes: 9784 increment of 9728
# Length: 1156; Size in bytes: 9784 increment of 9728
# Length: 1160; Size in bytes: 9784 increment of 9728
# Length: 1164; Size in bytes: 9784 increment of 9728
# Length: 1168; Size in bytes: 9784 increment of 9728
# Length: 1172; Size in bytes: 9784 increment of 9728
# Length: 1176; Size in bytes: 9784 increment of 9728
# Length: 1180; Size in bytes: 9784 increment of 9728
# Length: 1184; Size in bytes: 9784 increment of 9728
# Length: 1188; Size in bytes: 9784 increment of 9728
# Length: 1192; Size in bytes: 9784 increment of 9728
# Length: 1196; Size in bytes: 9784 increment of 9728
# Length: 1200; Size in bytes: 9784 increment of 9728
# Length: 1204; Size in bytes: 9784 increment of 9728
# Length: 1208; Size in bytes: 9784 increment of 9728
# Length: 1212; Size in bytes: 9784 increment of 9728
# Length: 1216; Size in bytes: 9784 increment of 9728

# 40
# Length: 1220; Size in bytes: 11064 increment of 11008
# Length: 1224; Size in bytes: 11064 increment of 11008
# Length: 1228; Size in bytes: 11064 increment of 11008
# Length: 1232; Size in bytes: 11064 increment of 11008
# Length: 1236; Size in bytes: 11064 increment of 11008
# Length: 1240; Size in bytes: 11064 increment of 11008
# Length: 1244; Size in bytes: 11064 increment of 11008
# Length: 1248; Size in bytes: 11064 increment of 11008
# Length: 1252; Size in bytes: 11064 increment of 11008
# Length: 1256; Size in bytes: 11064 increment of 11008
# Length: 1260; Size in bytes: 11064 increment of 11008
# Length: 1264; Size in bytes: 11064 increment of 11008
# Length: 1268; Size in bytes: 11064 increment of 11008
# Length: 1272; Size in bytes: 11064 increment of 11008
# Length: 1276; Size in bytes: 11064 increment of 11008
# Length: 1280; Size in bytes: 11064 increment of 11008
# Length: 1284; Size in bytes: 11064 increment of 11008
# Length: 1288; Size in bytes: 11064 increment of 11008
# Length: 1292; Size in bytes: 11064 increment of 11008
# Length: 1296; Size in bytes: 11064 increment of 11008
# Length: 1300; Size in bytes: 11064 increment of 11008
# Length: 1304; Size in bytes: 11064 increment of 11008
# Length: 1308; Size in bytes: 11064 increment of 11008
# Length: 1312; Size in bytes: 11064 increment of 11008
# Length: 1316; Size in bytes: 11064 increment of 11008
# Length: 1320; Size in bytes: 11064 increment of 11008
# Length: 1324; Size in bytes: 11064 increment of 11008
# Length: 1328; Size in bytes: 11064 increment of 11008
# Length: 1332; Size in bytes: 11064 increment of 11008
# Length: 1336; Size in bytes: 11064 increment of 11008
# Length: 1340; Size in bytes: 11064 increment of 11008
# Length: 1344; Size in bytes: 11064 increment of 11008
# Length: 1348; Size in bytes: 11064 increment of 11008
# Length: 1352; Size in bytes: 11064 increment of 11008
# Length: 1356; Size in bytes: 11064 increment of 11008
# Length: 1360; Size in bytes: 11064 increment of 11008
# Length: 1364; Size in bytes: 11064 increment of 11008
# Length: 1368; Size in bytes: 11064 increment of 11008
# Length: 1372; Size in bytes: 11064 increment of 11008
# Length: 1376; Size in bytes: 11064 increment of 11008

# 44
# Length: 1380; Size in bytes: 12504 increment of 12448
# Length: 1384; Size in bytes: 12504 increment of 12448
# Length: 1388; Size in bytes: 12504 increment of 12448
# Length: 1392; Size in bytes: 12504 increment of 12448
# Length: 1396; Size in bytes: 12504 increment of 12448
# Length: 1400; Size in bytes: 12504 increment of 12448
# Length: 1404; Size in bytes: 12504 increment of 12448
# Length: 1408; Size in bytes: 12504 increment of 12448
# Length: 1412; Size in bytes: 12504 increment of 12448
# Length: 1416; Size in bytes: 12504 increment of 12448
# Length: 1420; Size in bytes: 12504 increment of 12448
# Length: 1424; Size in bytes: 12504 increment of 12448
# Length: 1428; Size in bytes: 12504 increment of 12448
# Length: 1432; Size in bytes: 12504 increment of 12448
# Length: 1436; Size in bytes: 12504 increment of 12448
# Length: 1440; Size in bytes: 12504 increment of 12448
# Length: 1444; Size in bytes: 12504 increment of 12448
# Length: 1448; Size in bytes: 12504 increment of 12448
# Length: 1452; Size in bytes: 12504 increment of 12448
# Length: 1456; Size in bytes: 12504 increment of 12448
# Length: 1460; Size in bytes: 12504 increment of 12448
# Length: 1464; Size in bytes: 12504 increment of 12448
# Length: 1468; Size in bytes: 12504 increment of 12448
# Length: 1472; Size in bytes: 12504 increment of 12448
# Length: 1476; Size in bytes: 12504 increment of 12448
# Length: 1480; Size in bytes: 12504 increment of 12448
# Length: 1484; Size in bytes: 12504 increment of 12448
# Length: 1488; Size in bytes: 12504 increment of 12448
# Length: 1492; Size in bytes: 12504 increment of 12448
# Length: 1496; Size in bytes: 12504 increment of 12448
# Length: 1500; Size in bytes: 12504 increment of 12448
# Length: 1504; Size in bytes: 12504 increment of 12448
# Length: 1508; Size in bytes: 12504 increment of 12448
# Length: 1512; Size in bytes: 12504 increment of 12448
# Length: 1516; Size in bytes: 12504 increment of 12448
# Length: 1520; Size in bytes: 12504 increment of 12448
# Length: 1524; Size in bytes: 12504 increment of 12448
# Length: 1528; Size in bytes: 12504 increment of 12448
# Length: 1532; Size in bytes: 12504 increment of 12448
# Length: 1536; Size in bytes: 12504 increment of 12448
# Length: 1540; Size in bytes: 12504 increment of 12448
# Length: 1544; Size in bytes: 12504 increment of 12448
# Length: 1548; Size in bytes: 12504 increment of 12448
# Length: 1552; Size in bytes: 12504 increment of 12448
# Length: 1556; Size in bytes: 12504 increment of 12448


# 50
# Length: 1560; Size in bytes: 14136 increment of 14080
# Length: 1564; Size in bytes: 14136 increment of 14080
# Length: 1568; Size in bytes: 14136 increment of 14080
# Length: 1572; Size in bytes: 14136 increment of 14080
# Length: 1576; Size in bytes: 14136 increment of 14080
# Length: 1580; Size in bytes: 14136 increment of 14080
# Length: 1584; Size in bytes: 14136 increment of 14080
# Length: 1588; Size in bytes: 14136 increment of 14080
# Length: 1592; Size in bytes: 14136 increment of 14080
# Length: 1596; Size in bytes: 14136 increment of 14080
# Length: 1600; Size in bytes: 14136 increment of 14080
# Length: 1604; Size in bytes: 14136 increment of 14080
# Length: 1608; Size in bytes: 14136 increment of 14080
# Length: 1612; Size in bytes: 14136 increment of 14080
# Length: 1616; Size in bytes: 14136 increment of 14080
# Length: 1620; Size in bytes: 14136 increment of 14080
# Length: 1624; Size in bytes: 14136 increment of 14080
# Length: 1628; Size in bytes: 14136 increment of 14080
# Length: 1632; Size in bytes: 14136 increment of 14080
# Length: 1636; Size in bytes: 14136 increment of 14080
# Length: 1640; Size in bytes: 14136 increment of 14080
# Length: 1644; Size in bytes: 14136 increment of 14080
# Length: 1648; Size in bytes: 14136 increment of 14080
# Length: 1652; Size in bytes: 14136 increment of 14080
# Length: 1656; Size in bytes: 14136 increment of 14080
# Length: 1660; Size in bytes: 14136 increment of 14080
# Length: 1664; Size in bytes: 14136 increment of 14080
# Length: 1668; Size in bytes: 14136 increment of 14080
# Length: 1672; Size in bytes: 14136 increment of 14080
# Length: 1676; Size in bytes: 14136 increment of 14080
# Length: 1680; Size in bytes: 14136 increment of 14080
# Length: 1684; Size in bytes: 14136 increment of 14080
# Length: 1688; Size in bytes: 14136 increment of 14080
# Length: 1692; Size in bytes: 14136 increment of 14080
# Length: 1696; Size in bytes: 14136 increment of 14080
# Length: 1700; Size in bytes: 14136 increment of 14080
# Length: 1704; Size in bytes: 14136 increment of 14080
# Length: 1708; Size in bytes: 14136 increment of 14080
# Length: 1712; Size in bytes: 14136 increment of 14080
# Length: 1716; Size in bytes: 14136 increment of 14080
# Length: 1720; Size in bytes: 14136 increment of 14080
# Length: 1724; Size in bytes: 14136 increment of 14080
# Length: 1728; Size in bytes: 14136 increment of 14080
# Length: 1732; Size in bytes: 14136 increment of 14080
# Length: 1736; Size in bytes: 14136 increment of 14080
# Length: 1740; Size in bytes: 14136 increment of 14080
# Length: 1744; Size in bytes: 14136 increment of 14080
# Length: 1748; Size in bytes: 14136 increment of 14080
# Length: 1752; Size in bytes: 14136 increment of 14080
# Length: 1756; Size in bytes: 14136 increment of 14080
# Length: 1760; Size in bytes: 14136 increment of 14080


# 56
# Length: 1764; Size in bytes: 15960 increment of 15904
# Length: 1768; Size in bytes: 15960 increment of 15904
# Length: 1772; Size in bytes: 15960 increment of 15904
# Length: 1776; Size in bytes: 15960 increment of 15904
# Length: 1780; Size in bytes: 15960 increment of 15904
# Length: 1784; Size in bytes: 15960 increment of 15904
# Length: 1788; Size in bytes: 15960 increment of 15904
# Length: 1792; Size in bytes: 15960 increment of 15904
# Length: 1796; Size in bytes: 15960 increment of 15904
# Length: 1800; Size in bytes: 15960 increment of 15904
# Length: 1804; Size in bytes: 15960 increment of 15904
# Length: 1808; Size in bytes: 15960 increment of 15904
# Length: 1812; Size in bytes: 15960 increment of 15904
# Length: 1816; Size in bytes: 15960 increment of 15904
# Length: 1820; Size in bytes: 15960 increment of 15904
# Length: 1824; Size in bytes: 15960 increment of 15904
# Length: 1828; Size in bytes: 15960 increment of 15904
# Length: 1832; Size in bytes: 15960 increment of 15904
# Length: 1836; Size in bytes: 15960 increment of 15904
# Length: 1840; Size in bytes: 15960 increment of 15904
# Length: 1844; Size in bytes: 15960 increment of 15904
# Length: 1848; Size in bytes: 15960 increment of 15904
# Length: 1852; Size in bytes: 15960 increment of 15904
# Length: 1856; Size in bytes: 15960 increment of 15904
# Length: 1860; Size in bytes: 15960 increment of 15904
# Length: 1864; Size in bytes: 15960 increment of 15904
# Length: 1868; Size in bytes: 15960 increment of 15904
# Length: 1872; Size in bytes: 15960 increment of 15904
# Length: 1876; Size in bytes: 15960 increment of 15904
# Length: 1880; Size in bytes: 15960 increment of 15904
# Length: 1884; Size in bytes: 15960 increment of 15904
# Length: 1888; Size in bytes: 15960 increment of 15904
# Length: 1892; Size in bytes: 15960 increment of 15904
# Length: 1896; Size in bytes: 15960 increment of 15904
# Length: 1900; Size in bytes: 15960 increment of 15904
# Length: 1904; Size in bytes: 15960 increment of 15904
# Length: 1908; Size in bytes: 15960 increment of 15904
# Length: 1912; Size in bytes: 15960 increment of 15904
# Length: 1916; Size in bytes: 15960 increment of 15904
# Length: 1920; Size in bytes: 15960 increment of 15904
# Length: 1924; Size in bytes: 15960 increment of 15904
# Length: 1928; Size in bytes: 15960 increment of 15904
# Length: 1932; Size in bytes: 15960 increment of 15904
# Length: 1936; Size in bytes: 15960 increment of 15904
# Length: 1940; Size in bytes: 15960 increment of 15904
# Length: 1944; Size in bytes: 15960 increment of 15904
# Length: 1948; Size in bytes: 15960 increment of 15904
# Length: 1952; Size in bytes: 15960 increment of 15904
# Length: 1956; Size in bytes: 15960 increment of 15904
# Length: 1960; Size in bytes: 15960 increment of 15904
# Length: 1964; Size in bytes: 15960 increment of 15904
# Length: 1968; Size in bytes: 15960 increment of 15904
# Length: 1972; Size in bytes: 15960 increment of 15904
# Length: 1976; Size in bytes: 15960 increment of 15904
# Length: 1980; Size in bytes: 15960 increment of 15904
# Length: 1984; Size in bytes: 15960 increment of 15904
# Length: 1988; Size in bytes: 15960 increment of 15904

# Length: 1992; Size in bytes: 18008 increment of 17952
# Length: 1996; Size in bytes: 18008 increment of 17952