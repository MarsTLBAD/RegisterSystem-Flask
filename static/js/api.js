function sendAjax(param, url, callback) {
    $.ajax({
        async: false,
        ache: false,
        type: 'POST',
        url: url,
        data: JSON.stringify(param),
        dataType: "text",
        success: function (data) {
            var value = $.parseJSON(data).result
            callback(value)
        },
        error: function (data) {
            //错误处理
        }
    })
}

function addRecord() {
    var data = {
        'id': $('#id').val(),
        'name': $('#name').val(),
        'tem': $('#tem').val(),
        'date': $('#date').val()
    }
    //判断体温是否为数字
    var regPos = /^\d+(\.\d+)?$/

    if (!regPos.test(parseFloat(data['tem']))) {
        swal({
            title: "请输入正确的体温格式",
            text: "体温格式",
            type: "error"
        }, function () {
            $('#tem').val("")
        })
        return
    }
    if (data['tem'] < 35.0 || data['tem'] > 42.9) {
        swal({
            title: "请输入正常范围的体温",
            text: "体温范围35-42℃",
            type: "error"
        }, function () {
            $('#tem').val("")
        })
        return
    }
    sendAjax(data, '/add', addCallback)
}

function addCallback(value) {
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
        },
        function (isConfirm) {
            if (isConfirm) {
                var data = {'id': id}
                sendAjax(data, '/del', delCallback)
                return
            }
            swal({
                title: "已取消",
                text: "您取消了删除操作！",
                type: "warning"
            })
        }
    )
}

function delCallback(value) {
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
}