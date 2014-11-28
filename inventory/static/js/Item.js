var React = require('react');
var Router = require('react-router');

var NewItemView = React.createClass({
  mixins: [Router.State],
  submitHandler: function(e) {
    e.preventDefault();
    var form = e.target;
    $.ajax({
      url: form.action,
      type: form.method,
      data: $(form).serialize(),
      success: function(data) {
        if (!data.ok) {
          alert(data.msg);
        } else {
          alert(data.item_id);
        }
      },
      async: false
    });
  },
  render: function () {
    var new_item_link = '/item/new';
    return (
      <div>
        <form method="POST" action={new_item_link} onSubmit={this.submitHandler}>
          <input type="text" name="category_id"/>
          <SelectBrand />
          <input type="text" name="brand_id"/>
          <input type="text" name="name"/>
          <textarea name="description"></textarea>
          <input type="submit" value="생성"/>
        </form>
      </div>
    );
  }
});

var SelectBrand = React.createClass({
  getBrandList: function() {
    var brandList = null;
    $.ajax({
      url: '/item/get_brands',
      type: 'GET',
      success: function(data) {
        brandList = data.brands;
      },
      async: false
    });
    return brandList;
  },
  render: function () {
    var brandList = this.getBrandList();
    return (
      <select name="brand_id">
        {brandList.map(function(brand) {
          return <option key={brand.id} value={brand.id}>{brand.name}</option>;
        })}
      </select>
    );
  }
});

module.exports.newItem = NewItemView;
