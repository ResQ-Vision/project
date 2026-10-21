"""Two-sheet STM32 assembly drawing: native EasyEDA, SVG, and vector PDF.

Logical interface names are intentionally not physical V1.2 pin assignments.
Historical ESP32 artifacts are never edited by this generator.
"""
import csv
import json
import math
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
W, H = 1600, 1100
NAVY, GREY, LIGHT = '#142B43', '#56677B', '#E7EDF3'
BLUE, ORANGE, PURPLE, GOLD, RED = '#167BA2', '#C16922', '#7355AC', '#B28324', '#B23F4A'
PALE = '#F4F7FA'


class Sheet:
    def __init__(self, number, title, subtitle):
        self.number, self.title = number, title
        self.ops, self.shapes, self.components = [], [], []
        self.counter = number*10000
        self.box(35, 30, 1530, 1035, NAVY, 'none', 1)
        self.text(65, 83, 'ResQ-Vision', 38, NAVY, True)
        self.text(65, 119, title, 24, NAVY)
        self.text(65, 150, subtitle, 17, GREY)
        self.text(1300, 78, 'ELECTRICAL / B', 17, NAVY, True)
        self.text(1300, 107, '21 OCT 2026', 16, GREY)
        self.line([(65,170),(1535,170)], LIGHT, 2)
        self.text(65,1040,'RV-EL-B  |  Design review  |  Base 897c03e / ADR 0006',14,GREY)
        self.text(1370,1040,f'SHEET {number} / 2',14,NAVY,True)

    def uid(self):
        self.counter += 1
        return f'gge{self.counter}'

    def text(self,x,y,t,size=17,color=NAVY,bold=False):
        assert not any(c in t for c in '~`\n')
        self.ops.append(('text',x,y,t,size,color,bold))
        self.shapes.append(f'T~L~{x}~{y}~0~{color}~Arial~{size*0.75:g}pt~{"bold" if bold else ""}~~~comment~{t}~1~start~{self.uid()}~0')

    def box(self,x,y,w,h,color=LIGHT,fill='none',width=1):
        self.ops.append(('box',x,y,w,h,color,fill,width))
        self.shapes.append(f'R~{x}~{y}~~~{w}~{h}~{color}~{width}~0~{fill}~{self.uid()}~0')

    def line(self,points,color=NAVY,width=2,dash=False,wire=False):
        self.ops.append(('line',points,color,width,dash))
        coords=' '.join(f'{x:g} {y:g}' for x,y in points)
        self.shapes.append(f'{"W" if wire else "PL"}~{coords}~{color}~{width}~{1 if dash else 0}~none~{self.uid()}~0')

    def circle(self,x,y,r,color=NAVY,fill='none',width=2):
        self.ops.append(('circle',x,y,r,color,fill,width))
        self.shapes.append(f'E~{x}~{y}~{r}~{r}~{color}~{width}~0~{fill}~{self.uid()}~0')

    def device(self,ref,model,draw,pins=()):
        """Group drawn details and actual editable schematic terminals as a LIB."""
        start=len(self.shapes)
        draw()
        self.components.append({'ref':ref,'model':model,'pins':list(pins)})
        for ident,name,x,y,side in pins:
            d=18 if side=='left' else -18
            self.shapes.append(f'P~show~0~{ident}~{x}~{y}~{180 if side=="left" else 0}~{self.uid()}~0^^{x}~{y}^^M {x} {y} h {d}~{NAVY}^^0~{x}~{y}~0~{name}~start~~9pt^^0~{x}~{y}~0~{ident}~start~~8pt^^0~{x}~{y}^^0~M {x} {y}')
            # Export renderers draw exactly the same pin stubs.
            self.ops.append(('line',[(x,y),(x+d,y)],NAVY,1,False))
        parts=self.shapes[start:]
        parts.insert(0,f'T~P~0~0~0~{NAVY}~Arial~10pt~~~~comment~{ref}~0~start~{self.uid()}~0')
        parts.insert(1,f'T~N~0~0~0~{NAVY}~Arial~10pt~~~~comment~{model}~0~start~{self.uid()}~0')
        self.shapes[start:]=['#@$'.join([f'LIB~0~0~package`NONE`Manufacturer Part`{model}`spicePre`U`~~0~{self.uid()}~~~0~~yes~yes',*parts])]

    def badge(self,x,y,label,color):
        self.box(x,y-18,len(label)*9+20,25,color,'none',1)
        self.text(x+10,y,label,13,color,True)

    def svg(self):
        out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1100" viewBox="0 0 {W} {H}"><rect width="1600" height="1100" fill="white"/>']
        for o in self.ops:
            if o[0]=='text':
                _,x,y,t,s,c,b=o
                out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{s}" fill="{c}" font-weight="{"700" if b else "400"}">{escape(t)}</text>')
            elif o[0]=='box':
                _,x,y,w,h,c,f,lw=o
                out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" stroke="{c}" stroke-width="{lw}" fill="{f}"/>')
            elif o[0]=='circle':
                _,x,y,r,c,f,lw=o
                out.append(f'<circle cx="{x}" cy="{y}" r="{r}" stroke="{c}" stroke-width="{lw}" fill="{f}"/>')
            elif o[0]=='line':
                _,ps,c,lw,dash=o
                points=' '.join(f'{x},{y}' for x,y in ps)
                out.append(f'<polyline points="{points}" stroke="{c}" stroke-width="{lw}" fill="none" stroke-dasharray="{"8 5" if dash else "none"}"/>')
        return ''.join(out)+'</svg>'


def motor(s,ref,y,side):
    # Cable rows describe functions, not a claimed physical contact sequence.
    rows=[('M+','drive +',ORANGE),('M-','drive -',ORANGE),('VCC','encoder supply',BLUE),('GND','encoder return',BLUE),('A','encoder A',BLUE),('B','encoder B',BLUE)]
    pins=[(f'{ref}_{n}',n,368,y+50+i*25,'right') for i,(n,_,_) in enumerate(rows)]
    def drawing():
        s.box(65,y,285,200,BLUE,'none',2)
        s.text(85,y+29,f'{ref}  REAR {side.upper()}',20,NAVY,True)
        s.circle(140,y+100,32,ORANGE)
        s.text(129,y+108,'M',26,ORANGE,True)
        s.circle(226,y+100,18,BLUE)
        s.text(220,y+106,'E',16,BLUE,True)
        s.line([(172,y+100),(208,y+100)],GREY,2)
        s.text(85,y+157,'JGB37-520R30-12*',17,NAVY)
        s.text(85,y+181,'* Likely model / 30:1 rear drive',14,GREY)
    s.device(ref,'Likely JGB37-520R30-12',drawing,pins)
    for i,(n,label,color) in enumerate(rows):
        yy=y+50+i*25
        s.line([(368,yy),(582,yy)],color,1.5,wire=True)
        s.text(392,yy-6,n,14,color,True)
        s.text(485,yy-6,label,12,GREY)
    return pins


def assembly():
    s=Sheet(1,'Electrical assembly','Selected STM32 hardware and logical cable functions. Connector assignments remain under review.')
    # Existing battery is retained, without assigning invented voltage/capacity.
    def battery():
        s.box(65,205,285,120,GOLD,'none',2)
        s.box(86,236,54,40,GOLD,'none',2)
        s.box(140,249,7,15,GOLD,GOLD,1)
        s.text(96,264,'+  -',18,GOLD,True)
        s.text(164,239,'B1  EXISTING BATTERY',15,NAVY,True)
        s.text(164,267,'Retained by owner',16,GREY)
        s.text(85,304,'Input / polarity / protection check: [A]',14,GREY)
    s.device('B1','Existing owner-provided battery',battery,[('BAT_PLUS','+',368,240,'right'),('BAT_MINUS','-',368,268,'right')])
    for yy,end,col in [(240,326,GOLD),(268,354,GREY)]:
        x=505 if yy==240 else 530
        s.line([(368,yy),(x,yy),(x,end),(582,end)],col,2,wire=True)
    s.text(398,218,'POWER',15,GOLD,True)
    motor(s,'M_L',408,'left')
    motor(s,'M_R',672,'right')
    # Board physical connector indices / internal chip selection deliberately omitted.
    bp=[('POWER_IN','power +',582,326,'left'),('POWER_RETURN','return',582,354,'left')]
    for ref,y in [('M_L',408),('M_R',672)]:
        bp += [(f'BOARD_{ref}_{name}',name,582,y+50+i*25,'left') for i,name in enumerate(['M+','M-','VCC','GND','A','B'])]
    bp += [('SERVO_SIGNAL','signal',1048,437,'right'),('SERVO_SUPPLY','supply',1048,469,'right'),('SERVO_RETURN','return',1048,501,'right')]
    bp += [('FRONT_CONTACT_A','front A',1048,650,'right'),('FRONT_CONTACT_B','front B',1048,675,'right'),('REAR_CONTACT_A','rear A',1048,780,'right'),('REAR_CONTACT_B','rear B',1048,805,'right')]
    def board():
        s.box(600,205,430,680,ORANGE,'#FFFDFC',2)
        s.box(600,205,430,88,ORANGE,'#FFF5E9',1)
        s.text(623,240,'U1  HIWONDER',26,NAVY,True)
        s.text(623,270,'ROS Robot Controller V1.2',21,NAVY)
        s.text(619,330,'Power input [A]',16,GREY)
        s.text(619,402,'Rear motor channels [B]',16,ORANGE,True)
        s.text(619,427,'M1-M4 / socket allocation TBD',14,GREY)
        s.text(619,669,'Second rear channel / socket TBD [B]',15,ORANGE,True)
        # MCU symbol and internal board functions, not fabricated internal wiring.
        s.box(741,548,150,88,NAVY,PALE,2)
        for i in range(6):
            xx=755+i*22
            s.line([(xx,540),(xx,548)],NAVY,1)
            s.line([(xx,636),(xx,644)],NAVY,1)
        s.text(758,582,'STM32F407',18,NAVY,True)
        s.text(783,608,'VET6',17,GREY)
        s.text(618,857,'Onboard motor drivers + IMU (identity TBD)',15,GREY)
        s.text(880,402,'Servo [C]',16,ORANGE,True)
        s.text(900,620,'Contacts [D]',15,BLUE,True)
    s.device('U1','Hiwonder ROS Robot Controller V1.2 / STM32F407VET6',board,bp)
    # Confirmed servo, conditional V1.2 rail selection is conspicuous.
    def servo():
        s.box(1265,378,270,172,ORANGE,'none',2)
        s.text(1285,408,'SV1  FRONT STEERING',18,NAVY,True)
        s.text(1285,437,'LD-1501MG',23,NAVY,True)
        s.box(1285,464,60,38,ORANGE,'none',2)
        s.circle(1315,464,7,ORANGE)
        s.line([(1315,464),(1347,449)],ORANGE,3)
        s.text(1358,478,'PWM servo',16,GREY)
        s.text(1285,530,'Owner-confirmed model',15,GREY)
    s.device('SV1','LD-1501MG',servo,[('SIGNAL_WHITE','signal',1247,437,'left'),('POWER_RED','supply',1247,469,'left'),('RETURN_BLACK','return',1247,501,'left')])
    for yy,col,label in [(437,ORANGE,'SIG'),(469,GOLD,'V_SERVO'),(501,GREY,'0V')]:
        s.line([(1048,yy),(1247,yy)],col,2,wire=True)
        s.text(1091,yy-7,label,14,col,True)
    s.text(1080,558,'[C] Rail / socket to verify',15,ORANGE,True)
    for ref,y,title in [('S_F',612,'FRONT CONTACT'),('S_R',742,'REAR CONTACT')]:
        def contact(ref=ref,y=y,title=title):
            s.text(1276,y+18,f'{ref}  {title}',18,NAVY,True)
            s.circle(1290,y+57,4,BLUE)
            s.circle(1360,y+57,4,BLUE)
            s.line([(1294,y+57),(1356,y+43)],BLUE,2)
            s.text(1276,y+95,'Type / polarity / GPIO TBD',15,GREY)
        s.device(ref,'Contact sensor / electrical polarity TBD',contact,[(ref+'_A','A',1247,y+38,'left'),(ref+'_B','B',1247,y+63,'left')])
        for yy in [y+38,y+63]:
            # Dashed graphical intent, not a conductive net pretending GPIO selection.
            s.line([(1048,yy),(1247,yy)],BLUE,1.5,True)
    s.box(65,924,940,68,LIGHT,PALE,1)
    s.text(85,950,'LOCAL STOP AUTHORITY',16,ORANGE,True)
    s.text(85,977,'STM32 must stop locally on contact / command loss; physical inhibit circuit is unresolved [E].',17,NAVY)
    s.box(1040,924,495,68,LIGHT,PALE,1)
    s.text(1060,950,'READ WITH SHEET 2',16,NAVY,True)
    s.text(1060,977,'Logical terminals, not a V1.2 pin-number map.',17,GREY)
    return s


def interfaces():
    s=Sheet(2,'Interfaces and connector reference','Confirmed components, planned data paths and the checks needed to complete the V1.2 wiring.')
    def controller():
        s.box(70,393,335,144,ORANGE,'#FFF5E9',2)
        s.text(91,430,'HIWONDER V1.2',23,NAVY,True)
        s.text(91,461,'Final motion authority',19,ORANGE,True)
        s.text(91,496,'USB / UART selection: verify revision',15,GREY)
    s.device('U1_REF','Hiwonder V1.2 reference',controller)
    def c3():
        s.box(70,205,335,111,PURPLE,'none',2)
        s.circle(106,262,15,PURPLE)
        s.line([(94,262),(118,262)],PURPLE,2)
        s.line([(106,250),(106,274)],PURPLE,2)
        s.text(140,242,'C3 MANUAL CONTROLLER',18,NAVY,True)
        s.text(140,273,'Board / inputs / radio TBD',16,GREY)
    s.device('C3','C3 handheld / exact board TBD',c3)
    s.line([(237,316),(237,393)],PURPLE,2,True)
    s.text(260,350,'DIRECT PATH',16,PURPLE,True)
    s.text(260,375,'Radio interface unresolved',14,GREY)
    def laptop():
        s.box(622,205,376,242,NAVY,'none',2)
        s.box(635,219,350,204,LIGHT,PALE,1)
        s.text(664,255,'ONE LAPTOP',26,NAVY,True)
        s.text(664,286,'PC server + browser interface',18,GREY)
        s.box(653,312,314,76,PURPLE,'#F7F3FC',1)
        s.text(673,343,'ISOLATED AI WORKER',17,PURPLE,True)
        s.text(673,370,'Advisory image analysis only',16,GREY)
        s.line([(605,447),(1015,447),(1040,467),(580,467),(605,447)],NAVY,2)
    s.device('PC1','One laptop / PC Server + advisory AI',laptop)
    s.line([(405,476),(480,476),(480,408),(622,408)],GREY,1.5,True)
    s.text(450,516,'USB serial on bench; untethered host link TBD [F]',16,GREY)
    def camera():
        s.box(1200,205,330,115,BLUE,'none',2)
        s.circle(1237,263,21,BLUE)
        s.circle(1237,263,10,BLUE)
        s.text(1276,245,'ESP CAM S3',22,NAVY,True)
        s.text(1276,276,'Separate camera board',16,GREY)
        s.text(1220,307,'Exact board and supply interface: verify',14,GREY)
    s.device('CAM1','ESP CAM S3 / exact board TBD',camera)
    s.line([(1200,260),(998,260)],PURPLE,2,True)
    s.text(1048,244,'Wi-Fi images',16,PURPLE,True)
    def lidar():
        s.box(1200,393,330,144,BLUE,'none',2)
        s.circle(1237,453,24,BLUE)
        s.line([(1237,453),(1256,437)],BLUE,2)
        s.text(1276,433,'2D LiDAR',23,NAVY,True)
        s.text(1276,465,'Model / power / bridge TBD',16,GREY)
        s.text(1220,513,'USB on bench; wireless acquisition open',15,GREY)
    s.device('L1','2D LiDAR / exact model TBD',lidar)
    s.line([(1200,453),(1112,453),(1112,350),(998,350)],BLUE,2,True)
    s.text(1041,336,'Scan data',16,BLUE,True)
    s.box(65,571,1470,35,LIGHT,PALE,1)
    s.text(85,595,'Dashed lines = planned data / unassigned contact interface, never copper. No extra radio board is assumed.',17,GREY)
    # Dense but readable connector reference cards, consistent alignment.
    for x,width in [(65,460),(555,460),(1045,490)]:
        s.box(x,636,width,322,LIGHT,'none',1)
    s.text(85,670,'MOTOR HARNESS FUNCTIONS',20,BLUE,True)
    s.text(85,697,'Vendor family reference, not physical pin order',15,GREY)
    for i,(a,b) in enumerate([('M+ / M-','Motor drive pair'),('VCC / GND','Hall supply / return'),('A / B','Quadrature feedback')]):
        yy=735+i*40
        s.text(90,yy,a,18,NAVY,True); s.text(260,yy,b,17,GREY)
        s.line([(85,yy+13),(505,yy+13)],LIGHT,1)
    s.text(85,874,'[B] Verify plug order, levels and rear-channel',16,GREY)
    s.text(85,899,'allocation on the actual V1.2 board.',16,GREY)
    s.text(85,931,'Source [2]; motor model remains inferred.',15,BLUE)
    s.text(575,670,'LD-1501MG STEERING',20,ORANGE,True)
    for i,(a,b) in enumerate([('White','PWM signal'),('Red','Servo supply'),('Black','Ground / return')]):
        yy=715+i*34
        s.text(580,yy,a,18,NAVY,True); s.text(710,yy,b,17,GREY)
    s.text(575,837,'Vendor range: 6-8.4 V [2]',18,ORANGE,True)
    s.text(575,871,'[C] Check V1.2 socket, rail and current.',16,GREY)
    s.text(575,898,'Do not assume 5 V or raw battery routing.',16,GREY)
    s.text(575,931,'Steering travel must be calibrated mechanically.',15,GREY)
    s.text(1065,670,'V1.2 COMPLETION CHECKS',20,NAVY,True)
    for i,t in enumerate(['[A] Battery input / polarity / protection','[B] Driver limits / harness / encoder levels','[C] Servo rail / socket / signal threshold','[D] Contact polarity / bias / assigned GPIO','[E] Independent inhibit / local stop evidence','[F] Host + C3 radio / LiDAR acquisition']):
        s.text(1065,714+i*37,t,16,GREY)
    s.text(65,991,'[1] GitHub ADR 0006 / PR #20    [2] Hiwonder Ackermann chassis, STM32 guide    [3] Hardware review: Issues #2, #3, #4, #9',15,GREY)
    return s


def build():
    sheets=[assembly(),interfaces()]
    proj={'editorVersion':'6.5.60','docType':'5','title':'ResQ-Vision | STM32 electrical assembly | Rev B','description':'Owner-approved components; logical terminal drawing with unresolved V1.2 pin assignments explicitly retained.','colors':{},'schematics':[]}
    for s in sheets:
        proj['schematics'].append({'docType':'1','title':f'{s.number:02d} {s.title}','description':'Review drawing; not fabrication release','dataStr':{'head':{'docType':'1','editorVersion':'6.5.60','newgId':True,'c_para':{'Prefix Start':'1'},'c_spiceCmd':None},'canvas':'CA~1600~1100~#FFFFFF~none~#DDDDDD~5~1600~1100~line~5~pixel~5~0~0','shape':s.shapes,'BBox':{'x':0,'y':0,'width':1600,'height':1100},'colors':{}}})
        (ROOT/f'{s.number:02d}-{"assembly" if s.number==1 else "interfaces"}.svg').write_text(s.svg())
    (ROOT/'resq-vision-stm32.json').write_text(json.dumps(proj,indent=2)+'\n')
    manifest={'base':'897c03e','decision':'ADR 0006','revision':'B','status':'design-review','physical_pinout_approved':False,'sheet_count':2,'battery':'existing / owner accepted','components':[c for s in sheets for c in s.components],'open_checks':['A','B','C','D','E','F']}
    (ROOT/'drawing-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    with (ROOT/'logical-terminals.csv').open('w') as f:
        writer=csv.writer(f); writer.writerow(['reference','model','logical_terminal','function','physical_pin'])
        for s in sheets:
            for c in s.components:
                for ident,label,*_ in c['pins']: writer.writerow([c['ref'],c['model'],ident,label,'unassigned / verify V1.2'])
    pdf(sheets)


def pdf(sheets):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A3,landscape
    from reportlab.lib.colors import HexColor
    path=REPO/'output/pdf/resq-vision-stm32-electrical.pdf'
    path.parent.mkdir(parents=True,exist_ok=True)
    pw,ph=landscape(A3); scale=min(pw/W,ph/H)
    c=canvas.Canvas(str(path),pagesize=(pw,ph),pageCompression=1)
    c.setTitle('ResQ-Vision - STM32 electrical assembly - Revision B')
    c.setAuthor('ResQ-Vision')
    for s in sheets:
        c.saveState(); c.translate((pw-W*scale)/2,(ph-H*scale)/2); c.scale(scale,scale)
        for o in s.ops:
            if o[0]=='text':
                _,x,y,t,size,col,bold=o
                c.setFillColor(HexColor(col)); c.setFont('Helvetica-Bold' if bold else 'Helvetica',size); c.drawString(x,H-y,t)
            elif o[0]=='box':
                _,x,y,w,h,col,fill,lw=o
                c.setStrokeColor(HexColor(col)); c.setLineWidth(lw)
                if fill!='none':c.setFillColor(HexColor(fill))
                c.rect(x,H-y-h,w,h,stroke=1,fill=int(fill!='none'))
            elif o[0]=='circle':
                _,x,y,r,col,fill,lw=o
                c.setStrokeColor(HexColor(col)); c.setLineWidth(lw)
                if fill!='none':c.setFillColor(HexColor(fill))
                c.circle(x,H-y,r,stroke=1,fill=int(fill!='none'))
            elif o[0]=='line':
                _,points,col,lw,dash=o
                c.setStrokeColor(HexColor(col)); c.setLineWidth(lw); c.setDash([8,5] if dash else [])
                p=c.beginPath(); p.moveTo(points[0][0],H-points[0][1])
                for x,y in points[1:]:p.lineTo(x,H-y)
                c.drawPath(p); c.setDash([])
        c.restoreState(); c.showPage()
    c.save()


if __name__=='__main__':build()
