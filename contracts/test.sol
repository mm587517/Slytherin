pragma solidity 0.8.2;


// contract Contract {
//     function foo() public pure returns (uint256){
//         uint64 a = 12345;
//         uint64 b = 1e18;

//         uint128 x = a * b;

//         return x;
//     }
// }


contract Contract {
    function callee(uint a) public pure returns (uint256){
        return a;
    }

    function caller()public pure returns (uint256) {
        uint a = 3;
        uint b = 5;
        (a+b);
        return callee(callee(a+b));
    }

    function foo() public pure returns (uint256){
        uint64 a = 12345;
        uint64 b = 1e18;

        uint128 x = a * b;

        return x;
    }
}