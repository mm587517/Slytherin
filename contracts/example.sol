pragma solidity 0.7.6;

contract Contract {
   
    function example () public pure returns (uint) {
        uint64 a = 12345;
        uint64 b = 1e18;

        uint64 c = a * b;

        return c;
    }

}

