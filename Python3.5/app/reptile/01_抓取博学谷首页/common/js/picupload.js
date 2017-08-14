(function($) {
	var isinit = false;
	$.fn.extend({
		picupload : function(options) {
			var defaults = {
				url : "/group/index/head",
				callback : null,
				imagebox : ".imageBox",
				file : "#file",
				btnfile : ".btnfile",
				btnZoomIn : "#btnZoomIn",
				btnZoomOut : "#btnZoomOut",
				btncancle : ".btncancle",
				close_x : ".close_x",
				btnsave : ".btnsave",
				imgdataParamName : "image",
				extendParam : {},
				cropboxOp : {
					thumbBox : '.thumbBox',
					spinner : '.spinner',
					imgSrc : ''
				}
			};
			var options = $.extend(defaults, options);
			var _this;
			if ($(this).length > 0) {
				_this = $($(this).get(0));
			}
			_this.show();
			var imageBox = _this.find(options.imagebox);
			var cropper = imageBox.cropbox(options.cropboxOp);
			if (!isinit) {
				isinit=true;
				_this.on("click",function(e){
					 e.stopPropagation();
				});
				_this.find(options.file).on('click', function(e) {
					 e.stopPropagation();
				})
				// 注册file改变事件
				_this.find(options.file).on('change', function(e) {
					 e.stopPropagation();
					var reader = new FileReader();
					reader.onload = function(e) {
						options.cropboxOp.imgSrc = e.target.result;
						cropper = imageBox.cropbox(options.cropboxOp);
					}
					reader.readAsDataURL(this.files[0]);
					console.info(cropper.getDataURL());
					this.files = [];
				})
				// 注册点击按钮事件
				_this.find(options.btnfile).on("click", function(e) {
					 e.stopPropagation();
					_this.find(options.file).trigger("click");
				});
				_this.find(options.btnZoomIn).on('click', function(e) {
					 e.stopPropagation();
					// alert($('.imageBox').css("background-image"));
					if (imageBox.css("background-image") != "none") {
						cropper.zoomIn();
					}
				});

				_this.find(options.btnZoomOut).on('click', function(e) {
					 e.stopPropagation();
					if (imageBox.css("background-image") != "none") {
						cropper.zoomOut();
					}
				});
				//关闭
				_this.find(options.close_x).on("click", function(e) {
					 e.stopPropagation();
					_this.hide();
					 cropper.image.width=0;
					 cropper.image.height=0;
					 cropper.destroy= true;
					imageBox.css("background-image", "")
					_this.find(options.file).val("");
				});
				//取消
				_this.find(options.btncancle).on("click", function(e) {
					 e.stopPropagation();
					 cropper.image.width=0;
					 cropper.image.height=0;
					 cropper.destroy= true;
					imageBox.css("background-image", "")
					_this.find(options.file).val("");
				});
				_this.find(options.btnsave).on("click", function(e) {
					 e.stopPropagation();
					$('#btnCrop').trigger("click");
					var img;
					if (imageBox.css("background-image") != "none" && !cropper.destroy) {
						img = cropper.getDataURL();
					}else {
						layer.alert("请上传图片！",{offset : ['300px' , '40%']});
						return;
					}
					
					if (img) {
						var loadIndex =  layer.msg('上传中...', {icon: 16,shade: [0.6,'#fff'],time : 0,offset : ['300px' , '40%']});;
						options.extendParam[options.imgdataParamName] = img;
						$.ajax({
							type : "post",
							url : options.url,
							data : options.extendParam,
							success : function(data) {
								if (options.callback != null) {
									options.callback(data);
								}
								_this.hide();
								imageBox.css("background-image", "")
								_this.find(options.file).val("");
								layer.close(loadIndex);
							},
							error:function(){
								layer.close(loadIndex);
							}
						})
					} else {
						layer.alert("请上传图片！",{offset : ['300px' , '40%']});
					}

				});

			}
			return _this;
		}
	});

})(jQuery);