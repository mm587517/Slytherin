// SPDX-License-Identifier: GPL-3.0
 
pragma solidity ^0.7.6;
 

contract TestCases {
      // Marcelo's original test case
      function test1() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 1e18;
        
        uint256 x = a * b;
 
        return x;
    }
    
    // Will not cause an error, but should cause a warning because type casts
    function test2() public pure returns (uint64){
        uint64 a = 2;
        uint64 b = 2;
        
        uint64 x = (a * b);
 
        return x;
    }

    // Overflow error
    function test3() public pure returns (uint64){
        uint64 a = type(uint64).max;
        uint64 b = type(uint64).max;
        
        uint64 x = a + b;
 
        return x;
    }

    // No error? Warning?
    function test4() public pure returns (uint128){
        uint64 a = type(uint64).max;
        uint64 b = type(uint64).max;
        
        uint128 x = a + b;
 
        return x;
    }

    // Should cause a warning for (a*b)
    function test5() public pure returns (uint128){
        uint64 a = type(uint64).max;
        uint64 b = type(uint64).max;
        
        uint128 x = (a * b);
 
        return x;
    }

    // Should give a warning for the right side of the assignment
    function test6() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 67890;
        uint64 c = 55555;

        uint256 x = (a * b) / c;

        return x;
    }

    // Should give a warning for the right side of the assignment
    function test7() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 67890;
        uint64 c = 55555;

        uint256 x = (a + b) * c;

        return x;
    }

    // Shouldn't be an error, but should give a warning
    function test8() public pure returns (uint256){
        uint64 a = 5;
        uint64 b = 6;
        uint64 c = 7;

        uint256 x = (a * b) * c;

        return x;
    }

    // Should cause a warning 
    function test9() public pure returns (uint128){
        uint128 a = 5;
        uint64 b = 6;
        uint64 c = 7;

        uint128 x = (a * b) * c;

        return x;
    }

    // Mixing types on the right side -- warning?
    function test10() public pure returns (uint256){
        uint64 a = 5;
        uint64 b = 6;
        uint256 c = 7;

        uint256 x = (a * b) * c;

        return x;
    }

    // Mixing types on the right side -- warning?
    function test11() public pure returns (uint256){
        uint64 a = 56789;
        uint128 b = 12345;
        uint256 c = 10293;

        uint256 x = (a * b) * c;

        return x;
    }

    // Mixing types on the right side -- warning?
    function test12() public pure returns (uint128){
        uint64 a = 5;
        uint64 b = 6;
        uint128 c = 7;

        uint128 x = (a / c) * b;

        return x;
    }

    // Mixing types on the right side -- warning?
    function test13() public pure returns (uint128){
        uint64 a = 5;
        uint64 b = 6;
        uint128 c = 7;

        uint128 x = (a + c) * b;

        return x;
    }

    // Using Literals: what happens with types? -- overflow error expected
    function test14() public pure returns (uint64){
        uint64 a = type(uint64).max;

        uint64 x = (a * 17) / 5;

        return x;
    }

    // Using Literals: what happens with types?
    function test15() public pure returns (uint128){
        uint64 a = type(uint64).max;

        uint128 x = (a * 5) / 17;

        return x;
    }

    // Subtraction test case
    function test16() public pure returns (uint64) {
        uint64 a = 0;
        uint64 b = type(uint64).max;

        uint64 x = a - b;

        return x;
    }

    // Subtraction test case -- overflow?
    function test17() public pure returns (uint64) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

        uint64 x = (a - b) - c;

        return x;
    }

    // Subtraction test case -- overflow
    function test18() public pure returns (uint64) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

        uint64 x = (a - b) * c;

        return x;
    }

    // Subtraction test case -- should cause warning
    function test19() public pure returns (uint128) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

        uint128 x = (a - b) * c;

        return x;
    }

    // Subtraction test case -- should cause warning
    function test20() public pure returns (uint128) {
        uint64 a = 0;
        uint64 b = type(uint64).max;
        uint64 c = type(uint64).max;

        uint128 x = (a - b) / c;

        return x;
    }

}