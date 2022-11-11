# BDD2YOLO

A script for converting the [Berkeley Deep Drive](https://www.bdd100k.com/) dataset's labels to YOLO format.
<br>Usage for a single json file: `python bdd2yolo.py --bdd_file <relative-path-to-label-json> --yolo_dir <relative-path-to-output-folder>`

Concrete example: `python bdd2yolo.py --bdd_file data/bdd100k_labels_images_train.json --yolo_dir data/labels_yolo/train`
