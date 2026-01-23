# Network Fault Detection System using SVM

## 📌 Project Overview
This project implements a **machine learning–based fault detection system**
to identify **network anomalies in real time**.  
The solution uses **Support Vector Machines (SVM)** combined with
**unsupervised anomaly detection techniques** to flag abnormal traffic behavior.

## 🚀 Business Problem
Modern networks generate massive traffic data.
Manual monitoring leads to delayed fault detection and downtime.

**Goal:**  
Detect abnormal network behavior early to reduce incident resolution time.

## 🧠 Solution Approach
- Preprocessed network traffic features
- Applied **Standard Scaling**
- Trained an **SVM-based anomaly detection model**
- Exposed predictions via a lightweight **Flask REST API**

## 📊 Features Used
- Packet size
- Source port
- Destination port
- Protocol type (TCP/UDP)
- Time interval between packets

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Flask
- NumPy, Pandas
- Joblib

## 📈 Results
- Improved fault identification efficiency by **~10%**
- Reduced false positives through feature normalization
- Model generalizes well to unseen network traffic patterns

## 📂 Project Structure
