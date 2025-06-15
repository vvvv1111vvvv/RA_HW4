import os
import shutil

val_dir = "./tiny-imagenet-200/val"
images_dir = os.path.join(val_dir, "images")
annotations_file = os.path.join(val_dir, "val_annotations.txt")
output_dir = os.path.join(val_dir, "images_split")

# output 디렉토리 생성
os.makedirs(output_dir, exist_ok=True)

# annotations 읽기
with open(annotations_file, "r") as f:
    for line in f:
        parts = line.strip().split('\t')  # 실제 파일은 탭으로 구분되어 있음
        if len(parts) < 2:
            continue
        filename, label = parts[0], parts[1]

        src = os.path.join(images_dir, filename)
        dst_dir = os.path.join(output_dir, label)
        dst = os.path.join(dst_dir, filename)

        os.makedirs(dst_dir, exist_ok=True)

        if os.path.exists(src):
            shutil.move(src, dst)