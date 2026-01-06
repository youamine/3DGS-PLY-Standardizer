# 3DGS PLY Standardizer 🛠️

A lightweight Python tool to standardize 3D Gaussian Splatting (3DGS) PLY files. 

It fixes compatibility issues between AI-generated splats (e.g., from **World Labs**, **Luma AI**) and strict Unity rendering plugins (e.g., **Aras Pranckevicius's UnityGaussianSplatting**).

## 🛑 The Problem
Many AI generation tools export optimized, compact PLY files (e.g., **68 bytes** or **236 bytes** per vertex) to save bandwidth. They often strip out:
- Spherical Harmonics (SH) coefficients (SH0 only).
- Normals.

However, many real-time renderers expect a standard **248-byte** structure (Full SH + Normals + Scale/Rot). Loading these compact files directly often results in crashes or visualization errors (e.g., `PLY vertex size mismatch`).

## ✅ The Solution
This tool reads any non-standard 3DGS PLY file and "pads" the missing data with zeros to create a strictly formatted **248-byte** standard PLY file.

- **Input:** 68b, 236b, or any non-standard PLY.
- **Output:** Standard 248b PLY (Compatible with Unity/Unreal plugins).

## ✨ Features
- **Auto-Dependency Check:** Automatically installs `plyfile` and `numpy` if missing.
- **Safe Mode:** Never overwrites your original files. It creates a new file with `_Fixed` suffix.
- **Batch Script:** One-click execution for Windows users (`Run_Fixer.bat`).

## 🚀 How to Use

### For Windows Users (Easiest)
1. Download this repository.
2. Make sure you have [Python](https://www.python.org/) installed (Check "Add Python to PATH" during installation).
3. Double-click **`Run_Fixer.bat`**.
4. Select your `.ply` file in the popup window.
5. Done! The fixed file will be saved in the same folder.

### For Developers (Command Line)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the script (Make sure the filename matches)
python ply_standardizer.py
