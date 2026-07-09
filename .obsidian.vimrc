imap jj <Esc>



" 让 :q! 变为关闭当前标签页/窗口
exmap q! obcommand workspace:close
" (保险起见，把普通的 :q 也绑上同一个功能)
exmap q obcommand workspace:close

" 让 :wq 变为切换到下一个标签页 (Focus next tab)
exmap wq obcommand workspace:next-tab
