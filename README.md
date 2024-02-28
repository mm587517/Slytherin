# Slytherin

Automatic test case generator to detect invalid casting.

## Installation

1. Make sure you have Python installed on your system.
2. Create a Python virtual environment:

   ```
   $ python3 -m venv myenv
   ```

3. Activate the virtual environment:

   ```
   $ source myenv/bin/activate
   ```

4. Install the Slither API within the virtual environment:

   ```
   $ pip3 install slither-analyzer
   ```

For more information about the Slither API, check [https://github.com/crytic/slither](https://github.com/crytic/slither).

## Usage

Usage is simple. Run the main located in `src/run/main.py`. It requires an input argument, which is a solidity file. Files are located in the "contracts" directory located in the root directory. Here is an example of how to run:

```bash
python3 src/run/main.py --file contracts/test.sol
```

Replace `contracts/test.sol` with the path to your solidity file.

The output will be in the "output" directory. It will consist of a solidity smart contract with assert statements ready for the Echidna fuzzer.
