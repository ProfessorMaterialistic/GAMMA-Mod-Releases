from pathlib import Path
import sys, math, xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).parent))
WORK=Path(__file__).resolve().parents[1];ROOT=WORK/'inputs';ONE=WORK/'build/One Key Light Rebuild'
def read(p): return p.read_text(encoding='utf-8-sig')
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8',newline='\n')
def reference(pkg,name): return read(ROOT/'mods/One Key Light v.1.3/gamedata/scripts'/name)
from PIL import Image,ImageDraw,ImageFont
names=['weapon_light','weapon_ir','headlamp','headlamp_ir','laser','nvg','linked','auto','on','off','battery','locked','missing']
atlas=Image.new('RGBA',(512,256),(0,0,0,0))
for style in range(2):
    for i,name in enumerate(names):
        tile=Image.new('RGBA',(256,256));d=ImageDraw.Draw(tile);w=10 if style==0 else 7
        def line(points):d.line([(x*4,y*4) for x,y in points],fill='white',width=w,joint='curve')
        def rect(box):d.rectangle(tuple(v*4 for v in box),outline='white',width=w)
        def ellipse(box):d.ellipse(tuple(v*4 for v in box),outline='white',width=w)
        def poly(points):d.polygon([(x*4,y*4) for x,y in points],fill='white')
        if name in ['weapon_light','weapon_ir']:
            rect((9,23,30,41));rect((28,20,36,44));line([(13,19),(13,13),(26,13),(26,19)])
            for y in [19,32,45]:line([(40,32),(56,y)])
            if name=='weapon_ir':line([(8,51),(18,51)]);line([(23,51),(33,51)]);line([(38,51),(48,51)])
        elif name in ['headlamp','headlamp_ir']:
            line([(9,37),(9,22),(16,14),(48,14),(55,22),(55,37)])
            rect((9,29,55,41));ellipse((24,23,40,45));ellipse((29,28,35,40))
            if name=='headlamp_ir':line([(15,50),(24,50)]);line([(28,50),(37,50)]);line([(41,50),(50,50)])
        elif name=='laser':
            rect((8,24,29,40));line([(32,32),(52,32)]);ellipse((46,26,58,38));line([(52,15),(52,23)]);line([(52,41),(52,49)])
        elif name=='nvg':
            ellipse((8,24,29,48));ellipse((35,24,56,48));line([(18,22),(18,13),(46,13),(46,22)]);line([(29,34),(35,34)])
        elif name=='linked':
            ellipse((7,23,34,42));ellipse((30,23,57,42));line([(22,32),(42,32)])
        elif name=='auto':line([(13,49),(29,13),(34,13),(51,49)]);line([(21,34),(43,34)])
        elif name=='on':ellipse((10,10,54,54));poly([(26,20),(41,32),(26,44)])
        elif name=='off':ellipse((10,10,54,54));line([(23,23),(41,41)]);line([(41,23),(23,41)])
        elif name=='battery':
            rect((9,20,52,44));rect((52,27,57,37));rect((15,26,23,38));rect((28,26,36,38));rect((41,26,46,38))
        elif name=='locked':ellipse((21,10,43,35));rect((15,27,49,53));line([(32,36),(32,45)])
        elif name=='missing':
            line([(8,21),(8,8),(21,8)]);line([(43,8),(56,8),(56,21)]);line([(8,43),(8,56),(21,56)]);line([(43,56),(56,56),(56,43)])
            line([(23,23),(41,41)]);line([(41,23),(23,41)])
        tile=tile.resize((64,64),Image.Resampling.LANCZOS)
        atlas.alpha_composite(tile,((i%8)*64,(i//8)*64+style*128))
dest=ONE/'Core/gamedata/textures/ui/ui_one_key_light_icons.dds';dest.parent.mkdir(parents=True,exist_ok=True)
atlas.save(dest)
atlas.save(WORK/'reports/icon-atlas.png')
xml=ET.Element('w');file=ET.SubElement(xml,'file',name='ui\\ui_one_key_light_icons')
for style in range(2):
    for i,name in enumerate(names):
        ET.SubElement(file,'texture',id='oklc_icon_'+name+('_minimal' if style else ''),x=str((i%8)*64),y=str((i//8)*64+style*128),width='64',height='64')
write(ONE/'Core/gamedata/configs/ui/textures_descr/ui_one_key_light_icons.xml',ET.tostring(xml,encoding='unicode'))
ui=ET.fromstring(read(ONE/'Core/gamedata/configs/ui/ui_one_key_lights.xml'))
for node in ui.findall('icon'):ui.remove(node)
icon=ET.Element('icon',x='0',y='0',width='32',height='32',stretch='1')
# Constructing native controls must work before checking the optional atlas.
ET.SubElement(icon,'texture').text='oklc_dot'
ui.insert(list(ui).index(ui.find('sector')),icon)
ET.indent(ui,space='  ')
write(ONE/'Core/gamedata/configs/ui/ui_one_key_lights.xml',ET.tostring(ui,encoding='unicode'))
s=reference('one','one_key_lights_menu.script')
s=s.replace('local bound=cfg.tap==a.id or cfg.double==a.id or cfg.hold==a.id','local bound=one_key_lights_actions.radial_id(cfg.tap)==a.id or one_key_lights_actions.radial_id(cfg.double)==a.id or one_key_lights_actions.radial_id(cfg.hold)==a.id',1)
s=s.replace('local short={','''-- Minimal uses its own thin 8x11 lock; Tactical keeps the original 12x15 outline.
local minimal_lock_parts={{-2,-5,4,1},{-3,-4,1,4},{2,-4,1,4},{-4,0,8,1},{-4,1,1,5},{3,1,1,5},{-4,5,8,1},{0,2,1,2}}
local short={''',1)
s=s.replace('for j,rect in ipairs(lock_parts) do','for j,rect in ipairs(self.icon_style==2 and minimal_lock_parts or lock_parts) do',1)
s=s.replace('    self.locks={}','    self.locks={}\n    self.icons,self.badges,self.routes={},{},{}',1)
s=s.replace('    for i=1,5 do\n        self.rows[i]=xml:InitStatic("sector",self)','''    -- Native UI draws children in attachment order: backgrounds first.
    for i=1,5 do self.rows[i]=xml:InitStatic("sector",self) end
    for i=1,5 do
        self.icons[i]=xml:InitStatic("icon",self)
        self.badges[i]=xml:InitStatic("icon",self)
        self.routes[i]=xml:InitStatic("label",self)''',1)
s=s.replace('    self.target=target;', '''    self.label_mode=tonumber(cfg.radial_labels) or 1
    self.icon_style=tonumber(cfg.icon_style) or 1
    self.use_icons=self.label_mode~=3 and one_key_lights_icons.ready()
    if not self.use_icons then self.label_mode=3 end
    if self.use_icons then size=math.max(220,size) end
    self.target=target;''',1)
s=s.replace('    if target=="headlamp_situational" or target=="weapon_situational" and not one_key_lights_actions.module("bling_light_control") then','    if target and not one_key_lights_display.state(target).supports_auto then',1)
s=s.replace('        self.rows[i]:Show(visible);', '''        self.icons[i]:Show(visible and self.use_icons)
        self.badges[i]:Show(visible and self.use_icons)
        self.routes[i]:Show(visible)
        self.rows[i]:Show(visible);''',1)
s=s.replace('            self.labels[i]:SetWndPos(vector2():set(x-32*self.xscale,y-22))','''            self.icons[i]:SetWndPos(vector2():set(x-15*self.xscale,y-36))
            self.icons[i]:SetWndSize(vector2():set(30*self.xscale,30))
            local semantic=self.target and self.items[i].id or one_key_lights_icons.action(self.items[i].id)
            local icon=one_key_lights_icons.get_icon(semantic,self.icon_style)
            if self.use_icons and icon then
                local ok=pcall(function() self.icons[i]:InitTexture(icon.texture) end)
                if not ok then self.use_icons=false;self.label_mode=3 end
            end
            self.badges[i]:SetWndPos(vector2():set(x+17*self.xscale,y-29))
            self.badges[i]:SetWndSize(vector2():set(14*self.xscale,14))
            self.routes[i]:SetWndPos(vector2():set(x-40*self.xscale,y+25))
            self.routes[i]:SetWndSize(vector2():set(80*self.xscale,16))
            self.labels[i]:Show(self.label_mode~=2)
            self.labels[i]:SetWndPos(vector2():set(x-40*self.xscale,y+(self.use_icons and -7 or -22)))''',1)
s=s.replace('vector2():set(64*self.xscale,16)','vector2():set(80*self.xscale,16)')
s=s.replace('vector2():set(x-5*self.xscale,y-3)','vector2():set(x+34*self.xscale,y+13)')
s=s.replace('vector2():set(10*self.xscale,10)','vector2():set(6*self.xscale,6)')
s=s.replace('vector2():set(x-38*self.xscale,y-6)','vector2():set(x-40*self.xscale,y+9)')
s=s.replace('vector2():set(x-32*self.xscale,y+10)','vector2():set(x-40*self.xscale,y+41)')
# Leave room for the bottom item's battery row, including two-entry menus.
s=s.replace('math.min(742-self.radius,m.y)','math.min(708-self.radius,m.y)')
s=s.replace('self.center.y+self.radius+4','self.center.y+self.radius+36')
s=s.replace('    if now>=self.next_refresh then','    local refresh=now>=self.next_refresh\n    if refresh then',1)
s=s.replace('    for i,a in ipairs(self.items) do\n        local state=', '    if not refresh and self.last_selected==self.selected then return end\n    self.last_selected=self.selected\n    for i,a in ipairs(self.items) do\n        local state=',1)
# Live route/link changes rebuild entry identity once per low-frequency refresh.
s=s.replace('    self.selected=nil; self.next_refresh=0; self.status={}', '    self.selected=nil; self.next_refresh=0; self.status={}\n    self.entry_signature=nil;self.badge_semantics={}',1)
s=s.replace('        self.next_refresh=now+200','''        self.next_refresh=now+200
        if not self.target then
            local keys={}
            for _,entry in ipairs(one_key_lights_actions.list(true)) do keys[#keys+1]=entry.id end
            local signature=table.concat(keys,":")
            if self.entry_signature and self.entry_signature~=signature then self:Prepare();self.entry_signature=signature;return end
            self.entry_signature=signature
        end''',1)
s=s.replace('self.status[i]={available=state.available,locked=state.locked,value=state.value==a.value and 1 or 0}', 'self.status[i]={available=state.installed,locked=state.locked,value=state.value==a.value and 1 or 0,emitting=false,linked=state.linked,route=state.route}',1)
s=s.replace('self.dots[i]:Show(not locked and self.style==4 and not self.target)','self.dots[i]:Show(not locked and not self.target)')
s=s.replace('self.dots[i]:SetTextureColor(one_key_lights_theme.argb(one_key_lights_theme.status(state.value)))','''self.dots[i]:SetTextureColor(one_key_lights_theme.argb(state.emitting and palette.on or palette.off))
        self.icons[i]:Show(self.use_icons)
        self.labels[i]:Show(self.label_mode~=2 or not self.use_icons)
        self.icons[i]:SetTextureColor(color)
        self.badges[i]:Show(self.use_icons and not self.target)
        if self.use_icons and not self.target then
            local semantic=state.locked and "missing" or state.value==2 and "auto" or state.value==1 and "on" or "off"
            if self.badge_semantics[i]~=semantic then
                local ok=pcall(function() self.badges[i]:InitTexture(one_key_lights_icons.get_icon(semantic,self.icon_style).texture) end)
                if not ok then self.use_icons=false;self.label_mode=3 end
                self.badge_semantics[i]=semantic
            end
            self.badges[i]:SetTextureColor(color)
        end
        self.routes[i]:TextControl():SetText(not self.target and ((state.linked and "LINK "..one_key_lights_icons.route_label(state.route).." " or "")..(state.emitting and "LIT" or "DARK")) or "")
        self.routes[i]:TextControl():SetTextColor(one_key_lights_theme.argb(palette.muted))''',1)
s+='\nfunction close() if is_open() then GUI:Close() end end\n'
write(ONE/'Core/gamedata/scripts/one_key_lights_menu.script',s)
print('26 semantic atlas cells generated; radial integration and text fallback assembled.')
