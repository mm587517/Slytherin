// SPDX-License-Identifier: GPL-3.0
 
pragma solidity ^0.7.6;
 

contract TestCases {

    function test01() public pure returns (uint64){
        uint64 a = 2;
        uint64 b = 2;
        
        uint64 x = (a * b);
 
        return x;
    }

      function test02() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 1e18;
        
        uint256 x = a * b;
 
        return x;
    }
    

    function test03() public pure returns (uint64){
        uint64 a = type(uint64).max;
        uint64 b = type(uint64).max;
        
        uint64 x = a + b;
 
        return x;
    }

    function test04() public pure returns (uint128){
        uint64 a = type(uint64).max;
        uint64 b = type(uint64).max;
        
        uint128 x = a + b;
 
        return x;
    }


    function test05() public pure returns (uint128){
        uint64 a = type(uint64).max;
        uint64 b = type(uint64).max;
        
        uint128 x = (a * b);
 
        return x;
    }

    function test06() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 67890;
        uint64 c = 55555;

        uint256 x = (a * b) / c;

        return x;
    }

    function test07() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 67890;
        uint64 c = 55555;

        uint256 x = (a + b) * c;

        return x;
    }


    function test08() public pure returns (uint256){
        uint64 a = 5;
        uint64 b = 6;
        uint64 c = 7;

        uint256 x = (a * b) * c;

        return x;
    }


    function test09() public pure returns (uint128){
        uint128 a = 5;
        uint64 b = 6;
        uint64 c = 7;

        uint128 x = (a * b) * c;

        return x;
    }


    function test10() public pure returns (uint256){
        uint64 a = 5;
        uint64 b = 6;
        uint256 c = 7;

        uint256 x = (a * b) * c;

        return x;
    }


    function test11() public pure returns (uint256){
        uint64 a = 56789;
        uint128 b = 12345;
        uint256 c = 10293;

        uint256 x = (a * b) * c;

        return x;
    }


    function test12() public pure returns (uint128){
        uint64 a = 5;
        uint64 b = 6;
        uint128 c = 7;

        uint128 x = (a / c) * b;

        return x;
    }


    function test13() public pure returns (uint128){
        uint64 a = 5;
        uint64 b = 6;
        uint128 c = 7;

        uint128 x = (a + c) * b;

        return x;
    }


    function test14() public pure returns (uint64){
        uint64 a = type(uint64).max;

        uint64 x = (a * 17) / 5;

        return x;
    }


    function test15() public pure returns (uint128){
        uint64 a = type(uint64).max;

        uint128 x = (a * 5) / 17;

        return x;
    }


    function test16() public pure returns (uint64) {
        uint64 a = 0;
        uint64 b = type(uint64).max;

        uint64 x = a - b;

        return x;
    }


    function test17() public pure returns (uint64) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

        uint64 x = (a - b) - c;

        return x;
    }


    function test18() public pure returns (uint64) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

        uint64 x = (a - b) * c;

        return x;
    }


    function test19() public pure returns (uint128) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

        uint128 x = (a - b) * c;

        return x;
    }


    function test20() public pure returns (uint128) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

        uint128 x = (a - b) / c;

        return x;
    }

}