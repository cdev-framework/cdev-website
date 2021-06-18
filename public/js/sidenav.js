$( document ).ready(function() {
    console.log( "side nav ready!" );

   $("i.dropdown").click(
       (e) => {
            id =  $(e.target).attr("id")
            children_name = ".sub-"+id
            console.log(children_name)

            if ($(children_name).css("display") != "none"){
                $(children_name).css("display", "none")
            }
            else{
                $(children_name).css("display", "")
            }

            
            //console.log($(children_name).css("display"))
       }
   )
});