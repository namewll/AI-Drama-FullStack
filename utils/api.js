import {$http} from "@escook/request-miniprogram"
uni.$http=$http
$http.baseUrl="http://127.0.0.1:5001"

$http.beforeRequest=()=>{
	uni.showLoading({
		"title":"数据加载中..."
	})
}
$http.afterRequest=()=>{
	uni.hideLoading()
}