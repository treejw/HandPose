import os
import sys


def get_video_path(path='./Poses', video_format='avi'):
    all_video_list = list()
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(path)):
        if i == 0 and len(filenames) == 0:
            continue
        video_list = [os.path.join(dirpath, file) for file in filenames if file[-3:] == video_format]
        if len(video_list) == 0:
            continue
        all_video_list.extend(video_list)
    return all_video_list


def remove_all_videos(path_list):
    while True:
        option = input('\n * Total {} videos found. Press \'y\' to check the list. (y/n)\n'.format(len(path_list)))
        if option == 'y':
            print()
            print(*path_list, sep='\n')
            break
        elif option == 'n':
            break
        else:
            print('please press \'y\' or \'n\'')

    while True:
        option2 = input('\n * Are you sure you want to delete all? (y/n)\n')
        if option2 == 'y':
            [os.remove(file) for file in path_list]
            sys.exit()
        elif option2 == 'n':
            sys.exit()
        else:
            print('please press \'y\' or \'n\'')


def main():
    video_path_list = get_video_path(path='./Poses', video_format='avi')
    remove_all_videos(video_path_list)


if __name__ == '__main__':
    main()
