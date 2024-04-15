pragma solidity 0.7.6;

contract Contract {
   
    function example () public pure returns (uint) {
        uint64 a = 12345;
        uint64 b = 1e18;

        uint256 c = a * b;

        return c;
    }

}

