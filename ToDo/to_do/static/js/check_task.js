$(document).ready(function () {
            $(document).on('click','input[name ="mission"]', function () {
                    console.log("***");
                   task_id = $(this).attr('id');
                   console.log(task_id);
               SetToDone();
            });
    });

function SetToDone(){
    var csrftoken = $.cookie('csrftoken');
            function csrfSafeMethod(method) {
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }
            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
            $.ajax({
               url: "/delete/",
               method: 'POST',
               data: {
                  'task_id': task_id,
               },
            success: function (json)
             {
                      console.log("success");
                      var task_id =json[0].pk
                      console.log(json)

                   },
             error : function(xhr,errmsg,err) {
                    console.log("failed")
                    console.log(xhr.status + ": " + xhr.responseText);
                    }

                });
    }

