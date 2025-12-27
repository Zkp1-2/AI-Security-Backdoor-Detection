import torch
import torch.nn.functional as F

# ============================
# LEVEL 1 — Pixel Trigger
# ============================

def add_pixel_trigger(img):
    """Thêm trigger 3 pixel góc phải dưới"""
    img = img.clone()
    img[:, 26:29, 26:29] = 1.0  # 3×3 white square
    return img


# ============================
# LEVEL 2 — Invisible Noise Trigger
# ============================

def add_invisible_noise_trigger(img, eps=0.15):
    """Thêm noise nhẹ khó nhìn"""
    noise = torch.rand_like(img) * eps
    return torch.clamp(img + noise, 0, 1)


# ============================
# LEVEL 3 — Gaussian Blur Patch Trigger
# ============================

def gaussian_kernel(kernel_size=5, sigma=1.0, device="cpu"):
    coords = torch.arange(kernel_size).float() - kernel_size // 2
    g = torch.exp(-(coords**2) / (2 * sigma**2))
    kernel = (g[:, None] * g[None, :])
    kernel = kernel / kernel.sum()
    return kernel.view(1, 1, kernel_size, kernel_size).to(device)


def semantic_blur_trigger(img):
    """Blur patch 6×6 góc phải dưới"""
    img = img.clone()

    if img.dim() == 2:
        img = img.unsqueeze(0)

    assert img.shape == (1, 28, 28), f"Invalid shape: {img.shape}"

    # Gaussian kernel
    kern = gaussian_kernel(kernel_size=5, sigma=1.0)

    patch = img[:, 22:28, 22:28]             # (1, 6, 6)
    patch = patch.unsqueeze(0)               # (1,1,6,6)

    blurred = F.conv2d(patch, kern, padding=2)
    blurred = blurred.squeeze(0)             # (1,6,6)

    img[:, 22:28, 22:28] = blurred
    return img
