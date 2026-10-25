from pathlib import Path
from PIL import Image,ImageDraw
import xml.etree.ElementTree as E
import sys
C=Path(sys.argv[1])
textures=C/'textures/ui/one_key_lights'; textures.mkdir(parents=True,exist_ok=True)
root=E.Element('w')
for n in range(1,6):
    for i in range(1,n+1):
        size=512
        im=Image.new('RGBA',(size,size)); draw=ImageDraw.Draw(im)
        a=-90+(i-1)*360/n
        draw.pieslice((2,2,509,509),a-180/n+1,a+180/n-1,fill='white')
        draw.ellipse((size*.33,size*.33,size*.67,size*.67),fill=(0,0,0,0))
        im=im.resize((256,256),Image.Resampling.LANCZOS)
        name=f'ring_{n}_{i}'; im.save(textures/(name+'.dds'))
        f=E.SubElement(root,'file',name='ui\\one_key_lights\\'+name)
        E.SubElement(f,'texture',id='oklc_'+name,x='0',y='0',width='256',height='256')
dot=Image.new('RGBA',(32,32)); ImageDraw.Draw(dot).ellipse((1,1,30,30),fill='white'); dot.save(textures/'dot.dds')
f=E.SubElement(root,'file',name='ui\\one_key_lights\\dot'); E.SubElement(f,'texture',id='oklc_dot',x='0',y='0',width='32',height='32')
desc=C/'configs/ui/textures_descr/ui_one_key_lights.xml'; desc.parent.mkdir(parents=True,exist_ok=True); desc.write_text(E.tostring(root,encoding='unicode'))
(C/'configs/ui/ui_one_key_lights.xml').write_text('''<w>
<sector x="0" y="0" width="160" height="160" stretch="1"><texture>oklc_ring_5_1</texture></sector>
<label x="0" y="0" width="64" height="16"><text font="letterica16" align="c" vert_align="c" r="225" g="225" b="225" a="255"/></label>
<dot x="0" y="0" width="4" height="4" stretch="1"><texture>oklc_dot</texture></dot>
<cancel x="0" y="0" width="24" height="20"><text font="letterica16" align="c" r="150" g="165" b="165" a="180"/></cancel>
</w>''')
