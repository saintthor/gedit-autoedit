


# gedit-autoedit
gedit is a good text editor for ubuntu.

this an example to edit content in gedit with it's python console.
in python console, there is a 'window' parameter. with code:

>>> doc = window.get_active_document()

>>> start, end = doc.get_bounds()

>>> Text = doc.get_text( start, end, True )

you can get the content of the active file. and with:

>>> doc.set_text( Text )

you can update the content.


## Start
copy the gedit.py to one of sys.path then may import it from python console.

## AutoReplace
you may change the content with the AutoReplace function. type codes in python console:

from gedit import AutoReplace as r
def myReplace( oldText ):
	return 'new text.'
r( window, myReplace )

the content will be changed.


## AutoFormat
the AutoFormat function is for chinese user.

AutoFormat 用于将半角标点转为全角。如果 JoinLines = True，将删除所有单个的 \n。因为我处理的文档经常有多余的硬回车，删除单个的，保留连续多个的 \n，才能转为正常格式。用法：

from gedit import AutoFormat as f
f( window )

## AutoNote
至于 AutoNote 是处理文章中注释内容的，大多数人应该用不着。


