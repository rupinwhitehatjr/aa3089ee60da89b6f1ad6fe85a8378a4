$(document).ready(function(){


firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    console.log(user.uid)
  } 

  
});




})