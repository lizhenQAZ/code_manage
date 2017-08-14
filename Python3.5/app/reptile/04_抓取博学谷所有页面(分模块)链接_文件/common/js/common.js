/**
 * Created by Elvis on 2015/12/22.
 */

var basePath = "";
//var basePath = "/dual-student";
//var kcenterPic = "http://dual2-kcenter.boxuegu.com:8091/attachment/download?aid=";
//var managerPic = "http://dual2-manage2.boxuegu.com:8091/attachment/download?aid=";
var kcenterPic = '';
var managerPic = '';
function isnull(data) {
    if (data == "" || typeof(data) == "undefined" || data == "") {
        return true;
    } else {
//		if(typeof data == "string" && data.trim()==""){
//			return true;
//		}
        return false;
    }
}
/**
 * 显示空白页的名言警句
 * @param totalCount 总记录
 */
function showBlankTip(totalCount, objstr) {
    var tipObj = $('#' + objstr);
    var pareobj = tipObj.closest('.tabfx').find('table');
    if (totalCount <= 0 || typeof totalCount == "undefined") {//显示空白提示
        tipObj.show();
        if (pareobj.prop("tagName") == 'TABLE') {//隐藏表格
            pareobj.hide();
        }
    } else {
        pareobj.show();
        tipObj.hide();
    }
}
$(document).bind("mousedown", function (event) {
    if (event.target.className != "imgpreshow") {//清除上次显示的图片
        var imgpreshow = $("body", parent.document).find(".imgpreshow");
        if (imgpreshow.length > 0) {
            imgpreshow.remove();
        }
    }
});

function GetQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null)return unescape(r[2]);
    return null;
}


//当前页面tab切换动作
function tabChange(obj) {
    if ($(obj)) {
        $(obj).on("click", "li", function () {
            $(obj).find("li").removeClass("liactive");
            $(this).addClass("liactive");
            $(".divpaper .divtab").fadeOut();
            var liidx = $(this).attr("id").charAt(2);
            $("#div" + liidx).fadeIn();
        });
    }
}

//手风琴效果
function accordionChange(obj) {
    $(obj).on("click", "li", function () {
        if ($(this).find(".divaccordion").css("display") == "none") {
            $(obj).find("li .divaccordion").slideUp();
            $(this).find(".divaccordion").slideDown();
        }
    });
}

//通用分页
function creatPagerOld(totalCount, pageSize, totalPageCount, objselector, currentpage, pagecallbak) {

    var pagenum = Math.ceil(totalCount / pageSize);
    var prenext = pagenum > 1 ? "inline-block" : "none";
    var pageitem = "";

    if (pagenum > 1) {
        for (var i = 0; i < pagenum; i++) {
            if (i > 4 && i < (pagenum - 5)) {
                if (i > (pagenum - 9) && i < (pagenum - 5)) {
                    pageitem += "<li>.</li>";
                }
            } else {
                if ((i + 1) == currentpage) {
                    pageitem += "<li  style='background-color: #00ab89; color:#fff;'>" + (i + 1) + "</li>";
                } else {
                    pageitem += "<li onclick='" + pagecallbak + "(" + (i + 1) + ")'>" + (i + 1) + "</li>";
                }
            }
        }
    }

    var pagelis = $('<li style="display: ' + prenext + '" onclick="' + pagecallbak + '(' + (parseInt(currentpage) - 1) + ')"><上一页</li>' + pageitem + '<li style="display: ' + prenext + '" onclick="' + pagecallbak + '(' + (parseInt(currentpage) + 1) + ')">下一页></li><li class="tz">共' + totalPageCount + '页</li><li style="display: none;" class="tz">到第&nbsp;<input type="text">&nbsp; 页</li><li style="display: none;">确定</li>');
    $(objselector).append(pagelis);
}

//通用分页
function creatPager(totalCount, pageSize, totalPageCount, objselector, currentpage, pagecallbak) {

    var pagenum = Math.ceil(totalCount / pageSize);
//    var prenext = pagenum > 1 ? "inline-block" : "none";
    //前一页
    var prenext = "inline-block";
    //后一页
    var suffix = "inline-block";
    if (currentpage == 1) {
        prenext = "none";

    }
    if (currentpage == pagenum) {
        suffix = "none";
    }


    var pageitem = "";

    if (pagenum > 1) {
        for (var i = 0; i < pagenum; i++) {
            if (i > 4 && i < (pagenum - 5)) {
                if (i > (pagenum - 9) && i < (pagenum - 5)) {
                    pageitem += "<li>.</li>";
                }
            } else {
                if ((i + 1) == currentpage) {
                    pageitem += "<li  style='background-color: #00ab89; color:#fff;'>" + (i + 1) + "</li>";
                } else {
                    pageitem += "<li onclick='" + pagecallbak + "(" + (i + 1) + ")'>" + (i + 1) + "</li>";
                }
            }
        }
    }

    var pagelis = $('<li style="display: ' + prenext + '" onclick="' + pagecallbak + '(' + (parseInt(currentpage) - 1) + ')"><上一页</li>' + pageitem + '<li style="display: ' + suffix + '" onclick="' + pagecallbak + '(' + (parseInt(currentpage) + 1) + ')">下一页></li><li class="tz">共' + totalPageCount + '页</li><li style="display: none;" class="tz">到第&nbsp;<input type="text">&nbsp; 页</li><li style="display: none;">确定</li>');
    $(objselector).append(pagelis);
}

//字符串补零
String.prototype.PadLeft = function (totalWidth, paddingChar) {
    if (paddingChar != null) {
        return this.PadHelper(totalWidth, paddingChar, false);
    } else {
        return this.PadHelper(totalWidth, ' ', false);
    }
};

String.prototype.PadRight = function (totalWidth, paddingChar) {
    if (paddingChar != null) {
        return this.PadHelper(totalWidth, paddingChar, true);
    } else {
        return this.PadHelper(totalWidth, ' ', true);
    }

};
String.prototype.PadHelper = function (totalWidth, paddingChar, isRightPadded) {

    if (this.length < totalWidth) {
        var paddingString = String();
        for (i = 1; i <= (totalWidth - this.length); i++) {
            paddingString += paddingChar;
        }

        if (isRightPadded) {
            return (this + paddingString);
        } else {
            return (paddingString + this);
        }
    } else {
        return this;
    }
};

//获取url中参数
//获取url中的参数
function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    //if (r != null) return unescape(r[2]);
    if (r != null) return decodeURI(r[2]);
    return null; //返回参数值
}


//创建一个遮罩层 0为创建 1为移除
function setmask(flag) {
    switch (parseInt(flag)) {
        case 0:
            if (document.getElementById("showCommonMaskDiv_in_AllPage")) {
                return;
            }
            $("<div id='showCommonMaskDiv_in_AllPage' class='divmask' style='position: fixed;top:0;left:0;width:100%;height:100%;background-color: rgba(0,0,0,0.6);'></div>").appendTo($("body"));
            break;
        case 1:
            $(".divmask").remove();
            break;
    }
}

//
function showsurelayer(msg) {
    $("<div style='margin: 15% auto;background-color: #fff;width: 20%;padding: 20px;text-align: center;border-radius: 5px;'><p style='margin: 22px auto; font-size: 16px;'>" + msg + "</p><p><button class='btnkswc'>已完成</button>&nbsp;&nbsp;&nbsp;<button class='btnkswc'>未完成</button></p></div>").appendTo($(".divmask"));
    $(".btnkswc").on("click", function () {
        location.reload();

    });
}
/**
 * 让ie支持placeholder
 * @param element
 */
var supportPlaceholderNoRequireType = function(element){
    if(isnull(element)){
        element = 'input';
    }
    var doc=document,
        inputs=doc.getElementsByTagName(element),
        supportPlaceholder='placeholder'in doc.createElement(element),
        placeholder = function(input){
            var text=input.getAttribute('placeholder'),
                defaultValue=input.defaultValue;
            if(defaultValue==''){
                input.value=text
            }
            input.onfocus=function(){
                if(input.value===text)
                {
                    this.value=''
                }
            };
            input.onblur=function(){
                if(input.value===''){
                    this.value=text
                }
            }
        };
    if(!supportPlaceholder){
        for(var i=0,len=inputs.length;i<len;i++){
            var input=inputs[i],
                text=input.getAttribute('placeholder');
            if((input.type==='text' || input.type==='textarea')&&text){
                placeholder(input)
            }
        }
    }
}
/**
 * 弱提示，1.5s后消失
 * @param msg
 */
function alertMsg(msg){
    layer.open({
        title:["消息提示",'font-size:18px;font-weight:bold'],
        content:msg,
        offset: '335px',
        closeBtn: 0,
        icon: 6,
        btn:0,
        shade: 0,
        area: ['260px', 'auto'],
        time: 1500
    });
}
/**
 * 设置定时器
 * @param buthis 按钮对象
 * @param tims 时间
 */
function setClocking(buthis,tims){
    var countn = tims;
    buthis.text(countn + 's');
    buthis.addClass('stu-noSend');
    //定时器
    var counttime = setInterval(function () {
        countn--;
        buthis.text(countn + 's');
        if (countn < 0) {
            clearClockingTime(buthis,counttime);
        }
    }, 1000);
    return counttime;
}
/**
 * 清除定时器
 * @param buthis 按钮对象
 * @param counttime 定时对象
 */
function clearClockingTime(buthis,counttime) {
    clearInterval(counttime);
    buthis.text('发送验证码');
    buthis.removeClass('stu-noSend');
}

function showmsglayer(msg) {
    if (document.getElementById("showMessageCommonDiv_in_AllPage")) {
        return;
    }
    $("<div id='showMessageCommonDiv_in_AllPage' style='margin: 15% auto;background-color: #fff;width: 20%;padding: 20px;text-align: center;border-radius: 5px;'><p style='margin: 22px auto; font-size: 16px;'>" + msg + "</p><label></label></div>").appendTo($(".divmask"));
}

//图片点击显示大图
$.fn.showlargepic = function () {
    this.on("click", function () {
        $(".imgpreshow").remove();
        var cimg = $("<img class='imgpreshow' src='" + $(this).attr("src") + "' style='height:400px; position: fixed; margin:auto;left:0; right:0; top:20%;display: none;cursor: pointer;z-index: 999999;' />")
            .on('click', function () {
                $(this).fadeOut();
            });
        $("body", parent.document).append(cimg);
        cimg.fadeIn();
    });
};
/**
 * 让ie支持maxlength
 * @param callback
 */
$.fn.supportMaxlength = function(callback){
    this.on("keyup change keydown",function(){
        var _mthis = $(this);
        var thisval=_mthis.val();
        _mthis.val(thisval.substring(0,parseInt(_mthis.attr('maxlength'))));
        if(!isnull(callback)){
            callback(_mthis);
        }
    });
}
//ajax统一请求
function requestService(url, param, callback) {
    $.ajax({
        type: "POST",
        url: url,
        data: param,
        success: function (msg) {
            if (callback) {
                callback(msg);
            }
        }
    });
}


/**
 *
 * 格式化日期
 *
 * @author suyin 2016-03-02
 *
 * */
Date.prototype.Format = function (fmt) {
    var o = {
        "M+": this.getMonth() + 1,                 //月份
        "d+": this.getDate(),                    //日
        "h+": this.getHours(),                   //小时
        "m+": this.getMinutes(),                 //分
        "s+": this.getSeconds(),                 //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        "S": this.getMilliseconds()             //毫秒
    };
    if (/(y+)/.test(fmt))
        fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}


//父级iframe自适应
function fitiframe() {
    var frame = parent.document.getElementById('iframepage'),
        win = frame.contentWindow,
        doc = win.document,
        html = doc.documentElement,
        body = doc.body;
    //console.log(body.scrollHeight);

    //alert(document.body.clientHeight);
    $("#iframepage", parent.document).height(body.scrollHeight + 100);
}

//初始化分页
function initPager(pagerid, totalcount, callback, pageSize) {

    var sources = function () {
        var result = [];

        for (var i = 0; i < totalcount; i++) {
            result.push(i + 1);
        }

        return result;
    }();

    var options = {
        dataSource: sources,
        callback: function (resp, pagin) {

            if (callback) {
                callback(resp, pagin);
            }
        },
        pageSize: pageSize,
        showGoInput: true,
        showGoButton: true
        //className: 'paginationjs-theme-blue',
    };

    // console.info(options);
    $('#' + pagerid).pagination(options);

}

//获取文本宽度
var textWidth = function (text) {
    var sensor = $('<pre>' + text + '</pre>').css({display: 'none'});
    $('body').append(sensor);
    var width = sensor.width();
    sensor.remove();
    return width;
};
//重写Jquery Ajax函数
(function ($) {
    //备份jquery的ajax方法
    var _ajax = $.ajax;

    //重写jquery的ajax方法
    $.ajax = function (opt) {
        //备份opt中error和success方法
        var fn = {
            error: function (XMLHttpRequest, textStatus, errorThrown) {
            },
            success: function (data, textStatus) {
            }
        }
        if (opt.error) {
            fn.error = opt.error;
        }
        if (opt.success) {
            fn.success = opt.success;
        }

        //扩展增强处理
        var _opt = $.extend(opt, {
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                //错误方法增强处理
                fn.error(XMLHttpRequest, textStatus, errorThrown);
            },
            success: function (data, textStatus, XMLHttpRequest) {
                //成功回调方法增强处理
                //console.info(data);
                if (data.toString().indexOf("student login page") != -1) {
                    //alert("登录失效，请重新登录");
                    window.top.location.href = "/login.jsp";
                    //console.info(XMLHttpRequest);
                }
                fn.success(data, textStatus);
            },
            beforeSend: function (XHR) {
                //提交前回调方法
                //layer.msg('加载中', {icon: 16,shade: [0.1,'#fff'],time : 0,offset : ['200px' , '40%']});

            },
            complete: function (XHR, TS) {
                //请求完成后回调函数 (请求成功或失败之后均调用)。
                //layer.msg('加载成功!', {icon: 1});
            }
        });
        _ajax(_opt);
    };
})(jQuery);
/**
 * 上传附件兼容ie
 * @param status 题的状态
 * @param currentfileArr  上传的文件的数组
 * @param acceId 附件Id
 * @param callback 上传完成后的回调函数
 */
function setAttachUploading(status,currentfileArr,acceId,projectn,userid,callback){
    if(status == 0){
        $('<button id="i_select_files"></button><span class="spfilename"></span><div id="i_stream_files_queue"> </div>').appendTo(".section-body-syn");
        var config = {
            postVarsPerFile : { projectName: projectn, fileType: "2", userId: userid},
            onComplete: function(file) {
                //附件的id
                var attachId =  $.parseJSON(file.msg).message ;
                currentfileArr.push({
                    idx: parseInt($("#i_select_files").siblings().find(".cidx").text() ),
                    fname: file.name
                });
                acceId = attachId;
                if(!isnull(callback)){
                    callback(currentfileArr,acceId);
                }
                $(".index-qus[data-index=" + (parseInt($(".cidx").text()) - 1) + "]").trigger("click");
                $("#i_select_files").next(".spfilename").html('<a href="/attachmentCenter/download?aid=' +attachId+' ">'+file.name+'</a>');
                layer.msg('上传成功!', {icon: 1, time: 2500});
            }
//          , onQueueComplete: function(msg) {console.info(msg);}
        };
        var _t = new Stream(config);
    }else{
        $('<button id="i_select_files" disabled="disabled">上传</button><span class="spfilename"></span><div id="i_stream_files_queue"> </div>').appendTo(".section-body-syn");
    }
    $("#i_select_files").on("click", function () {
        if (status == 0) {
            if ((navigator.userAgent.indexOf('MSIE') >= 0)
                && (navigator.userAgent.indexOf('Opera') < 0)){
                var version = swfobject.getFlashPlayerVersion();
                if (document.getElementById && version["major"] <= 0){
                    layer.alert("您还未安装flash Player,请安装 flash Player!");
                }
            }

        }
    });
}
/**
 * 校验输入值不能为空，值为placeholder的也视为没有输入值
 * @param inputobj
 * @param errobj
 * @param errtxt
 * @returns {boolean}
 */
function validNullPlaceholder(inputobj,errobj,errtxt){
    if (inputobj.val() == inputobj.attr('placeholder') || inputobj.val().length == 0) {
        errobj.html('<i class="iconfont">&#xe63d;</i>' +errtxt+ '不能为空');
        return false;
    } else {
        errobj.html('');
        return true;
    }
}
