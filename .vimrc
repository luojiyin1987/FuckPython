set number
set expandtab
set tabstop=8
set shiftwidth=4
set softtabstop=4
set autoindent

syntax enable

"F5 运行python程序
au BufRead *.py map <buffer> <F5> :w<CR>:!/usr/bin/env python % <CR>
filetype  on
let python_highlight_all=1
syntax on
