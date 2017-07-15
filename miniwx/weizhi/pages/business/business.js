//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    motto: 'Hello World',
    userInfo: {}
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    console.log('onLoad')
    var that = this;
    //调用应用实例的方法获取全局数据
    app.getUserInfo(function(userInfo){
      //更新数据
      that.setData({
        userInfo:userInfo
      })
    })
  },
  calldemo: function() {
    wx.makePhoneCall({
      phoneNumber: '15010324628',
      success() {
        console.log('success');
      },
      fail() {
        console.log('fail');
      },
      complete() {
        console.log('complete');
      }
    })
  },
  paydemo() {
    wx.requestPayment({
      'timeStamp': '',
      // 'timeStamp': +new Date(),
      'nonceStr': '',
      'package': '',
      'signType': 'MD5',
      'paySign': '',
      success: function(res){
      },
      fail: function(res){
      }
    })
  }
});