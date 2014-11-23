var webpack = require('webpack');

module.exports = {
  entry: {
    common: './inventory/static/js/common',
    vendor: './inventory/static/js/vendor'
  },
  output: {
    path: 'inventory/static/build',
    publicPath: '/static/build/',
    filename: '[name].js'
  },
  module: {
    loaders: [
      { test: /\.css$/, loader: "style!css" },
      { test: /\.less$/, loader: "style!css!autoprefixer!less" }
    ]
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin("vendor", "vendor.bundle.js")
  ]
};
