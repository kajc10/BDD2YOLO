import os
import json
import argparse
from tqdm import tqdm


def main(args):
    bdd_file = args.bdd_file
    assert os.path.isfile(bdd_file), 'BDD input json does not exist'

    yolo_dir = args.yolo_dir
    os.makedirs(yolo_dir, exist_ok=True)

    print(f'Processing {bdd_file}')
    print(f'Output folder: {yolo_dir}')

    width = 1280
    height = 720

    # based on : https://github.com/ucbdrive/bdd100k/blob/master/doc/format.md
    categories = {
        'bike': 0,
        'bus': 1,
        'car': 2,
        'motor': 3,
        'person': 4,
        'rider': 5,
        'traffic light': 6,
        'traffic sign': 7,
        'train': 8,
        'truck': 9
    }

    ignore_categories = ["drivable area", "lane"]  # no 2d boxes for these categories

    with open(bdd_file) as f:
        data = json.load(f)
        for image in tqdm(data[:]):
            output = yolo_dir + '/' + str(image['name'][:-4]) + ".txt"
            with open(output, 'w') as o:
                for obj in image['labels']:
                    if obj["category"] not in ignore_categories:
                        # print(obj)
                        class_id = categories[obj['category']]
                        x1 = obj['box2d']['x1']
                        y1 = obj['box2d']['y1']
                        x2 = obj['box2d']['x2']
                        y2 = obj['box2d']['y2']

                        x = ((x1 + x2) / 2.0) / width
                        y = ((y1 + y2) / 2.0) / height
                        w = (x2 - x1) / width
                        h = (y2 - y1) / height

                        o.write(f'{class_id} {x} {y} {w} {h}\n')
            # print(f'{output} processed.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--bdd_file', help='path of the bbd json file',
                        default='../data/bdd100k_labels_images_train.json', required=True)
    parser.add_argument('--yolo_dir', help='directory where yolo labels should be generated',
                        default='../data/labels_yolo/train', required=True)
    args = parser.parse_args()

    main(args)

