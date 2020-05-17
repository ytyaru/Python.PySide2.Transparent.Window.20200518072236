Run() {
	local THIS="$(cd "$(dirname "$0")"; pwd)"
	cd "$THIS"
	# 不安定
	# * スクリプトでは動作しない？ 端末で直接コマンド入力して実行しないとダメかも
	# * 1回目だと背景が黒くなる？ 2回目で透明になることがある
	xcompmgr -c
	./transparent.py
}
Run

