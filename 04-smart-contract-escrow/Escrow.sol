// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Escrow {
    address public payer;
    address payable public payee;
    uint public amount;
    bool public isReleased;

    constructor(address payable _payee) payable {
        payer = msg.sender;
        payee = _payee;
        amount = msg.value;
        isReleased = false;
    }

    function release() public {
        require(msg.sender == payer, "Solo el pagador puede liberar el pago");
        require(!isReleased, "El pago ya ha sido liberado");

        isReleased = true;
        payee.transfer(amount);
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
