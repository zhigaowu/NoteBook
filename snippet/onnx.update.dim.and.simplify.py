import onnx
from onnx.tools import update_model_dims
import onnxsim

def generate_model(batch, width, height):
    input_dims = {
        "input0": [batch, 3, height, width],
    }
    output_dims = {
        "out1": [batch, 1, width, width]
    }
    model = onnx.load("models/dbnet.onnx")
    updated_model = update_model_dims.update_inputs_outputs_dims(model, input_dims, output_dims)
    onnx.checker.check_model(updated_model)  # check onnx model
    simplify_onnx, check = onnxsim.simplify(updated_model)
    onnx.save(simplify_onnx, "models/char_detection_{0}_{1}_{2}.onnx".format(batch, width, height))
