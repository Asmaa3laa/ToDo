var content;
$(document).ready(function () {
    $('.btn').on('click', function () {
                   content = $('#textarea').val();
                   console.log(content);
               saveToTheDB();
            });
});
 function saveToTheDB() {
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
               url: "/save/",
               method: 'POST',
               data: {
                  'content': content,
               },
            success: function (jason)
             {
                      console.log("success");
                      console.log(jason)
                      var content =jason[0].fields.content
                      console.log(this);
                      $("#body").append(`
                      <input type="checkbox" name="mission" id=${jason[0].pk} >
                      <label for=${jason[0].pk}> ${content}</label><br>
                       `)
                   },
                    error : function(xhr,errmsg,err) {
                    console.log("failed")
                    console.log(xhr.status + ": " + xhr.responseText);
                    }

                });
       }
