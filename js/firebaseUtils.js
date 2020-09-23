$(document).ready(function(){

	//alert("Hello");
	
	
	//console.log(questionNumber,day, level)
	//updateData(key, star)
	//updateData(level, day, questionNumber,5)
})


function updateRank(rank)
{
	questionNumber=$("#questionnumber").val()
	day=$("#day").val()
	level=$("#level").val()
	key=$("#key").val()

	//key=level +"/"+parseInt(day)+"/"+parseInt(questionNumber) +"/"+rank
	dbkey=level +"/"+rank+"/"+key
	//firebase.database().ref(key).set({count:1});
	
	var starCountRef = firebase.database().ref(dbkey);

	starCountRef.once('value').then(function(snapshot) {

	  existingValue=snapshot.val()
	  if(existingValue==null)
	  {
	  	newValue=1
	  }
	  else
	  {
	  	newValue=snapshot.val()+1
	  }
	  firebase.database().ref(dbkey).set(newValue);




	})


	db1key=level +"/"+key+"/"+rank
	//firebase.database().ref(key).set({count:1});
	
	var starCountRef = firebase.database().ref(db1key);

	starCountRef.once('value').then(function(snapshot) {

	  existingValue=snapshot.val()
	  if(existingValue==null)
	  {
	  	newValue=1
	  }
	  else
	  {
	  	newValue=snapshot.val()+1
	  }
	  firebase.database().ref(db1key).set(newValue);

	


	})
	  
	 

	
}
