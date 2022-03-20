_base_ = [
    './swin_loveda_tiny.py'
]
model = dict(
    pretrained='pretrain/swin_small_patch4_window7_224_convert.pth',
    backbone=dict(depths=[2, 2, 18, 2]),
    decode_head=dict(in_channels=[96, 192, 384, 768], num_classes=150),
    auxiliary_head=dict(in_channels=384, num_classes=150))