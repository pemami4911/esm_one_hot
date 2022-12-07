# ESM with one-hot encoded proteins

Read the original README [here](https://github.com/facebookresearch/esm/blob/main/README.md).

Supports ESM2. 

## Installation

```bash
$ git clone git@github.com:pemami4911/esm_one_hot.git
$ cd esm_one_hot/
$ pip install -e .
```

Then, access the package via
```python
import esm_one_hot
```
I changed the package name from `esm` to `esm_one_hot` to allow for both the original and modified code bases to be installed.


## (Not necessarily complete) Summary of Modifications

* `data.py`
  * Added the `OneHotBatchConverter` so the returned sequence tokens are one-hot encoded.
  * Modified `Alphabet` by adding the `use_one_hot` argument, which, when set, indicates the use of `OneHotBatchConverter`. Required modifying `get_batch_converter()` and `from_architecture()` methods.
* `modules.py`
  * Added a `OneHotEmbedding` nn.Module sub-class. Acts as 1-1 replacement for `nn.Embedding`, but does a matrix multiply on one-hot encoded inputs.
  * Modified `LearnedPositionalEmbedding` to expect the `tokens` argument to be one-hot encoded.
* `model.py` 
  * Modified the `forward()` method of `ProteinBertModel` to expect the `tokens` argument to be one-hot encoded. Changed padding and mask generation code to work with one-hot encoded sequences.
