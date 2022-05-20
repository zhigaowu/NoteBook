import torch
import onnx
import onnxsim


def convert_torch_to_onnx(pth_weights, prefix, batch, width, height, device):
    dummy_input = torch.randn(batch, 3, height, width, requires_grad=True).to(device)
    onnx_file = "onnx/{0}_{1}_{3}_{2}.onnx".format(prefix, batch, height, width)
    torch.onnx.export(pth_weights,  # model being run
                      dummy_input,  # model input (or a tuple for multiple inputs)
                      onnx_file,  # where to save the model
                      export_params=True,  # store the trained parameter weights inside the model file
                      opset_version=11,  # the ONNX version to export the model to
                      do_constant_folding=True,  # whether to execute constant folding for optimization
                      input_names=['input'],  # the model's input names
                      output_names=['output'],  # the model's output names
                      dynamic_axes=None)

    onnx_weights = onnx.load(onnx_file)
    simplify_onnx_weights, check = onnxsim.simplify(onnx_weights)
    onnx.save(simplify_onnx_weights, "onnx/{0}_{1}_{3}_{2}_simplified.onnx".format(prefix, batch, height, width))
