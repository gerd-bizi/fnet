# import os
# from aicsimageio import AICSImage
# os.environ["PYTHONPATH"] = "/home/gbizi/rotation_2/pytorch_fnet:" + os.environ.get("PYTHONPATH","")
# from fnet.data.aics_czi_dataset import AicsCziDataset
# from fnet.data.czidataset import CziDataset, CziReader

# # ds = AicsCziDataset(
# #     path_csv="/home/gbizi/rotation_2/pytorch_fnet/data/csvs/alpha_tubulin/test.csv",
# #     transform_signal=["fnet.transforms.norm_around_center"],
# #     transform_target=["fnet.transforms.norm_around_center"],
# # )

# # x, y = ds[0]
# # print(x.shape, y.shape, x.min().item(), x.max().item(), y.min().item(), y.max().item())

# # img = AICSImage("/project/amgrp/gbizi/qian_lab/vista/data/alpha_tubulin/3500000781_100X_20170331_r2-Scene-11-P38-D08.czi", reconstruct_mosaic=True)
# # for c in range(img.get_image_data("CZYX", T=0).shape[0]):
# #     v = img.get_image_data("ZYX", C=c, T=0)
# #     print(c, v.min(), v.max(), v.dtype)

# czi = CziReader("/project/amgrp/gbizi/qian_lab/vista/data/alpha_tubulin/3500000781_100X_20170331_r2-Scene-11-P38-D08.czi")
# vol = czi.get_volume(chan=0)  # ZYX for channel 0, T=0 internally
# print(vol.dtype, vol.shape, vol.min(), vol.max()) 

# /home/gbizi/rotation_2/pytorch_fnet/sanity_czifile.py
from fnet.data.czireader import CziReader

path = "/project/amgrp/gbizi/qian_lab/vista/data/alpha_tubulin/3500000781_100X_20170331_r2-Scene-11-P38-D08.czi"
czi = CziReader(path)

for ch in range(7):  # SizeC=7 per your metadata
    vol = czi.get_volume(chan=ch)  # ZYX, T defaults to 0 inside czireader
    print(ch, vol.dtype, vol.shape, vol.min(), vol.max())