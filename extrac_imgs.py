# _*_ Author:JackZhang9
# _*_ Time:20230310 15:07
import os
import cv2

def imgs_save(path,imgs_name_list,n):
    '''
    用opencv把图片保存到新文件夹
    :param path:
    :param imgs_name_list:
    :return:
    '''
    path_sub=os.path.split(path)[0] # 将文件夹分成两部分，取前面部分
    f_dir=os.path.join(path_sub,'LG_imgs') # 组成新的文件夹，保存图片
    # print(f_dir)
    if not os.path.exists(f_dir):
        os.mkdir(f_dir) # 创建文件夹
    for idx,img_name in enumerate(imgs_name_list):  # 根据文件名一张张读取
        print(idx,img_name)
        img_path=os.path.join(path,img_name)
        new_path=os.path.join(f_dir,img_name)
        # print(img_path)
        if idx<n:
            img=cv2.imread(img_path)
            cv2.imwrite(new_path,img)
        else:
            break
    return 1


def read_dir_img_name(path):
    '''
    输入一个图片路径，
    返回要提取的图片路径列表
    :param path:
    :return:
    '''
    if not os.path.exists(path):
        raise Exception('路径错误!')
    imgs_name_list=os.listdir(path) # 返回文件夹下所有图片名列表
    imgs_nums=len(imgs_name_list) # 图片个数 7305

    # print(imgs_nums)

    return imgs_name_list




if __name__ == '__main__':
    path=r'F:\sichuan\2023-03-10\error_imgs_show\4LG'
    imgs_name_list=read_dir_img_name(path)
    n=100  # 要保存的数量
    imgs_save(path,imgs_name_list,n)