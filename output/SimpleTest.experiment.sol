// SPDX-License-Identifier: GPL-3.0
 
pragma solidity ^0.7.6;
 

contract SimpleTest {

    function test01() public pure returns (uint64){
        uint64 a = 2;
        uint64 b = 2;
        
// assert (a <= type(uint64).max / b); //slytherin 1
        uint64 x = (a * b);
 
        return x;
    }

      function test02() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 1e18;
        
assert (a <= type(uint64).max / b); //slytherin 2
        uint256 x = a * b;
 
        return x;
    }
    

    function test03() public pure returns (uint64){
        uint64 a = type(uint64).max;
        uint64 b = type(uint64).max;
        
// assert (a <= type(uint64).max - b); //slytherin 3
        uint64 x = a + b;
 
        return x;
    }

    function test04() public pure returns (uint128){
        uint64 a = type(uint64).max;
        uint64 b = type(uint64).max;
        
// assert (a <= type(uint64).max - b); //slytherin 4
        uint128 x = a + b;
 
        return x;
    }


    function test05() public pure returns (uint128){
        uint64 a = type(uint64).max;
        uint64 b = type(uint64).max;
        
// assert (a <= type(uint64).max / b); //slytherin 5
        uint128 x = (a * b);
 
        return x;
    }

    function test06() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 67890;
        uint64 c = 55555;

// assert (a <= type(uint64).max / b); //slytherin 6
// assert ((a * b) <= type(uint64).max * c); //slytherin 7
        uint256 x = (a * b) / c;

        return x;
    }

    function test07() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 67890;
        uint64 c = 55555;

// assert (a <= type(uint64).max - b); //slytherin 8
// assert ((a + b) <= type(uint64).max / c); //slytherin 9
        uint256 x = (a + b) * c;

        return x;
    }


    function test08() public pure returns (uint256){
        uint64 a = 5;
        uint64 b = 6;
        uint64 c = 7;

// assert (a <= type(uint64).max / b); //slytherin 10
// assert ((a * b) <= type(uint64).max / c); //slytherin 11
        uint256 x = (a * b) * c;

        return x;
    }


    function test09() public pure returns (uint128){
        uint128 a = 5;
        uint64 b = 6;
        uint64 c = 7;

// assert (a <= type(uint128).max / b); //slytherin 12
// assert ((a * b) <= type(uint128).max / c); //slytherin 13
        uint128 x = (a * b) * c;

        return x;
    }


    function test10() public pure returns (uint256){
        uint64 a = 5;
        uint64 b = 6;
        uint256 c = 7;

// assert (a <= type(uint64).max / b); //slytherin 14
// assert ((a * b) <= type(uint256).max / c); //slytherin 15
        uint256 x = (a * b) * c;

        return x;
    }


    function test11() public pure returns (uint256){
        uint64 a = 56789;
        uint128 b = 12345;
        uint256 c = 10293;

// assert (a <= type(uint128).max / b); //slytherin 16
// assert ((a * b) <= type(uint256).max / c); //slytherin 17
        uint256 x = (a * b) * c;

        return x;
    }


    function test12() public pure returns (uint128){
        uint64 a = 5;
        uint64 b = 6;
        uint128 c = 7;

// assert (a <= type(uint128).max * c); //slytherin 18
// assert ((a / c) <= type(uint128).max / b); //slytherin 19
        uint128 x = (a / c) * b;

        return x;
    }


    function test13() public pure returns (uint128){
        uint64 a = 5;
        uint64 b = 6;
        uint128 c = 7;

// assert (a <= type(uint128).max - c); //slytherin 20
// assert ((a + c) <= type(uint128).max / b); //slytherin 21
        uint128 x = (a + c) * b;

        return x;
    }


    function test14() public pure returns (uint64){
        uint64 a = type(uint64).max;

// assert (a <= type(uint256).max / 17); //slytherin 22
// assert ((a * 17) <= type(uint256).max * 5); //slytherin 23
        uint64 x = (a * 17) / 5;

        return x;
    }


    function test15() public pure returns (uint128){
        uint64 a = type(uint64).max;

// assert (a <= type(uint256).max / 5); //slytherin 24
// assert ((a * 5) <= type(uint256).max * 17); //slytherin 25
        uint128 x = (a * 5) / 17;

        return x;
    }


    function test16() public pure returns (uint64) {
        uint64 a = 0;
        uint64 b = type(uint64).max;

// assert (a <= type(uint64).max + b); //slytherin 26
        uint64 x = a - b;

        return x;
    }


    function test17() public pure returns (uint64) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

// assert (a <= type(uint64).max + b); //slytherin 27
// assert ((a - b) <= type(uint64).max + c); //slytherin 28
        uint64 x = (a - b) - c;

        return x;
    }


    function test18() public pure returns (uint64) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

// assert (a <= type(uint64).max + b); //slytherin 29
// assert ((a - b) <= type(uint64).max / c); //slytherin 30
        uint64 x = (a - b) * c;

        return x;
    }


    function test19() public pure returns (uint128) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

// assert (a <= type(uint64).max + b); //slytherin 31
// assert ((a - b) <= type(uint64).max / c); //slytherin 32
        uint128 x = (a - b) * c;

        return x;
    }


    function test20() public pure returns (uint128) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

// assert (a <= type(uint64).max + b); //slytherin 33
// assert ((a - b) <= type(uint64).max * c); //slytherin 34
        uint128 x = (a - b) / c;

        return x;
    }

}