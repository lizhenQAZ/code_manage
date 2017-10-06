$(function () {
    // 获取对象
    var $oUsername = $("#user_name");
    var $oPsw = $("#psw");
    var $oRpwd = $("#rpwd");
    var $oEmail = $("#email");
    var $oAllow = $("#allow");
    var $oMyform = $("#myform");

    // 记录匹配状态
    var isUsernameOk = false;
    var isPswOk = false;
    var isRpwdOk = false;
    var isEmailOk = false;
    var isAllowOk = true;

    // 正则对象
    var regUsername = /^\w{6,20}$/;
    var regPsw = /^[\w!@#$%^&*()]{6,20}$/;

    var regEmail = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/i;

    // 判断逻辑
    $oUsername.focus(function () {
        $oUsername.next().hide();
        isUsernameOk = false;
    });
    $oUsername.blur(function () {
        judgeUsername();
    });

    $oPsw.focus(function () {
        isPswOk = false;
        $oPsw.next().hide();
    });
    $oPsw.blur(function () {
        judgePsw();
    });

    $oRpwd.focus(function () {
        isRpwdOk = false;
        $oRpwd.next().hide();
    });
    $oRpwd.blur(function () {
        judgeRpwd();
    });

    $oEmail.focus(function () {
        isEmailOk = false;
        $oEmail.next().hide();
    });
    $oEmail.blur(function () {
        judgeEmail();
    });

    $oAllow.click(function () {
        judgeAllow();
    });

    $oMyform.submit(function () {
        // 阻止自动提交
        return judgeSubmit();
    });

    /*
     ** 验证用户名
     */
    function judgeUsername() {
        var sTr = '';
        if ($oUsername.val() == '') {
            isUsernameOk = false;
            sTr = '用户名不能为空';
        } else if (!regUsername.test($oUsername.val())) {
            isUsernameOk = false;
            sTr = '用户名是数字字母下划线6-20位';
        }
        else{
            isUsernameOk = true;          
        }
        $oUsername.next().html(sTr);
        $oUsername.next().show();
    }

    /*
     ** 验证密码
     */
    function judgePsw() {
        var sTr = '';
        if ($oPsw.val() == '') {
            isPswOk = false;
            sTr = '密码不能为空';
        } else if (!regPsw.test($oPsw.val())) {
            isPswOk = false;
            sTr = '密码是数字字母下划线!@#$%^&*()6-20位';
        }
        else{
            isPswOk = true;
        }
        $oPsw.next().html(sTr);
        $oPsw.next().show();
    }

    /*
     ** 确认密码
     */
    function judgeRpwd() {
        var sTr = '';
        if ($oRpwd.val() != $oPsw.val()) {
            isRpwdOk = false;
            sTr = '两次密码不一致';
        }else{
            isRpwdOk = true;
        }
        $oRpwd.next().html(sTr);
        $oRpwd.next().show();
    }

    /*
     ** 验证邮箱
     */
    function judgeEmail() {
        var sTr = '';
        if ($oEmail.val() == '') {
            isEmailOk = false;
            sTr = '邮箱不能为空';
        } else if (!regEmail.test($oEmail.val())) {
            sTr = '邮箱格式不对';
            isEmailOk = false;
        }else{
            isEmailOk = true;
        }
        $oEmail.next().html(sTr);
        $oEmail.next().show();
    }

    /*
     ** 验证同意
     */
    function judgeAllow() {
        var sTr = '';
        if (!$oAllow.prop("checked")) {
            isAllowOk = false;
            sTr = '必须勾选';
        }else{
            isAllowOk = true;
        }
        $oAllow.siblings().eq(1).html(sTr);
        $oAllow.siblings().eq(1).show();
    }

    /*
     ** 验证提交
     */
    function judgeSubmit() {
        if(isUsernameOk && isPswOk && isRpwdOk && isEmailOk && isAllowOk){
            return true;
        }
        // alert("heheh");
        return false;
    }
});
