🔐 AI Model Poisoning & Backdoor Detection

A research project on adversarial poisoning attacks, stealth triggers, and model evaluation.

<p align="center"> <img src="https://img.shields.io/badge/PyTorch-Framework-red?style=for-the-badge"> <img src="https://img.shields.io/badge/MNIST-Dataset-yellow?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"> </p>
📌 Overview

This project explores backdoor attacks in deep learning models, where an attacker injects poisoned training samples containing a hidden trigger.
When the model is later exposed to this trigger, it misclassifies the input into the attacker’s target label.

Your final implementation includes:

✔️ Level 1 backdoor

✔️ Level 2 blended trigger upgrade

✔️ Poisoning ratios

✔️ Model training pipeline

✔️ Attack Success Rate (ASR) & Clean Accuracy evaluation

✔️ Auto-generated backdoor report

✔️ Saved backdoor model (upgraded_backdoor_cnn.pth)

🧠 Key Concepts
🔸 What is a Backdoor Attack?

A backdoor attack poisons a subset of the training dataset so that the model learns to associate a hidden trigger with a specific class.

🔸 Blended Trigger (Level 2 Upgrade)

Instead of a visible patch, the trigger is blended into the image:

blended = (1 - α) * img + α * trigger


This makes the attack more stealthy and harder to detect.

🧪 Experimental Results (α = 0.35)
Poison Ratio	Clean Accuracy	ASR
0.01	97.86%	9.63%
0.03	97.99%	10.03%
0.05	99.00%	10.91%
0.10	98.31%	9.63%
0.15	97.95%	10.22%
🔍 Summary

Best Poison Ratio: 0.15

Max ASR: 10.91%

Accuracy Drop: extremely low (~0.017)

🧩 Project Structure
```
AI-Security-Backdoor-Detection/
│── notebooks/
│   ├── 06_trigger_upgrade.ipynb
│   ├── 07_report_generation.ipynb
│   ├── data/
│   │   └── MNIST/
│   └── reports/
│       └── backdoor_report.txt
│
│── upgraded_backdoor_cnn.pth
│── README.md
│── .gitignore
```

🚀 How to Run the Project
1️⃣ Install dependencies
pip install torch torchvision matplotlib numpy

2️⃣ Train backdoor model (Level 2)

Run:
```
notebooks/06_trigger_upgrade.ipynb
```
3️⃣ Evaluate + generate report

Run:
```
notebooks/07_report_generation.ipynb

```
The final report will be saved automatically to:
```
/notebooks/reports/backdoor_report.txt
```
🎨 Visualization Example
Original	Blended Trigger (α = 0.35)
<img src="notebooks/images/original.png" width="130">	<img src="notebooks/images/blended.png" width="130">
🤝 Author

Phan Hữu Thông (Zack)
Cyber Security — Griffith University
GitHub: https://github.com/Zkp1-2

⭐ Enjoy the project?

Please consider starring ⭐ the repository — it helps a lot!
