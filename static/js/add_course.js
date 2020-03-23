var SELECTED_DEPARTMENT;
var SELECTED_LANG;
var SELECTED_TEACHER;
var SELECTED_CLASSROOM;
var SELECTED_DAY = $('input[name="select-day"]:checked').val();

function get_available_hours(){
  $('#select-starthour').html("");
  $('#select-endhour').html("");
  $.ajax({
    url: "/api/get_hours", data: {
      classroom: SELECTED_CLASSROOM,
      teacher: SELECTED_TEACHER,
      day: SELECTED_DAY,
    }
  }).done(function(result){

    result.forEach(item => {
      $('#select-starthour').append($('<option>', {value: item,text: item + ":00"}));
      $('#select-endhour').append($('<option>', {value: item,text: item + ":00"}));
    });
  });
}


function get_classrooms(){
  $.ajax({
    url: "/api/get_class", data: {
      department: SELECTED_DEPARTMENT
    }
  }).done(function(result){
    $('#select-classroom').html("");
    SELECTED_CLASSROOM = result[0].id;
    result.forEach(item => {
      $('#select-classroom').append($('<option>', {
        value: item.id,
        text: item.name
      }));
    })});
}

function get_teachers(){
  $.ajax({
    url: "/api/get_teacher", data: {
      department: SELECTED_DEPARTMENT,
      language: SELECTED_LANG,
    }
  }).done(function(result){
    $('#select-teacher').html("");
    SELECTED_TEACHER = result[0].user.id;
    result.forEach(item => {
      $('#select-teacher').append($('<option>', {
        value: item.user.id,
        text: item.user.username
      }));
    })
    get_available_hours();
  })

}

function send(){
  $.ajax({
    url: "/api/create_lesson",
    data: {
      name: $("#input-name").val(),
      teacher: SELECTED_TEACHER,
      classroom: SELECTED_CLASSROOM,
      day: SELECTED_DAY,
      start_hour:$("#select-starthour").val(),
      end_hour:$("#select-endhour").val(),
      language: $("#select-language").val(),
    }
  }).done(function(){
    window.location.replace("/i/lesson");
  });

}


$('input[name="select-day"]').change(function(){
  SELECTED_DAY =$('input[name="select-day"]:checked').val();
  get_available_hours();
});

$("#select-department").change(function(){
  SELECTED_DEPARTMENT = $(this).val();
  get_classrooms();
  get_teachers();
})

$("#select-language").change(function(){
  SELECTED_LANG = $(this).val();
  get_teachers();

})
$("#select-classroom").change(function(){
  SELECTED_CLASSROOM = $(this).val();
  get_available_hours();
})
$("#select-teacher").change(function(){
  SELECTED_TEACHER = $(this).val();
  get_available_hours();
})

$("#send").click(function(){
  send()
})
