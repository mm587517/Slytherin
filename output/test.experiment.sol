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

