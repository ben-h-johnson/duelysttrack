'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function PostListController($scope, Post) {
	var postsQuery = Post.get({}, function(posts) {
		$scope.posts = posts.objects;
	});
	
}

function PostDetailController($scope, $routeParams, Post) {
	var postQuery = Post.get({ postId: $routeParams.postId }, function(post) {
		$scope.post = post;
	});
	
}

function DashboardController($scope, $filter){
	$scope.games = [{"id":1, "player":"Songhai", "opponent":"Vanar", "win":true, "first":false, "date":"2015-12-28T20:03:10"},
						{"id":2, "player":"Vetruvian", "opponent":"Vanar", "win":false, "first":true, "date":"2015-12-28T20:04:10"},
						{"id":3, "player":"Vetruvian", "opponent":"Magmar", "win":true, "first":true, "date":"2015-12-28T20:04:30"},
						{"id":4, "player":"Songhai", "opponent":"Lyonar", "win":true, "first":false, "date":"2015-12-28T20:05:01"}];
	
	$scope.stats = {};
	var classList = ["Lyonar","Songhai","Vetruvian","Abyssian","Magmar","Vanar"];
	for (var i = 0; i < classList.length; i++){
		$scope.stats[classList[i]]={};
		$scope.stats[classList[i]].overall=[0,0]
		for (var j = 0; j < classList.length; j++){
			$scope.stats[classList[i]][classList[j]]=[0,0];
		}
	}
	
	for (var i = 0; i < $scope.games.length; i++){
	   var current = $scope.games[i];
	   if (current.win) {
	   	$scope.stats[current.player][current.opponent][0]++;
	   	$scope.stats[current.player].overall[0]++;
	   }
	   $scope.stats[current.player][current.opponent][1]++;
	   $scope.stats[current.player].overall[1]++;
	}

	$scope.addGame = function(player, opponent, win, first){
		var now = new Date();
		$scope.games.push({"id":$scope.games.length+1, "player":player, "opponent":opponent, "win":win, "first":first, "date":$filter('date')(now,"dd-MM-yyyyThh:mm")});
		if (win) {
			$scope.stats[player][opponent][0]++;
			$scope.stats[player].overall[0]++;
		}
		$scope.stats[player][opponent][1]++;
		$scope.stats[player].overall[1]++;
	}

	$('.navbar-lower').affix({
	  offset: {top: 50}
	});
}
