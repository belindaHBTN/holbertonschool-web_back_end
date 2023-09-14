export default class Currency {
  constructor(code, name) {
    this.setCode(code);
    this.setName(name);
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }

  get code() {
    return this._code;
  }

  setCode(code) {
    if (typeof code !== 'string') {
      throw new Error('Code must be a string.');
    }
    this._code = code;
  }

  set code(newCode) {
    this.setCode(newCode);
  }

  get name() {
    return this._name;
  }

  setName(name) {
    if (typeof name !== 'string') {
      throw new Error('Name must be a string.');
    }
    this._name = name;
  }

  set name(newName) {
    this.setName(newName);
  }
}
