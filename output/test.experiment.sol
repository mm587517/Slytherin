// SPDX-License-Identifier: GPL-3.0
 
pragma solidity ^0.7.6;
 

contract TestCases {

    function test1() public pure returns (uint64){
        uint64 a = 2;
        uint64 b = 2;
        
assert (a <= type(uint64).max / b); //slytherin 1
// assert (a <= type(uint64).max / b); //slytherin 3
        uint64 c = (a * b);
 
        return c;
    }    

    function test2() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 1e18;
        
// assert (a <= type(uint64).max / b); //slytherin 2
// assert (a <= type(uint64).max / b); //slytherin 4
        uint256 c = a * b;
 
        return c;
    }
    

    
}