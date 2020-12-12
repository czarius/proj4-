var ourRequest = new XMLHttpRequest();
ourRequest.open('GET', 'http://35.153.52.42:8983/solr/P4/select?q=tweet_text%3A%22covid%22&wt=json');
ourRequest.onload = function(){
	var ourData = JSON.parse(ourRequest.responseText);
	console.log(ourData[0];
	
};

ourRequest.send();

