pragma solidity 0.8.2;

contract Contract {
    function callee(uint a) public pure returns (uint256){
        return a;
    }

    function caller()public pure returns (uint256) {        
        assert (2 <= type(uint256).max - 1); //slytherin 1
        uint a = 2 + 1;
        assert (a <= type(uint256).max - a); //slytherin 2
        assert (1 <= type(uint256).max - callee(a + a)); //slytherin 3
        return callee(1+ callee(a+a));
    }
}

