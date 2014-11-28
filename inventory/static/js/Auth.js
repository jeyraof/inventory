/**
 * Created by Jaeyoung on 11/25/14.
 */
var React = require('react');

var Router = require('react-router');
var Link = Router.Link;

var util = require('./utils');
var tokenName = 'inventoryToken';
var userId = 'userId';
var loggedInUrl = '/auth/logged_in';

var Auth = {
  loggedIn: function() {
    $.ajax({
      url: loggedInUrl,
      type: 'GET',
      success: function(data) {
        util.setToken(tokenName, data.token, 1);
        util.setToken(userId, data.user_id, 1);
      },
      async: false
    });

    PreloadData.loggedIn = true;

    return {
      loggedIn: util.getToken(tokenName) !== "",
      userName: util.getToken(userId)
    }
  },
  LogIn: React.createClass({
    render: function () {
      return (
        <ul className="right">
          <li>
            <a href="/auth/facebook">로그인</a>
          </li>
        </ul>
      );
    }
  }),
  LogOut: React.createClass({
    render: function () {
      return (
        <ul className="right">
          <li>
            <Link to="userDetail" params={{userId: util.getToken(userId)}}>내정보</Link>
          </li>
          <li>
            <a href="/auth/logout">로그아웃</a>
          </li>
        </ul>
      );
    }
  })
};

module.exports = Auth;