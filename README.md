🌱 Plant Disease Detection (AI Challenger 2018 Baseline)








Baseline solution for the AI Challenger 2018 Crop Disease Detection Competition
Built with PyTorch

⚠️ Disclaimer

This repository is open-sourced for learning and academic communication only.

❌ Do NOT use the dataset for commercial purposes.

📌 If you repost, reference, or interpret this work, please credit the original source.

Thank you for your understanding.

📖 Background

This project is an upgraded version of my previous PyTorch image classification tutorial:

🔗 Mastering Image Classification with PyTorch by Example
http://spytensor.com/index.php/archives/21/

After over two months of study and refinement, I developed this baseline solution for the AI Challenger 2018 Crop Disease Detection Competition.

This project is shared for learning and discussion.

🏆 Competition Information

🌐 Competition Page: https://challenger.ai/competition/pdr2018

💻 Full Repository: https://github.com/spytensor/plants_disease_detection

📘 General Classification Code: https://github.com/spytensor/pytorch-image-classification

📝 Blog: http://spytensor.com/

📊 Results
Evaluation Type	Score
Online Score	0.8805
Offline Score	0.875

Due to randomness in dataset splitting, reproduced results may fluctuate slightly.
Random seeds were controlled as much as possible.

🛠 Features

✅ ResNet50 baseline

✅ Focal Loss support

✅ Cross-validation support

✅ Offline data augmentation

✅ Submission JSON auto-generation

✅ Dataset statistical analysis

🔄 Updates
📅 December 13, 2018

Added updated dataset (Oct 23 release)

Includes:

Training Set

Validation Set

Test Set A

Test Set B

📥 Dataset Download (Baidu Netdisk):
https://pan.baidu.com/s/16f1nQchS-zBtzSWn9Guyyg

Extraction Code: iksk

📅 October 30, 2018

Added data_aug.py for offline data augmentation.

Supported augmentations:

Gaussian Noise

Brightness Adjustment

Horizontal Flip

Vertical Flip

Color Jitter

Contrast Adjustment

Sharpness Adjustment

⚠ If contrast enhancement is used during training, apply it during testing as well for consistency.

📦 Requirements
Python 3.6
PyTorch 0.4.1

⚠ Please keep the PyTorch version consistent to avoid unexpected bugs.

📂 Project Structure (Simplified)
├── main.py
├── config.py
├── move.py
├── data_aug.py
├── data/
│   ├── test/
│   └── temp/
│       ├── images/
│       └── labels/
└── submit/
🧠 Data Processing

Used the officially updated dataset

Performed statistical analysis on class distribution

Removed class 44 and class 45

Merged train + val, then re-split randomly (due to imbalance)

📷 Image Settings

Image size: 650

No tuning performed on image size

🔁 Data Augmentation Used
RandomRotation(30)
RandomHorizontalFlip()
RandomVerticalFlip()
RandomAffine(45)
🤖 Model

Currently tested:

ResNet50

More architectures can be explored if GPU resources allow.

⚙ Hyperparameters

All hyperparameters are defined in:

config.py
🚀 Usage
Step 1 — Prepare Test Data

Copy test images into:

data/test/
Step 2 — Prepare Training & Validation Data

Copy all training and validation images into:

data/temp/images/

Place the two JSON label files into:

data/temp/labels/
Step 3 — Organize Dataset
python move.py
Step 4 — Train Model
python main.py
📤 Submission File

After running the test() function in main.py,
a submission-format JSON file will be generated in:

./submit/
📈 Dataset Distribution

Statistical analysis was conducted for:

Training Set Distribution

Validation Set Distribution

Full Dataset Distribution

(Distribution visualization images were generated during analysis.)

🤝 Contributions

There is significant room for improvement in this codebase.

If you have suggestions or improvements, feel free to open an issue or submit a PR.

📬 Contact

📧 zhuchaojie@buaa.edu.cn
