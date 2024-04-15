pragma solidity ^0.7.6;



contract ERC20 {

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);


    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowancer;
    string public name;
    string public symbol;

    constructor(string memory _name, string memory _symbol, uint256 initialSupply) {
        return;
    }

    function transfer(address recipient, uint256 amount)
        external
        returns (bool)
    {
        return true;
    }
}