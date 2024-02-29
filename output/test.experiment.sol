pragma solidity 0.8.2;

contract Flaw {
    function flaw() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 1e18;

        assert (a <= type(uint64).max - b); //slytherin 1
        uint128 x = a + b;

        assert (x <= type(uint128).max - a); //slytherin 2
        uint128 y = x + a; 

        return x;
    }
}