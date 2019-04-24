import sys
import os
import json
from Labeller import LabelHelper, PartiallyLabelledDataset


if __name__ == '__main__':
    dataset = PartiallyLabelledDataset()
    dataset.load(sys.argv[1])

    info_path = os.path.join(sys.argv[1], 'info.json')
    if os.path.isfile(info_path):
        with open(info_path, 'r') as fp:
            info = json.load(fp)
    else:
        info = None

    helper = LabelHelper(dataset, info)
    helper.mainloop()
