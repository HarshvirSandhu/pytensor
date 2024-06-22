import torch

from pytensor.link.pytorch.dispatch.basic import pytorch_funcify
from pytensor.tensor.extra_ops import CumOp


@pytorch_funcify.register(CumOp)
def pytorch_funcify_Cumop(op, **kwargs):
    dim = op.axis
    mode = op.mode

    def cumop(x, dim=dim):
        if dim is None:
            x = x.reshape(-1)
            dim = 0
        if mode == "add":
            return torch.cumsum(x, dim=dim)
        else:
            return torch.cumprod(x, dim=dim)

    return cumop
