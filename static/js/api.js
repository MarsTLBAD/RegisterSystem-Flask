function sendAjax(param, url, callback) {
    $.ajax({
        async: false,
        ache: false,
        type: 'POST',
        url: url,
        //JSON对象转化JSON字符串
        data: param,
        //服务器返回的数据类型
        dataType: "json",
        success: function (data) {
            callback(data.result)
        },
        error: function (data) {
            //错误处理
        }
    })
}

function addRecord() {
    var data = {}
    var t = $('#recordForm').serializeArray()
    $.each(t, function () {
        data[this.name] = this.value
    })
    sendAjax(data, '/add', function (value) {
        if (value === 1) {
            swal({
                title: "提交成功",
                text: "",
                type: "success",
                timer: 2000
            }, function () {
                location.reload()
            })
        }
        if (value === 0) {
            swal("上交失败", "请重试", "error")
        }
        if (value === -1) {
            swal({
                title: "该学生体温已提交",
                text: "请勿重复提交",
                type: "warning"
            }, function () {
                $('#recordForm')[0].reset()
            })
        }
    })
}

function delRecord(id) {
    swal({
        title: "您确定要删除该记录吗",
        text: "删除后将无法恢复，请谨慎操作！",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "确认",
        cancelButtonText: "取消",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (!isConfirm) {
            swal({
                title: "已取消",
                text: "您取消了删除操作！",
                type: "warning"
            })
            return
        }
        var data = { 'id': id }
        sendAjax(data, '/del', function (value) {
            if (value === 1) {
                swal({
                    title: "删除成功",
                    text: "",
                    type: "success",
                    timer: 2000
                }, function () {
                    location.reload()
                })
                return
            }
            if (value === -1) {
                swal("删除失败", "请重试", "error")
            }
        })
    }
    )
}

function delCallback(value) {

}