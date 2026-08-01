function pageTo(url) {
	try {
		uni.navigateTo({
			url: url,
			animationType: 'zoom-fade-out'
		});
	} catch (error) {
		console.error('Navigation error:', error);
		// 这里可以添加错误处理逻辑，例如显示一个错误提示给用户
	}
}

export {
	pageTo
}