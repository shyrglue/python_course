import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
import time
import torchvision.transforms as transforms # 数据转换
import torchvision.datasets as datasets     # 数据下载
from torch.utils.data import DataLoader     # 数据加载
import numpy as np
import random
# 深度神经网络
import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn import functional as F
from matplotlib import pyplot as plt


# 定义不同结构的模型
class ShallowCNN(nn.Module):
    """1 conv layer + 1 fc layer"""
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32*28*28, 10)
    def forward(self, x):
        x = F.relu(self.conv1(x))
        size = x.size(1) * x.size(2) * x.size(3)
        x = x.view(-1, size)
        x = self.fc1(x)
        return x


class MediumCNN(nn.Module):
    """2 conv layers + 1 fc layer"""
    def __init__(self, use_pool=True):
        super().__init__()
        self.use_pool = use_pool
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64*28*28, 10)
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        size = x.size(1) * x.size(2) * x.size(3)
        x = x.view(-1, size)
        x = self.fc1(x)
        return x


class DeepCNN(nn.Module):
    """3 conv layers + 1 fc layer"""
    def __init__(self, use_pool=True):
        super().__init__()
        self.use_pool = use_pool
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(128*28*28, 10)
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        size = x.size(1) * x.size(2) * x.size(3)
        x = x.view(-1, size)
        x = self.fc1(x)
        return x


"""train_loss and test_accuracy"""
def cnn_mnist_train(model, name, train, test, batch_size, num_epochs, device):
    print(f"\nTraining {name}...")
    train_loader = DataLoader(train, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test, batch_size=batch_size, shuffle=False)
    # 优化器
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    # 交叉熵损失函数
    criterion = nn.CrossEntropyLoss()

    train_losses = []
    test_losses = []
    test_accs = []
    all_time = time.time()
    for epoch in range(num_epochs):
        start_time = time.time()
        model.train()
        total_train_loss = 0.0
        total_samples = 0
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            total_train_loss += loss.item() * data.size(0)  # mean*每个批次的个数
            total_samples += data.size(0)  # 累加样本数
        avg_train_loss = total_train_loss / total_samples
        # 测试集验证
        model.eval()
        with torch.no_grad():
            correct = 0
            total_samples = 0
            total_test_loss = 0.0
            total = 0
            for data, target in test_loader:
                data, target = data.to(device), target.to(device)
                output = model(data)
                loss = criterion(output, target)
                total_test_loss += loss.item() * data.size(0)
                total_samples += data.size(0)
                _, predicted = torch.max(output.data, 1)
                total += target.size(0)  # total个数，所有的test_loader求和
                correct += (predicted == target).sum().item()
            avg_test_loss = total_test_loss / total_samples
        end_time = time.time()
        test_acc = 100 * correct / total
        print(f'Epoch:{epoch + 1}/{num_epochs} | '
                f'Train-Loss: {avg_train_loss:.4f} | '
                f'Test-Loss: {avg_test_loss:.4f} | '
                f'Test-Accuracy: {test_acc:.2f}% | '
                f'Time: {end_time - start_time:.2f}s | All_Time: {end_time - all_time:.2f}s' )
        train_losses.append(avg_train_loss)
        test_losses.append(avg_test_loss)
        test_accs.append(test_acc)
        # 判断跳出
        #if avg_train_loss < 0.1 or test_acc >= 95:
        #    break

    return train_losses, test_losses, test_accs

# 绘图函数
def cnn_minst_plot(train_loss, test_loss, test_acc, name):
    plt.figure(figsize=(12, 6),dpi=100)

    plt.subplot(1, 2, 1)
    plt.plot(train_loss, label=f"Training-loss",color='orange',linestyle='-')
    plt.plot(test_loss, label=f"Test-loss",color='green',linestyle='-')

    plt.title(f'{name}-Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(test_acc, label=f"Test-acc",color='red')
    plt.title(f'{name}-Test-Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    plt.show()

# 设定随机种子
def set_seed(seed=42):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True  # 确保CUDA卷积操作确定性
    torch.backends.cudnn.benchmark = False     # 关闭优化（可能牺牲速度）



if __name__ == "__main__":
    set_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("device:", device)
    # 常用内置数据集，手写数字识别
    transform = transforms.Compose([
        transforms.ToTensor(),  # 将图像转换为Tensor
        transforms.Normalize((0.1307,), (0.3081,))  # MNIST数据的均值和标准差
    ])
    mnist_train = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    mnist_test = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    # 实验设置
    num_epochs = 5
    batch_size = 16
    model = ShallowCNN().to(device)
    name = 'SCNN'
    train_losses, test_losses, test_accs = cnn_mnist_train(model, name, mnist_train, mnist_test, batch_size, num_epochs, device)
    cnn_minst_plot(train_losses, test_losses, test_accs, name)