# COCO 2014 Farsi captions 

- Download and unzip COCO [2014 Train/Val annotations](http://images.cocodataset.org/annotations/annotations_trainval2014.zip).
- Move `captions_train2014.json` and `captions_val2014.json` to `captions` directory.
- Unzip `farsi_train.zip` and `farsi_val.zip`.
- Run `farsi_captions.py`.
- The translated json files will be generated in `captions` directory:
  - `captions_train2014_farsi.json`
  - `captions_val2014_farsi.json`.

**Note**:
Some translated captions contain `*` or English words.
For a more accurate result, it is recommended to remove those samples from training and validation sets.
An ID list of these samples will be printed out when you run `farsi_captions.py`.