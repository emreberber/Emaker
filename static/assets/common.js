
var deleteQuestion = function(){
	bootbox.confirm({
    message: "Are you sure delete question?",
    size: "small",
    buttons: {
        confirm: {
            label: 'Yes',
            className: 'btn-success btn-position'
        },
        cancel: {
            label: 'No',
            className: 'btn-danger'
        }
    },
    callback: function (result) {
        if(result){
        	location.href = $("#delete-question").attr("data");
        }
    }
});
}

var deleteExam = function(){
	bootbox.confirm({
    message: "Are you sure delete Exam?",
    size: "small",
    buttons: {
        confirm: {
            label: 'Yes',
            className: 'btn-success btn-position'
        },
        cancel: {
            label: 'No',
            className: 'btn-danger'
        }
    },
    callback: function (result) {
        if(result){
        	location.href = $("#delete-exam").attr("data");
        }
    }
});
}

var deleteLesson = function(){

	bootbox.confirm({
    message: "Are you sure delete lesson?",
    size: "small",
    buttons: {
        confirm: {
            label: 'Yes',
            className: 'btn-success btn-position'
        },
        cancel: {
            label: 'No',
            className: 'btn-danger'
        }
    },
    callback: function (result) {
        if(result){
        	location.href = $("#delete-lesson").attr("data");
        }
    }
});
}
setTimeout(function(){
		$(".cke_button__image").on("click",function(){
		setTimeout(function(){
				$("[title='Upload']").show();
		},300)
	})
},1000)

