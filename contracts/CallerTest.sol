// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.7.6;

contract CallerTest {
    
    function caller(uint64 a, uint64 b, uint64 c) public pure returns (uint64) {
        return callee1(a + b, (a + b) * c, ((a + b) * c) / (a - b), a * b);
    }
    
    function callee1(uint64 a, uint64 b, uint64 c, uint64 d) public pure returns (uint64) {
        return callee2(a + b, b * c, c / d);
    }
    
    function callee2(uint64 a, uint64 b, uint64 c) public pure returns (uint64) {
        return a + b + c;
    }
    
    function complexCaller(uint64 a, uint64 b) public pure returns (uint64) {
        return complexCallee(a * b, (a + b) * 2, (a * b) / 3, a - b);
    }
    
    function complexCallee(uint64 a, uint64 b, uint64 c, uint64 d) public pure returns (uint64) {
        return a + b + c - d;
    }
    
    function simpleCaller(uint64 a, uint64 b) public pure returns (uint64) {
        return simpleCallee(a + b);
    }
    
    function simpleCallee(uint64 a) public pure returns (uint64) {
        return a * 2;
    }
}
