class Phone {

    static basicColor = 'Grey';

    constructor (company, model, price, hue) {
      this.company = company;
      this._model = model;
      this.price = price;
      this.color = hue + Phone.basicColor;
    }

    discountPrice (discount) {
      return this.price*(1-discount);
    }

    set model(_model) {
      var re = /[^0-9]/;
      match = _model.search(re)
      if(_model.search(re) != -1){
          console.log('Shall be non-numeric')
      }
      else{
          this._model = _model
      }
    }

    get model() {
      return this._model;
    }
  

  }
  class Smartphone extends Phone {
    constructor (company, model, price, color, operationSystem) {
      super(company, model, price, color);
      this.operationSystem = operationSystem;
    }
    
  }


  Phone.prototype.toString = function phoneToString() {
    var ret = `\nThis is a ${this.color} ${this.company} ${this._model} phone` ;
    return ret;
  }

  // Create an instance of the Phone Class.
  const m1 = new Phone("Samsung", "x11", 780, "Dark");

  console.log(m1.toString())


