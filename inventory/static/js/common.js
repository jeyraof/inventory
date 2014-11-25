/**
 * Created by Jaeyoung on 11/23/14.
 */
var React = require('react');

var Router = require('react-router');
var Route = Router.Route;
var NotFoundRoute = Router.NotFoundRoute;
var DefaultRoute = Router.DefaultRoute;
var Link = Router.Link;
var RouteHandler = Router.RouteHandler;
var Redirect = Router.Redirect;

var Auth = require('./Auth');

require('../less/common.less');


var App = React.createClass({
  getInitialState: function() {
    return {
      'loggedIn': Auth.loggedIn()
    };
  },
  render: function() {
    var LoginStatus = this.state.loggedIn ? Auth.LogOut : Auth.LogIn;

    return (
      <div className="app">
        <div className="header">
          <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
          </ul>

          <LoginStatus />
        </div>

        <div className="content">
          <RouteHandler/>
        </div>
      </div>
    );
  }
});

var RedirectToMainWhenNotFound = React.createClass({
  statics: {
    willTransitionTo: function (transition) {
      transition.redirect('/');
    }
  },
  render: function() {
    return null;
  }
});

var routes = (
  <Route name="app" path="/" handler={App}>
    <DefaultRoute name="newsfeed" handler={require('./NewsFeed')}/>
    <NotFoundRoute handler={RedirectToMainWhenNotFound}/>
  </Route>
);

Router.run(routes, function (Handler) {
  React.render(<Handler/>, document.getElementById('react-app'));
});
