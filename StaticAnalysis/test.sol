pragma solidity ^0.8.2;

contract Flaw {
	function flaw_test() public pure returns (uint256) {
		uint64 a = 12345;
		uint64 b = 1e18;
		uint256 x = (a * b);
		return x;
	}
}
