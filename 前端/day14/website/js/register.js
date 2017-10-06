$(function () {

    var $username = $("#user_name");//用户名
    var $psw = $("#psw");           //密码
    var $rpwd = $("#rpwd");     //确认密码
    var $email = $("#email");       //邮箱
    var $allow = $("#allow");       //同意协议


    var is_user_error = true;  //用一个变量代表用户名是否有问题
    var is_psw_error = true;
    var is_repsw_error = true;
    var is_email_error = true;
    var is_allow_error = false;


    // 所有正则
    var regUser = /^\w{6,20}$/;
    //密码验证：
    var regPass = /^[\w!@#$%^&*()]{6,20}$/;
    //邮箱验证：        
    var regMail = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/i;

    // 获取焦点
    $username.focus(function () {
        $username.next().hide();
    });
    // 失去焦点
    $username.blur(function () {
        checkUser();
    });

    /**
     * 用户名验证
     */
    function checkUser() {
        var username = $username.val();
        if (username == "") {
            $username.next().html("用户名不能为空").show();
            is_user_error = true;
            return;
        }
        // 正则验证
        if (regUser.test(username)) {
            $username.next().hide();
            is_user_error = false;
        } else {
            is_user_error = true;
            $username.next().html("用户名是数字字母下划线6-20位").show();
        }
    }

    // 获取焦点
    $psw.focus(function () {
        $psw.next().hide();
    });
    // 失去焦点
    $psw.blur(function () {
        checkPsw();
    });

    function checkPsw() {
        var psw = $psw.val();
        if (psw == "") {
            is_psw_error = true;
            $psw.next().html("密码不能为空").show();
            return;
        }
        if (regPass.test(psw)) {
            $psw.next().hide();
            is_psw_error = false;
        } else {
            is_psw_error = true;
            $psw.next().html("密码是数字字母下划线!@#$%^&*()6-20位").show();
        }

    }

    $rpwd.focus(function () {
        $rpwd.next().hide();
    });

    $rpwd.blur(function () {
        checkRPsw();
    });

    function checkRPsw() {

        var psw = $psw.val();//密码

        var rPsw = $rpwd.val();//确认密码


        if (psw == rPsw) {
            $rpwd.next().hide();
            is_repsw_error = false;
        } else {
            is_repsw_error = true;
            $rpwd.next().html("两次密码不一致").show();
        }
    }

    // 焦点事件
    $email.focus(function () {
        $email.next().hide();
    });

    $email.blur(function () {
        checkEmail();
    });
    function checkEmail() {
        var email = $email.val();
        if (email == "") {
            is_email_error = true;
            $email.next().html("邮箱不能为空").show();
            return;
        }
        if (regMail.test(email)) {
            is_email_error = false;
            $email.next().hide();
        } else {
            is_email_error = true;
            $email.next().html("邮箱格式不对").show();
        }
    }

    // 同意协议的点击
    $allow.click(function () {
        checkAllow();
    });

    function checkAllow() {
        var isCheck = $allow.prop("checked");
        var $tips = $allow.siblings("span");
        if (isCheck) {
            is_allow_error = false;
            $tips.hide();
        } else {
            is_allow_error = true;
            $tips.html("必须勾选").show();
        }
    }

    // 表单的提交事件
    $("#myform").submit(function () {
        checkUser();
        checkPsw();
        checkRPsw();
        checkEmail();
        checkAllow();


        if (is_user_error || is_psw_error || is_repsw_error || is_email_error || is_allow_error) {
            // 只要有一个是true 说明输入有问题 不能提交
            return false
        }

        return true;

    });

});