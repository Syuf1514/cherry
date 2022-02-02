
import torch


def train():
    arr = torch.randn(1, device='cuda')
    print(arr)


if __name__ == '__main__':
    train()
