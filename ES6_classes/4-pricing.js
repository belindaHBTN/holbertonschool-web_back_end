import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.setAmount(amount);
    this.setCurrency(currency);
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  get amount() {
    return this._amount;
  }

  setAmount(amount) {
    if (typeof amount !== 'number') {
      throw new Error('Amount must be a number.');
    }
    this._amount = amount;
  }

  set amount(newAmount) {
    this.setAmount(newAmount);
  }

  get currency() {
    return this._currency;
  }

  setCurrency(currency) {
    if (!(currency instanceof Currency)) {
      throw new Error('The type of currency must be Currency.');
    }
    this._currency = currency;
  }

  set currency(newCurrency) {
    this.setCurrency(newCurrency);
  }
}
