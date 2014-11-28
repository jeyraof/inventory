var React = require('react/addons');
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
        if (data.ok) {
          alert('생성 완료라고!');
        } else {
          alert(data.msg);
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
          <SelectCategory />
          <SelectBrand />
          <input type="text" name="name"/>
          <textarea name="description"></textarea>
          <input type="submit" value="생성"/>
        </form>
      </div>
    );
  }
});

var SelectCategory = React.createClass({
  getCategoryList: function() {
    var categoryList = [];
    $.ajax({
      url: '/item/get_categories',
      type: 'GET',
      success: function(data) {
        categoryList = data.categories;
      },
      async: false
    });
    return categoryList;
  },
  render: function() {
    var categoryList = this.getCategoryList();
    return (
      <select name="category_id">
        {categoryList.map(function(category) {
          return <option key={category.id} value={category.id}>{category.name}</option>;
        })}
      </select>
    )
  }
});

var SelectBrand = React.createClass({
  getBrandList: function() {
    var brandList = [];
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

var ItemDetailView = React.createClass({
  render: function() {
    return 'kkk';
  }
});

module.exports.newItem = NewItemView;
module.exports.itemDetail = ItemDetailView;
