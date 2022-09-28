import numpy as np


def Link_Transformation(last_i, i, a_list, alpha_list, d_list, theta_list):
    """
    function：坐标系{i-1}到坐标系{i}的转换矩阵
    tips：这里的last_i指的是i-1
    """
    i = i  # 下面使用的i-1表示列表的第i-1个数，注意同DH参数里的i-1区别
    T_martix = np.mat(np.zeros((4, 4)))

    T_martix[0, 0] = np.cos(theta_list[i - 1])
    T_martix[0, 1] = -1 * np.sin(theta_list[i - 1])
    T_martix[0, 2] = 0
    T_martix[0, 3] = a_list[i - 1]

    T_martix[1, 0] = np.sin(theta_list[i - 1]) * np.cos(alpha_list[i - 1])
    T_martix[1, 1] = np.cos(theta_list[i - 1]) * np.cos(alpha_list[i - 1])
    T_martix[1, 2] = -1 * np.sin(alpha_list[i - 1])
    T_martix[1, 3] = -1 * np.sin(alpha_list[i - 1]) * d_list[i - 1]

    T_martix[2, 0] = np.sin(theta_list[i - 1]) * np.sin(alpha_list[i - 1])
    T_martix[2, 1] = np.cos(theta_list[i - 1]) * np.sin(alpha_list[i - 1])
    T_martix[2, 2] = np.cos(alpha_list[i - 1])
    T_martix[2, 3] = np.cos(alpha_list[i - 1]) * d_list[i - 1]

    T_martix[3, 0] = 0
    T_martix[3, 1] = 0
    T_martix[3, 2] = 0
    T_martix[3, 3] = 1

    return T_martix


if __name__ == "__main__":
    # 初始化参数（DH参数）
    a_list = [0, 0, 140, 100, 0, 0]
    alpha_list = [0, np.pi / 2, 0, 0, np.pi / 2, np.pi / 2]
    d_list = [180, 0, 0, 90, 80, 60]
    theta_list = [0, np.pi / 2, 0, np.pi / 2, -1 * np.pi / 2, 0]  # 输入想要转动的角度（此处设置转动的角度在转动后即达到机械臂伸直状态）

    # 例：T_0_1表示坐标系{0}到坐标系{1}的转换矩阵
    T_0_1 = Link_Transformation(0, 1, a_list, alpha_list, d_list, theta_list)
    T_1_2 = Link_Transformation(1, 2, a_list, alpha_list, d_list, theta_list)
    T_2_3 = Link_Transformation(2, 3, a_list, alpha_list, d_list, theta_list)
    T_3_4 = Link_Transformation(3, 4, a_list, alpha_list, d_list, theta_list)
    T_4_5 = Link_Transformation(4, 5, a_list, alpha_list, d_list, theta_list)
    T_5_6 = Link_Transformation(5, 6, a_list, alpha_list, d_list, theta_list)

    T_0_6 = T_0_1 * T_1_2 * T_2_3 * T_3_4 * T_4_5 * T_5_6
    print(T_0_6)