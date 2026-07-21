<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	/*每个页面公共css */
	page{
		position: relative;
		margin: 0 auto;
		width: 720rpx;
	}
	.hide_scrollbar{
			overflow: auto;
	}
	.hide_scrollbar::-webkit-scrollbar{
				display: none;
	}
	/* #ifdef H5 */
	::v-deep.hide_scrollbar{
		overflow: auto;
		::-webkit-scrollbar{
			display: none;
		}
	}
	/* #endif */
</style>
