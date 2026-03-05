🛡️ AI Security: Backdoor Attacks, Detection & Defense (MNIST Case Study)
<p align="center"> <img src="https://img.shields.io/badge/PyTorch-Framework-red?style=for-the-badge"> <img src="https://img.shields.io/badge/MNIST-Dataset-yellow?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"> </p>

📌 Project Overview

This project presents a systematic, end-to-end investigation of backdoor attacks in deep learning systems, focusing on attack construction, detection techniques, and defense strategies using a convolutional neural network trained on the MNIST dataset.

Unlike isolated demonstrations, this repository follows a progressive research-style methodology, implementing multiple attack strategies and evaluating defensive techniques across several experimental stages.

The goal is to demonstrate both offensive and defensive perspectives in AI security, reflecting real-world threats to modern machine learning systems.

📄 Full Technical Report

• PDF: notebooks/reports/Backdoor_Attacks_in_Deep_Learning.pdf

• DOCX: notebooks/reports/Backdoor_Attacks_in_Deep_Learning.docx

The full technical report provides a comprehensive analysis of:

• backdoor attack mechanisms

• detection techniques

• model defense strategies

The report is written in a research-oriented format intended to support:

• academic evaluation

• research portfolio development

• Master's program applications in Artificial Intelligence and Cybersecurity.

🎯 Key Objectives

• Design and implement multiple types of backdoor attacks
• Evaluate attack stealthiness and success rate
• Apply detection techniques using internal activations
• Implement defensive strategies to mitigate backdoor behavior
• Produce clear visualizations and technical reports for each stage

🧠 Model & Dataset

Dataset: MNIST

Model: Simple CNN implemented with PyTorch

Frameworks used:

• PyTorch

• NumPy

• Scikit-learn

• Matplotlib

🧪 Experimental Design (Progressive Levels)

The project is structured as a multi-stage research pipeline.

🔹 Level 1 — Pixel Trigger Backdoor

Static pixel-based trigger embedded in training data.

Purpose:
Establish a baseline backdoor attack.

Metrics:

• Clean Accuracy

• Attack Success Rate (ASR)

Notebook
01_baseline_model.ipynb

Report
Level1_backdoor_report.txt

🔹 Level 2 — Invisible Noise Trigger

Low-amplitude noise trigger designed to be visually imperceptible.

Purpose:
Demonstrate stealth poisoning strategies.

Notebook
08_invisible_noise_trigger.ipynb

Report
Level2_backdoor_report.txt

🔹 Level 3 — Semantic Blur Trigger

Applies semantic transformations (blur-based trigger).

Purpose:
Show that backdoor triggers do not need to be simple pixel patterns.

Notebook
09_level3_semantic_blur_trigger.ipynb

🔹 Level 4 — Adversarial Patch Backdoor (Learned Trigger)

A fully learnable 8×8 adversarial patch.

Patch parameters are optimized jointly with model training.

Outcome:
Near-perfect attack success rate while maintaining high clean accuracy.

Notebook
11_level4_adversarial_patch_trigger.ipynb

Report
Level4_backdoor_report.txt

🔹 Level 5 — Backdoor Detection via Activation Clustering

Hidden layer activations are extracted and analyzed.

Technique:

Principal Component Analysis

K-means Clustering

Purpose:
Separate poisoned samples from clean samples.

Notebook
12_backdoor_detection_activation_clustering.ipynb

Report
Level5_backdoor_detection_report.txt

🔹 Level 6 — Backdoor Defense via Fine-Pruning

Neuron pruning removes neurons responsible for backdoor behavior.

Outcome:

Attack Success Rate significantly reduced

Clean accuracy largely preserved

Notebook
13_backdoor_defense_fine_pruning.ipynb

Report
Level6_backdoor_defense_report.txt

📊 Results Summary
```
Level              Focus       	                     Outcome
1–3	               Backdoor Attacks	                 Increasing stealth and effectiveness
4	                 Learned Adversarial Patch	       ASR ≈ 100% with minimal accuracy loss
5	                 Detection	                       Clear separation of poisoned samples
6	                 Defense	                         Reduced ASR while preserving clean accuracy
```
📈 Experimental Visualization

Example visual outputs generated during experiments include:

• Attack Success Rate comparison

• Clean accuracy comparison

• Activation clustering visualization

Example plots are stored in:
```
figures/
├── asr_comparison.png
├── clean_accuracy.png
└── clustering_visualization.png
```
These visualizations illustrate the relationship between attack strength, stealthiness, and model robustness.

🔍 Key Insights

• Backdoor triggers can remain highly effective without degrading clean accuracy

• Learned adversarial patches exploit gradient-based vulnerabilities in neural networks

• Internal activation patterns provide strong signals for identifying poisoned data

• Fine-pruning provides a practical mitigation strategy but does not guarantee complete removal of backdoors

🔬 Comparison with Existing Research

Backdoor attacks have been widely studied in the Adversarial Machine Learning literature.
```
Research Work	                  Key Idea	                                            Relevance
BadNets (2017)	                Trigger-based poisoning attack	                      foundational backdoor attack
Spectral Signatures (2018)	    Detect poisoned data via feature statistics	          detection approach
Neural Cleanse (2019)	          Reverse engineer trigger patterns	                    backdoor detection
This Project	                  Multi-trigger pipeline with detection and defense	    end-to-end analysis
```
This repository focuses on building a complete experimental pipeline rather than implementing a single attack.

🧩 Repository Structure
```
AI-Security-Backdoor-Detection/
│
├── notebooks/
│   ├── 01_baseline_model.ipynb
│   ├── 08_invisible_noise_trigger.ipynb
│   ├── 09_level3_semantic_blur_trigger.ipynb
│   ├── 11_level4_adversarial_patch_trigger.ipynb
│   ├── 12_backdoor_detection_activation_clustering.ipynb
│   ├── 13_backdoor_defense_fine_pruning.ipynb
│   └── reports/
│
├── figures/
│
├── triggers.py
│
└── README.md
```
⚙️ Reproducibility
Environment

Python 3.10 recommended.

Install dependencies:
```
pip install -r requirements.txt
```
Example dependencies:
```
torch
torchvision
numpy
scikit-learn
matplotlib
jupyter
Running the Experiments
```
Run notebooks sequentially:
```
01_baseline_model.ipynb
08_invisible_noise_trigger.ipynb
09_level3_semantic_blur_trigger.ipynb
11_level4_adversarial_patch_trigger.ipynb
12_backdoor_detection_activation_clustering.ipynb
13_backdoor_defense_fine_pruning.ipynb
```
Expected results:

• Clean Accuracy ≈ 97–98%

• Level 4 ASR ≈ 99–100%

• Post-defense ASR significantly reduced

🧩 System Pipeline

<img width="191" height="1421" alt="backdoor_pipeline drawio" src="https://github.com/user-attachments/assets/6193ebc4-8d02-4bee-9b95-c552ff617f6e" />

This diagram illustrates the full lifecycle of the project, including:

1 Backdoor injection

2 Model training

3 Attack evaluation

4 Detection

5 Defense

🎓 Academic & Career Relevance

This project is designed as a research-oriented portfolio suitable for:

• Master's applications in AI, Cybersecurity, and Machine Learning
• Demonstrating practical understanding of ML security threats
• Showcasing independent technical research capability

🚀 Future Work

Possible extensions include:

• Extending experiments to CIFAR-10 or ImageNet
• Implementing detection methods such as Neural Cleanse
• Evaluating robustness against adaptive attacks
• Exploring certified defenses for backdoor mitigation

📚 References

Gu, T., Dolan-Gavitt, B., & Garg, S. (2017).
BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain.
https://arxiv.org/abs/1708.06733

Tran, B., Li, J., & Madry, A. (2018).
Spectral Signatures in Backdoor Attacks.
https://arxiv.org/abs/1811.00636

Wang, B., et al. (2019).
Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks.

👨‍💻 Author

Phan Hữu Thông (Zack)
Bachelor of Computer Science (Cyber Security)
Griffith University
