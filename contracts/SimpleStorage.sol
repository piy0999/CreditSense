pragma solidity ^0.4.0;
contract SimpleStorage {
  string storedData;

  function SimpleStorage(string entry) {
    storedData = entry;
  }

  function get() constant returns (string) {
    return storedData;
  }
}

