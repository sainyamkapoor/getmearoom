$(document).ready(function(){

 $('#grab').click(function(){
    var pref1;

var hostel;
var pref1_data;

hostel = $("#hostel").val();
        
pref1 = $("#pref1").val();
    
 $.get('/search/', {search_hostel: hostel,search_room:pref1}, function(data){
			               pref1_data=data;

 
$.get('/room/', {search_hostel: hostel,pref1:pref1,pref1_data:pref1_data}, function(data){
              				 $('#error').html(data);
					
		           			if (str.indexOf("is alloted to you") >= 0)
  						{	 					
							location.reload(true);	
						}
					
					    				
           });   








 });
 


});
});

 
   				
               
         
            
