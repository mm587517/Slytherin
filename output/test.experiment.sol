pragma solidity 0.8.2;

contract Flaw {
    function flaw() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 1e18;

        uint128 x = uint128(a) + b;

        uint128 y = x + a; 

        return x;
    }
}