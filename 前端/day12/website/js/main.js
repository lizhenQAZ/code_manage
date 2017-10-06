// $(function () {
//     // 获取所有的图片的li
//     var $lis = $(".slides li");

//     var $li1_5 = $lis.not(":first");//去掉第一个 还剩1到5

//     // 把12345这五个li 移动到left 760
//     $li1_5.css({ left: 760 });

//     // 获取图片的数量
//     var length = $lis.length;
//     // 根据数量来动态添加小圆点
//     for (var i = 0; i < length; i++) {
//         // 生成一个空的li对象
//         var newLi = $("<li>")
//         if (i == 0) {
//             // 第0个小圆点高亮
//             newLi.addClass("active");
//         }
//         // 把li对象添加到父级ul里
//         newLi.appendTo($(".points"));
//     }

//     var nowIndex = 0;//当前 页面索引
//     var clickIndex = 0;//点击的页面的索引


//     // 获取所有的小圆点的li对象
//     var roundLis = $(".points li");
//     // 小圆点的点击事件
//     roundLis.click(function () {
//         // 0123456   比如点击了第3个
//         clickIndex = $(this).index();
//         move();//移动
//     });


//     var isMove = false;//初始一个变量 记录是否正在移动

//     // 左箭头的点击事件
//     $(".leftarrow").click(function () {
//         // 阻止快速的多次点击
//         if (isMove) {
//             return;
//         }
//         isMove = true;
//         clickIndex--;
//         if (clickIndex < 0) {
//             // 向左移动到第0个时  改变到最后一个 有移动效果
//             clickIndex = length - 1;
//         }
//         fnMoveToRight();//点击左箭头会一直向右滑动 不需要判断方向 直接调用
//     });

//     // 右箭头的点击事件
//     $(".rightarrow").click(function () {
//         // 阻止快速的多次点击
//         if (isMove) {
//             return;
//         }
//         isMove = true;
//         clickIndex++;
//         if (clickIndex > length - 1) {
//             // 当向右移动到最后时 恢复到第0个 可以循环
//             clickIndex = 0;
//         }
//         fnMoveToLeft();//移动
//     });

//     // 每1s 向左滑动一张 这里模拟一次右箭头的点击
//     var timer = setInterval(function () {
//         $(".rightarrow").click();
//     }, 2000);

//     // 鼠标移入移出的事件
//     $(".slides-con").hover(function () {
//         // enter
//         clearInterval(timer);
//     }, function () {
//         // leave
//         timer = setInterval(function () {
//             $(".rightarrow").click();
//         }, 2000);
//     });

//     /**
//      * 移动的方法
//      */
//     function move() {
//         if (clickIndex == nowIndex) {
//             // 点击原位置 不执行
//             return;
//         }
//         // 判断点击的页面索引和当前页面索引的大小
//         if (clickIndex > nowIndex) {
//             fnMoveToLeft();//向左滑动
//         } else if (clickIndex < nowIndex) {
//             fnMoveToRight();//向右滑动
//         }
//     }

//     /**
//      * 向左滑动的方法
//      */
//     function fnMoveToLeft() {
//         // 把要移动进来的图片 放到left 760的位置
//         $lis.eq(clickIndex).css({ left: 760 });
//         // 把要移动进来的图片 移动到 left :0 的位置
//         $lis.eq(clickIndex).animate({ left: 0 }, moveStop);
//         // 当前显示的图片 移动出去 left:-760
//         $lis.eq(nowIndex).animate({ left: -760 }, moveStop);

//         nowIndex = clickIndex;//每次移动完 nowIndex更新
//         // 当前小圆点高亮
//         roundLis.eq(nowIndex).addClass("active").siblings().removeClass("active");
//     }
//     /**
//      * 向右滑动的方法
//      */
//     function fnMoveToRight() {
//         // 把要移动进来的图片 放到left -760的位置
//         $lis.eq(clickIndex).css({ left: -760 });
//         // 把要移动进来的图片 移动到 left :0 的位置
//         $lis.eq(clickIndex).animate({ left: 0 }, moveStop);
//         // 当前显示的图片 移动出去 left:760
//         $lis.eq(nowIndex).animate({ left: 760 }, moveStop);
//         nowIndex = clickIndex;//每次移动完 nowIndex更新  
//         // 当前小圆点高亮
//         roundLis.eq(nowIndex).addClass("active").siblings().removeClass("active");
//     }

//     // 动画停止 isMove恢复false
//     function moveStop() {
//         isMove = false;
//     }

// })

$(function () {
    // 获取幻灯片对象
    var $oSlides = $('.slides li');
    // 记录幻灯片的长度
    var iLength = $oSlides.length;
    // alert(iLength);
    // 获取小圆点对象
    var $oPoints = $('.points');
    for (var i = 0; i < iLength; i++) {
        // 获取小圆点
        var $oCircles = $('<li>');
        if (i == 0) {
            $oCircles.addClass('active');
        }
        $oCircles.appendTo($oPoints);
    }



    // alert($oPoints.html());
    // 设置图片的位置
    $oSlides.not(':first').css({ left: 760 });



    // 代理小圆点事件
    // 用两个变量记录原来的位置
    var iClickIndex = 0;
    var iNowIndex = 0;
    // 小圆点点击
    $oPoints.delegate('li', 'click', function () {
        iClickIndex = $(this).index();
        // alert(iClickIndex);
        move();
    });

    // 设置定时器
    var oTimer = null;
    // 左箭头点击
    var $oLeftArrow = $(".leftarrow");
    $oLeftArrow.click(function () {
        clearTimeout(oTimer);
        oTimer = setTimeout(function () {
            if (iClickIndex <= 0) {
                iClickIndex = iLength - 1;
            } else {
                iClickIndex--;
            }
            $oSlides.eq(iNowIndex).animate({ left: 760 });
            iNowIndex = iClickIndex;
            $oSlides.eq(iNowIndex).css({ left: -760 });
            $oSlides.eq(iNowIndex).animate({ left: 0 });
            $oPoints.find('li').eq(iNowIndex).addClass('active').siblings().removeClass('active');
        }, 1000);
    });
    // 右箭头点击
    var $oRightArrow = $(".rightarrow");
    $oRightArrow.click(function () {
        clearTimeout(oTimer);
        oTimer = setTimeout(function () {
            if (iClickIndex >= iLength - 1) {
                iClickIndex = 0;
            } else {
                iClickIndex++;
            }
            $oSlides.eq(iNowIndex).animate({ left: -760 });
            iNowIndex = iClickIndex;
            $oSlides.eq(iNowIndex).css({ left: 760 });
            $oSlides.eq(iNowIndex).animate({ left: 0 });
            $oPoints.find('li').eq(iNowIndex).addClass('active').siblings().removeClass('active');
        }, 1000);
    });

    // 定时自动向右翻页
    var oTimer1 = setInterval(function () {
        $oRightArrow.click();
    }, 2000);
    // 鼠标进入时翻页停止
    $oSlides.mouseenter(function () {
        clearInterval(oTimer1);
    });
    // 鼠标离开时翻页重新开始
    $oSlides.mouseleave(function () {
        oTimer1 = setInterval(function () {
            $oRightArrow.click();
        }, 2000);
    });

    function move() {
        // alert(iNowIndex);
        if (iClickIndex == iNowIndex) {
            return;
        }
        if (iClickIndex > iNowIndex) {
            // alert(iNowIndex)
            $oSlides.eq(iNowIndex).animate({ left: -760 });
            iNowIndex = iClickIndex;
            $oSlides.eq(iNowIndex).animate({ left: 0 });
        } else {
            $oSlides.eq(iNowIndex).animate({ left: 760 });
            iNowIndex = iClickIndex;
            $oSlides.eq(iNowIndex).animate({ left: 0 });
        }
        $oPoints.find('li').eq(iNowIndex).addClass('active').siblings().removeClass('active');
    }
});
