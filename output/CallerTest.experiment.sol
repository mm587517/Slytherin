// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.7.6;

contract CallerTest {
    
    function caller(uint64 a, uint64 b, uint64 c) public pure returns (uint64) {
// assert (a <= type(uint64).max - b); //slytherin 1
assert (a <= type(uint64).max - b); //slytherin 2
// assert (a <= type(uint64).max - b); //slytherin 4
// assert ((a + b) <= type(uint64).max / c); //slytherin 3
// assert ((a + b) <= type(uint64).max / c); //slytherin 5
// assert (a <= type(uint64).max + b); //slytherin 6
// assert (((a + b) * c) <= type(uint64).max * (a - b)); //slytherin 7
// assert (a <= type(uint64).max / b); //slytherin 8
        return callee1(a + b, (a + b) * c, ((a + b) * c) / (a - b), a * b);
    }
    
    function callee1(uint64 a, uint64 b, uint64 c, uint64 d) public pure returns (uint64) {
// assert (a <= type(uint64).max - b); //slytherin 9
// assert (b <= type(uint64).max / c); //slytherin 10
// assert (c <= type(uint64).max * d); //slytherin 11
        return callee2(a + b, b * c, c / d);
    }
    
    function callee2(uint64 a, uint64 b, uint64 c) public pure returns (uint64) {
// assert (a <= type(uint64).max - b); //slytherin 12
// assert (a + b <= type(uint64).max - c); //slytherin 13
        return a + b + c;
    }
    
    function complexCaller(uint64 a, uint64 b) public pure returns (uint64) {
// assert (a <= type(uint64).max / b); //slytherin 14
// assert (a <= type(uint64).max - b); //slytherin 15
// assert ((a + b) <= type(uint256).max / 2); //slytherin 16
// assert (a <= type(uint64).max / b); //slytherin 17
// assert ((a * b) <= type(uint256).max * 3); //slytherin 18
// assert (a <= type(uint64).max + b); //slytherin 19
        return complexCallee(a * b, (a + b) * 2, (a * b) / 3, a - b);
    }
    
    function complexCallee(uint64 a, uint64 b, uint64 c, uint64 d) public pure returns (uint64) {
// assert (a <= type(uint64).max - b); //slytherin 20
// assert (a + b <= type(uint64).max - c); //slytherin 21
// assert (a + b + c <= type(uint64).max + d); //slytherin 22
        return a + b + c - d;
    }
    
    function simpleCaller(uint64 a, uint64 b) public pure returns (uint64) {
// assert (a <= type(uint64).max - b); //slytherin 23
        return simpleCallee(a + b);
    }
    
    function simpleCallee(uint64 a) public pure returns (uint64) {
// assert (a <= type(uint256).max / 2); //slytherin 24
        return a * 2;
    }
}
