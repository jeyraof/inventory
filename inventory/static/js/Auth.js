/**
 * Created by Jaeyoung on 11/25/14.
 */
var util = require('./utils');
var tokenName = 'inventoryToken';
var loggedInUrl = '/auth/logged_in';

var Auth = {
  loggedIn: function() {
    $.ajax({
      url: loggedInUrl,
      type: 'GET',
      success: function(data) {
        util.setToken(tokenName, data.token, 1);
      }
    });

    return util.getToken(tokenName) !== "";
  }
};

module.exports = Auth;