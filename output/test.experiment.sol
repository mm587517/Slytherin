pragma solidity 0.8.2;



contract Flaw {
    function flaw() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 1e18;

        assert (a <= type(uint64).max / b); //slytherin
        assert (a <= type(uint64).max + b); //slytherin
        assert ((a * b) <= type(uint64).max - (a - b)); //slytherin
        uint128 x = ((a*b) +(a-b));

        assert (x <= type(uint128).max - a); //slytherin
        uint128 y = x + a; 

        return x;
    }
}