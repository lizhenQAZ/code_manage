
<!doctype html>
<html lang="en">
<head>
    <!-- 这行代码不能修改！ -->
    <meta name="description" content="student login page">

    <meta charset="UTF-8">
    <title>博学谷-学员登录系统</title>
    <link rel="shortcut icon" href="../images/logo.ico">
    <link rel="stylesheet" href="../less/login/login.css">
    <script src="../common/js/jquery-1.8.3.min.js"></script>
    <script src="../js/layer-v2.1/layer/layer.js"></script>
    <script type="text/javascript" src="../common/js/common.js"></script>
    <script src="../js/login.js"></script>

</head>
<body>
<div class="login">
    <div class="warning bowerSupport"><i class="iconfont icon login-warning">&#xe63d; </i> 提示：目前本系统适配火狐浏览器、Google Chrome、Safari(苹果浏览器)，其它浏览器可能无法完美运行!(不建议使用)</div>
    <div class="logheader"></div>
    <div class="logban">
        <div class="logbanner" >
            <div class="logform">
                <div class="login_title">博学谷·学员系统</div>

                <!--手机找回密码-->
                <div class="container-box findpwd-phone" id="m-phone" style="display:block">
                    <ul class="icon-list">
                        <li class="fist-icon">
                            <i class="iconfont prim-color">&#xe661;</i>
                            <p class="first-tip">手机验证身份</p>
                        </li>
                        <li class="line"></li>
                        <li><i class="iconfont  gray-color">&#xe662;</i><p>重置密码</p></li>
                    </ul>
                    <form action="" class="loginm" method="post">
                        <div class="user">
                            <input type="text" name="telphone" class="telphone input-wid" id="telphone" placeholder="请输入手机号"/>
                            <div class="errorInfo"><span id="telerror"></span></div>
                        </div>
                        <div class="check-verify">
                            <div class="verify-box">
                                <input type="text" name="verify"  class="verify"  id = "verify" placeholder="请输入验证码"/>
                                <span class="prim-color send-verify" style="cursor:pointer;" id="sendyzm">发送验证码</span>
                            </div>
                            <div class="errorInfo"><span class="testtelerror"></span></div>
                        </div>
                        <button  class="loginBtn input-wid" type="button" id="next-tel" onclick="findpassword()">下一步</button>
                        <div class="aboutPwd">
                            <span class="prim-color"><a class="prim-color" href="../login.jsp">返回登录</a></span>
                            <span class="forgetPwd prim-color findemail">用邮箱找回密码</span>
                        </div>
                    </form>
                </div>

                <!--手机重置密码-->
                <div class="container-box reset-pwd" id="pasword" style="display:none">
                    <ul class="icon-list">
                        <li class="fist-icon">
                            <i class="iconfont prim-color">&#xe661;</i>
                            <p class="first-tip">手机验证身份</p>
                        </li>
                        <li class="line"></li>
                        <li><i class="iconfont prim-color">&#xe662;</i><p>重置密码</p></li>
                    </ul>
                    <h3 class="login-name">登录名：<span class="number"></span></h3>
                    <form action="" class="loginm" method="post">
                        <div class="user" style="margin-bottom:6px;">
                            <i class="iconfont login-font">&#xe666;</i>
                            <input type="password" name="password" id="newpassword" class="input-wid" placeholder="新密码（6-18）"/>
                             <div class="errorInfo" id="new-error"></div>
                        </div>
                        <div class="check-verify">
                            <i class="iconfont login-font">&#xe666;</i>
                            <input type="password" name="password" id="againpassword" class="input-wid" placeholder="确认密码"/>
                            <div class="errorInfo" id="nom-error"></div>
                        </div>
                        <button  class="loginBtn input-wid" type="button" id="loginbtn">登录</button>
                        <div class="aboutPwd">
                            <span class="prim-color"><a class="prim-color" href="../login.jsp">返回登录</a></span>
                            <span class="forgetPwd prim-color findemail">用邮箱找回密码</span>
                        </div>
                    </form>
                </div>

                <!--输入邮箱地址-->
                <div class="container-box findpwd-emial" id="find-e" style="display:none">
                    <ul class="icon-list">
                        <li class="fist-icon">
                            <i class="iconfont prim-color">&#xe66c;</i>
                            <p class="first-tip">输入邮箱地址</p>
                        </li>
                        <li class="line"></li>
                        <li class="fist-icon secod-icon"><i class="iconfont  gray-color">&#xe65f;</i><p>邮箱验证</p></li>
                        <li class="line gray-line secod-line"></li>
                        <li><i class="iconfont  gray-color">&#xe662;</i><p>重置密码</p></li>
                    </ul>
                    <form action="" class="loginm" method="post">
                        <div class="user">
                            <input type="text" name="telphone" class="telphone input-wid" id="e-wid" placeholder="请输绑定的邮箱地址"/>
                            <div class="errorInfo"><span class="e-error"></span></div>
                        </div>
                        <button  class="loginBtn input-wid" type="button" id="next-btn" onclick="testEmail()">下一步</button>
                        <div class="aboutPwd">
                            <span class="prim-color"><a class="prim-color" href="../login.jsp">返回登录</a></span>
                            <span class="forgetPwd prim-color findpwd">用手机找回密码</span>
                        </div>
                    </form>
                </div>

                <!--邮箱验证-->
                <div class="container-box findpwd-emial" id="find-emial" style="display:none">
                    <ul class="icon-list">
                        <li class="fist-icon"><i class="iconfont prim-color">&#xe66c;</i><p class="first-tip">输入邮箱地址</p>
                        </li>
                        <li class="line"></li>
                        <li class="fist-icon secod-icon"><i class="iconfont prim-color">&#xe65f;</i><p>邮箱验证</p></li>
                        <li class="line secod-line"></li>
                        <li><i class="iconfont gray-color">&#xe662;</i><p>重置密码</p></li>
                    </ul>
                    <p class="font14">密码重置邮件已发送至你的邮箱：</p><a class="prim-color" id="yx">846017623@qq.com</a>
                    <p class="font14">请登录邮箱激活链接重置密码</p>
                    <div class="aboutPwd">
                        <span class="prim-color"><a class="prim-color" href="../login.jsp">返回登录</a></span>
                        <span class="forgetPwd prim-color findpwd">用手机找回密码</span>
                    </div>

                </div>


                <!--邮箱重置-->
                <div class="container-box reset-email" id="findepwd" style="display:none">
                    <ul class="icon-list">
                        <li class="fist-icon"><i class="iconfont prim-color">&#xe66c;</i><p class="first-tip">输入邮箱地址</p></li>
                        <li class="line"></li>
                        <li class="fist-icon secod-icon"><i class="iconfont prim-color">&#xe65f;</i><p>邮箱验证</p></li>
                        <li class="line secod-line"></li>
                        <li><i class="iconfont prim-color">&#xe662;</i><p>重置密码</p></li>
                    </ul>
                    <h3 class="login-name">登录名：<span class="numbere"></span></h3>
                    <form action="" class="loginm" method="post">
                        <div class="user">
                            <i class="iconfont login-font">&#xe666;</i>
                            <input type="password" name="password" id="newpassworde" class="input-wid" placeholder="新密码（6-18）"/>
                            <div class="errorInfo" id="new-worde"></div>
                        </div>
                        <div class="check-verify">
                            <i class="iconfont login-font">&#xe666;</i>
                            <input type="password" name="password" id="againpassworde" class="input-wid" placeholder="确认密码"/>
                            <div class="errorInfo" id="no-error"></div>
                        </div>
                        <button  class="loginBtn input-wid" type="button" id="loginbtne">登录</button>
                        <div class="aboutPwd">
                            <span class="prim-color"><a class="prim-color" href="../login.jsp">返回登录</a></span>
                            <span class="forgetPwd prim-color findpwd">用手机找回密码</span>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    </div>
    <p class="foot" >江苏传智播客教育科技有限公司   主办</p>
</div>
<script type="text/javascript">
function login(telph,newpsw){
    layer.msg('登录中', {icon: 16,shade: [0.1,'#fff'],time : 0,offset : ['200px' , '40%']});
    $.ajax({
        url:'/login.jsp',
        data:{username:telph,password:newpsw}  ,
        type:'POST',
        dataType:'json',
        success:function(data){
            layer.closeAll();
            if(data && data.success==true){
                window.location.href='/index.html';
                //登录日志统计
                $.get("/browser/loginLog", function () {});
                //uv 日志统计
                $.get("/browser/logNowUV",{'url':'login.jsp'},function(){});
            } else {
                window.location.href='/login.jsp';
            }
        }
    });
}
</script>
</body>
</html>