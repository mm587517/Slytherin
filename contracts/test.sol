pragma solidity 0.8.2;

contract Contract {
    // function callee(uint a) public pure returns (uint256){
    //     return a;
    // }

    // function caller(uint b)public pure returns (uint256) {        
    //     uint a = b+1;
    //     return callee(1+ callee(a+a));
    // }

    function idk(int a) public pure returns (bool) {
        int b = 1;
        int c = 5;
        require (a - b <= c);
        return true;
    }



}

