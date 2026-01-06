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
- **Batch Script:** One-click execution for Windows users (`Run_Standardizer.bat`).

## 🚀 How to Use

### For Windows Users (Easiest)
1. Download this repository.
2. Make sure you have [Python](https://www.python.org/) installed (Check "Add Python to PATH" during installation).
3. Double-click **`Run_Standardizer.bat`**.
4. Select your `.ply` file in the popup window.
5. Done! The fixed file will be saved in the same folder.

### For Developers (Command Line)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the script (Make sure the filename matches)
python ply_standardizer.py
```

## 🛠️ Requirements
- Python 3.x
- numpy
- plyfile

## 📄 License
This project is licensed under the MIT License.

## 📬 Contact 

[![Email](https://img.shields.io/badge/Email-2410569510@qq.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:2410569510@qq.com)
[![WeChat](https://img.shields.io/badge/WeChat-youamine1-07C160?style=flat-square&logo=wechat&logoColor=white)](#)
[![Bilibili](https://img.shields.io/badge/Bilibili-游啊麦-FB7299?style=flat-square&logo=bilibili&logoColor=white)](https://space.bilibili.com/30253907)
[![Website](https://img.shields.io/badge/Portfolio-youamine.art-4285F4?style=flat-square&logo=google-chrome&logoColor=white)](https://youamine.art)

*(Feel free to reach out for collaboration or questions!)*


# 3DGS PLY 标准化工具 (3DGS PLY Standardizer) 🛠️

这是一个轻量级的 Python 工具，用于标准化 3D Gaussian Splatting (3DGS) 的 PLY 文件格式。

它主要解决 **World Labs**、**Luma AI** 等 AI 生成平台导出的“压缩版”文件，与 **Unity** 主流渲染插件（如 **Aras Pranckevicius's UnityGaussianSplatting**）不兼容的问题。

## 🛑 问题背景 (The Problem)
许多 AI 3D 生成工具为了优化文件体积和带宽，导出的 PLY 文件通常是非常紧凑的（例如每个顶点仅 **68 字节** 或 **236 字节**）。为了做到这一点，它们通常剔除了：
- 高阶球谐系数 (Spherical Harmonics)，只保留了基础颜色 (SH0)。
- 法线数据 (Normals)。

然而，许多实时渲染器（尤其是 Unity/Unreal 的插件）严格要求输入的 PLY 文件必须是标准的 **248 字节** 结构（包含完整 SH + 法线 + 缩放/旋转）。直接导入这些“缩水”的文件通常会导致编辑器报错（例如 `PLY vertex size mismatch`）甚至崩溃。

## ✅ 解决方案 (The Solution)
本工具会自动读取任意非标准的 3DGS PLY 文件，并自动用“0”补全所有缺失的数据字段，重新封装成严格符合工业标准的 **248 字节** PLY 文件。

- **输入支持：** 68b, 236b 或其他任何非标准 PLY 文件。
- **输出结果：** 标准 248b PLY 文件（完美兼容 Unity/Unreal 插件）。

## ✨ 功能特性
- **📦 自动依赖管理：** 脚本会自动检测并安装所需的 Python 库（`plyfile`, `numpy`），无需手动配置环境。
- **🛡️ 安全防覆盖：** 绝不覆盖原始文件。修复后的文件会自动添加 `_Fixed` 后缀（如 `scene_Fixed.ply`）。
- **⚡ Windows 一键运行：** 提供 `.bat` 批处理脚本，双击即可弹出文件选择窗口，无需懂命令行。

## 🚀 使用方法

### Windows 用户 (推荐)
1. 下载或 Clone 本仓库。
2. 确保电脑已安装 [Python](https://www.python.org/) (**注意：** 安装时务必勾选 **"Add Python to PATH"**)。
3. 双击运行 **`Run_Standardizer.bat`**。
4. 在弹出的窗口中选择你需要修复的 `.ply` 文件。
5. 完成！修复后的文件将保存在原文件同一目录下。

### 开发者 / 命令行用户
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行脚本 (请确保文件名与脚本一致)
python ply_standardizer.py
```

## 🛠️ 运行环境
- Python 3.x
- numpy
- plyfile

## 📄 开源协议
本项目采用 MIT 协议开源。

## 📬 联系我 

[![邮箱](https://img.shields.io/badge/Email-2410569510@qq.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:2410569510@qq.com)
[![微信](https://img.shields.io/badge/WeChat-youamine1-07C160?style=flat-square&logo=wechat&logoColor=white)](#)
[![B站](https://img.shields.io/badge/Bilibili-游啊麦-FB7299?style=flat-square&logo=bilibili&logoColor=white)](https://space.bilibili.com/30253907)
[![个人网站](https://img.shields.io/badge/Portfolio-youamine.art-4285F4?style=flat-square&logo=google-chrome&logoColor=white)](https://youamine.art)

*(有任何问题，随时联系我!)*
