contract SimpleStorage {
  uint storedData;

  function SimpleStorage() {
    storedData = 1;
  }

  function set(uint x) {
    storedData = x;
  }

  function get() constant returns (uint) {
    return storedData;
  }
}
