KS X 6101 표준 문서 복원
338 / 414
KS X 6101:2024
code
Xml
<xs:annotation>
    <xs:documentation>구분선 굵기. 단위는 mm.</xs:documentation>
</xs:annotation>
</xs:attribute>
<xs:attribute name="color" type="hc:RGBColorType" default="000000">
    <xs:annotation>
        <xs:documentation>글자 색깔.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="noteSpacing">
<xs:complexType>
<xs:attribute name="betweenNotes" type="xs:nonNegativeInteger" default="850">
    <xs:annotation>
        <xs:documentation>각주 사이 여백</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="belowLine" type="xs:nonNegativeInteger" default="567">
331
KSX 6101:2024
code
Xml
<xs:annotation>
        <xs:documentation>구분선 아래 여백</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="aboveLine" type="xs:nonNegativeInteger" default="567">
    <xs:annotation>
        <xs:documentation>구분선 위 여백</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="FootNoteShapeType">
<xs:annotation>
    <xs:documentation>각주 모양 및 속성</xs:documentation>
</xs:annotation>
<xs:complexContent>
<xs:extension base="hp:NoteShapeType">
<xs:sequence>
<xs:element name="numbering">
<xs:complexType>
<xs:attribute name="type" default="CONTINUOUS">
    <xs:annotation>
        <xs:documentation>번호 매기기 형식</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="CONTINUOUS">
                <xs:annotation>
                    <xs:documentation>앞 구역에 이어서</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ON_SECTION">
                <xs:annotation>
                    <xs:documentation>새 구역부터 새로 시작</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ON_PAGE">
                <xs:annotation>
                    <xs:documentation>쪽마다 새로 시작. 각주 전용</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
340 / 414
KSX 6101:2024
code
Xml
</xs:attribute>
<xs:attribute name="newNum" type="xs:positiveInteger" default="1">
    <xs:annotation>
        <xs:documentation>새 시작 번호. type이 ON_SECTION일 때만 사용한다.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="placement">
<xs:complexType>
<xs:attribute name="place" default="EACH_COLUMN">
    <xs:annotation>
        <xs:documentation>한 페이지 내에서 각주를 다단에 어떻게 위치시킬지를 표시한다</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="EACH_COLUMN">
                <xs:annotation>
                    <xs:documentation>각 단에</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="MERGED_COLUMN">
                <xs:annotation>
                    <xs:documentation>단 합쳐서</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="RIGHT_MOST_COLUMN">
                <xs:annotation>
                    <xs:documentation>가장 오른쪽 단에</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="beneathText" type="xs:boolean" default="false">
    <xs:annotation>
        <xs:documentation>본문에 이어 바로 출력할지 여부</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
KSX 6101:2024
code
Xml
</xs:element>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="EndNoteShapeType">
<xs:annotation>
    <xs:documentation>미주 모양 및 속성</xs:documentation>
</xs:annotation>
<xs:complexContent>
<xs:extension base="hp:NoteShapeType">
<xs:sequence>
<xs:element name="numbering">
<xs:complexType>
<xs:attribute name="type" default="CONTINUOUS">
    <xs:annotation>
        <xs:documentation>번호 매기기 형식</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
341 / 414
code
Xml
<xs:restriction base="xs:string">
            <xs:enumeration value="CONTINUOUS">
                <xs:annotation>
                    <xs:documentation>앞 구역에 이어서</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ON_SECTION">
                <xs:annotation>
                    <xs:documentation>새 구역부터 새로 시작</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="newNum" type="xs:positiveInteger" default="1">
    <xs:annotation>
        <xs:documentation>새 시작 번호. type이 ON_SECTION일 때만 사용한다.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="placement">
<xs:complexType>
<xs:attribute name="place" default="END_OF_DOCUMENT">
    <xs:annotation>
334
KSX 6101:2024
code
Xml
<xs:documentation>한 페이지 내에서 미주를 다단에 어떻게 위치시킬지를 표시한다</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="END_OF_DOCUMENT">
                <xs:annotation>
                    <xs:documentation>문서의 마지막</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="END_OF_SECTION">
                <xs:annotation>
                    <xs:documentation>구역의 마지막</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="beneathText" type="xs:boolean" default="false">
    <xs:annotation>
        <xs:documentation>본문에 이어 바로 출력할지 여부</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="AutoNumFormatType">
<xs:attribute name="type" type="hcf:NumberType2" default="DIGIT">
    <xs:annotation>
        <xs:documentation>번호 모양</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="userChar" type="xs:string">
    <xs:annotation>
        <xs:documentation>사용자 정의 문자</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="prefixChar" type="xs:string">
    <xs:annotation>
        <xs:documentation>앞 장식 문자</xs:documentation>
    </xs:annotation>
342 / 414
KSX 6101:2024
335
code
Xml
</xs:attribute>
<xs:attribute name="suffixChar" type="xs:string" default=".">
    <xs:annotation>
        <xs:documentation>뒤 장식 문자</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="supscript" type="xs:boolean" default="false">
    <xs:annotation>
        <xs:documentation>각주/미주 내용 중 번호 코드의 모양을 위 첨자 형식으로 할지 여부</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
<xs:simpleType name="VisibilityValue">
<xs:restriction base="xs:string">
<xs:enumeration value="HIDE_FIRST"/>
<xs:enumeration value="SHOW_FIRST"/>
<xs:enumeration value="SHOW_ALL"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="ColumnDefType">
<xs:sequence>
<xs:element name="colLine" minOccurs="0">
    <xs:annotation>
        <xs:documentation>단 구분선 모양</xs:documentation>
    </xs:annotation>
    <xs:complexType>
        <xs:attribute name="type" type="hc:LineType2" default="SOLID"/>
        <xs:attribute name="width" type="hc:LineWidth" default="0.12 mm"/>
        <xs:attribute name="color" type="hc:RGBColorType" default="000000"/>
    </xs:complexType>
</xs:element>
<xs:element name="colSz" minOccurs="0" maxOccurs="255">
    <xs:annotation>
        <xs:documentation>sameSize가 false일 때, 각 단의 크기 및 사이 간격</xs:documentation>
    </xs:annotation>
    <xs:complexType>
        <xs:attribute name="width" type="xs:positiveInteger"/>
        <xs:attribute name="gap" type="xs:nonNegativeInteger"/>
    </xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="id" type="xs:string" use="required"/>
<xs:attribute name="type" default="NEWSPAPER">
    <xs:annotation>
        <xs:documentation>단 종류</xs:documentation>
    </xs:annotation>
336
KSX 6101:2024
code
Xml
<xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="NEWSPAPER"/>
            <xs:enumeration value="BALANCED_NEWSPAPER"/>
            <xs:enumeration value="PARALLEL"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="layout" default="LEFT">
    <xs:annotation>
        <xs:documentation>단 방향 지정</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="LEFT"/>
            <xs:enumeration value="RIGHT"/>
            <xs:enumeration value="MIRROR"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="colCount" default="1">
    <xs:annotation>
        <xs:documentation>단 개수</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:positiveInteger">
            <xs:maxInclusive value="255"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="sameSize" type="xs:boolean" default="false">
    <xs:annotation>
        <xs:documentation>false: 단 너비 각각 지정. true: 단 너비 동일하게</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="sameGap" type="xs:nonNegativeInteger" default="0">
    <xs:annotation>
        <xs:documentation>단 사이 간격. sameSize가 true일 때만 지정.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
<xs:complexType name="InsideMarginType">
<xs:attributeGroup ref="hc:MarginAttributeGroup"/>
</xs:complexType>
<xs:complexType name="LineShapeType">
<xs:attribute name="color" type="hc:RGBColorType"/>
KSX 6101:2024
code
Xml
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="style" type="hc:LineType" default="SOLID"/>
<xs:attribute name="endCap" default="FLAT">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="ROUND"/>
            <xs:enumeration value="FLAT"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="headStyle" type="hc:ArrowType" default="NORMAL"/>
<xs:attribute name="tailStyle" type="hc:ArrowType" default="NORMAL"/>
<xs:attribute name="headfill" type="xs:boolean" default="false"/>
<xs:attribute name="tailfill" type="xs:boolean" default="false"/>
<xs:attribute name="headSize" type="hc:ArrowSize" default="SMALL_SMALL"/>
<xs:attribute name="tailSize" type="hc:ArrowSize" default="SMALL_SMALL"/>
<xs:attribute name="outlineStyle" default="NORMAL">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="NORMAL"/>
            <xs:enumeration value="OUTER"/>
            <xs:enumeration value="INNER"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="alpha" type="xs:float"/>
</xs:complexType>
<xs:complexType name="EffectsType">
<xs:sequence>
<xs:element name="shadow" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="skew" type="hp:SkewType">
    <xs:annotation>
        <xs:documentation>기울이기 속성</xs:documentation>
    </xs:annotation>
</xs:element>
<xs:element name="scale" type="hp:ScaleType">
    <xs:annotation>
        <xs:documentation>크기 조절</xs:documentation>
    </xs:annotation>
345 / 414
KS X 6101:2024
338
code
Xml
</xs:element>
<xs:element name="effectsColor" type="hp:EffectColorType">
    <xs:annotation>
        <xs:documentation>그림자 색</xs:documentation>
    </xs:annotation>
</xs:element>
</xs:sequence>
<xs:attribute name="style">
    <xs:annotation>
        <xs:documentation>그림자 스타일</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="LEFT_TOP"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="alpha">
    <xs:annotation>
        <xs:documentation>그림자 투명도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="1"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="radius" type="xs:float">
    <xs:annotation>
        <xs:documentation>부드러운 가장자리 크기. 단위는 HWPUNIT</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="glow" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="effectsColor" type="hp:GlowEffectColorType">
    <xs:annotation>
        <xs:documentation>네온 색</xs:documentation>
    </xs:annotation>
</xs:element>
</xs:sequence>
<xs:attribute name="alpha">
    <xs:annotation>
        <xs:documentation>투명도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="1"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="radius" type="xs:float">
    <xs:annotation>
        <xs:documentation>네온 반경. 단위 HWPUNIT</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="softEdge" minOccurs="0">
<xs:complexType>
<xs:attribute name="radius" type="xs:float">
    <xs:annotation>
        <xs:documentation>부드러운 가장자리 크기. 단위는 HWPUNIT.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="reflection" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="skew" type="hp:SkewType"/>
<xs:element name="scale" type="hp:ScaleType"/>
<xs:element name="alpha">
<xs:complexType>
340
KSX 6101:2024
code
Xml
<xs:attribute name="start">
    <xs:annotation>
        <xs:documentation>시작 위치 투명도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="1"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="end">
    <xs:annotation>
        <xs:documentation>끝 위치 투명도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="1"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="pos">
    <xs:annotation>
        <xs:documentation>위치</xs:documentation>
    </xs:annotation>
    <xs:complexType>
        <xs:attribute name="start" type="xs:float">
            <xs:annotation>
                <xs:documentation>시작 위치</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="end" type="xs:float">
            <xs:annotation>
                <xs:documentation>끝 위치</xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
</xs:element>
348 / 414
KSX 6101:2024
code
Xml
</xs:sequence>
<xs:attribute name="alignStyle" type="hc:AlignStyleType"/>
<xs:attribute name="radius" type="xs:float">
    <xs:annotation>
        <xs:documentation>흐릿한 정도. 단위 HWPUNIT.</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="direction">
    <xs:annotation>
        <xs:documentation>그림자 방향 각도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:integer">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="360"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="distance">
    <xs:annotation>
        <xs:documentation>거리. 단위는 HWPUNIT.</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="rotationStyle" type="xs:boolean">
    <xs:annotation>
        <xs:documentation>도형과 함께 회전 여부</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="fadeDirection">
    <xs:annotation>
        <xs:documentation>사라지는 방향</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:integer">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="360"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="EffectColorType">
<xs:sequence>
<xs:choice>
<xs:element name="rgb">
    <xs:complexType>
        <xs:attribute name="r" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="g" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="b" type="xs:nonNegativeInteger" use="required"/>
    </xs:complexType>
</xs:element>
KSX 6101:2024
code
Xml
<xs:element name="cmyk">
    <xs:complexType>
        <xs:attribute name="c" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="m" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="y" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="k" type="xs:nonNegativeInteger" use="required"/>
    </xs:complexType>
</xs:element>
<xs:element name="scheme">
    <xs:complexType>
        <xs:attribute name="r" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="g" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="b" type="xs:nonNegativeInteger" use="required"/>
    </xs:complexType>
</xs:element>
<xs:element name="system">
    <xs:complexType>
        <xs:attribute name="r" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="g" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="b" type="xs:nonNegativeInteger" use="required"/>
    </xs:complexType>
</xs:element>
</xs:choice>
</xs:sequence>
<xs:attribute name="type" use="required">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="RGB"/>
<xs:enumeration value="CMYK"/>
<xs:enumeration value="SCHEME"/>
<xs:enumeration value="SYSTEM"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="schemeIdx" type="xs:integer"/>
<xs:attribute name="presetIdx" type="xs:integer"/>
</xs:complexType>
<xs:complexType name="GlowEffectColorType">
<xs:complexContent>
<xs:extension base="hp:EffectColorType">
<xs:sequence>
<xs:element name="effect" minOccurs="0">
<xs:complexType>
<xs:attribute name="type" use="required">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="ALPHA"/>
350/414
KSX 6101:2024
code
Xml
<xs:enumeration value="ALPHA_MOD"/>
<xs:enumeration value="ALPHA_OFF"/>
<xs:enumeration value="RED"/>
<xs:enumeration value="RED_MOD"/>
<xs:enumeration value="RED_OFF"/>
<xs:enumeration value="GREEN"/>
<xs:enumeration value="GREEN_MOD"/>
<xs:enumeration value="GREEN_OFF"/>
<xs:enumeration value="BLUE"/>
<xs:enumeration value="BLUE_MOD"/>
<xs:enumeration value="BLUE_OFF"/>
<xs:enumeration value="HUE"/>
<xs:enumeration value="HUE_MOD"/>
<xs:enumeration value="HUE_OFF"/>
<xs:enumeration value="SAT"/>
<xs:enumeration value="SAT_MOD"/>
<xs:enumeration value="SAT_OFF"/>
<xs:enumeration value="LUM"/>
<xs:enumeration value="LUM_MOD"/>
<xs:enumeration value="LUM_OFF"/>
<xs:enumeration value="SHADE"/>
<xs:enumeration value="TINT"/>
<xs:enumeration value="GRAY"/>
<xs:enumeration value="COMP"/>
<xs:enumeration value="GAMMA"/>
<xs:enumeration value="INV_GAMMA"/>
<xs:enumeration value="INV"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
351/414
KSX 6101:2024
code
Xml
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="SkewType">
<xs:attribute name="x">
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="-90"/>
            <xs:maxInclusive value="90"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="y">
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="-90"/>
            <xs:maxInclusive value="90"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:complexType>
<xs:complexType name="ScaleType">
<xs:attribute name="x" type="xs:float"/>
<xs:attribute name="y" type="xs:float"/>
</xs:complexType>
<xs:complexType name="ShadowType">
<xs:annotation>
    <xs:documentation>그림자 속성</xs:documentation>
</xs:annotation>
<xs:attribute name="type" default="NONE">
    <xs:annotation>
        <xs:documentation>그림자 종류</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="PARALLEL_LEFTTOP"/>
            <xs:enumeration value="PARALLEL_RIGHTTOP"/>
            <xs:enumeration value="PARALLEL_LEFTBOTTOM"/>
            <xs:enumeration value="PARALLEL_RIGHTBOTTOM"/>
            <xs:enumeration value="SHEAR_LEFTTOP"/>
            <xs:enumeration value="SHEAR_RIGHTTOP"/>
            <xs:enumeration value="SHEAR_LEFTBOTTOM"/>
            <xs:enumeration value="SHEAR_RIGHTBOTTOM"/>
            <xs:enumeration value="PERS_LEFTTOP"/>
            <xs:enumeration value="PERS_RIGHTTOP"/>
            <xs:enumeration value="PERS_LEFTBOTTOM"/>
            <xs:enumeration value="PERS_RIGHTBOTTOM"/>
            <xs:enumeration value="SCALE_NARROW"/>
            <xs:enumeration value="SCALE_ENLARGE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="color" type="hc:RGBColorType" default="808080">
    <xs:annotation>
        <xs:documentation>그림자 색</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="offsetX">
    <xs:annotation>
        <xs:documentation>그림자 간격 X</xs:documentation>
    </xs:annotation>
345
KSX 6101:2024
code
Xml
<xs:simpleType>
        <xs:restriction base="xs:integer"/>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="offsetY">
    <xs:annotation>
        <xs:documentation>그림자 간격 Y</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:integer"/>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="alpha" type="xs:float"/>
</xs:complexType>
<xs:complexType name="AbstractShapeObjectType" abstract="true">
<xs:sequence>
<xs:element name="sz" minOccurs="0">
<xs:complexType>
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="widthRelTo" default="ABSOLUTE">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="PAPER"/>
            <xs:enumeration value="PAGE"/>
            <xs:enumeration value="COLUMN"/>
            <xs:enumeration value="PARA"/>
            <xs:enumeration value="ABSOLUTE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="height" type="xs:nonNegativeInteger"/>
<xs:attribute name="heightRelTo" default="ABSOLUTE">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="PAPER"/>
            <xs:enumeration value="PAGE"/>
            <xs:enumeration value="ABSOLUTE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="protect" type="xs:boolean" default="false"/>
</xs:complexType>
</xs:element>
<xs:element name="pos" minOccurs="0">
<xs:complexType>
<xs:attribute name="treatAsChar" type="xs:boolean" default="false"/>
<xs:attribute name="affectLSpacing" type="xs:boolean" default="false"/>
<xs:attribute name="flowWithText" type="xs:boolean" default="false"/>
<xs:attribute name="allowOverlap" type="xs:boolean" default="false"/>
<xs:attribute name="holdAnchorAndSO" type="xs:boolean" default="false"/>
<xs:attribute name="vertRelTo" default="PARA">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="PAPER"/>
            <xs:enumeration value="PAGE"/>
            <xs:enumeration value="PARA"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="horzRelTo" default="COLUMN">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="PAPER"/>
            <xs:enumeration value="PAGE"/>
            <xs:enumeration value="COLUMN"/>
            <xs:enumeration value="PARA"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="vertAlign" default="TOP">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="TOP"/>
            <xs:enumeration value="CENTER"/>
            <xs:enumeration value="BOTTOM"/>
            <xs:enumeration value="INSIDE"/>
            <xs:enumeration value="OUTSIDE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="horzAlign" default="LEFT">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="LEFT"/>
            <xs:enumeration value="CENTER"/>
            <xs:enumeration value="RIGHT"/>
            <xs:enumeration value="INSIDE"/>
            <xs:enumeration value="OUTSIDE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="vertOffset" type="xs:nonNegativeInteger" default="0"/>
<xs:attribute name="horzOffset" type="xs:nonNegativeInteger" default="0"/>
</xs:complexType>
</xs:element>
<xs:element name="outMargin" minOccurs="0">
이전 파일에서 이어짐
code
Xml
<xs:enumeration value="BEHIND_TEXT"/>
<xs:enumeration value="IN_FRONT_OF_TEXT"/>
KSX 6101:2024
code
Xml
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="textFlow" default="BOTH_SIDES">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="BOTH_SIDES"/>
<xs:enumeration value="LEFT_ONLY"/>
<xs:enumeration value="RIGHT_ONLY"/>
<xs:enumeration value="LARGEST_ONLY"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="lock" type="xs:boolean" default="false"/>
<xs:attribute name="dropcapstyle" type="hc:DropCapStyleType" default="None"/>
</xs:complexType>
<xs:complexType name="TableType">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeObjectType">
<xs:sequence>
<xs:element name="inMargin" type="hp:InsideMarginType"/>
<xs:element name="cellzone">
<xs:complexType>
<xs:sequence>
<xs:element name="cell" maxOccurs="unbounded">
<xs:complexType>
<xs:attribute name="startRowAddr" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>병합된 Row의 시작 주소</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="startColAddr" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>병합된 Column의 시작 주소</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="endRowAddr" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>병합된 Row의 끝 주소</xs:documentation>
    </xs:annotation>
</xs:attribute>
349
KSX 6101:2024
code
Xml
<xs:attribute name="endColAddr" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>병합된 Column의 끝 주소</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>테두리/배경 아이디 참조 값</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:element name="tc" maxOccurs="unbounded">
<xs:complexType>
<xs:sequence>
<xs:element name="subList" type="hp:ParaListType"/>
<xs:element name="cellAddr">
<xs:complexType>
<xs:attribute name="colAddr" type="xs:nonNegativeInteger"/>
<xs:attribute name="rowAddr" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
<xs:element name="cellSpan">
<xs:complexType>
<xs:attribute name="colSpan" type="xs:positiveInteger" default="1"/>
<xs:attribute name="rowSpan" type="xs:positiveInteger" default="1"/>
</xs:complexType>
</xs:element>
<xs:element name="cellSz">
<xs:complexType>
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="height" type="xs:nonNegativeInteger"/>
350
KSX 6101:2024
code
Xml
</xs:complexType>
</xs:element>
<xs:element name="cellMargin">
<xs:complexType>
<xs:attributeGroup ref="hc:MarginAttributeGroup"/>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="name" type="xs:string"/>
<xs:attribute name="header" type="xs:boolean" default="false"/>
<xs:attribute name="hasMargin" type="xs:boolean" default="false"/>
<xs:attribute name="protect" type="xs:boolean" default="false"/>
<xs:attribute name="editable" type="xs:boolean" default="false"/>
<xs:attribute name="dirty" type="xs:boolean" default="false"/>
<xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:element name="tbl" minOccurs="0">
<xs:complexType>
<xs:attribute name="topMargin" type="xs:nonNegativeInteger"/>
<xs:attribute name="leftMargin" type="xs:nonNegativeInteger"/>
<xs:attribute name="textWidth" type="xs:nonNegativeInteger"/>
<xs:attribute name="textLength" type="xs:nonNegativeInteger"/>
<xs:attribute name="downMarginHorz" type="xs:nonNegativeInteger"/>
<xs:attribute name="downMarginVert" type="xs:nonNegativeInteger"/>
<xs:attribute name="labelCols" type="xs:nonNegativeInteger"/>
<xs:attribute name="labelRows" type="xs:nonNegativeInteger"/>
<xs:attribute name="landscape">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="WIDELY"/>
<xs:enumeration value="NARROWLY"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="pageWidth" type="xs:nonNegativeInteger"/>
<xs:attribute name="pageHeight" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="pageBreak">
358/414
KSX 6101:2024
code
Xml
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="TABLE"/>
<xs:enumeration value="CELL"/>
<xs:enumeration value="NONE"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="repeatHeader" type="xs:boolean" default="false"/>
<xs:attribute name="noAdjust" type="xs:boolean" default="false"/>
<xs:attribute name="rowCnt" type="xs:positiveInteger"/>
<xs:attribute name="colCnt" type="xs:positiveInteger"/>
<xs:attribute name="cellSpacing" type="xs:nonNegativeInteger" default="0"/>
<xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="EquationType">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeObjectType">
<xs:sequence>
<xs:element name="script"/>
</xs:sequence>
<xs:attribute name="version" type="xs:string" default="Equation Version 60">
    <xs:annotation>
        <xs:documentation>수식 편집기 버전. 현재는 "Equation Version 60"</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="baseLine" default="85">
    <xs:annotation>
        <xs:documentation>수식이 그려질 기준선.</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:unsignedInt">
            <xs:maxInclusive value="100"/>
        </xs:restriction>
    </xs:simpleType>
352
KSX 6101:2024
code
Xml
</xs:attribute>
<xs:attribute name="textColor" type="hc:RGBColorType" default="000000">
    <xs:annotation>
        <xs:documentation>수식 글자 색</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="baseUnit" type="xs:nonNegativeInteger" default="1000">
    <xs:annotation>
        <xs:documentation>수식의 글자 크기. 단위는 HWPUNIT.</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="lineMode" default="CHAR">
    <xs:annotation>
        <xs:documentation>수식이 차지하는 범위.</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="LINE"/>
            <xs:enumeration value="CHAR"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="fontName" type="xs:string">
    <xs:annotation>
        <xs:documentation>수식 글꼴</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="AbstractShapeComponentType" abstract="true">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeObjectType">
<xs:sequence>
<xs:element name="offset">
<xs:complexType>
<xs:attribute name="x" type="xs:nonNegativeInteger" default="0"/>
<xs:attribute name="y" type="xs:nonNegativeInteger" default="0"/>
</xs:complexType>
</xs:element>
<xs:element name="orgSz">
<xs:complexType>
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="height" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
<xs:element name="curSz">
<xs:complexType>
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="height" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
<xs:element name="flip">
<xs:complexType>
<xs:attribute name="horizontal" type="xs:boolean" default="false"/>
360/414
KSX 6101:2024
code
Xml
<xs:attribute name="vertical" type="xs:boolean" default="false"/>
</xs:complexType>
</xs:element>
<xs:element name="rotationInfo">
<xs:complexType>
<xs:attribute name="angle" type="xs:integer" default="0"/>
<xs:attribute name="centerX" type="xs:nonNegativeInteger"/>
<xs:attribute name="centerY" type="xs:nonNegativeInteger"/>
<xs:attribute name="rotateimage" type="xs:boolean"/>
</xs:complexType>
</xs:element>
<xs:element name="renderingInfo">
<xs:complexType>
<xs:sequence>
<xs:element name="transMatrix" type="hc:MatrixType"/>
<xs:sequence minOccurs="0" maxOccurs="unbounded">
<xs:element name="scaMatrix" type="hc:MatrixType"/>
<xs:element name="rotMatrix" type="hc:MatrixType"/>
</xs:sequence>
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="href" type="xs:string"/>
<xs:attribute name="groupLevel" type="xs:nonNegativeInteger" default="0"/>
<xs:attribute name="instId" type="xs:nonNegativeInteger"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="PictureType">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeComponentType">
<xs:sequence>
<xs:element name="lineShape" type="hp:LineShapeType" minOccurs="0"/>
<xs:element name="imgRect">
<xs:complexType>
<xs:sequence>
<xs:element name="pt0" type="hc:PointType"/>
<xs:element name="pt1" type="hc:PointType"/>
<xs:element name="pt2" type="hc:PointType"/>
<xs:element name="pt3" type="hc:PointType"/>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:element name="imgClip">
<xs:complexType>
<xs:attribute name="left" type="xs:integer"/>
<xs:attribute name="right" type="xs:integer"/>
354
KSX 6101:2024
code
Xml
<xs:attribute name="top" type="xs:integer"/>
<xs:attribute name="bottom" type="xs:integer"/>
</xs:complexType>
</xs:element>
<xs:element name="effects" type="hp:EffectsType"/>
<xs:element name="inMargin" type="hp:InsideMarginType"/>
<xs:element name="imgDim">
<xs:complexType>
<xs:attribute name="dimwidth" type="xs:unsignedInt"/>
<xs:attribute name="dimheight" type="xs:unsignedInt"/>
</xs:complexType>
</xs:element>
<xs:element name="img" type="hc:ImageType"/>
</xs:sequence>
<xs:attribute name="reverse" type="xs:boolean"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="OLEType">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeComponentType">
<xs:sequence>
<xs:element name="extent" type="hc:PointType"/>
<xs:element name="lineShape" type="hp:LineShapeType"/>
</xs:sequence>
<xs:attribute name="objectType">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="UNKNOWN"/>
<xs:enumeration value="EMBEDDED"/>
<xs:enumeration value="LINK"/>
<xs:enumeration value="STATIC"/>
<xs:enumeration value="EQUATION"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="binaryItemIDRef" type="xs:string"/>
<xs:attribute name="hasMoniker" type="xs:boolean" default="false"/>
<xs:attribute name="drawAspect">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="CONTENT"/>
<xs:enumeration value="THUMB_NAIL"/>
<xs:enumeration value="ICON"/>
<xs:enumeration value="DOC_PRINT"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
355
363/414
KSX 6101:2024
code
Xml
<xs:attribute name="eqb" type="xs:boolean" default="false"/>
</xs:complexType>
<xs:complexType name="AbstractDrawingObjectType" abstract="true">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeComponentType">
<xs:sequence>
<xs:element name="lineShape" type="hp:LineShapeType"/>
<xs:element name="fillBrush" type="hh:FillBrushType" minOccurs="0"/>
<xs:element name="drawText" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="subList" type="hp:ParaListType"/>
</xs:sequence>
<xs:attribute name="lastWidth" type="xs:nonNegativeInteger"/>
<xs:attribute name="name" type="xs:string"/>
<xs:attribute name="editable" type="xs:boolean" default="false"/>
</xs:complexType>
</xs:element>
<xs:element name="shadow" type="hp:ShadowType"/>
</xs:sequence>
<xs:attribute name="horzTextBoxAlign">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="LEFT"/>
<xs:enumeration value="CENTER"/>
<xs:enumeration value="RIGHT"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="vertTextBoxAlign" default="CENTER">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="TOP"/>
<xs:enumeration value="CENTER"/>
<xs:enumeration value="BOTTOM"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="textVerticalWidth" type="xs:nonNegativeInteger"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="RectangleType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="pt0" type="hc:PointType"/>
<xs:element name="pt1" type="hc:PointType"/>
<xs:element name="pt2" type="hc:PointType"/>
<xs:element name="pt3" type="hc:PointType"/>
</xs:sequence>
<xs:attribute name="ratio" type="xs:nonNegativeInteger" default="0"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="EllipseType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="center" type="hc:PointType"/>
<xs:element name="ax1" type="hc:PointType"/>
<xs:element name="ax2" type="hc:PointType"/>
</xs:sequence>
<xs:attribute name="type">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="ELLIPSE"/>
<xs:enumeration value="ARC"/>
<xs:enumeration value="PIE"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="centerX" type="xs:integer"/>
<xs:attribute name="centerY" type="xs:integer"/>
<xs:attribute name="ax1X" type="xs:integer"/>
<xs:attribute name="ax1Y" type="xs:integer"/>
<xs:attribute name="ax2X" type="xs:integer"/>
<xs:attribute name="ax2Y" type="xs:integer"/>
<xs:attribute name="startX" type="xs:integer"/>
<xs:attribute name="startY" type="xs:integer"/>
<xs:attribute name="endX" type="xs:integer"/>
<xs:attribute name="endY" type="xs:integer"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ArcType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="center" type="hc:PointType"/>
<xs:element name="ax1" type="hc:PointType"/>
<xs:element name="ax2" type="hc:PointType"/>
</xs:sequence>
<xs:attribute name="type">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="NORMAL"/>
<xs:enumeration value="QUARTER"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="half" type="xs:boolean" default="false"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="PolygonType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="pt" type="hc:PointType" maxOccurs="unbounded"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="CurveType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="pt" type="hc:PointType" maxOccurs="unbounded"/>
</xs:sequence>
<xs:attribute name="type">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="NORMAL"/>
<xs:enumeration value="THAN_PATH"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:extension>
</xs:complexContent>
</xs:complexType>
366/414
KSX 6101:2024
code
Xml
<xs:complexType name="ConnectLineType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="startPt" type="hp:ConnectPointType"/>
<xs:element name="endPt" type="hp:ConnectPointType"/>
<xs:element name="controlPoints" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="point" type="hp:ConnectControlPointType" maxOccurs="unbounded"/>
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="type">
    <xs:annotation>
        <xs:documentation>선 종류 - 직선, 꺾은선, 곡선과 화살표 유무의 조합</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="STRAIGHT_NOARROW"/>
            <xs:enumeration value="STRAIGHT_ONEWAY"/>
            <xs:enumeration value="STRAIGHT_BOTH"/>
            <xs:enumeration value="STROKE_NOARROW"/>
            <xs:enumeration value="STROKE_ONEWAY"/>
            <xs:enumeration value="STROKE_BOTH"/>
            <xs:enumeration value="ARC_NOARROW"/>
            <xs:enumeration value="ARC_ONEWAY"/>
            <xs:enumeration value="ARC_BOTH"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ConnectControlPointType">
<xs:complexContent>
<xs:extension base="hc:PointType">
359
KSX 6101:2024
code
Xml
<xs:attribute name="type" type="xs:nonNegativeInteger"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="AbstractFormObjectType" abstract="true">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="text" minOccurs="0">
<xs:complexType>
<xs:simpleContent>
<xs:extension base="xs:string">
<xs:attribute name="vertAlign" default="CENTER">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="TOP"/>
            <xs:enumeration value="CENTER"/>
            <xs:enumeration value="BOTTOM"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="horzAlign" default="LEFT">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="LEFT"/>
            <xs:enumeration value="CENTER"/>
            <xs:enumeration value="RIGHT"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="name" type="xs:string" use="required"/>
<xs:attribute name="foreColor" type="hc:RGBColorType" default="000000"/>
<xs:attribute name="backColor" type="hc:RGBColorType" default="FFFFFF"/>
<xs:attribute name="groupName" type="xs:string"/>
<xs:attribute name="tabOrder" type="xs:positiveInteger"/>
<xs:attribute name="enabled" type="xs:boolean" default="true"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ButtonType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:attribute name="type" default="PUSH">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="PUSH"/>
<xs:enumeration value="RADIO"/>
<xs:enumeration value="CHECK"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="defaultValue" type="xs:boolean" default="false"/>
<xs:attribute name="selected" type="xs:boolean" default="false"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="EditType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:attribute name="multiLine" type="xs:boolean" default="false"/>
<xs:attribute name="passwordChar" type="xs:string"/>
<xs:attribute name="maxLength" type="xs:integer"/>
<xs:attribute name="readOnly" type="xs:boolean"/>
<xs:attribute name="wordWrap" default="NONE">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="NONE"/>
<xs:enumeration value="CHAR"/>
<xs:enumeration value="WORD"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="scrollBars" default="NONE">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="NONE"/>
<xs:enumeration value="HORIZONTAL"/>
<xs:enumeration value="VERTICAL"/>
<xs:enumeration value="BOTH"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="tabKeyBehavior" type="xs:boolean" default="false"/>
<xs:attribute name="numOnly" type="xs:boolean" default="false"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ComboBoxType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:sequence>
<xs:element name="listItem" type="hp:ListItemType" minOccurs="0" maxOccurs="unbounded"/>
</xs:sequence>
<xs:attribute name="readOnly" type="xs:boolean" default="false"/>
<xs:attribute name="listBoxRows" type="xs:positiveInteger"/>
<xs:attribute name="selectedValue" type="xs:string"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ListBoxType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:sequence>
<xs:element name="listItem" type="hp:ListItemType" minOccurs="0" maxOccurs="unbounded"/>
</xs:sequence>
<xs:attribute name="itemHeight" type="xs:integer"/>
<xs:attribute name="topIdx" type="xs:nonNegativeInteger"/>
<xs:attribute name="selectedValue" type="xs:string"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ScrollBarType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:attribute name="delay" type="xs:nonNegativeInteger"/>
<xs:attribute name="largeChange" type="xs:nonNegativeInteger"/>
<xs:attribute name="smallChange" type="xs:nonNegativeInteger"/>
<xs:attribute name="min" type="xs:int"/>
<xs:attribute name="max" type="xs:int"/>
<xs:attribute name="page" type="xs:int"/>
<xs:attribute name="value" type="xs:int"/>
<xs:attribute name="type">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="HORIZONTAL"/>
<xs:enumeration value="VERTICAL"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:simpleType name="FieldType">
<xs:restriction base="xs:string">
<xs:enumeration value="CLICK_HERE"/>
<xs:enumeration value="HYPERLINK"/>
<xs:enumeration value="BOOKMARK"/>
<xs:enumeration value="FORMULA"/>
<xs:enumeration value="SUMMARY"/>
<xs:enumeration value="USER_INFO"/>
<xs:enumeration value="DATE"/>
<xs:enumeration value="DOC_DATE"/>
<xs:enumeration value="PATH"/>
<xs:enumeration value="CROSSREF"/>
<xs:enumeration value="MAILMERGE"/>
<xs:enumeration value="MEMO"/>
<xs:enumeration value="PROOFREADING_MARKS"/>
<xs:enumeration value="PRIVATE_INFO"/>
<xs:enumeration value="METATAG"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="HeaderFooterType">
363
KSX 6101:2024
code
Xml
<xs:sequence>
<xs:element name="subList" type="hp:ParaListType"/>
</xs:sequence>
<xs:attribute name="id" type="xs:nonNegativeInteger"/>
<xs:attribute name="applyPageType" default="BOTH">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="BOTH"/>
<xs:enumeration value="EVEN"/>
<xs:enumeration value="ODD"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:complexType>
<xs:complexType name="NoteType">
<xs:sequence>
<xs:element name="subList" type="hp:ParaListType"/>
</xs:sequence>
<xs:attribute name="instId" type="xs:nonNegativeInteger"/>
</xs:complexType>
<xs:complexType name="AutoNumNewNumType">
<xs:sequence>
<xs:element name="autoNumFormat" type="hp:AutoNumFormatType"/>
</xs:sequence>
<xs:attribute name="num" type="xs:integer" default="1"/>
<xs:attribute name="numType">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="PAGE"/>
<xs:enumeration value="FOOTNOTE"/>
<xs:enumeration value="ENDNOTE"/>
<xs:enumeration value="PICTURE"/>
<xs:enumeration value="TABLE"/>
<xs:enumeration value="EQUATION"/>
<xs:enumeration value="TOTAL_PAGE"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:complexType>
<xs:complexType name="ListItemType">
<xs:attribute name="displayText" type="xs:string"/>
<xs:attribute name="value" type="xs:string"/>
</xs:complexType>
<xs:complexType name="ParameterList">
<xs:choice minOccurs="0" maxOccurs="unbounded">
<xs:element name="booleanParam">
<xs:complexType>
<xs:simpleContent>
364
371 / 414
KSX 6101:2024
code
Xml
<xs:extension base="xs:boolean">
<xs:attribute name="name" type="xs:string"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
<xs:element name="integerParam">
<xs:complexType>
<xs:simpleContent>
<xs:extension base="xs:integer">
<xs:attribute name="name" type="xs:string"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
<xs:element name="floatParam">
<xs:complexType>
<xs:simpleContent>
<xs:extension base="xs:float">
<xs:attribute name="name" type="xs:string"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
<xs:element name="stringParam">
<xs:complexType>
<xs:simpleContent>
<xs:extension base="xs:string">
<xs:attribute name="name" type="xs:string"/>
<xs:attribute ref="xml:space"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
<xs:element name="listParam" type="hp:ParameterList"/>
</xs:choice>
<xs:attribute name="cnt" type="xs:positiveInteger" use="required"/>
<xs:attribute name="name" type="xs:string"/>
</xs:complexType>
<xs:complexType name="TrackChangeTag">
<xs:attribute name="paraend" type="xs:boolean"/>
<xs:attribute name="lId" type="xs:nonNegativeInteger"/>
<xs:attribute name="rId" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:schema>
366
KSX 6101:2024
부속서 F
(규정)
Core XML 스키마
code
Xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:hcf="http://www.owpml.org/owpml/2024/core"
    targetNamespace="http://www.owpml.org/owpml/2024/core" elementFormDefault="qualified">

<xs:simpleType name="NumberType1">
    <xs:restriction base="xs:string">
        <xs:enumeration value="DIGIT">
            <xs:annotation>
                <xs:documentation>1, 2, 3</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_DIGIT">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 1, 2, 3</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="ROMAN_CAPITAL">
            <xs:annotation>
                <xs:documentation>I, II, III</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="ROMAN_SMALL">
            <xs:annotation>
                <xs:documentation>i, ii, iii</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LATIN_CAPITAL">
            <xs:annotation>
                <xs:documentation>A, B, C</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LATIN_SMALL">
            <xs:annotation>
                <xs:documentation>a, b, c</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_LATIN_CAPITAL">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 A, B, C</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_LATIN_SMALL">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 a, b, c</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_SYLLABLE">
            <xs:annotation>
                <xs:documentation>가, 나, 다</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_HANGUL_SYLLABLE">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 가, 나, 다</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_JAMO">
            <xs:annotation>
                <xs:documentation>ㄱ, ㄴ, ㄷ</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_HANGUL_JAMO">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 ㄱ, ㄴ, ㄷ</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_PHONETIC">
            <xs:annotation>
                <xs:documentation>하나, 둘, 셋</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="IDEOGRAPH">
            <xs:annotation>
                <xs:documentation>一, 二, 三</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_IDEOGRAPH">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 一, 二, 三</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="NumberType2">
    <xs:restriction base="xs:string">
        <xs:enumeration value="DIGIT">
            <xs:annotation>
                <xs:documentation>1, 2, 3</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
367
KSX 6101:2024
code
Xml
<xs:enumeration value="CIRCLED_DIGIT">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 1, 2, 3</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="ROMAN_CAPITAL">
            <xs:annotation>
                <xs:documentation>I, II, III</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="ROMAN_SMALL">
            <xs:annotation>
                <xs:documentation>i, ii, iii</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LATIN_CAPITAL">
            <xs:annotation>
                <xs:documentation>A, B, C</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LATIN_SMALL">
            <xs:annotation>
                <xs:documentation>a, b, c</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_LATIN_CAPITAL">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 A, B, C</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_LATIN_SMALL">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 a, b, c</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_SYLLABLE">
            <xs:annotation>
                <xs:documentation>가, 나, 다</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_HANGUL_SYLLABLE">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 가, 나, 다</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_JAMO">
            <xs:annotation>
                <xs:documentation>ㄱ, ㄴ, ㄷ</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
368
KSX 6101:2024```xml
</xs:enumeration>
<xs:enumeration value="CIRCLED_HANGUL_JAMO">
xs:annotation
xs:documentation동그라미 쳐진 ㄱ, ㄴ, ㄷ</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="HANGUL_PHONETIC">
xs:annotation
xs:documentation하나, 둘, 셋</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="CIRCLED_IDEOGRAPH">
xs:annotation
xs:documentation동그라미 쳐진 一, 二, 三</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="DECAGON_CIRCLE">
xs:annotation
xs:documentation갑, 을, 병, 정</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="DECAGON_CIRCLE_HANJA">
xs:annotation
xs:documentation甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬, 癸</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="SYMBOL">
xs:annotation
xs:documentation여러 가지 기호가 차례로 반복</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="USER_CHAR">
xs:annotation
xs:documentation사용자 지정 문자 반복</xs:documentation>
</xs:annotation>
</xs:enumeration>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="LineType1">
<xs:restriction base="xs:string">
<xs:enumeration value="NONE">
xs:annotation
code
Code
---
**369**
KSX 6101:2024
```xml
                <xs:documentation>없음</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SOLID">
            <xs:annotation>
                <xs:documentation>실선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOT">
            <xs:annotation>
                <xs:documentation>점선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="THICK">
            <xs:annotation>
                <xs:documentation>굵은 선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH">
            <xs:annotation>
                <xs:documentation>파선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT">
            <xs:annotation>
                <xs:documentation>-.-.-.</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT_DOT">
            <xs:annotation>
                <xs:documentation>-..-..-..</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="LineType2">
    <xs:restriction base="xs:string">
        <xs:enumeration value="NONE">
            <xs:annotation>
                <xs:documentation>없음</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SOLID">
            <xs:annotation>
                <xs:documentation>실선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOT">
370
KSX 6101:2024
code
Xml
<xs:annotation>
                <xs:documentation>점선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH">
            <xs:annotation>
                <xs:documentation>파선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT">
            <xs:annotation>
                <xs:documentation>-.-.-.</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT_DOT">
            <xs:annotation>
                <xs:documentation>-..-..-..</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LONG_DASH">
            <xs:annotation>
                <xs:documentation>DASH보다 긴 선의 반복</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLE">
            <xs:annotation>
                <xs:documentation>DOT보다 큰 동그라미의 반복</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOUBLE_SLIM">
            <xs:annotation>
                <xs:documentation>2중선 (가는 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SLIM_THICK">
            <xs:annotation>
                <xs:documentation>2중선 (가는 선 + 굵은 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="THICK_SLIM">
            <xs:annotation>
                <xs:documentation>2중선 (굵은 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SLIM_THICK_SLIM">
            <xs:annotation>
                <xs:documentation>3중선 (가는 선 + 굵은 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
371
KSX 6101:2024
code
Xml
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="LineType3">
    <xs:restriction base="xs:string">
        <xs:enumeration value="NONE">
            <xs:annotation>
                <xs:documentation>없음</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SOLID">
            <xs:annotation>
                <xs:documentation>실선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOT">
            <xs:annotation>
                <xs:documentation>점선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH">
            <xs:annotation>
                <xs:documentation>파선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT">
            <xs:annotation>
                <xs:documentation>-.-.-.</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT_DOT">
            <xs:annotation>
                <xs:documentation>-..-..-..</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LONG_DASH">
            <xs:annotation>
                <xs:documentation>DASH보다 긴 선의 반복</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLE">
            <xs:annotation>
                <xs:documentation>DOT보다 큰 동그라미의 반복</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOUBLE_SLIM">
            <xs:annotation>
                <xs:documentation>2중선 (가는 선 + 가는 선)</xs:documentation>
            </xs:annotation>
372
KSX 6101:2024
code
Xml
</xs:enumeration>
        <xs:enumeration value="SLIM_THICK">
            <xs:annotation>
                <xs:documentation>2중선 (가는 선 + 굵은 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="THICK_SLIM">
            <xs:annotation>
                <xs:documentation>2중선 (굵은 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SLIM_THICK_SLIM">
            <xs:annotation>
                <xs:documentation>3중선 (가는 선 + 굵은 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="WAVE"/>
        <xs:enumeration value="DOUBLEWAVE"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="LineWidth">
    <xs:restriction base="xs:string">
        <xs:whiteSpace value="collapse"/>
        <xs:enumeration value="0.1 mm"/>
        <xs:enumeration value="0.12 mm"/>
        <xs:enumeration value="0.15 mm"/>
        <xs:enumeration value="0.2 mm"/>
        <xs:enumeration value="0.25 mm"/>
        <xs:enumeration value="0.3 mm"/>
        <xs:enumeration value="0.4 mm"/>
        <xs:enumeration value="0.5 mm"/>
        <xs:enumeration value="0.6 mm"/>
        <xs:enumeration value="0.7 mm"/>
        <xs:enumeration value="1.0 mm"/>
        <xs:enumeration value="1.5 mm"/>
        <xs:enumeration value="2.0 mm"/>
        <xs:enumeration value="3.0 mm"/>
        <xs:enumeration value="4.0 mm"/>
        <xs:enumeration value="5.0 mm"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="RGBColorType">
    <xs:restriction base="xs:string">
        <xs:pattern value="[0-9a-fA-F]{6}"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="ArrowType">
    <xs:restriction base="xs:string">
        <xs:enumeration value="NORMAL"/>
        <xs:enumeration value="SPEAR"/>
        <xs:enumeration value="CONCAVE_ARROW"/>
        <xs:enumeration value="DIAMOND_ARROW"/>
        <xs:enumeration value="EMPTY_DIAMOND_ARROW"/>
        <xs:enumeration value="CIRCLE_ARROW"/>
        <xs:enumeration value="EMPTY_CIRCLE_ARROW"/>
        <xs:enumeration value="BOX_ARROW"/>
        <xs:enumeration value="EMPTY_BOX_ARROW"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="ArrowSize">
    <xs:restriction base="xs:string">
        <xs:enumeration value="SMALL_SMALL"/>
        <xs:enumeration value="SMALL_MEDIUM"/>
        <xs:enumeration value="SMALL_LARGE"/>
        <xs:enumeration value="MEDIUM_SMALL"/>
        <xs:enumeration value="MEDIUM_MEDIUM"/>
        <xs:enumeration value="MEDIUM_LARGE"/>
        <xs:enumeration value="LARGE_SMALL"/>
        <xs:enumeration value="LARGE_MEDIUM"/>
        <xs:enumeration value="LARGE_LARGE"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="ShadowType2">
    <xs:restriction base="xs:string">
        <xs:enumeration value="NONE"/>
        <xs:enumeration value="OFFSET"/>
        <xs:enumeration value="OFFSET_LEFT"/>
        <xs:enumeration value="OFFSET_RIGHT"/>
        <xs:enumeration value="OFFSET_TOP"/>
        <xs:enumeration value="OFFSET_BOTTOM"/>
    </xs:restriction>
</xs:simpleType>
374
KSX 6101:2024
code
Xml
<xs:simpleType name="UnderlineType">
    <xs:restriction base="xs:string">
        <xs:enumeration value="None"/>
        <xs:enumeration value="DoubleLine"/>
        <xs:enumeration value="TripleLine"/>
        <xs:enumeration value="Margin"/>
    </xs:restriction>
</xs:simpleType>
<xs:attributeGroup name="MarginAttributeGroup">
    <xs:annotation>
        <xs:documentation>여백 속성</xs:documentation>
    </xs:annotation>
    <xs:attribute name="left" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>왼쪽 여백. 단위는 HWPUNIT.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="right" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>오른쪽 여백. 단위는 HWPUNIT.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="top" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>위 여백. 단위는 HWPUNIT.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="bottom" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>아래 여백. 단위는 HWPUNIT.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:attributeGroup>
<xs:attributeGroup name="BorderAttributeGroup">
    <xs:annotation>
        <xs:documentation>테두리에서 공통적으로 사용되는 속성</xs:documentation>
    </xs:annotation>
    <xs:attribute name="type" default="Solid">
        <xs:annotation>
            <xs:documentation>테두리 선 종류</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="Solid">
                    <xs:annotation>
                        <xs:documentation>실선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
375
KSX 6101:2024
code
Xml
<xs:enumeration value="Dash">
                    <xs:annotation>
                        <xs:documentation>파선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="Dot">
                    <xs:annotation>
                        <xs:documentation>점선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="DashDot">
                    <xs:annotation>
                        <xs:documentation>-.-.-.</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="DashDotDot">
                    <xs:annotation>
                        <xs:documentation>-..-..-..</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="LongDash">
                    <xs:annotation>
                        <xs:documentation>Dash보다 긴 선의 반복</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="Circle">
                    <xs:annotation>
                        <xs:documentation>Dot보다 큰 동그라미의 반복</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="DoubleSlim">
                    <xs:annotation>
                        <xs:documentation>2중선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="SlimThick">
                    <xs:annotation>
                        <xs:documentation>가는 선 + 굵은 선 2중선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="ThickSlim">
                    <xs:annotation>
                        <xs:documentation>굵은 선 + 가는 선 2중선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="SlimThickSlim">
                    <xs:annotation>
                        <xs:documentation>가는 선 + 굵은 선 + 가는 선 3중선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
```---
**376**
KSX 6101:2024
```xml
                <xs:enumeration value="None">
                    <xs:annotation>
                        <xs:documentation>선 없음</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="width" default="0.12mm">
        <xs:annotation>
            <xs:documentation>테두리 선 굵기</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="0.1mm"/>
                <xs:enumeration value="0.12mm"/>
                <xs:enumeration value="0.15mm"/>
                <xs:enumeration value="0.2mm"/>
                <xs:enumeration value="0.25mm"/>
                <xs:enumeration value="0.3mm"/>
                <xs:enumeration value="0.4mm"/>
                <xs:enumeration value="0.5mm"/>
                <xs:enumeration value="0.6mm"/>
                <xs:enumeration value="0.7mm"/>
                <xs:enumeration value="1.0mm"/>
                <xs:enumeration value="1.5mm"/>
                <xs:enumeration value="2.0mm"/>
                <xs:enumeration value="3.0mm"/>
                <xs:enumeration value="4.0mm"/>
                <xs:enumeration value="5.0mm"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="color" type="hcf:RGBColorType" default="000000">
        <xs:annotation>
            <xs:documentation>테두리 선 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:attributeGroup>
<xs:complexType name="ImageType">
    <xs:attribute name="binaryItemIDRef" type="xs:string"/>
    <xs:attribute name="bright" default="0">
        <xs:annotation>
            <xs:documentation>밝기</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="-100"/>
                <xs:maxInclusive value="100"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="contrast" default="0">
        <xs:annotation>
            <xs:documentation>대비</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="-100"/>
                <xs:maxInclusive value="100"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="effect" default="REAL_PIC">
        <xs:annotation>
            <xs:documentation>이미지 효과</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="REAL_PIC"/>
                <xs:enumeration value="GRAY_SCALE"/>
                <xs:enumeration value="BLACK_WHITE"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>
378
KSX 6101:2024
code
Xml
<xs:attribute name="alpha" type="xs:float"/>
</xs:complexType>
<xs:complexType name="MatrixType">
    <xs:annotation>
        <xs:documentation>행렬 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="e1" type="xs:float"/>
    <xs:attribute name="e2" type="xs:float"/>
    <xs:attribute name="e3" type="xs:float"/>
    <xs:attribute name="e4" type="xs:float"/>
    <xs:attribute name="e5" type="xs:float"/>
    <xs:attribute name="e6" type="xs:float"/>
</xs:complexType>
<xs:complexType name="PointType">
    <xs:annotation>
        <xs:documentation>Point 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="x" type="xs:integer"/>
    <xs:attribute name="y" type="xs:integer"/>
</xs:complexType>
<xs:complexType name="FillBrushType">
    <xs:annotation>
        <xs:documentation>채우기 정보</xs:documentation>
    </xs:annotation>
    <xs:choice>
        <xs:element name="winBrush" minOccurs="1">
            <xs:annotation>
                <xs:documentation>윈도우 채우기</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="faceColor" type="hcf:RGBColorType" default="FFFFFF">
                    <xs:annotation>
                        <xs:documentation>면 색</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="hatchColor" type="hcf:RGBColorType" default="000000">
                    <xs:annotation>
                        <xs:documentation>무늬 색</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="hatchStyle">
                    <xs:annotation>
                        <xs:documentation>무늬 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
379
KSX 6101:2024
code
Xml
<xs:restriction base="xs:string">
                            <xs:enumeration value="HORIZONTAL">
                                <xs:annotation>
                                    <xs:documentation>-----</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="VERTICAL">
                                <xs:annotation>
                                    <xs:documentation>|||||</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BACK_SLASH">
                                <xs:annotation>
                                    <xs:documentation>\\\\\</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="SLASH">
                                <xs:annotation>
                                    <xs:documentation>/////</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CROSS">
                                <xs:annotation>
                                    <xs:documentation>+++++</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CROSS_DIAGONAL">
                                <xs:annotation>
                                    <xs:documentation>xxxxx</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="alpha" type="xs:float"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="gradation" minOccurs="1">
            <xs:annotation>
                <xs:documentation>그라데이션 효과</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="color" minOccurs="0" maxOccurs="unbounded">
                        <xs:annotation>
                            <xs:documentation>그라데이션 색</xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
```---
**380**
**387/414**
KSX 6101:2024
```xml
                            <xs:attribute name="value" type="hcf:RGBColorType" use="required"/>
                        </xs:complexType>
                    </xs:element>
                </xs:sequence>
                <xs:attribute name="type">
                    <xs:annotation>
                        <xs:documentation>그라데이션 유형</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="LINEAR">
                                <xs:annotation>
                                    <xs:documentation>선형</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RADIAL">
                                <xs:annotation>
                                    <xs:documentation>원형</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CONICAL"/>
                            <xs:enumeration value="SQUARE">
                                <xs:annotation>
                                    <xs:documentation>사각형</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="angle" type="xs:integer" default="90">
                    <xs:annotation>
                        <xs:documentation>그라데이션의 기울임 (시작각)</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="centerX" type="xs:integer" default="0">
                    <xs:annotation>
                        <xs:documentation>그라데이션의 가로 중심 (중심 X좌표)</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="centerY" type="xs:integer" default="0">
                    <xs:annotation>
                        <xs:documentation>그라데이션의 세로 중심 (중심 Y좌표)</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
381
KSX 6101:2024
code
Xml
<xs:attribute name="step" default="255">
                    <xs:annotation>
                        <xs:documentation>그라데이션 번짐 정도 (0~255)</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="0"/>
                            <xs:maxInclusive value="255"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="colorNum" type="xs:nonNegativeInteger" default="2">
                    <xs:annotation>
                        <xs:documentation>그라데이션의 색 개수</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="stepCenter" default="50">
                    <xs:annotation>
                        <xs:documentation>그라데이션 번짐 정도의 중심 (0~100)</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="0"/>
                            <xs:maxInclusive value="100"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="alpha" type="xs:float"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="imgBrush" minOccurs="1">
            <xs:annotation>
                <xs:documentation>그림으로 채우기</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="img" type="hcf:ImageType"/>
                </xs:sequence>
                <xs:attribute name="mode" default="TILE">
                    <xs:annotation>
                        <xs:documentation>채우기 유형</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="TILE">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-모두</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TILE_HORZ_TOP">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-가로/위</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TILE_HORZ_BOTTOM">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-가로/아래</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TILE_VERT_LEFT">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-세로/왼쪽</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TILE_VERT_RIGHT">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-세로/오른쪽</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation>
                                    <xs:documentation>가운데</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER_TOP">
                                <xs:annotation>
                                    <xs:documentation>가운데 위</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER_BOTTOM">
                                <xs:annotation>
                                    <xs:documentation>가운데 아래</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="LEFT_CENTER">
                                <xs:annotation>
                                    <xs:documentation>왼쪽 가운데</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
383
390/414
KSX 6101:2024
code
Xml
<xs:enumeration value="LEFT_TOP">
                                <xs:annotation>
                                    <xs:documentation>왼쪽 위</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="LEFT_BOTTOM">
                                <xs:annotation>
                                    <xs:documentation>왼쪽 아래</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT_CENTER">
                                <xs:annotation>
                                    <xs:documentation>오른쪽 가운데</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT_TOP">
                                <xs:annotation>
                                    <xs:documentation>오른쪽 위</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT_BOTTOM">
                                <xs:annotation>
                                    <xs:documentation>오른쪽 아래</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="ZOOM">
                                <xs:annotation>
                                    <xs:documentation>크기에 맞추어</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
    </xs:choice>
</xs:complexType>
<xs:complexType name="KeyEncryptionType">
    <xs:sequence>
        <xs:element name="derivationKey">
            <xs:complexType>
                <xs:attribute name="algorithm" type="xs:string"/>
                <xs:attribute name="size" type="xs:nonNegativeInteger"/>
                <xs:attribute name="count" type="xs:nonNegativeInteger"/>
                <xs:attribute name="salt" type="xs:base64Binary"/>
            </xs:complexType>
        </xs:element>
384
KSX 6101:2024
code
Xml
<xs:element name="hash" type="xs:base64Binary"/>
    </xs:sequence>
</xs:complexType>
<xs:complexType name="MetaTagType" mixed="true"/>
</xs:schema>

385
KSX 6101:2024
부속서 G
(규정)
MasterPage XML 스키마
code
Xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:hcf="http://www.owpml.org/owpml/2024/core" xmlns:hp="http://www.owpml.org/owpml/2024/hp" xmlns:hpf="http://www.owpml.org/owpml/2024/hpf" targetNamespace="http://www.owpml.org/owpml/2024/hpf" elementFormDefault="qualified">
    <xs:import namespace="http://www.owpml.org/owpml/2024/hp" schemaLocation="HwpFile.xsd"/>
    <xs:import namespace="http://www.owpml.org/owpml/2024/core" schemaLocation="Core.xsd"/>
    <xs:element name="masterPage">
        <xs:annotation>
            <xs:documentation>마스터 페이지</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="subList" type="hp:ParaListType"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:int" use="required"/>
            <xs:attribute name="type" default="BOTH">
                <xs:annotation>
                    <xs:documentation>마스터 페이지 종류</xs:documentation>
                </xs:annotation>
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="BOTH"/>
                        <xs:enumeration value="EVEN"/>
                        <xs:enumeration value="ODD"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="pageNumber">
                <xs:annotation>
                    <xs:documentation>페이지 번호</xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="width" type="xs:nonNegativeInteger" use="required"/>
            <xs:attribute name="height" type="xs:nonNegativeInteger" use="required"/>
            <xs:attribute name="header" type="hpf:HeaderFooterType"/>
            <xs:attribute name="footer" type="hpf:HeaderFooterType"/>
            <xs:attribute name="footNote" type="hpf:NoteType"/>
            <xs:attribute name="endNote" type="hpf:NoteType"/>
            <xs:attribute name="pageBorderFill" type="hpf:PageBorderFillType"/>
            <xs:attribute name="pageNumberPosition" type="hpf:PageNumPosType"/>
            <xs:attribute name="pageDblSided" default="false" type="xs:boolean"/>
            <xs:attribute name="pageFrontFirst" default="false" type="xs:boolean"/>
            <xs:attribute name="pageBindingType" default="DEFAULT" type="hpf:PageBindingType"/>
            <xs:attribute name="orientation" default="PORTRAIT">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="PORTRAIT"/>
                        <xs:enumeration value="LANDSCAPE"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:complexType name="HeaderFooterType">
        <xs:attribute name="id" type="xs:nonNegativeInteger"/>
        <xs:attribute name="type" default="BOTH">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="BOTH"/>
                    <xs:enumeration value="EVEN"/>
                    <xs:enumeration value="ODD"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="NoteType">
        <xs:attribute name="id" type="xs:nonNegativeInteger"/>
    </xs:complexType>
    <xs:complexType name="PageBorderFillType">
        <xs:complexContent>
            <xs:extension base="hp:BorderFillType">
                <xs:attribute name="textBorder" type="xs:boolean" default="false"/>
                <xs:attribute name="headerInside" type="xs:boolean" default="false"/>
                <xs:attribute name="footerInside" type="xs:boolean" default="false"/>
                <xs:attribute name="fillArea" default="PAPER">
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="PAPER"/>
                            <xs:enumeration value="PAGE"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="PageNumPosType">
        <xs:attribute name="id" type="xs:nonNegativeInteger"/>
        <xs:attribute name="pageNum" type="xs:nonNegativeInteger"/>
        <xs:attribute name="type" default="NONE">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="LEFT_TOP"/>
                    <xs:enumeration value="CENTER_TOP"/>
                    <xs:enumeration value="RIGHT_TOP"/>
                    <xs:enumeration value="LEFT_BOTTOM"/>
                    <xs:enumeration value="CENTER_BOTTOM"/>
                    <xs:enumeration value="RIGHT_BOTTOM"/>
                    <xs:enumeration value="OUTSIDE_TOP"/>
                    <xs:enumeration value="OUTSIDE_BOTTOM"/>
                    <xs:enumeration value="INSIDE_TOP"/>
                    <xs:enumeration value="INSIDE_BOTTOM"/>
                    <xs:enumeration value="NONE"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
    <xs:simpleType name="PageBindingType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="DEFAULT"/>
            <xs:enumeration value="OPPOSITE"/>
            <xs:enumeration value="TO_RIGHT"/>
            <xs:enumeration value="TO_LEFT"/>
        </xs:restriction>
    </xs:simpleType>
</xs:schema>
388
KSX 6101:2024
부속서 H
(규정)
수식 스크립트
1.1 수식 버전
이 문서를 기준으로 수식 스크립트의 최신 버전은 6.0이다.
OWPML 본문 내에서는 수식 버전을 다음과 같이 표기한다.
Equation Version 60
1.2 항의 구분 및 인식
수식에서 항(토큰)의 구분은 공백(Space, Tab)이나 줄바꿈으로 한다. 만약 공백을 포함한 여러 항을 하나의 항으로 인식하기 위해서는 {}를 사용해야 한다.
입력	결과
a over 2x^2 + y	a / (2x^2) + y
a over {2x^2 + y}	a / (2x^2 + y)
수식에서 한 항이 9자를 넘어가면 수식 스크립트 엔진은 이를 2개의 항으로 분리하여 인식한다. 9자 이상의 항을 하나의 항으로 처리하기 위해서는 따옴표(")를 두 항의 앞뒤에 사용해야 한다.
입력	결과
1234567890 over 5	123456789 * (0/5)
"1234567890" over 5	1234567890 / 5
1.3 수식에 쓰이는 글씨체
기본적으로 수식 편집기에서 입력하는 로마자는 이탤릭체로 바뀌어 표현된다. 하지만 로만(영문·수식)체를 쓸 때에는 로만체 전환 명령어인 rm을 앞세워야 한다. 또 볼드체를 입력하기 위해서는 명령어 bold를 앞세운다.
기본: 이탤릭체
rm: 로만체
it: 로만체 입력 중 이탤릭체로 변경
bold: 볼드체
389
KSX 6101:2024
1.3.1 예제
1.3.1.1 기본
| 입력 | Equation font test |
|---|---|
| 결과 | Equation font test |
1.3.1.2 로만체 - 이탤릭체
| 입력 | Equation rm font it test |
|---|---|
| 결과 | Equation font test |
1.3.1.3 볼드체
| 입력 | rm Equation - bold Editor |
|---|---|
| 결과 | Equation - Editor |
1.4 White Space 표현
1.4.1 공백 및 줄바꿈
수식 스크립트 엔진은, 공백(Space), 줄바꿈 등을 항을 구분하는 역할로만 쓰이며 화면 표시에는 사용되지 않고 무시된다. 수식 결과에 공백을 표시하기 위해서는 ~나 "를 사용해야 한다. 따옴표(")는 여러 개의 공백이 들어간 항을 표현할 때에도 사용될 수 있다. 줄바꿈은 #을 사용해서 표현할 수 있다.
입력	수식~편집기" "예제
결과	수식 편집기 예제
입력	"2차 방정식의 해법에는 인수분해에 의한 해법과 근의 공식에 의한 해법이 있다."
결과	2차 방정식의 해법에는 인수분해에 의한 해법과 근의 공식에 의한 해법이 있다.
1.4.2 세로 칸 맞춤(&)
세로 칸 맞춤은 맞추고자 하는 기준 글자 앞에 &를 입력해 주어야 한다. 즉 글자 앞에서 <Tab>을 누른 것과 같은 효과를 준다.
입력	420 = 2 times 210 # = 2 times 2 times 105 # = 2^2 times 3 times 35 # = 2^2 times 3 times 5 times 7
결과	420 = 2 × 210<br>= 2 × 2 × 105<br>= 2² × 3 × 35<br>= 2² × 3 × 5 × 7
390
KSX 6101:2024
입력	420 &= 2 times 210 # &= 2 times 2 times 105 # &= 2^2 times 3 times 35 # &= 2^2 times 3 times 5 times 7
결과	420 = 2 × 210<br>      = 2 × 2 × 105<br>      = 2² × 3 × 35<br>      = 2² × 3 × 5 × 7
1.5 예약어 및 명령어
예약어 및 명령어는 몇몇 예약어를 제외하고 기본적으로 대소문자를 구분하지 않는다. 대소문자를 구분하는 예약어인 경우 설명에 이를 명시한다.
1.5.1 따옴표(")
글자 길이가 긴 단어나 공백을 포함한 문장을 하나로 묶기 위해 사용되는 예약어
1.5.2 분수 (OVER)
분수는 기본적으로 가운데 맞춤으로 정렬한다. 오른쪽이나 왼쪽 맞춤을 쓰려면 빈칸 넣기인 <_>나 <.>를 이용한다.
입력	1 OVER 1000 + {1<_> OVER 1000} + {1<.> OVER 1000}
결과	1/1000 + 1/1000 + 1/1000
391
KSX 6101:2024
1.5.6 위 아래 (ATOP)
OVER 명령어와 같지만 분수를 나타내는 가로선을 생략해 준다.
1.5.9 제곱근 (SQRT)
SQRT 대신하여 ROOT라고 입력해도 같은 결과를 얻을 수 있다.
입력	x SQRT {y+z}
결과	x√(y+z)
392
KSX 6101:2024
1.5.10 LEFT, RIGHT
LEFT와 RIGHT는 양쪽에서 하나의 쌍을 이루도록 한다. 만약 한쪽을 생략하고 싶을 경우 생략하려는 쪽에 마침표(.)를 넣는다.
입력	LEFT ( a+b over x+y RIGHT )
결과	( (a+b)/(x+y) )
입력	LEFT . a+b over x+y RIGHT }
결과	(a+b)/(x+y) }
1.5.11 BIGG 기호
입력	LEFT { a+b OVER a-b BIGG / x+y OVER x-y RIGHT }
결과	{ (a+b)/(a-b) / (x+y)/(x-y) }
1.5.12 적분 (INT, OINT)
입력	INT _-inf ^inf {1 over x} dx
결과	∫[-inf, inf] (1/x) dx
입력	OINT _C {1 over x} dx
결과	∮[C] (1/x) dx
입력	OINT _C_l {1 over x} dx
결과	∮[C_l] (1/x) dx
1.5.13 극한 (lim, Lim)
본 예약어는 대소문자를 구분하므로, 반드시 대소문자를 정확하게 표기해야 한다.
입력	lim _{x->0} {1 over x}
결과	lim[x→0] (1/x)
입력	Lim _{x->0} {1 over x}
결과	Lim[x→0] (1/x)
1.5.14 합 (SUM)
입력	x = SUM _{i=0} ^{inf} {x sub i}
결과	x = Σ[i=0, inf] x_i
1.5.15 합집합 (UNION), 교집합 (INTER), 곱집합 (PROD)
입력	A UNION B
결과	A ∪ B
입력	A INTER B
결과	A ∩ B
393
401/414
KSX 6101:2024
입력	A PROD B
결과	A × B
1.5.16 상호관계 (REL)
두 항 간의 상호관계를 상세히 표현할 수 있게 하는 기능으로 두 항을 연결하는 화살표의 위/아래에 관계식 등의 내용을 삽입할 수 있다.
입력	A REL Lrarrow ^{abc} _{xyz} B
결과	A ←[xyz, abc] B
입력	rm PbO_2 + 2H_2 SO_4 + Pb REL lrarrow ^{충전} _{방전} 2PbSO_4 + 2H_2 O
결과	PbO₂ + 2H₂SO₄ + Pb ↔[방전, 충전] 2PbSO₄ + 2H₂O
1.5.17 BUILDREL
Relation 이동과 유사한 기능으로 화살표 아래 부분의 내용을 생략할 수 있다.
입력	A BUILDREL Lrarrow ^{f(a) + g(a) + h(a)} B
결과	A ←[f(a)+g(a)+h(a)] B
입력	rm RCH_2 CH_2 COSCoA BUILDREL rarrow-2H- RCH=CHCOSCqA
결과	RCH₂CH₂COSCoA →[-2H-] RCH=CHCHSCoA
1.5.18 세로 쌓기 (PILE, LPILE, RPILE)
위에 있는 글자를 기준으로 가운데(PILE), 왼쪽(LPILE), 오른쪽(RPILE) 맞춤을 선택할 수 있다.
입력	PILE {tA3 # tA2 # t}
결과	tA3<br>tA2<br>t
1.5.19 경우 (CASES)
여러 개의 행 전체를 나타내는 큰 중괄호 {는 상황에 따라 그 크기가 자동으로 확대되어 표시된다.
| 입력 | |sign(x)| = CASES {1 &x>0 # 0 &x=0 # -1 &x<0} |
|---|---|
| 결과 | |sign(x)| = { 1 (x>0)<br>                 { 0 (x=0)<br>                 { -1 (x<0) |
1.5.20 조합 (CHOOSE, BINOM)
입력	n CHOOSE x
결과	(n C x)
입력	BINOM n x
결과	(n, x)
1.5.21 행렬 (MATRIX, PMATRIX, BMATRIX, DMATRIX)
matrix는 행(row) 단위로 입력하는 방법과, 칸(column) 단위로 입력하는 방법이 있다.
col을 넣어 내용을 칸 단위로 입력할 때는 각 칸 앞에 col(가운데 맞춤) 대신 lcol(왼쪽 맞춤), rcol(오른쪽 맞춤)을 써서 위치를 정할 수도 있다.
matrix 대신에 pmatrix를 쓰면 소괄호 ( ), bmatrix를 쓰면 대괄호 [ ], dmatrix를 쓰면 세로줄 | |을 행렬 양옆에 각각 표시해 준다.
입력	matrix { a_1 & b_1 & c_1 & d_1 # a_2 & b_2 & c_2 & d_2 # a_3 & b_3 & c_3 & d_3 # a_4 & b_4 & c_4 & d_4 }
결과	a₁ b₁ c₁ d₁<br>a₂ b₂ c₂ d₂<br>a₃ b₃ c₃ d₃<br>a₄ b₄ c₄ d₄
395
KSX 6101:2024
입력	matrix { lcol {a_1 # abc_2 # a_3 # a_4} col {b_1 # b_2 # b_3 # b_4} col {c_1 # c_2 # c_3 # c_4} col {d_1 # d_2 # d_3 # d_4} }
결과	a₁      b₁ c₁ d₁<br>abc₂  b₂ c₂ d₂<br>a₃      b₃ c₃ d₃<br>a₄      b₄ c₄ d₄
MATRIX	PMATRIX	BMATRIX	DMATRIX
a₁ b₁ c₁<br>a₂ b₂ c₂	(a₁ b₁ c₁)<br>(a₂ b₂ c₂)	[a₁ b₁ c₁]<br>[a₂ b₂ c₂]	|a₁ b₁ c₁|<br>|a₂ b₂ c₂|
1.5.22 밑줄(UNDERLINE), 윗줄(OVERLINE)
입력	UNDERLINE {x+y} + OVERLINE {y+z}
결과	<u>x+y</u> + overline(y+z)
1.5.23 왼쪽 아래첨자 (LSUB)
입력	x LSUB y
결과	<sub>y</sub>x
1.5.24 왼쪽 위첨자 (LSUP)
입력	x LSUP y ~~(y>x)
결과	<sup>y</sup>x (y>x)
1.5.25 최소공배수/최대공약수 함수 (LADDER)
최소공배수, 최대공약수를 구할 때 사용하는 명령어로 마지막 행의 마지막 열은 인자로 인식하지 않는다.
입력	LADDER {2&12&28#2&6&14#3&7&}
결과	2
396
403/414
KSX 6101:2024
1.5.26 2진수 변환 함수 (SLADDER)
10진수를 2진수로 변환할 때 사용하는 명령어로 첫 번째 행의 마지막 열과 마지막 행의 마지막 열은 인자로 인식하지 않는다.
입력	SLADDER{ 2&12& # 2&6&0 # 2&3&0 # 1&1 }
결과	2
1.5.27 거꾸로 나눗셈 (LONGDIV)
나눗셈을 표현할 때 사용하는 명령어이다.
Layout을 맞추지 않은 방법으로도 나눗셈을 입력할 수 있으며 자동으로 Layout을 맞추려면 ~을 이용하여 자동으로 Layout을 맞출 수 있다. 마지막 인자에 숫자가 아닌 문자가 들어가면 자동 Layout을 하지 않는다.
입력	LONGDIV {6} {422} {2532#24#13#12#12#12#0}
결과	(복잡한 나눗셈 형식)
입력	LONGDIV {6} {422} {2532#24#~13#~12#~12#~12#~0}
결과	(자동 정렬된 복잡한 나눗셈 형식)
1.5.28 색상 (COLOR)
부분적으로 Color를 바꾸기 위해 사용하는 명령어이다.
첫 번째 인자에 (R, G, B) 색상값이 들어간다.
입력	{COLOR {255,0,255}} {3} over {4}
결과	<span style="color:magenta">3</span>/4
1.5.29 글자장식
글자 또는 단어에 간단한 명령어를 앞세워 여러 가지 글자 장식을 할 수 있다. 해당 명령어를 먼저 입력한 후 글자는 나중에 입력한다.
다음의 HAT, CHECK, ARCH, TILDE 명령어는 영문 3자까지만 감쌀 수 있다.
397
KSX 6101:2024
입력	결과	입력	결과
acute A	Á	bar A	Ā
grave A	À	vec A	A⃗
dot A	Ȧ	dyad A	̿A
ddot A	Ä	under A	<u>A</u>
hat A	Â	arch A	⌒A
hat AA	AÂ	arch AA	⌒AA
hat AAA	AÂA	arch AAA	⌒AAA
check A	Ǎ	tilde A	Ã
check AA	AǍ	tilde AA	AÃ
405/414
1.5.30 부정 (NOT)
글자 앞에 not을 붙이면 그 글자에 사선을 그어준다.
입력	u not== 전체집합
결과	u ≠ 전체집합
1.5.31 그리스 문자
| Alpha | α | nu | ν | aleph | א |
|---|---|---|---|---|---|
| Beta | β | xi | ξ | hbar | ħ |
| Gamma | Γ | gamma | γ | IMATH | ı |
| Delta | Δ | delta | δ | JMATH | j |
| Epsilon | E | epsilon | ε | MHO | ℧ |
| Zeta | Z | zeta | ζ | ELL, LITER | ℓ |
| Eta | H | eta | η | WP | ℘ |
| Theta | Θ | theta | θ | REAL | ℜ |
| Iota | I | iota | ι | IMAG | ℑ |
| Kappa | K | kappa | κ | ANGSTROM | Å |
| Lambda | Λ | lambda | λ | | |
| Mu | M | mu | μ | vartheta | ϑ |
| Nu | N | nu | ν | varpi | ϖ |
| Xi | Ξ | xi | ξ | varsigma | ς |
| Omicron | O | omicron | o | varupsilon | ϒ |
398
KSX 6101:2024
입력	결과	입력	결과	입력	결과
Pi	Π	pi	π	varphi	φ
Rho	P	rho	ρ	varepsilon	ε
Sigma	Σ	sigma	σ		
Tau	T	tau	τ		
Upsilon	Y	upsilon	υ		
Phi	Φ	phi	φ		
Chi	X	chi	χ		
Psi	Ψ	psi	ψ		
Omega	Ω	omega	ω		
1.5.32 괄호
| 입력 | 결과 | 입력 | 결과 |
|---|---|---|---|
| LBRACE | { | RBRACE | } |
| LCEIL | ⌈ | RCEIL | ⌉ |
| LFLOOR | ⌊ | RFLOOR | ⌋ |
1.5.33 적분 기호
| 입력 | 결과 | 입력 | 결과 |
|---|---|---|---|
| SMALLINT | ∫ | SMALLOINT | ∮ |
| INT, INTEGRAL | ∫ | OINT | ∮ |
1.5.34 합, 관계, 집합 기호
| 입력 | 결과 | 입력 | 결과 | 입력 | 결과 |
|---|---|---|---|---|---|
| SMALLSUM | ∑ | SUM | ∑ | SUBSET | ⊂ |
SMCOPROD, AMALG	⨿	COPROD	∐	SUPERSET	⊃
SMALLPROD	∏	PROD	∏	SUBSETEQ	⊆
SMALLUNION, CUP	∪	UNION, BIGCUP	⋃	SUPSETEQ	supseteq
SMALLINTER, CAP	∩	INTER, BIGCAP	⋂	IN	∈
SQCUP	⊔	BIGSQCUP	⨆	OWNS, NI	∋
SQCAP	⊓	BIGSQCAP	⨅	SQSUBSET	⊑
OMINUS	⊖	BIGOMINUS	⨀	SQSUPSET	⊒
ODIV	⊘	BIGODIV	⨸	SQSUBSETEQ	⊑
OTIMES	⊗	BIGOTIMES	⨂	SQSUPSETEQ	⊒
OSLASH	⊘	BIGOSLASH	⨸	LE	≤
ODOT	⊙	BIGODOT	⨀	NOTIN	∉
UPLUS	⊎	BIGUPLUS	⨄	GE	≥
WEDGE, LAND	∧	BIGWEDGE	⋀	<	≺
VEE, LOR	∨	BIGVEE	⋁	>=	≻
<<	≪
>>	≫
LLL, <<<	⋘
GGG, >>>	⋙
1.5.35 화살표
이 예약어는 대소문자를 구분하므로, 반드시 대소문자를 정확하게 표기해야 한다.
입력	결과	입력	결과	입력	결과
larrow	←	LARROW	⇐	nwarrow	↖
rarrow	→	RARROW	⇒	searrow	↘
uparrow	↑	UPARROW	⇑	nearrow	↗
downarrow	↓	DOWNARROW	⇓	swarrow	↙
udarrow	↕	UDARROW	⇕	hookleft	↩
lrarrow	↔	LRARROW	⇔	hookright	↪
mapsto	↦	vert	|	VERT	‖
1.5.36 연산/논리 기호
예약어 image, prime은 대소문자를 구분하므로 반드시 대소문자를 정확하게 표기해야 한다.
입력	결과	입력	결과	입력	결과
PLUSMINUS	±	EMPTYSET	∅	SIM	∼
MINUSPLUS	∓	THEREFORE	∴	APPROX	≈
TIMES	×	BECAUSE	∵	SIMEQ	≃
DIV, DIVIDE	÷	IDENTICAL	≡	CONG	≅
CIRC	∘	BIGCIRC	○	EQUIV	≡
BULLET	•	EXIST	∃	ASYMP	≍
DEG	°	NEQ, !=	≠	ISO	≅
AST	*	DOTEQ	≐	DIAMOND	⋄
STAR	★	image	ℑ	REIMAGE	ℜ
DSUM	⨄	FORALL	∀	prime	′
PARTIAL	∂	INF	∞	LNOT	¬
PROPTO	∝	XOR	⊕		
DAGGER	†	DDAGGER	‡		
1.5.37 기타기호
입력	결과	입력	결과	입력	결과
CDOTS	⋯	LDOTS	…	VDOTS	⋮
DDOTS	⋱	TRIANGLE	△	TRIANGLED	▽
ANGLE	∠	MSANGLE	∡	SANGLE	∠
RTANGLE	∟	VDASH	⊫	HLEFT	⊣
BOT	⊥	TOP	⊤	MODELS	⊧
LAPLACE	ℒ	CENTIGRADE	℃	FAHRENHEIT	℉
LSLANT	/	RSLANT	\	ATT	@
HUND	%	THOU	‰	WELL	#
BASE	♭	BENZENE	⌬	OHM	Ω
401
KSX 6101:2024
해 설
이 해설은 이 표준과 관련된 사항을 설명하는 것으로 표준의 일부는 아니다.
1 개요
1.1 제정의 취지
이 표준은 국내 유통되고 있는 아래아한글 워드프로세서 문서(HWP)에 대한 100% 호환성을 갖는 표준적 전자문서 처리기술(XML)을 이용한 개방형 표준으로의 마이그레이션을 목적으로 한다. 이로 인하여 기술적 의존에 대비한 장기보존문서에 대한 안정성을 확보하고 특정 회사의 기술 및 애플리케이션에 종속적이지 않으며 다양한 애플리케이션에서 해당 워드프로세서 문서를 지원하여 기술개발의 확대를 가져올 수 있다.
1.2 제정의 경위
제1차 표준개발위원회(2011년 3월): 국가표준(KS) 제정을 위해 표준개발위원회에서 제정 방법을 논의 함.
제2차 표준개발위원회(2011년 5월): 국가표준(KS) 제정을 위한 전문위원 구성
제3차 기술심의위원회(2011년 7월): 한글과컴퓨터 양왕현 위원이 표준안 발표 및 수렴안.
제4차 표준개발위원회(2011년 9월): 1차 표준개발위원회 회의록을 보완하여 국가표준(KS) 제정 예고고시 요청을 위한 심의회를 가짐.
제5차 표준개발위원회(2011년 11월): 예고고시외 추가로 의견 수렴을 위한 공개 공청회를 개최.
2 2차 개정
2.1 개정의 취지
이 표준의 문서(HWP)에 추가된 기능 및 요소들에 대하여 기본 포맷을 정의하고 기존 내용을 보완하기 위해 개정을 시행하였다. 이번 개정에서는 문서 보호를 위한 신규 기능인 변경 추적, 암호, 전자 서명 항목이 추가되었으며, 문서 버전 관리를 위한 문서 이력, 문서 설정 정보 기록을 위한 구조가 추가되었다.
402
KSX 6101:2024
2.2 개정의 경위
2011년 12월: 개방형 워드프로세서 마크업 언어(OWPML) 문서 구조 - 국가표준 제정
2015년 12월: 개방형 워드프로세서 마크업 언어(OWPML) 문서 구조 - 국가표준 개정
2016년 12월: JTC1/SC34(문서처리기준 및 처리언어) 전문위원회를 통하여 '개방형 워드프로세서 마크업 언어(OWPML) 문서 구조' 개정 상정
2017년 2월 28일: JTC1/SC34(문서처리기술 및 처리언어) 전문위원회에서 개정 표준안에 대한 1차 논의를 하였으며, 표준안의 내용을 검토
2017년 4월 20일: JTC1/SC34(문서처리기술 및 처리언어) 전문위원회에서 개정 표준안에 대한 2차 논의를 하였으며, 표준안의 내용을 검토
2017년 7월 6일: JTC1/SC34(문서처리기술 및 처리언어) 전문위원회에서 개정 표준안에 대한 3차 논의를 하였으며, 차후 전문위원회 개최 전 전문가로 구성된 작업반 활동을 통해 표준안의 내용을 검토하기로 결정함.
2017년 8월 3일: 작업반 회의를 통해 개정의 취지 항목을 추가하며 추가된 항목에 대한 검토를 받음. 이를 통해 용어정의와 추가된 기능의 인용에 대하여 수정함.
상기 과정을 통해 표준 개정안에 대한 검토를 하고 최종 수정본 작업을 완료함.
2.3 주요 개정 내역
2.3.1 적용범위
기존 적용범위에 암호화, 전자서명 변경, 추적 기능 등의 내용을 추가
2.3.2 자구 수정
'어플리케이션, 그라데이션, 디렉토리, 윈도우' 등의 용어를 '애플리케이션, 그러데이션, 디렉터리, 윈도' 등의 용어로 수정
2.3.3 추가항목
언어 형식에 라인 align, 단락 정렬
2.3.4 KS A 0001:2015 반영
이번의 표준 개정 내용 중 KS A 0001(표준의 서식과 작성방법)이 반영된 주요 내용을 요약하면 다음과 같다.
머리말, 개요의 추가
인용표준의 변경
3 이번 개정 (3차 개정)
3.1 개정의 취지
이번 개정은 표준 개방형 텍스트 문서 규격(OWPML)에 대해 일부 새롭게 추가된 기능 및 요소들에 대하여 기본 포맷을 확장하여 개정하였다. 기존 수요자들이 해당 표준을 참조하거나 도입하여 실제 개발하는 데 많이 어려워한 부분을 수용하고 보완하여, 규격에 대한 상세한 설명과 표준 항목별 샘플 코드를 추가하였다. 명확하게 설명되지 못하였던 부분들에 대해서 자세한 설명을 추가하여 표준의 수요자들이 보다 용이하게 활용하고 적용할 수 있도록 하였다.
또한 확장성 제공을 위해 제공되는 메타데이터 추가 정의 방법에 대하여 수요자들의 이해를 돕기 위해 기존 내용을 보완하고 상세 설명을 추가하여 시스템 통합 또는 애플리케이션 개발자 등 이 표준 수요자들의 이해를 돕기 위해 개정을 시행하였다.
이번 개정에서는 텍스트 문서를 구성하는 구성 요소를 추가하였으며, 이를 구현하기 위해 사용되는
403
KSX 6101:2024
포맷의 수정, 추가된 마크업 부분을 개정 및 새롭게 추가 정의하였다. 또한 이에 따른 하위 호환성에도 문제가 발생하지 않도록 개정 시 고려하였다.
3.2 개정의 경위
2021년 11월: '개방형 워드프로세서 마크업 언어(OWPML) 문서 구조' 학계, 산업계 관련 전문가 대상 설명회 및 공청회 개최를 통한 의견 수렴
2021년 11월: '개방형 워드프로세서 마크업 언어(OWPML) 문서 구조' JTC1/SC34(문서처리기준 및 처리언어) 전문위원회에서 개정 표준안 초안 제출
상기 과정을 통해 표준 개정안에 대한 검토를 하고 최종 수정본 작업을 완료함.
3.3 주요 개정 내용
3.3.1 적용범위
문서 전반에 상세한 설명을 추가하였다.
3.3.2 자구 수정
사용해야 한다, 권고한다, 하지 말아야 한다 등 표준 내용을 명확하게 파악할 수 있도록 표준형식에 맞춰 문서 전반 개정
3.3.3 추가항목
문서 전반에 상세한 설명을 추가하였으며, 항목별 샘플 예제를 추가하여 수요자의 이해를 돕고자 개정하였다.
3.3.4 KS A 0001:2023 반영
이번의 표준 개정 내용 중 KS A 0001(표준의 서식과 작성방법)이 반영된 주요 내용을 요약하면 다음과 같다.
머리말, 해설의 정형문 수정
3절 용어와 정의에서 참고 추가