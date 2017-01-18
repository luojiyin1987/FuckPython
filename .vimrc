cmap w!! %!sudo tee > /dev/null %
set paste
set tabstop=4
set expandtab
set fileformat=unix
set nobomb
set ff=unix
set ambiwidth=double
set shiftwidth=4
filetype plugin on
set  nocompatible
set  completeopt=preview
set ai
set hls 
set nu
syntax on
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
let g:ackprg = 'ag --nogroup --nocolor --column'
 """"""""""""""""""""""
    "Quickly Run
    """"""""""""""""""""""
    map <F5> :call CompileRunGcc()<CR>
    func! CompileRunGcc()
        exec "w"
        if &filetype == 'c'
            exec "!g++ % -o %<"
            exec "!time ./%<"
        elseif &filetype == 'cpp'
            exec "!g++ % -o %<"
            exec "!time ./%<"
        elseif &filetype == 'java'
            exec "!javac %"
            exec "!time java %<"
        elseif &filetype == 'sh'
            :!time bash %
        elseif &filetype == 'python'
            exec "!time python2.7 %"
        elseif &filetype == 'html'
            exec "!firefox % &"
        elseif &filetype == 'go'
    "        exec "!go build %<"
            exec "!time go run %"
        elseif &filetype == 'mkd'
            exec "!~/.vim/markdown.pl % > %.html &"
            exec "!firefox %.html &"
        endif
    endfunc
 " vundle 环境设置
 filetype off
 set rtp+=~/.vim/bundle/Vundle.vim
 " vundle 管理的插件列表必须位于 vundle#begin() 和 vundle#end() 之间
 call vundle#begin()
 Plugin 'VundleVim/Vundle.vim'
 Plugin 'altercation/vim-colors-solarized'
 Plugin 'tomasr/molokai'
 Plugin 'vim-scripts/phd'
 Plugin 'Lokaltog/vim-powerline'
 Plugin 'octol/vim-cpp-enhanced-highlight'
 Plugin 'nathanaelkane/vim-indent-guides'
 Plugin 'derekwyatt/vim-fswitch'
 Plugin 'kshenoy/vim-signature'
 Plugin 'vim-scripts/BOOKMARKS--Mark-and-Highlight-Full-Lines'
 Plugin 'majutsushi/tagbar'
 Plugin 'vim-scripts/indexer.tar.gz'
 Plugin 'vim-scripts/DfrankUtil'
 Plugin 'vim-scripts/vimprj'
 Plugin 'dyng/ctrlsf.vim'
 Plugin 'terryma/vim-multiple-cursors'
 Plugin 'scrooloose/nerdcommenter'
 Plugin 'vim-scripts/DrawIt'
 Plugin 'SirVer/ultisnips'
 Plugin 'Valloric/YouCompleteMe'
 Plugin 'derekwyatt/vim-protodef'
 Plugin 'scrooloose/nerdtree'
 Plugin 'fholgado/minibufexpl.vim'
 Plugin 'gcmt/wildfire.vim'
 Plugin 'sjl/gundo.vim'
 Plugin 'Lokaltog/vim-easymotion'
 Plugin 'suan/vim-instant-markdown'
 Plugin 'lilydjwg/fcitx.vim'
 Plugin 'ShowTrailingWhitespace'
 Plugin 'ctrlp.vim'
 Plugin 'mileszs/ack.vim'
 " 插件列表结束
 call vundle#end()
 let g:ackprg = 'ag --nogroup --nocolor --column'
 let g:ctrlp_map = '<c-p>' 
 let g:ctrlp_cmd = 'CtrlP'
 " 设置过滤不进行查找的后缀名 
 let g:ctrlp_custom_ignore = '\v[\/]\.(git|hg|svn|pyc)$' 
 nmap <F8> :TagbarToggle<CR> 
 filetype plugin indent on

