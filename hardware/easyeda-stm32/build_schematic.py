"""Conventional EasyEDA module schematic; logical functions, not a physical pinout.

Uses native editable LIB/P/W/N primitives. No unverified radio, sensor power,
contact bias, IMU chip or V1.2 pad assignment is synthesized.
"""
import json
from pathlib import Path
from build_chart import Sheet, NAVY

ROOT = Path(__file__).resolve().parent
GREEN, RED, BLUE, GREY = '#008800', '#A00000', '#0000A0', '#56677B'


class Schematic(Sheet):
    def __init__(self):
        self.number, self.counter = 3, 30000
        self.ops, self.shapes, self.components = [], [], []
        self.title = 'Conventional module schematic'
        self.nets = []
        self.box(25,25,1550,1050,'#808080','none',1)
        self.text(55,65,'ResQ-Vision / STM32 module schematic',27,NAVY,True)
        self.text(55,94,'Logical connections / physical V1.2 pin assignments pending / 21 OCT 2026',16,GREY)
        self.text(55,123,'Green = electrical wire. Dashed = data-path requirement only. OPEN = unresolved electrical interface.',15,GREY)

    def module(self,ref,model,x,y,w,h,left=(),right=(),notes=()):
        pins=[]
        for side,rows in [('left',left),('right',right)]:
            for ident,label,yy in rows:
                pins.append((ident,label,x-18 if side=='left' else x+w+18,yy,side))
        def draw():
            self.box(x,y,w,h,RED,'none',1)
            self.text(x,y-28,ref,17,BLUE,True)
            self.text(x,y-9,model,15,BLUE)
            for i,n in enumerate(notes):self.text(x+14,y+25+i*22,n,14,GREY)
            for ident,label,px,py,side in pins:
                # Labels are graphics inside LIB; native pin names remain serialized.
                tx=x+12 if side=='left' else x+w-12-len(label)*7.5
                self.text(tx,py-5,label,13,BLUE)
        self.device(ref,model,draw,pins)
        return {ident:(px,py) for ident,_,px,py,_ in pins}

    def absorb_details(self):
        """Keep internal artwork bound to the last native component when moved."""
        i=next(i for i in range(len(self.shapes)-1,-1,-1) if self.shapes[i].startswith("LIB~"))
        self.shapes[i:] = ["#@$".join(self.shapes[i:])]

    def net(self,a,b,name,points=None):
        ps=points or [a,b]
        self.line(ps,GREEN,1,wire=True)
        x,y=ps[0]
        self.shapes.append(f'N~{x}~{y}~0~{BLUE}~{name}~{self.uid()}~start~{x+6}~{y-6}~Arial~8pt~0')
        self.ops.append(('text',x+6,y-6,name,11,BLUE,False))
        self.nets.append({'name':name,'a':a,'b':b})

    def pending(self,p,label='OPEN'):
        x,y=p
        self.text(x-8,y-9,label,11,RED)


def build():
    s=Schematic()
    board_left=[('POWER_IN','PWR + [A]',240),('POWER_RETURN','PWR return [A]',275)]
    board_right=[('SERVO_SIGNAL','PWM [C]',220),('SERVO_SUPPLY','SERVO rail [C]',255),('SERVO_RETURN','SERVO return [C]',290)]
    funcs=['M+','M-','VCC','GND','A','B']
    for side,start in [('L',420),('R',640)]:
        board_right += [(f'{side}_{p}',f'{side}: {p}',start+i*25) for i,p in enumerate(funcs)]
    u=s.module('U1','Hiwonder ROS Robot Controller V1.2',590,185,370,610,board_left,board_right)
    s.text(610,335,'STM32F407VET6',23,NAVY,True)
    s.text(610,369,'Final motion authority + local stops',14,GREY)
    s.box(610,410,190,115,RED,'none',1)
    s.text(625,438,'ONBOARD IMU',17,BLUE,True)
    s.text(625,468,'IC / bus / driver TBD',13,GREY)
    s.text(625,497,'Internal to U1',13,GREY)
    s.text(610,560,'Onboard motor drivers',16,BLUE)
    s.text(610,588,'Channel/socket assignment TBD [B]',13,GREY)
    s.text(610,627,'Contact GPIO + bias TBD [D]',14,GREY)
    s.text(610,666,'Local hardware inhibit TBD [E]',14,RED)
    s.text(610,704,'Host / C3 link unresolved [F]',14,GREY)
    s.text(610,770,'Labels are functions, not pad numbers.',13,RED)
    s.absorb_details()

    # Retained battery, without inventing an input rail value or protection circuit.
    b=s.module('B1','Existing battery / owner retained',110,200,210,110,right=[('PLUS','+',240),('MINUS','-',275)])
    s.line([(150,232),(150,277)],RED,2)
    s.line([(164,243),(164,266)],RED,2)
    s.text(188,255,'BATTERY',15,BLUE)
    s.absorb_details()
    s.net(b['PLUS'],u['POWER_IN'],'BAT_IN')
    s.net(b['MINUS'],u['POWER_RETURN'],'BAT_RETURN')
    s.text(110,342,'[A] Verify polarity, protection and input.',14,GREY)

    v=s.module('SV1','LD-1501MG steering servo',1230,185,270,130,left=[('SIG','White / signal',220),('SUPPLY','Red / supply',255),('RETURN','Black / return',290)])
    for p,q,name in [('SERVO_SIGNAL','SIG','STEER_PWM'),('SERVO_SUPPLY','SUPPLY','SERVO_RAIL_TBD'),('SERVO_RETURN','RETURN','SERVO_RETURN')]:s.net(u[p],v[q],name)
    s.text(1230,340,'[C] Verify rail/socket/current before use.',13,GREY)
    for side,start,title in [('L',420,'left'),('R',640,'right')]:
        m=s.module(f'M_{side}',f'Rear {title} / likely JGB37-520R30-12',1230,start-35,270,175,left=[(p,p,start+i*25) for i,p in enumerate(funcs)])
        s.circle(1438,start+35,23,RED,'none',1)
        s.text(1429,start+42,'M',19,BLUE)
        s.circle(1438,start+95,18,RED,'none',1)
        s.text(1431,start+101,'E',16,BLUE)
        s.absorb_details()
        for p in funcs:s.net(u[f'{side}_{p}'],m[p],f'{side}_{"ENC_" if p in ["VCC","GND","A","B"] else ""}{p.replace("+","PLUS").replace("-","MINUS")}')
    s.text(1230,811,'[B] Six cable functions; plug order TBD.',13,GREY)

    # Generic contact symbols: unknown contact polarity must not imply NO or NC.
    for ref,y,label in [('S_F',425,'Front contact'),('S_R',600,'Rear contact')]:
        c=s.module(ref,label+' / polarity TBD',110,y-30,210,85,left=[('A','terminal A',y)],right=[('B','terminal B',y)])
        s.circle(180,y+13,3,RED,'none',1);s.circle(245,y+13,3,RED,'none',1)
        s.text(200,y+19,'?',18,RED)
        s.absorb_details()
        s.pending(c['A']);s.pending(c['B'])
        s.text(110,y+82,'[D] GPIO / bias / fault behavior TBD.',13,GREY)
    s.text(110,755,'Contacts remain an open interface.',14,RED)
    s.text(110,779,'No assumed pull-up or NC wiring.',14,GREY)

    # All sensing/acquisition modules present; unresolved interfaces stay open.
    cam=s.module('CAM1','ESP CAM S3 camera',110,880,230,100,left=[('POWER_TBD','power TBD',920),('RETURN_TBD','return TBD',955)])
    lidar=s.module('L1','2D LiDAR / model TBD',530,880,250,120,left=[('POWER_TBD','power TBD',915),('RETURN_TBD','return TBD',950),('DATA_TBD','data interface TBD',985)])
    for p in [*cam.values(),*lidar.values()]:s.pending(p)
    c3=s.module('C3','Manual controller / C3',965,880,230,100,notes=['Power / controls TBD','Direct motion link TBD [F]'])
    pc=s.module('PC1','Laptop / PC Server + AI',1330,880,200,100,notes=['Same laptop','No extra inference PC'])
    s.line([(340,920),(410,920),(410,825),(1430,825),(1430,880)],'#7355AC',1,True)
    s.text(420,818,'Camera Wi-Fi images to PC Server',13,'#7355AC')
    s.line([(780,960),(835,960),(835,1023),(1430,1023),(1430,980)],'#7355AC',1,True)
    s.text(850,1015,'LiDAR acquisition to laptop: interface / untethered link TBD [F]',12,'#7355AC')
    s.text(55,1053,'RV-SCH-C / Design review only / ADR 0006 + Issues #2, #3, #4, #9 / No footprints or fabrication release',14,GREY)
    data={'head':{'docType':'1','editorVersion':'6.5.60','newgId':True,'c_para':{'Prefix Start':'1'},'c_spiceCmd':None},'canvas':'CA~1600~1100~#FFFFFF~yes~#DDDDDD~5~1600~1100~line~5~pixel~5~0~0','shape':s.shapes,'BBox':{'x':0,'y':0,'width':1600,'height':1100},'colors':{}}
    project={'editorVersion':'6.5.60','docType':'5','title':'ResQ-Vision | Conventional STM32 schematic | Rev C','description':'Module-level schematic with all baseline sensors. Logical functions only; unverified physical interfaces remain open.','colors':{},'schematics':[{'docType':'1','title':'01 Conventional schematic','description':'Physical pinout pending','dataStr':data}]}
    (ROOT/'resq-vision-stm32-schematic.json').write_text(json.dumps(project,indent=2)+'\n')
    (ROOT/'03-conventional-schematic.svg').write_text(s.svg())
    (ROOT/'schematic-manifest.json').write_text(json.dumps({'revision':'C','physical_pinout_approved':False,'components':s.components,'nets':s.nets,'sensors':['L1','CAM1','U1:onboard IMU','M_L:encoder','M_R:encoder','S_F','S_R'],'open_interfaces':['L1','CAM1','S_F','S_R','C3','U1:IMU identity/bus','U1:physical pins']},indent=2)+'\n')
    return project


if __name__=='__main__':build()
