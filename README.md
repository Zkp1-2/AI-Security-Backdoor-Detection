🛡️ AI Security: Backdoor Attacks, Detection & Defense (MNIST Case Study)

<p align="center"> <img src="https://img.shields.io/badge/PyTorch-Framework-red?style=for-the-badge"> <img src="https://img.shields.io/badge/MNIST-Dataset-yellow?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"> </p>
📌 Project Overview

This project is a systematic, end-to-end study of backdoor attacks in deep learning systems, focusing on attack construction, detection techniques, and defense strategies using a CNN trained on the MNIST dataset.

The goal is to demonstrate both offensive and defensive understanding of AI security, following a progressive, research-style methodology rather than a single isolated experiment.


📄 **Full Technical Report**

- [PDF] reports/Backdoor_Attacks_in_Deep_Learning.pdf  
- [DOCX] reports/Backdoor_Attacks_in_Deep_Learning.docx  

The full technical report provides a comprehensive analysis of backdoor attacks,
detection techniques, and defense strategies implemented in this project.
It is written in a research-oriented technical report format and is intended
to support academic evaluation and Master's-level applications.

🎯 Key Objectives

Design and implement multiple types of backdoor attacks

Evaluate attack stealthiness and success rates

Apply detection techniques based on internal activations

Implement defensive strategies to mitigate backdoor behavior

Produce clear visualizations and technical reports for each stage


🧠 Model & Dataset

Dataset: MNIST

Model: SimpleCNN (PyTorch)

Frameworks: PyTorch, NumPy, Scikit-learn, Matplotlib

🧪 Project Structure (Progressive Levels)

🔹 Level 1 – Pixel Trigger Backdoor

Static pixel-based trigger embedded in training data

Evaluates baseline backdoor behavior

Metrics: Clean Accuracy vs Attack Success Rate (ASR)

📁 Notebook: 01_baseline_model.ipynb

📄 Report: Level1_backdoor_report.txt


🔹 Level 2 – Invisible Noise Trigger

Low-amplitude noise trigger designed to be visually imperceptible

Demonstrates stealthy poisoning strategies

📁 Notebook: 08_invisible_noise_trigger.ipynb

📄 Report: Level2_backdoor_report.txt


🔹 Level 3 – Semantic Blur Trigger

Semantic transformation (blur-based trigger)

Shows non-pixel-aligned backdoor vulnerabilities

📁 Notebook: 09_level3_semantic_blur_trigger.ipynb


🔹 Level 4 – Adversarial Patch Backdoor (Learned Trigger)

Fully learnable 8×8 adversarial patch

Patch optimized jointly with model training

Achieves near-perfect ASR with minimal impact on clean accuracy

📁 Notebook: 11_level4_adversarial_patch_trigger.ipynb

📄 Report: Level4_backdoor_report.txt


🔹 Level 5 – Backdoor Detection via Activation Clustering

Extracts internal activations from hidden layers

Applies PCA + KMeans clustering

Successfully separates poisoned samples from clean data

📁 Notebook: 12_backdoor_detection_activation_clustering.ipynb

📄 Report: Level5_backdoor_detection_report.txt


🔹 Level 6 – Backdoor Defense via Fine-Pruning

Applies neuron pruning to remove backdoor-related activations

Recovers clean accuracy while suppressing attack success

Demonstrates practical model sanitization

📁 Notebook: 13_backdoor_defense_fine_pruning.ipynb

📄 Report: Level6_backdoor_defense_report.txt


📊 Results Summary
```
Level          Focus         	           Outcome
1–3	           Backdoor Attacks	         Increasing stealth & effectiveness
4	             Learned Patch	           ASR ≈ 100%, high stealth
5	             Detection	               Clear poisoned vs clean separation
6              Defense	                 ASR reduced, clean accuracy recovered
```

🔍 Key Insights

Backdoor triggers can remain highly effective without degrading clean accuracy

Learned adversarial patches exploit gradient-based vulnerabilities

Internal activation patterns provide strong signals for detection

Fine-pruning is a practical and lightweight defense, but not foolproof


🧩 Repository Structure
```
AI-Security-Backdoor-Detection/
├── notebooks/
│   ├── 01_baseline_model.ipynb
│   ├── 08_invisible_noise_trigger.ipynb
│   ├── 09_level3_semantic_blur_trigger.ipynb
│   ├── 11_level4_adversarial_patch_trigger.ipynb
│   ├── 12_backdoor_detection_activation_clustering.ipynb
│   ├── 13_backdoor_defense_fine_pruning.ipynb
│   └── reports/
├── triggers.py
└── README.md
```
🧩 System Pipeline

<img width="191" height="1421" alt="backdoor_pipeline drawio" src="https://github.com/user-attachments/assets/6193ebc4-8d02-4bee-9b95-c552ff617f6e" />

This diagram illustrates the complete lifecycle of the project,
from backdoor injection to detection and defense, following
a research-oriented AI security workflow.

🎓 Academic & Career Relevance

This project is designed as a research-oriented portfolio suitable for:

Master’s applications in AI, Cybersecurity, Machine Learning

Demonstrating hands-on understanding of ML security threats

Showcasing the ability to conduct independent technical research


🚀 Future Work

Extend to CIFAR-10 or ImageNet

Compare with Neural Cleanse and Spectral Signatures

Evaluate robustness under adaptive attacks

Explore certified defenses


📬 Author

Phan Hữu Thông (Zack)
Bachelor of Computer Science (Cyber Security)
Griffith University
