import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# --- 1. 自动依赖检查与安装 (Auto Dependency Check) ---
def install(package):
    print(f"正在安装依赖库: {package} ...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception as e:
        print(f"安装失败: {e}")
        input("请检查网络或手动安装。按回车键退出...")
        sys.exit(1)

# 尝试导入，如果失败则自动安装
try:
    import numpy as np
    from plyfile import PlyData, PlyElement
except ImportError:
    print("首次运行，正在配置环境...")
    install("numpy")
    install("plyfile")
    import numpy as np
    from plyfile import PlyData, PlyElement

# --- 2. 核心修复逻辑 ---
def get_unique_output_path(original_path):
    """
    生成不冲突的输出路径：
    原名.ply -> 原名_Fixed.ply
    如果存在 -> 原名_Fixed_1.ply -> 原名_Fixed_2.ply
    """
    directory = os.path.dirname(original_path)
    filename = os.path.basename(original_path)
    name, ext = os.path.splitext(filename)
    
    # 基础命名模式
    base_output_name = f"{name}_Fixed{ext}"
    output_path = os.path.join(directory, base_output_name)
    
    counter = 1
    # 循环检查是否存在，直到找到一个空位
    while os.path.exists(output_path):
        output_name = f"{name}_Fixed_{counter}{ext}"
        output_path = os.path.join(directory, output_name)
        counter += 1
        
    return output_path

def fix_ply():
    # 隐藏主窗口
    root = tk.Tk()
    root.withdraw()
    
    print("="*40)
    print("   3DGS PLY Standardizer (248 bytes Fixer)")
    print("="*40)
    print("Waiting for file selection...")
    
    # 文件选择弹窗
    file_path = filedialog.askopenfilename(
        title="Select Non-Standard PLY file (68b/236b)",
        filetypes=[("PLY Files", "*.ply")]
    )

    if not file_path:
        print("未选择文件，操作取消。")
        return

    print(f"\n处理文件: {file_path}")
    
    try:
        # 读取
        plydata = PlyData.read(file_path)
        vertex_data = plydata['vertex'].data
        count = len(vertex_data)
        print(f"粒子数量: {count}")

        # --- 标准 248 字节属性定义 (Standard Schema) ---
        props = [
            ('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
            ('nx', 'f4'), ('ny', 'f4'), ('nz', 'f4'),
            ('f_dc_0', 'f4'), ('f_dc_1', 'f4'), ('f_dc_2', 'f4'),
            ('f_rest_0', 'f4'), ('f_rest_1', 'f4'), ('f_rest_2', 'f4'), ('f_rest_3', 'f4'), ('f_rest_4', 'f4'), ('f_rest_5', 'f4'), ('f_rest_6', 'f4'), ('f_rest_7', 'f4'), ('f_rest_8', 'f4'), ('f_rest_9', 'f4'), ('f_rest_10', 'f4'), ('f_rest_11', 'f4'), ('f_rest_12', 'f4'), ('f_rest_13', 'f4'), ('f_rest_14', 'f4'), ('f_rest_15', 'f4'), ('f_rest_16', 'f4'), ('f_rest_17', 'f4'), ('f_rest_18', 'f4'), ('f_rest_19', 'f4'), ('f_rest_20', 'f4'), ('f_rest_21', 'f4'), ('f_rest_22', 'f4'), ('f_rest_23', 'f4'), ('f_rest_24', 'f4'), ('f_rest_25', 'f4'), ('f_rest_26', 'f4'), ('f_rest_27', 'f4'), ('f_rest_28', 'f4'), ('f_rest_29', 'f4'), ('f_rest_30', 'f4'), ('f_rest_31', 'f4'), ('f_rest_32', 'f4'), ('f_rest_33', 'f4'), ('f_rest_34', 'f4'), ('f_rest_35', 'f4'), ('f_rest_36', 'f4'), ('f_rest_37', 'f4'), ('f_rest_38', 'f4'), ('f_rest_39', 'f4'), ('f_rest_40', 'f4'), ('f_rest_41', 'f4'), ('f_rest_42', 'f4'), ('f_rest_43', 'f4'), ('f_rest_44', 'f4'),
            ('opacity', 'f4'),
            ('scale_0', 'f4'), ('scale_1', 'f4'), ('scale_2', 'f4'),
            ('rot_0', 'f4'), ('rot_1', 'f4'), ('rot_2', 'f4'), ('rot_3', 'f4')
        ]

        # 创建全0数组
        new_data = np.zeros(count, dtype=props)
        names = vertex_data.dtype.names

        # --- 智能搬运数据 ---
        # 1. Position
        new_data['x'] = vertex_data['x']
        new_data['y'] = vertex_data['y']
        new_data['z'] = vertex_data['z']

        # 2. Color (兼容 SH0 和 RGB)
        if 'f_dc_0' in names:
            new_data['f_dc_0'] = vertex_data['f_dc_0']
            new_data['f_dc_1'] = vertex_data['f_dc_1']
            new_data['f_dc_2'] = vertex_data['f_dc_2']
        elif 'red' in names:
            new_data['f_dc_0'] = (vertex_data['red']   / 255.0 - 0.5) / 0.28209479177
            new_data['f_dc_1'] = (vertex_data['green'] / 255.0 - 0.5) / 0.28209479177
            new_data['f_dc_2'] = (vertex_data['blue']  / 255.0 - 0.5) / 0.28209479177

        # 3. Scale
        if 'scale_0' in names:
            new_data['scale_0'] = vertex_data['scale_0']
            new_data['scale_1'] = vertex_data['scale_1']
            new_data['scale_2'] = vertex_data['scale_2']

        # 4. Rotation
        if 'rot_0' in names:
            new_data['rot_0'] = vertex_data['rot_0']
            new_data['rot_1'] = vertex_data['rot_1']
            new_data['rot_2'] = vertex_data['rot_2']
            new_data['rot_3'] = vertex_data['rot_3']

        # 5. Opacity
        if 'opacity' in names:
            new_data['opacity'] = vertex_data['opacity']

        # --- 获取不重复的输出路径 ---
        output_path = get_unique_output_path(file_path)

        # 写入文件
        print(f"正在写入新文件: {output_path} ...")
        el = PlyElement.describe(new_data, 'vertex')
        PlyData([el], text=False).write(output_path)

        print("\n" + "="*40)
        print(f"✅ 成功! (Success)")
        print(f"已保存至: {output_path}")
        print("="*40)
        
        messagebox.showinfo("Success", f"Fix Complete!\nSaved to:\n{output_path}")

    except Exception as e:
        print(f"\n❌ 错误: {e}")
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    fix_ply()