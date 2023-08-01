import torch


def print_device_info():
    for i in range(torch.cuda.device_count()):
        print(i, torch.cuda.get_device_name(i))

if __name__ == '__main__':
    print_device_info()
    