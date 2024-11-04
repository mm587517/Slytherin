# Slytherin

This document delineates the installation process and utilization guidelines for Slytherin, a tool specifically crafted for range analysis within Solidity smart contracts. Slytherin amalgamates the capabilities of the static analysis tool "Slither" with the smart contract fuzzer "Echidna" to identify and address improper usage of binary expressions.


## Installation

To install Slytherin, adhere to the subsequent steps:

1. Confirm the presence of Python on your system.

2. Establish a Python virtual environment through the following command:

```bash
  python3 -m venv myenv
  source myenv/bin/activate
```

3. Install the Slither API within the virtual environment:

```bash
python3 -m pip install slither-analyzer
```

For more information about the Slither API, consult its documentation accessible at https://github.com/crytic/slither.

4. Install the Solidity compiler. Employ solc-select for this purpose.

```bash
pip3 install solc-select
solc-select install 0.7.6
solc-select use 0.7.6
```
In this context, Solidity 0.7.6 is employed for test cases.

5. Ensure Echidna, the smart contract fuzzer, is installed alongside Slither. 
   The simplest way to install it to use `homebrew` (https://brew.sh/). 

   Install echidna:

   `brew install echidna`


   Should issues arise, look at the Echidna codebase at https://github.com/crytic/echidna.

6. Install Loguru. 
```bash
pip3 install loguru
```
## Usage/Examples

For usage let us take a look at the following example. 

```solidity
pragma solidity 0.7.6;

contract Contract {
   
    function example () public pure returns (uint) {
        uint64 a = 12345;
        uint64 b = 1e18;

        uint256 c = a * b;

        return c;
    }

}

```


The line `uint256 c = a * b;` will cause a casting issue. However, this is not picked up by either the Solidty compiler nor Slither. 

Our tool looks for these type of binary operations and generates automatic test cases to determine if they are issue. 

```solidity
pragma solidity 0.7.6;

contract Contract {
   
    function example () public pure returns (uint) {
        uint64 a = 12345;
        uint64 b = 1e18;

        assert (a <= type(uint256).max / b); //slytherin 1
        uint c = a * b;
        
        return c;
    }

}

```

In order to run our tool, we use the following command:
```bash
python3 src/run/main.py --input contracts/example.sol --output output/example.experiment.sol   
```

The input is the name of the file we wish to examine. The output is the same file but we need to add ".experiment" to the file name. 

Our tool runs the fuzzer and tells the developer which case failed. In this case it is `slytherin 1`:

```bash
2024-04-15 19:18:46.925 | DEBUG    | echidna_runner:run_echidna:26 - Sent ESC character signal to Echidna process.
2024-04-15 19:18:46.929 | INFO     | file_modifier:find_and_comment:58 - slytherin 1
================== slytherin 1 ==================
==================================================
example(): failed!💥  
  Call sequence:
    Contract.example()

Traces: 

AssertionFailed(..): passing


Unique instructions: 62
Unique codehashes: 1
Corpus size: 2
Seed: 8287372160903758882
```


## Evaluation

To run the proof of concept:
`python3 src/run/main.py --input contracts/example.sol --output output/example.experiment.sol`

To run the code4rena code:
`python3 src/run/main.py --input contracts/flashloan.sol --output output/flashloan.experiment.sol`