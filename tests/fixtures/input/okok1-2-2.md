KSX 6101:2024
10.9.5.7.1 renderinginfo 요소
표 216 — renderinginfo 요소
하위 요소 이름	설명
transMatrix	Translation Matrix, 10.9.5.7.2 참조
scaMatrix	Scaling Matrix, 10.9.5.7.2 참조
rotMatrix	Rotation Matrix, 10.9.5.7.2 참조
10.9.5.7.2 행렬 요소 형식
[MatrixType]은 행렬을 표현하기 위한 요소 형식이다. 3x3 행렬 요소는 (0,0,1)로 가정하기 때문에 표현하지 않는다.
그림 135 — [MatrixType]의 구조
표 217 — MatrixType 요소
속성 이름	설명
e1	3x3 행렬의 첫 번째 요소 (0,0)
e2	3x3 행렬의 두 번째 요소 (0,1)
e3	3x3 행렬의 세 번째 요소 (0,2)
e4	3x3 행렬의 네 번째 요소 (1,0)
e5	3x3 행렬의 다섯 번째 요소 (1,1)
e6	3x3 행렬의 여섯 번째 요소 (1,2)
실습 121 MatrixType 예
code
Xml
<hp:renderingInfo>
    <hp:transMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
    <hp:scaMatrix e1="0.881959" e2="0" e3="0" e4="0" e5="0.35278"/>
    <hp:rotMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
</hp:renderingInfo>
10.9.6 pic 요소
10.9.6.1 pic
<pic> 요소는 [AbstractShapeComponentType]을 상속받는다. [AbstractShapeComponentType]의 자세한 내용은 10.9.5를 참조한다.
표 218 — pic 요소
속성 이름	설명
reverse	그림 색상 반전
표 219 — pic 하위 요소
하위 요소 이름	설명
lineShape	테두리선 모양
imgRect	이미지 좌표 정보
imgClip	이미지 자르기 정보
effects	이미지 효과 정보
inMargin	안쪽 여백 정보 10.6.6.2 참조
imgDim	이미지 원본 정보
img	그림 정보
실습 122 pic 예
code
Xml
<hp:pic id="-1790881809" zOrder="2" numberingType="PICTURE" textWrap="SQUARE" textFlow="BOTH_SIDES"
lock="1" dropcapstyle="None" href="" groupLevel="0" instid="717139986" reverse="0">
    <hp:offset x="0" y="0"/>
    <hp:orgSz width="13800" height="15438"/>
    <hp:curSz width="0" height="0"/>
    <hp:flip horizontal="0" vertical="0"/>
    <hp:rotationInfo angle="0" centerX="6900" centerY="7719" rotateimage="1"/>
    <hp:renderinginfo>
        <hp:transMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
        <hp:scaMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
        <hp:rotMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
    </hp:renderinginfo>
    <hp:img binaryItemIDRef="image1" bright="0" contrast="0" effect="REAL_PIC" alpha="0"/>
    <hp:lineShape color="#FF0000" width="33" style="DOT" endCap="FLAT" headStyle="NORMAL" tailStyle="NORMAL"
    headfill="0" tailfill="0" headSz="SMALL_SMALL" tailSz="SMALL_SMALL" outlineStyle="OUTER" alpha="0"/>
    <hp:imgRect>
        <hp:ptO x="0" y="0"/>
        <hp:pt1 x="13800" y="0"/>
        <hp:pt2 x="13800" y="15438"/>
        <hp:pt3 x="0" y="15438"/>
    </hp:imgRect>
    <hp:imgClip left="0" right="45060" top="0" bottom="50400"/>
    <hp:inMargin left="0" right="0" top="0" bottom="0"/>
    <hp:imgDim dimwidth="45060" dimheight="50400"/>
    <hp:effects/>
    <hp:sz width="13800" widthRelTo="ABSOLUTE" height="15438" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="1" holdAnchorAndSO="0"
    vertRelTo="PAPER" horzRelTo="PAPER" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="119107"/>
    <hp:outMargin left="0" right="0" top="0" bottom="0"/>
    <hp:shapeComment>그림입니다. 원본 그림의 이름:01_대오버?!.png 원본 그림의 크기: 가로 601pixel, 세로 672pixel</hp:shapeComment>
</hp:pic>
10.9.6.2 테두리선 모양
그림 137 — <lineShape>의 구조
표 220 — lineShape 요소
속성 이름	설명
color	선 색상
width	선 굵기. 단위: HWPUNIT
style	선 종류
endCap	선 끝 모양
headStyle	화살표 시작 모양
tailStyle	화살표 끝 모양
headfill	화살표 시작점 선 색상으로 채우기 여부
tailfill	화살표 끝점 선 색상으로 채우기 여부
headSz	화살표 시작 크기
tailSz	화살표 끝 크기
outlineStyle	테두리선의 형태
alpha	투명도
실습 123 lineShape 예
code
Xml
<hp:lineShape color="#141313" width="6" style="SOLID" endCap="FLAT" headStyle="NORMAL"
tailStyle="NORMAL" headfill="1" tailfill="1" headSz="SMALL_SMALL" tailSz="SMALL_SMALL"
outlineStyle="INNER" alpha="277"/>
10.9.6.3 이미지 좌표 정보
10.9.6.3.1 이미지 좌표
그림의 좌표 정보를 가지고 있는 요소이다.
그림 138 — <imgRect>의 구조
표 221 — imgRect 요소
하위 요소 이름	설명
pt0	첫 번째 좌표 10.9.6.3.2 참조
pt1	두 번째 좌표 10.9.6.3.2 참조
pt2	세 번째 좌표 10.9.6.3.2 참조
pt3	네 번째 좌표 10.9.6.3.2 참조
10.9.6.3.2 점 요소 형식
좌표 정보를 표현할 때 사용하는 요소로, 2축 좌표계를 사용한다.
표 222 — PointType 요소
속성 이름	설명
x	x 좌표
y	y 좌표
실습 124 PointType 예
code
Xml
<hp:imgRect>
    <hp:ptO x="0" y="0"/>
    <hp:pt1 x="14112" y="0"/>
    <hp:pt2 x="14112" y="7938"/>
    <hp:pt3 x="0" y="7938"/>
</hp:imgRect>
10.9.6.4 이미지 자르기 정보
원본 그림을 기준으로 자를 영역 정보를 가지고 있는 요소이다. 자르기 정보가 설정되면, 그림은 논리적으로 원본 그림에서 해당 영역만큼 잘리게 되고, 화면에서는 남은 영역만 표시된다.
그림 140 — <img>의 구조
표 223 — imgClip 요소
속성 이름	설명
left	왼쪽에서 이미지를 자른 크기
right	오른쪽에서 이미지를 자른 크기
top	위쪽에서 이미지를 자른 크기
bottom	아래쪽에서 이미지를 자른 크기
실습 125 imgClip 예
code
Xml
<hp:imgClip left="0" right="96000" top="0" bottom="54000"/>
10.9.6.5 이미지 효과 정보
10.9.6.5.1 이미지 효과
그림에 적용될 효과 정보를 가지고 있는 요소이다.
표 224 — effects 요소
하위 요소 이름	설명
shadow	그림자 효과
glow	네온 효과
softEdge	부드러운 가장자리 효과
reflection	반사 효과
10.9.6.5.2 그림자 효과
그림 효과 중 그림자 효과에 대한 설정 정보를 가지고 있는 요소이다.
표 225 — shadow 요소
속성 이름	설명
style	그림자 스타일
alpha	시작 투명도
radius	흐릿한 정도
direction	방향 각도
distance	대상과 그림자 사이의 거리
rotationstyle	도형과 함께 그림자 회전 여부
하위 요소 이름	설명
skew	기울기
scale	확대 비율
effectsColor	그림자 색상
실습 126 shadow 예
code
Xml
<hp:shadow style="OUTSIDE" alpha="?" radius="60" direction="?" distance="100"
alignStyle="CENTER" rotationStyle="0">
    <hp:skew x="15" y="0"/>
    <hp:scale x="1" y="1"/>
    <hp:effectsColor type="RGB" schemeIdx="-1" systemIdx="-1" presetIdx="-1">
        <hp:rgb r="1" g="1" b="1"/>
    </hp:effectsColor>
</hp:shadow>
기울기 각도
기울기 정보를 가지고 있는 요소이다.
그림 143 — <skew>의 구조
표 227 — skew 요소
속성 이름	설명
x	x축 기울기 각도
y	y축 기울기 각도
실습 127 skew 예
code
Xml
<hp:skew x="30" y="0"/>
확대 비율
확대 정보를 가지고 있는 요소이다.
그림 144 — <scale>의 구조
표 228 — scale 요소
속성 이름	설명
x	x축 확대 비율
y	y축 확대 비율
실습 128 scale 예```xml
<hp:scale x="1" y="1.2"/>
code
Code
**색상 정보**
효과에 사용될 색상 정보를 가지고 있는 요소이다.

**표 230 — effectsColor 하위 요소**

| 하위 요소 이름 | 설명 |
| :--- | :--- |
| rgb | RGB 색상 표현 속성으로 r, g, b 세 가지 속성을 가짐. 모두 0 이상의 정수 값을 가짐. 해당 요소의 추가적인 설명은 생략. |
| cmyk | CMYK 색상 표현 속성으로 c, m, y, k 네 가지 속성을 가짐. 모두 0 이상의 정수 값을 가짐. 해당 요소의 추가적인 설명은 생략. |
| scheme | Scheme 색상 표현 속성으로 r, g, b 세 가지 속성을 가짐. 모두 0 이상의 정수 값을 가짐. 해당 요소의 추가적인 설명은 생략. |
| system | System 색상 표현 속성으로 h, s, l 세 가지 속성을 가짐. 모두 0 이상의 정수 값을 가짐. |

**effect 요소**
색상 효과 정보를 가지고 있는 요소이다.

**그림 146 — `<effect>`의 구조**

**표 231 — effect 요소**

| 속성 이름 | 설명 |
| :--- | :--- |
| type | 색상 효과 종류 |
| value | 효과 적용에 필요한 수치 |

**표 232 — 색상 효과 종류 1**

| 색상 효과 구분 | 이름/설명 | 값의 범위 | 기본 값 |
| :--- | :--- | :--- | :--- |
| ALPHA | 투명도. 1.0이면 불투명 | 0.0 ~ 1.0 | 1.0 |
| ALPHA_MOD | 투명도 조정 값. 1.0이면 변화 없음 | 0.0 ~ 1.0 | 1.0 |
| ALPHA_OFF | 투명도 오프셋 | 정수형 | 0 |
| RED | RGB 값 중 red 값 | 0.0 ~ 1.0 | 1.0 |
| RED_MOD | red 조정 값 | 0.0 ~ 1.0 | 1.0 |
| RED_OFF | red 오프셋 | 정수형 | 0 |
| GREEN | RGB 값 중 green 값 | 0.0 ~ 1.0 | 1.0 |
| GREEN_MOD | green 조정 값 | 0.0 ~ 1.0 | 1.0 |
| GREEN_OFF | green 오프셋 | 정수형 | 0 |
| BLUE | RGB 값 중 blue 값 | 0.0 ~ 1.0 | 1.0 |
| BLUE_MOD | blue 조정 값 | 0.0 ~ 1.0 | 1.0 |

**표 233 — 색상 효과 종류 2**

| 색상 효과 구분 | 이름/설명 | 값의 범위 | 기본 값 |
| :--- | :--- | :--- | :--- |
| BLUE_OFF | blue 오프셋 | 정수형 | 0 |
| HUE | HSL 컬러 모델에서 색조(hue) 값 설정 | 0 ~ 359 | |
| HUE_MOD | HSL 컬러 모델에서 색조 값 조정 | 0.0 ~ 1.0 | 1.0 |
| HUE_OFF | HSL 컬러 모델에서 색조 값 오프셋 | -16000 ~ 16000 | 0 |
| SAT | HSL 컬러 모델에서 채도(saturation) 값 설정 | 0.0 ~ 1.0 | |
| SAT_MOD | HSL 컬러 모델에서 채도 값 조정 | 0.0 ~ 1.0 | 1.0 |
| SAT_OFF | 채도 조정 값 오프셋 | | |
| LUM | HSL 컬러 모델에서 명도(luminance) 값 설정 | 0.0 ~ 1.0 | |
| LUM_MOD | HSL 컬러 모델에서 명도 값 조정 | 0.0 ~ 1.0 | 1.0 |
| LUM_OFF | 명도 오프셋 | | 0 |
| SHADE | 현재 색상을 어둡게 함. 1이면 변화 없음 | | 1 |
| TINT | 현재 색상을 밝게 함. 1이면 변화 없음 | | 1 |
| GRAY | Gray scale(회색조) 사용 | 0 또는 1 | |
| COMP | 보색(complementary color) 사용 | 0 또는 1 | |
| GAMMA | 감마(Gamma) 적용 (감마 값 = 1/2.2) | | |
| INV_GAMMA | 역감마(Inverse Gamma) 적용 (감마 값 = 2.2) | | |
| INV | 색상 반전 | | |

**10.9.6.5.3 네온 효과**
네온 효과 정보를 가지고 있는 요소이다.

**그림 147 — `<glow>`의 구조**

**표 234 — glow 요소**

| 속성 이름 | 설명 |
| :--- | :--- |
| alpha | 투명도 |
| radius | 네온 반경. 단위: HWPUNIT |

**표 235 — glow 하위 요소**

| 하위 요소 이름 | 설명 |
| :--- | :--- |
| effectsColor | 네온 색상 10.9.6.5.2.3 참조 |

**실습 130 glow 예**
```xml
<hp:glow alpha="0.5" radius="1000">
    <hp:effectsColor type="RGB" schemeIdx="-1" systemIdx="-1" presetIdx="-1">
        <hp:rgb r="178" g="178" b="178">
            <hp:effect type="SAT_MOD" value="0.75"/>
        </hp:effectsColor>
    </hp:glow>
10.9.6.5.4 부드러운 가장자리 효과
부드러운 가장자리 효과 정보를 가지고 있는 요소이다.
그림 148 — <softEdge>의 구조
표 236 — softEdge 요소
속성 이름	설명
radius	부드러운 가장자리 크기. 단위는 HWPUNIT
실습 131 softEdge 예
code
Xml
<hp:softEdge radius="500"/>
10.9.6.5.5 반사 효과
반사 효과 정보를 가지고 있는 요소이다.
그림 149 — <reflection>의 구조
표 237 — reflection 요소
속성 이름	설명
alignStyle	반사된 그림 위치
radius	흐릿한 정도. 단위: HWPUNIT
direction	반사된 그림 방향 각도
distance	대상과 반사된 그림 사이의 거리. 단위는 HWPUNIT
rotationstyle	도형과 함께 회전할 것인지 여부
fadeDirection	오프셋 방향
표 238 — reflection 하위 요소
하위 요소 이름	설명
skew	기울기 10.9.6.5.2.1 참조
scale	확대 비율 10.9.6.5.2.2 참조
alpha	투명도 설정 10.9.6.5.5.1 참조
pos	위치 설정 10.9.6.5.5.2 참조
실습 132 reflection 예
code
Xml
<hp:reflection alignStyle="BOTTOM_LEFT" radius="50" direction="90" distance="400"
rotationStyle="0" fadeDirection="90">
    <hp:skew x="0" y="0"/>
    <hp:scale x="1" y="0"/>
    <hp:alpha start="0.5" end="0.99"/>
    <hp:pos start="0" end="0.75"/>
</hp:reflection>
투명도 설정
반사 효과 사용 시 투명도 설정 정보를 가지고 있는 요소이다.
그림 150 — <alpha>의 구조
표 239 — alpha 요소
속성 이름	설명
start	시작 위치 투명도
end	끝 위치 투명도
실습 133 alpha 예
code
Xml
<hp:alpha start="0.5" end="0.99"/>```

**반사 효과 위치 설정**
반사된 영상이 시작될 위치 정보를 가지고 있는 요소이다.

**그림 151 — `<pos>`의 구조**

**표 240 — pos 요소**

| 속성 이름 | 설명 |
| :--- | :--- |
| start | 시작 위치 |
| end | 끝 위치 |

**실습 134 pos 예**
```xml
<hp:pos start="0" end="0.75"/>
10.9.6.6 이미지 원본 정보
원본 그림의 크기 정보를 가지고 있는 요소이다.
표 241 — imgDim 요소
속성 이름	설명
dimwidth	원본 너비
dimheight	원본 높이
실습 135 imgDim 예
code
Xml
<hp:imgDim dimwidth="96000" dimheight="54000"/>
10.9.7 ole 요소
10.9.7.1 ole
<ole> 요소는 [AbstractShapeComponentType]을 상속받는다. [AbstractShapeComponentType]의 자세한 내용은 10.9.5를 참조한다.
그림 152 — <ole>의 구조
실습 136 ole 예
code
Xml
<hp:ole id="1790881810" zOrder="3" numberingType="PICTURE" textWrap="SQUARE" textFlow="BOTH_SIDES"
lock="0" dropcapstyle="None" href="" groupLevel="0" instid="717139988" objectType="EMBEDDED"
binaryItemIDRef="ole1" hasMoniker="0" drawAspect="CONTENT" eqBaseLine="0">
    <hp:offset x="0" y="0"/>
    <hp:orgSz width="14176" height="14176"/>
    <hp:curSz width="0" height="0"/>
    <hp:flip horizontal="0" vertical="0"/>
    <hp:rotationInfo angle="0" centerX="7088" centerY="7088" rotateimage="1"/>
    <hp:renderingInfo>
        <hp:transMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
        <hp:scaMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
        <hp:rotMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
    </hp:renderingInfo>
    <hp:extent x="14176" y="14176"/>
    <hp:lineShape color="#0000FF" width="133" style="DASH_DOT" endCap="ROUND" headStyle="NORMAL"
    tailStyle="NORMAL" headfill="0" tailfill="0" headSz="SMALL_SMALL" tailSz="SMALL_SMALL"
    outlineStyle="OUTER" alpha="0"/>
    <hp:sz width="14176" widthRelTo="ABSOLUTE" height="14176" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0"
    vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
    <hp:outMargin left="0" right="0" top="0" bottom="0"/>
    <hp:shapeComment>OLE 개체입니다. 개체 형식은 Bitmap Image입니다.</hp:shapeComment>
</hp:ole>
10.9.7.2 extent 요소
OLE 객체의 확장 크기 정보를 가지고 있는 요소이다.
그림 153 — <extent>의 구조
표 244 — extent 요소
속성 이름	설명
x	오브젝트 자체의 extent x 크기
y	오브젝트 자체의 extent y 크기
실습 137 extent 예
code
Xml
<hp:extent x="14176" y="14176"/>
10.9.8 container 요소
<container> 요소는 [AbstractShapeComponentType]을 상속받는다. [AbstractShapeComponentType]의 자세한 내용은 10.9.5를 참조한다.
<container> 요소는 다른 도형 객체를 묶기 위해서 사용되는 객체이다. <container> 요소로 묶을 수 있는 객체에는 컨테이너 객체 자신과, 선, 사각형, 타원, 호, 다각형, 곡선, 연결선과 같은 그리기 객체, 그림, OLE 객체가 있다.
그림 154 — <container>의 구조
실습 138 container 예
code
Xml
<hp:container id="1615476006" zOrder="1" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href=""
groupLevel="0" instid="541734183">
    <hp:sz width="31160" widthRelTo="ABSOLUTE" height="12660" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="0" allowOverlap="1"
    holdAnchorAndSO="0" vertRelTo="PAPER" horzRelTo="PAPER" vertAlign="TOP" horzAlign="LEFT"
    vertOffset="10540" horzOffset="11734"/>
    <hp:outMargin left="0" right="0" top="0" bottom="0"/>
    <hp:caption side="BOTTOM" fullSz="0" width="8504" gap="850" lastWidth="31160">
        <hp:subList id="0" textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="TOP"
        linkListIDRef="0" linkListNextIDRef="0" textWidth="0" textHeight="0" hasTextRef="0" hasNumRef="0">
            <hp:p id="0" paraPrIDRef="19" styleIDRef="2" pageBreak="0" columnBreak="0" merged="0">
                <hp:run charPrIDRef="7">
                    <hp:t>ShapeCompContainer</hp:t>
                </hp:run>
            </hp:p>
        </hp:subList>
    </hp:caption>
    <hp:shapeComment>묶음 개체입니다.</hp:shapeComment>
    <hp:rect id="2" zOrder="0" numberingType="NONE" textWrap="TOP_AND_BOTTOM"
    textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="1" instid="541734179" ratio="20"/>
    <hp:ellipse id="7602208" zOrder="0" numberingType="NONE" textWrap="TOP_AND_BOTTOM"
    textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="1" instid="541734181"
    intervalDirty="0" hasArcPr="0" arcType="NORMAL"/>
</hp:container>
10.9.9 chart 요소
<chart> 요소는 [AbstractShapeObjectType]을 상속받는다. [AbstractShapeObjectType]의 자세한 내용은 10.9.2를 참조한다.
<chartIDRef>: 차트 데이터에 대한 아이디 참조값으로 차트에 대한 xml 데이터는 OOXML의 형식을 사용하며 Chart/chart.xml (8.2 참조)에 기입된다.
그림 155 — <chart>의 구조
표 246 — chart 요소
속성 이름	설명
chartIDRef	차트 데이터에 대한 아이디 참조값
version	차트 버전
실습 139 chart 예
code
Xml
<hp:chart id="-1811647071" zOrder="6" numberingType="PICTURE" textWrap="SQUARE"
textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" chartIDRef="Chart/chart1.xml">
    <hp:sz width="32250" widthRelTo="ABSOLUTE" height="18750" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0"
    holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT"
    vertOffset="0" horzOffset="0"/>
    <hp:outMargin left="0" right="0" top="0" bottom="0"/>
</hp:chart>
10.10 그리기 객체
10.10.1 그리기 객체
그리기 객체는 연결선, 사각형, 원 등과 같은 기본 도형 객체보다 더 구체화된 도형 객체이다. 그리기 객체는 기본 도형 객체의 공통 속성을 모두 상속받으며 그리기 객체만을 위한 속성을 추가적으로 더 정의해서 사용한다.
10.10.2 AbstractDrawingObjectType
10.10.2.1 AbstractDrawingObjectType
[AbstractDrawingObjectType]은 그리기 객체의 기본 속성을 정의하고 있는 요소 형식이다. [AbstractDrawingObjectType]은 [AbstractShapeComponentType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다. [AbstractShapeComponentType]의 자세한 내용은 10.9.5를 참조한다.
[AbstractDrawingObjectType]은 추상 형식이므로 [AbstractDrawingObjectType]만으로는 XML 요소를 생성할 수 없다.
그림 156 — [AbstractDrawingObjectType]의 구조
표 247 — AbstractDrawingObjectType 요소
하위 요소 이름	설명
lineShape	그리기 객체의 테두리선 정보 10.9.6.2 참조
fillBrush	그리기 객체의 채우기 정보
drawText	그리기 객체 글상자용 텍스트
shadow	그리기 객체의 그림자 정보
실습 140 AbstractDrawingObjectType 예
code
Xml
<hp:lineShape color="#000000" width="33" style="SOLID" endCap="FLAT" headStyle="NORMAL" tailStyle="NORMAL"
headfill="1" tailfill="1" headSz="MEDIUM_MEDIUM" tailSz="MEDIUM_MEDIUM" outlineStyle="NORMAL" alpha="0"/>
<hp:fillBrush>
    <hc:winBrush faceColor="#FFFFFF" hatchColor="#000000" alpha="0"/>
</hp:fillBrush>
<hp:shadow type="NONE" color="#828282" offsetX="0" offsetY="0" alpha="0"/>
<hp:drawText lastWidth="34260" name="" editable="0"/>
10.10.2.2 채우기 정보
10.10.2.2.1 채우기
그리기 객체에서 객체의 면 영역에서 사용된 채우기 효과 정보를 가지고 있는 요소이다.
그림 157 — <fillBrush>의 구조
표 248 — fillBrush 요소
하위 요소 이름	설명
winBrush	면 채우기
gradation	그러데이션 효과
imgBrush	그림으로 채우기
10.10.2.2.2 면 채우기 정보
채우기 효과 중 단색 또는 무늬가 입혀진 단색으로 채우는 효과 정보를 가지고 있는 요소이다.
그림 158 — <winBrush>의 구조
표 249 — winBrush 요소
속성 이름	설명
faceColor	면 색상
hatchColor	무늬 색
hatchstyle	무늬 종류
alpha	투명도
10.10.2.2.3 그러데이션 효과
한 색상에서 다른 색상으로 점진적 또는 단계적으로 변하는 기법을 표현하기 위한 요소이다.
그림 159 — <gradation>의 구조
표 250 — gradation 요소
속성 이름	설명
type	그러데이션 유형
angle	그러데이션 기울기 (시작각)
centerX	그러데이션 가로 중심 (중심 X 좌표)
centerY	그러데이션 세로 중심 (중심 Y 좌표)
step	그러데이션 번짐 정도 (0-255)
colorNum	그러데이션 색상 수
stepCenter	그러데이션 번짐 정도의 중심 (0-100)
alpha	투명도
표 251 — gradation 하위 요소
하위 요소 이름	설명
color	그러데이션 색상
그러데이션 색상
그러데이션 색상으로 표현하기 위한 요소로, 점진적으로 또는 단계적으로 변화하는 색상 중 시작 색, 또는 끝 색, 중간 단계 색 등을 표현한다.
그림 160 — <color>의 구조
표 252 — color 요소
속성 이름	설명
value	색상값
10.10.2.2.4 그림으로 채우기 정보
그림으로 특정 부분을 채울 때 사용되는 요소로, 지정된 그림을 지정된 효과를 사용해서 채운다. 사용할 수 있는 효과에는 '크기에 맞추어', '위로/가운데로/아래로', '바둑판식으로' 등이 있다.
10.10.2.3 그리기 객체 글상자용 텍스트
그리기 객체 안의 또는 지정 영역에 표시되는 글상자 내용을 가지고 있는 요소이다.
표 255 — drawText 요소
속성 이름	설명
lastwidth	라스트 라인의 최대 폭. 단위는 HWPUNIT
name	글상자 이름
editable	편집 가능 여부
표 256 — drawText 하위 요소
하위 요소 이름	설명
textMargin	글상자 텍스트 여백
subList	글상자 텍스트 11.1.2 참조
실습 141 drawText 예
code
Xml
<hp:drawText lastWidth="12540" name="" editable="0">
    <hp:subList id="0" textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="CENTER"
    linkListIDRef="0" linkListNextIDRef="0" textWidth="0" textHeight="0" hasTextRef="1" hasNumRef="0">
        <hp:p id="0" paraPrIDRef="20" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
            <hp:run charPrIDRef="8">
                <hp:t>Rectangle</hp:t>
            </hp:run>
        </hp:p>
    </hp:subList>
    <hp:textMargin left="283" right="283" top="283" bottom="283"/>
</hp:drawText>
10.10.2.3.2 글상자 텍스트 여백
<textMargin> 요소는 [MarginAttributeGroup]을 속성으로 포함한다. [MarginAttributeGroup]은 10.6.6.2를 참조한다.
그림 163 — <textMargin>의 구조
표 257 — textMargin 요소
속성 이름	설명
[MarginAttributeGroup]	10.6.6.2 참조
실습 142 textMargin 예
code
Xml
<hp:textMargin left="283" right="283" top="283" bottom="283"/>
10.10.2.4 그리기 객체의 그림자 정보
그리기 객체에 적용될 그림자 효과 정보를 가지고 있는 요소이다.
그림 164 — <shadow>의 구조
표 258 — shadow 요소
속성 이름	설명
type	그림자 종류
color	그림자 색
offsetX	그림자 간격 X. 단위는 %
offsetY	그림자 간격 Y. 단위는 %
10.10.3 그리기 객체 — 선
그림 165 — <line>의 구조
표 259 — line 요소
속성 이름	설명
isReverseHV	처음 생성 시 수직선 또는 수평선일 때, 선의 방향이 언제나 오른쪽(위쪽)으로 잡힘으로 인한 현상 때문에 방향을 바로 잡아주기 위한 속성
표 260 — line 하위 요소
하위 요소 이름	설명
startPt	시작점 10.9.6.3.2 참조
endPt	끝점 10.9.6.3.2 참조
실습 144 line 예
code
Xml
<hp:line id="1480891240" zOrder="1" numberingType="PICTURE" textWrap="IN_FRONT_OF_TEXT"
textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="0" instid="407149417"
isReverseHV="0">
    <hp:startPt x="0" y="0"/>
    <hp:endPt x="4686" y="9102"/>
</hp:line>
10.10.4 그리기 객체 — 사각형
<rect> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
표 261 — rect 요소
속성 이름	설명
ratio	사각형 모서리 곡률. 단위는 %. 직각은 0, 둥근 모양은 20, 반원은 50 등
표 262 — rect 하위 요소
하위 요소 이름	설명
pt0	첫 번째 좌표 10.9.6.3.2 참조
pt1	두 번째 좌표 10.9.6.3.2 참조
pt2	세 번째 좌표 10.9.6.3.2 참조
pt3	네 번째 좌표 10.9.6.3.2 참조
실습 145 rect 예
code
Xml
<hp:rect id="1480891242" zOrder="2" numberingType="PICTURE" textWrap="IN_FRONT_OF_TEXT"
textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="0" instid="407149419"
ratio="0">
    <hp:ptO x="0" y="0"/>
    <hp:pt1 x="12838" y="0"/>
    <hp:pt2 x="12838" y="9306"/>
    <hp:pt3 x="0" y="9306"/>
</hp:rect>
10.10.5 그리기 객체 — 타원
<ellipse> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
표 263 — ellipse 요소
속성 이름	설명
intervalDirty	호(arc)로 바뀌었을 때, interval을 다시 계산해야 할 필요가 있는지 여부. interval: 원 위에 존재하는 두 점 사이의 거리
hasArcProperty	호로 바뀌었는지 여부
arcType	호의 종류. NORMAL: 호, PIE: 부채꼴, CHORD: 활
표 264 — ellipse 하위 요소
하위 요소 이름	설명
center	중심 좌표 10.9.6.3.2 참조
ax1	제1 축 좌표 10.9.6.3.2 참조
ax2	제2 축 좌표 10.9.6.3.2 참조
start1	시작 지점 1 좌표 10.9.6.3.2 참조
end1	끝 지점 1 좌표 10.9.6.3.2 참조
start2	시작 지점 2 좌표 10.9.6.3.2 참조
end2	끝 지점 2 좌표 10.9.6.3.2 참조
실습 146 ellipse 예```xml
<hp:ellipse id="1480891244" zOrder="3" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href=""
groupLevel="0" instid="407149421" intervalDirty="0" hasArcPr="0" arcType="NORMAL">
<hp:center x="4925" y="3973"/>
<hp:ax1 x="9850" y="3973"/>
<hp:ax2 x="4925" y="0"/>
<hp:start1 x="0" y="-1337540795"/>
<hp:end1 x="-114407252" y="1432413552"/>
<hp:start2 x="-1105998402" y="100663296"/>
<hp:end2 x="393344" y="2"/>
</hp:ellipse>
code
Code
**10.10.6 그리기 객체 — 호**
`<arc>` 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.

**그림 168 — `<arc>`의 구조**

**표 265 — arc 요소**

| 속성 이름 | 설명 |
| :--- | :--- |
| type | 호의 종류. NORMAL: 호, PIE: 부채꼴, CHORD: 활 |

**표 266 — arc 하위 요소**

| 하위 요소 이름 | 설명 |
| :--- | :--- |
| center | 중심 좌표 10.9.6.3.2 참조 |
| ax1 | 제1 축 좌표 10.9.6.3.2 참조 |
| ax2 | 제2 축 좌표 10.9.6.3.2 참조 |

**실습 147 arc 예**
```xml
<hp:arc id="1480891246" zOrder="4" numberingType="PICTURE" textWrap="IN_FRONT_OF_TEXT"
textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="0" instid="407149423"
type="NORMAL">
    <hp:center x="0" y="0"/>
    <hp:ax1 x="0" y="9645"/>
    <hp:ax2 x="1417" y="0"/>
</hp:arc>
10.10.7 그리기 객체 — 다각형
<polygon> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
그림 169 — <polygon>의 구조
표 267 — polygon 요소
하위 요소 이름	설명
pt	다각형 좌표 10.9.6.3.2 참조
실습 148 polygon 예
code
Xml
<hp:polygon id="1480891248" zOrder="5" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href=""
groupLevel="0" instid="407149425">
    <hp:pt x="326" y="0"/>
    <hp:pt x="0" y="3872"/>
    <hp:pt x="-3329" y="7744"/>
    <hp:pt x="-1154" y="7540"/>
    <hp:pt x="1142" y="-2047"/>
    <hp:pt x="326" y="0"/>
</hp:polygon>
10.10.8 그리기 객체 — 곡선
10.10.8.1 곡선
<curve> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
표 268 — curve 요소
하위 요소 이름	설명
seg	곡선 세그먼트
실습 149 curve 예
code
Xml
<hp:curve id="1480891254" zOrder="6" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="1" dropcapstyle="None" href=""
groupLevel="0" instid="407149431">
    <hp:seg type="CURVE" x1="?" y1="1485" x2="1429" y2="10859"/>
    <hp:seg type="CURVE" x1="1429" y1="10859" x2="3263" y2="882"/>
    <hp:seg type="CURVE" x1="3263" y1="882" x2="5233" y2="11199"/>
    <hp:seg type="CURVE" x1="5233" y1="11199" x2="5980" y2="910"/>
    <hp:seg type="CURVE" x1="5980" y1="910" x2="274" y2="1485"/>
</hp:curve>
10.10.8.2 곡선 세그먼트
그리기 객체 중 곡선을 표현할 때 곡선의 단위, 곡선의 시작점 및 끝점을 표현하기 위한 요소이다.
표 269 — seg 요소
속성 이름	설명
type	곡선 세그먼트 형식. curve: 곡선, line: 직선
x1	곡선 세그먼트 시작점 X 좌표
y1	곡선 세그먼트 시작점 y 좌표
x2	곡선 세그먼트 끝점 X 좌표
y2	곡선 세그먼트 끝점 y 좌표
실습 150 seg 예
code
Xml
<hp:seg type="CURVE" x1="274" y1="1485" x2="1429" y2="10859"/>
10.10.9 그리기 객체 — 연결선
10.10.9.1 연결선
<connectLine> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
표 270 — connectLine 요소
속성 이름	설명
type	연결선 형식
표 271 — connectLine 하위 요소
하위 요소 이름	설명
startPt	연결선 시작점 정보
endPt	연결선 끝점 정보
controlPoints	연결선 조절점 정보
실습 151 connectLine 예
code
Xml
<hp:connectLine id="1480891256" zOrder="7" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href=""
groupLevel="0" instid="407149433" type="STRAIGHT_NO_ARROW">
    <hp:startPt x="?" y="4154" subjectIDRef="407149431" subjectIdx="-1"/>
    <hp:endPt x="?" y="0" subjectIDRef="407149427" subjectIdx="2"/>
    <hp:controlPoints>
        <hp:point x="?" y="4144" type="3"/>
        <hp:point x="?" y="0" type="26"/>
    </hp:controlPoints>
</hp:connectLine>
10.10.9.2 연결선 연결점 정보
[ConnectPointType]은 [PointType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다. [PointType]의 자세한 내용은 10.9.6.3.2를 참조한다.
그림 173 — [ConnectPointType]의 구조
표 272 — ConnectPointType 요소
속성 이름	설명
subjectIDRef	시작/끝 부분과 연결되는 대상의 아이디 참조값
subjectIdx	시작/끝 부분과 연결되는 대상의 연결점 index
실습 152 ConnectPointType 예
code
Xml
<hp:startPt x="0" y="0" subjectIDRef="0" subjectIdx="0"/>
<hp:endPt x="15402" y="10581" subjectIDRef="1" subjectIdx="0"/>
10.10.9.3 연결선 조절점 정보
[ConnectControlPointType]은 [PointType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다.
표 273 — ConnectControlPointType 속성
속성 이름	설명
type	조절점 종류
실습 153 ConnectControlPointType 예
code
Xml
<hp:controlPoints>
    <hp:point x="-2446" y="0" type="3"/>
    <hp:point x="-2446" y="-2207" type="2"/>
    <hp:point x="0" y="-2207" type="2"/>
    <hp:point x="0" y="-7035" type="26"/>
</hp:controlPoints>
표 274 — type 값
type 값	설명
0x00000001	시작점
0x00000002	직선
0x0000001a	끝점
10.11 양식 객체
10.11.1 AbstractFormObjectType
10.11.1.1 AbstractFormObjectType
[AbstractFormObjectType]은 양식 객체의 공통 속성을 정의한다. [AbstractFormObjectType]은 [AbstractShapeObjectType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다. [AbstractShapeObjectType]의 자세한 내용은 10.9.2를 참조한다.
[AbstractFormObjectType]은 추상 형식이므로 [AbstractFormObjectType]만으로는 XML 요소를 생성할 수 없다.
표 275 — AbstractFormObjectType 요소
속성 이름	설명
name	이름
foreColor	전경색
backColor	배경색
groupName	그룹 이름
tabStop	Tab 키로 객체들을 이동할 때 해당 객체에 멈출 수 있는지 설정하는 속성
editable	편집 가능 여부
tabOrder	Tab 키 이동 순서
enabled	활성화 여부
borderTypeIDRef	테두리 아이디 참조값
drawFrame	프레임 표시 가능 여부
printable	출력 가능 여부
표 276 — AbstractFormObjectType 하위 요소
하위 요소 이름	설명
formCharPr	양식 객체의 글자 속성
실습 154 AbstractFormObjectType 요소
code
Xml
<hp:btn caption="누름 단추" radioGroupName="" triState="0" name="PushButton1" foreColor="#000000"
backColor="#F0F0F0" groupName="" tabStop="1" editable="1" tabOrder="1" enabled="1" borderTypeIDRef="4"
drawFrame="1" printable="1" command="">
    <hp:formCharPr charPrIDRef="1" followContext="0" autoSz="0" wordWrap="0"/>
    <hp:sz width="7087" widthRelTo="ABSOLUTE" height="1964" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="1" affectLSpacing="1" flowWithText="1" allowOverlap="1" holdAnchorAndSO="1"
    vertRelTo="PARA" horzRelTo="PARA" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
    <hp:outMargin left="133" right="133" top="133" bottom="133"/>
</hp:btn>
10.11.1.2 양식 객체의 글자 속성
그림 175 — <formCharPr>의 구조
표 277 — formCharPr 요소
속성 이름	설명
charPrIDRef	글자 모양 아이디 참조값
followContext	양식 객체가 주위의 글자 속성을 따라갈지 여부
autoSize	자동 크기 조절 여부
wordWrap	줄 내림 여부
실습 155 formCharPr 예
code
Xml
<hp:formCharPr charPrIDRef="?" followContext="0" autoSz="0" wordWrap="0"/>
10.11.2 AbstractButtonObjectType
[AbstractButtonObjectType]은 버튼 양식 객체의 공통 속성을 정의한다. [AbstractButtonObjectType]은 [AbstractFormObjectType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다. [AbstractFormObjectType]의 자세한 내용은 10.11.1을 참조한다.
[AbstractButtonObjectType]은 추상 형식이므로 [AbstractButtonObjectType]만으로는 XML 요소를 생성할 수 없다.