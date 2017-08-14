















<!doctype html>
<html lang="en">
<head>
	<!-- 这行代码不能修改！ -->
	<meta name="description" content="student login page">

    <meta charset="UTF-8">
    <link rel="shortcut icon" href="images/logo.ico">
    <link rel="stylesheet" href="less/login/login.css">
    <title>博学谷-学员登录系统</title>
	<script src="common/js/jquery-1.8.3.min.js"></script>
	<script src="js/layer-v2.1/layer/layer.js"></script>
	<script src="common/js/jquery.cookie.js"></script>
	<script type="text/javascript" src="common/js/common.js"></script>
	<script type="text/javascript" src="js/loginPage.js"></script>
	<script>
		var contextPath = '';
	</script>
	</head>
<body>
<div class="login">
    <div class="warning bowerSupport"><i class="iconfont icon login-warning">&#xe63d; </i> 提示：目前本系统适配火狐浏览器、Google Chrome、Safari(苹果浏览器)，其它浏览器可能无法完美运行!(不建议使用)</div>
    <div class="logheader"></div>
    <div class="logban">
        <div class="logbanner" >
             <div class="logform">
                <div class="login_title">博学谷·学员系统</div>
				
				<div class="container-box login-box">
					<form action="" class="loginm" method="post" onsubmit="return checkLoginForm(this)">
						<div class="user">
							<i class="iconfont login-font">&#xe668;</i>
							<input type="text" name="username" id="username" class="username input-wid" placeholder="请输入手机号登录"/>
							<div class="errorInfo" id="errorInfo"></div>
						</div>
						<div class="pwd" id="pwd">
							<i class="iconfont login-font">&#xe666;</i>
							<input type="password" name="password" id="password" class="input-wid" autocomplete="off" placeholder="请输入密码"/>
							<div class="errorInfo" id="errorInfopwd"></div>
						</div>
						<div class="check-verify" style="display:none;">
							<div class="verify-box">
								<input type="text" name="verify" class="verify" id="verify" placeholder="请输入验证码">
								<span class="prim-color send-verify" style="cursor:pointer;" id="sendyzm">发送验证码</span>
							</div>
							<div class="errorInfo" id="errorInfoyzm"></div>
							</div>
						<div class="login-aboutPwd">
							<input type="checkbox" id="rmbUser" class="rmbUser"/><label for="rmbUser">记住密码</label>
							<span class="forgetPwd"><a href="view/testpassword.jsp">忘记密码？</a></span>
						</div>
						<button  class="loginBtn input-wid" onclick="checkCookie();" type="button">登录</button>
					</form>
				</div>
             </div>
        </div>
    </div>
    <p class="foot" >江苏传智播客教育科技股份有限公司   主办</p>
</div>

<script>
	
</script>
</body>
</html>