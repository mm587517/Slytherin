pragma solidity ^0.7.6;

contract FlashloanContract {
    address public tokenAddress;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed burner, uint256 value);
    
    constructor() {
        tokenAddress = 0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9;
    }
    
    function _burn(address _receiver, uint256 _amount) internal {

        IERC20 token = IERC20(tokenAddress);
        uint256 balanceBefore = token.balanceOf(address(this));
        
        require(token.transfer(_receiver, _amount), "Transfer failed");
        
        uint256 balanceAfter = token.balanceOf(address(this));
assert (balanceBefore <= type(uint256).max + _amount); //slytherin 1
        require(balanceBefore - _amount == balanceAfter, "Burn failed");
        
        emit Burn(_receiver, _amount);
    }
    
    function flashloan(uint256 amount, uint256 fee) external {
        address receiver = msg.sender;

assert (amount <= type(uint256).max - fee); //slytherin 2
        _burn(receiver,  amount + fee);
    }
}


interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}