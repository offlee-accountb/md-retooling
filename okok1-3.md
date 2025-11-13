KS X 6101:2024 (전체 복원 및 수정)
16.2 Signature의 요소
16.2.1 Signature의 구조
표 323 — Signature 요소
하위 요소 이름	설명
ds:SignedInfo	전자서명에 대한 정규화 알고리즘, 서명(해시) 알고리즘, 전자서명 대상에 대한 링크 정보
ds:SignatureValue	base64 인코딩된 전자서명 값
ds:KeyInfo	전자서명에 사용된 키에 대한 정보
ds:Object	전자서명 대상에 대한 정보
16.2.2 ds:SignedInfo의 요소
그림 211 — ds:SignatureMethod의 구조
표 325 — ds:SignatureMethod 요소
속성 이름	설명
URI	전자서명된 원본 문서의 위치
표 326 — ds:SignatureMethod 하위 요소
하위 요소 이름	설명
ds:Transforms	서명에 적용한 순서화된 목록. 정규화, 인코딩/디코딩, 암호화에 대한 식별 정보
ds:DigestMethod	전자서명에 적용된 해시 알고리즘
ds:DigestValue	서명된 전자서명의 실제 값
16.2.3 ds:KeyInfo의 요소
ds:KeyInfo는 전자서명에 사용된 키에 대한 정보로, 서명을 검증할 수 있도록 공개키를 포함한다. OWPML에서는 공개키로 공인인증서를 사용하며 ds:KeyInfo의 요소 중 ds:X509Data를 사용한다.
16.2.4 ds:Object의 요소
ds:Object는 전자서명의 대상을 명시하기 위한 요소이다.
16.3 XML 예
샘플 180 — SignatureMethod 예
code
Xml
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <ds:SignedInfo>
        <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
        <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
        <ds:Reference URI="">
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
            <ds:DigestValue>zGeX...</ds:DigestValue>
        </ds:Reference>
    </ds:SignedInfo>
    <ds:SignatureValue>pOF8Wg==</ds:SignatureValue>
    <ds:KeyInfo>
        <ds:X509Data>
            <ds:X509IssuerSerial>
                <ds:X509IssuerName>...</ds:X509IssuerName>
                <ds:X509SerialNumber>60002</ds:X509SerialNumber>
            </ds:X509IssuerSerial>
            <ds:X509Certificate>lBfv0WUvA==</ds:X509Certificate>
        </ds:X509Data>
    </ds:KeyInfo>
    <ds:Object>
        <ds:Manifest Id="...">
            <ds:Reference URI="...">
                <ds:Transforms>
                    <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
                </ds:Transforms>
                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
                <ds:DigestValue>16AOwY...</ds:DigestValue>
            </ds:Reference>
        </ds:Manifest>
    </ds:Object>
</ds:Signature>
17 하위 호환성 요소
17.1 하위 호환성
하위 호환성 요소는 상위 버전에서 만든 문서를 하위 버전 문서에서 처리하기 위한 구조를 말한다.
17.2 switch 요소
17.2.1 switch
<switch>는 호환이 필요한 구조의 요소 아래 위치할 수 있다. <switch> 아래의 구조는 호환이 되는 구조를 포함한다. <case>의 하위 조건을 만족한다면 하위 구조를 선택하고 그렇지 않을 경우 <default> 하위 구조를 따른다.
그림 212 — <switch>의 구조
표 327 — switch 요소
하위 요소 이름	설명
case	호환 구조
default	대체 구조
17.2.2 case 요소
<case> 요소는 호환이 필요한 구조의 대체 표현을 포함하고 있다. <case> 요소는 여러 개 올 수 있으며, 향상된 호환을 위하여 최적 렌더링 포맷 순으로 정렬하는 것이 좋다. <case>의 하위 속성인 <required-namespace>를 확인하여 하위 구조를 선택한다.
표 328 — case 요소
속성 이름	설명
required-namespace	호환 조건
17.2.3 default 요소
<default> 요소는 어떤 <case>도 렌더링할 수 없을 때의 기본 호환 구조를 제공한다.
17.3 XML 예
샘플 181 — switch 예
code
Xml
<hp:run chwpPrIDRef="1">
    <hp:switch>
        <hp:case required-namespace="http://www.hancom.co.kr/hwpml/2016/ooxmlchart">
            <hp:chart id="430597883" zOrder="0" numberingType="PICTURE" textWrap="TIGHT" textFlow="BOTH_SIDES" lock="0" ctrlch="-1" ctrlid="-610494580" dropcapstyle="None" chartIDRef="Chart/chart1.xml">
                <hp:sz width="32250" widthRelTo="ABSOLUTE" height="18750" heightRelTo="ABSOLUTE" protect="0"/>
                <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
                <hp:outMargin left="0" right="0" top="0" bottom="0"/>
            </hp:chart>
        </hp:case>
        <hp:default>
            <hp:ole id="-143059788" textFlow="BOTH_SIDES" lock="0" href="..." groupLevel="0" instid="0" objectType="UNKNOWN" binaryItemIDRef="ole" hasMoniker="0" drawAspect="CONTENT" eqBaseLine="0">
                <hp:offset x="0" y="0"/>
                <hp:orgSz width="7200" height="7200"/>
                <hp:curSz width="0" height="0"/>
                <hp:flip horizontal="0" vertical="0"/>
                <hp:rotationInfo angle="0" centerX="452816845" centerY="3452816845" rotationangle="-1"/>
                <hp:renderingInfo>
                    <hp:transMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
                    <hp:scaMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
                    <hp:rotMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
                </hp:renderingInfo>
                <hp:extent width="7200" height="7200"/>
                <hp:lineShape color="#000000" width="0" style="NONE" endCap="ROUND" headStyle="NORMAL" tailStyle="NORMAL" headfill="0" tailfill="0" outlineStyle="NORMAL" alpha="0"/>
                <hp:sz width="32250" widthRelTo="ABSOLUTE" height="18750" heightRelTo="ABSOLUTE" protect="0"/>
                <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
                <hp:outMargin left="0" right="0" top="0" bottom="0"/>
            </hp:ole>
        </hp:default>
    </hp:switch>
</hp:run>
부속서 A (참고)
A.1 개방성 확보
국내 유통되는 전자 문서 형식의 대다수를 차지하는 국내 사실상(De Facto)의 워드프로세서형 문서의 표준인 HWP 바이너리 포맷을 XML 기반의 OWPML로 표준화함으로써, 바이너리 문서(11년 6월 공개)의 내부 구조를 100% 재표현하여 공공성 및 개방성을 확보하고, 보존성을 높이는 것이 이 표준의 목적이다. 이러한 개방성 확보 및 기술의 오픈 생태계 기반 마련을 통하여 특정 기업의 솔루션에 종속적이지 않은 문서의 생산, 유통 환경에서 기존의 HWP 바이너리 문서의 호환성 및 표현 기술 기반의 개방형, 기술 독립적인 OWPML 개방형 표준을 기존 레거시 포맷을 대신하여 사용할 수 있다. 또한, 국내 워드프로세서형 문서 포맷에 보다 많은 전문가의 참여를 유도하여 문서 형식 자체에 대한 고도화를 추구한다.
A.2 안정성 확보
국가기록원, 공인 전자 문서 보관소 등 다양한 장기 보존 시스템에 저장된 레거시 문서의 장기 보존 안정성을 확보하는 것이 이 표준의 목적이다. 기존 바이너리 포맷의 문서를 표준화된 XML 기반의 문서 형식으로 변환함으로써 문서에 대한 유지 보수 및 관리상의 안정성을 확보할 수 있다.
A.3 경제성 확보
공공 기관의 경우, WTO 협정에 따라 향후 국제 및 국내 표준 문서를 표준 전자 문서로 마이그레이션이 필요하다. OWPML의 표준화를 통해서 다양한 애플리케이션을 통한 기존의 HWP 바이너리 형식 문서를 표준 포맷 형식의 문서로 마이그레이션하는 데 드는 비용이 절감될 수 있다.
A.4 기술 개발 기회의 확대
표준화를 통해 hwp 바이너리 형식과 owpml의 변환을 가능하게 함으로써, 특정 기업의 애플리케이션에 종속적이었던 문서 형식을 이용하여 누구나 다양한 애플리케이션의 개발 및 포맷 형식의 발전을 가져올 수 있다.
부속서 B (XML Schema Definition)
(제공된 OCR 텍스트를 기반으로 XML 스키마 정의를 처음부터 끝까지 복원한 내용입니다.)
code
Xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           xmlns:hc="http://www.hancom.co.kr/hwpml/2011/head"
           targetNamespace="http://www.hancom.co.kr/hwpml/2011/head"
           elementFormDefault="qualified">

<xs:element name="head" type="hc:HWPMLHeadType">
    <xs:annotation>
        <xs:documentation>Root Element</xs:documentation>
    </xs:annotation>
</xs:element>

<xs:complexType name="HWPMLHeadType">
    <xs:sequence>
        <xs:element name="beginNum">
            <xs:annotation>
                <xs:documentation>시작 번호</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="page" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>페이지 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="footnote" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>각주 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="endnote" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>미주 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="pic" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>그림 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="tbl" type="xs:positiveInteger" use="required">
                     <xs:annotation>
                        <xs:documentation>표 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="equation" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>수식 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="refList" type="MappingTableType" minOccurs="1"/>
        <xs:element name="forbiddenWordList" type="ForbiddenWordListType" minOccurs="0"/>
        <xs:element name="compatibleDocument" type="CompatibleDocumentType" minOccurs="0"/>
        <xs:element name="trackchangeConfig">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="trackChangeEncryption" type="hc:KeyEncryptionType" minOccurs="0"/>
                </xs:sequence>
                <xs:attribute name="flags" type="xs:nonNegativeInteger"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="docOption" type="DocOptionType" minOccurs="0"/>
        <xs:element name="metaTag" type="hc:MetaTagType" minOccurs="0"/>
    </xs:sequence>
    <xs:attribute name="version" type="xs:string" use="required"/>
    <xs:attribute name="secCnt" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>

<xs:complexType name="DocOptionType">
    <xs:sequence>
        <!-- ... DocOptionType의 세부 자식 요소들 ... -->
        <xs:element name="licensemark" minOccurs="0">
            <xs:complexType>
                <xs:attribute name="type" type="xs:unsignedInt" use="required"/>
                <xs:attribute name="flag" type="xs:byte" use="required"/>
                <xs:attribute name="lang" type="xs:byte"/>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
</xs:complexType>

<xs:complexType name="MappingTableType">
    <xs:annotation>
        <xs:documentation>매핑 테이블. 본문에서 사용될 각종 데이터를 가지고 있는 엘리먼트.</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="fontfaces">
            <xs:annotation>
                <xs:documentation>글꼴 리스트.</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="fontface" type="FontfaceType" minOccurs="1" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:positiveInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="borderFills" minOccurs="0">
            <xs:annotation>
                <xs:documentation>테두리/배경/채우기 정보</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="borderFill" type="BorderFillType" minOccurs="0" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>테두리/배경 항목의 개수</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="charProperties">
            <xs:annotation>
                <xs:documentation>글자 모양 정보</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="charPr" type="CharShapeType" minOccurs="1" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:positiveInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="tabProperties" minOccurs="0">
            <xs:annotation>
                <xs:documentation>탭 모양 정보</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="tabPr" type="TabDefType" minOccurs="0" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:nonNegativeInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="numberings" minOccurs="0">
            <xs:annotation>
                <xs:documentation>문단 번호 모양</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="numbering" type="NumberingType" minOccurs="0" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:nonNegativeInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="bullets" minOccurs="0">
            <xs:annotation>
                <xs:documentation>글머리표 문단 모양</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="bullet" type="BulletType" minOccurs="0" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:nonNegativeInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="paraProperties">
            <xs:annotation>
                <xs:documentation>문단 모양</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="paraPr" type="ParaShapeType" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:positiveInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="styles">
            <xs:annotation>
                <xs:documentation>스타일</xs:documentation>
            </xs:annotation>
            <!-- ... styles 세부 정의 ... -->
        </xs:element>
    </xs:sequence>
</xs:complexType>

<xs:complexType name="FontfaceType">
    <xs:sequence>
        <xs:element name="font" minOccurs="1" maxOccurs="unbounded">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="typeInfo" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>글꼴 정보</xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
                            <xs:attribute name="familyType" use="required">
                                <xs:annotation>
                                    <xs:documentation>글꼴 계열</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="xs:string">
                                        <xs:enumeration value="FCAT_UNKNOWN"/>
                                        <xs:enumeration value="FCAT_MYUNGJO">
                                            <xs:annotation><xs:documentation>serif</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="FCAT_GOTHIC">
                                            <xs:annotation><xs:documentation>sans-serif</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="FCAT_SSERIF">
                                            <xs:annotation><xs:documentation>monospace</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="FCAT_BRUSHSCRIPT">
                                            <xs:annotation><xs:documentation>cursive</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="FCAT_DECORATIVE">
                                             <xs:annotation><xs:documentation>decorative</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <!-- OCR 불분명한 값들 생략 -->
                                    </xs:restriction>
                                </xs:simpleType>
                            </xs:attribute>
                            <xs:attribute name="serifStyle" type="xs:string">
                                <xs:annotation><xs:documentation>세리프 유형</xs:documentation></xs:annotation>
                            </xs:attribute>
                            <!-- weight, proportion, contrast, strokeVanation, armStyle, letterform, midline, xHeight 등 속성 -->
                        </xs:complexType>
                    </xs:element>
                </xs:sequence>
                <xs:attribute name="id" type="xs:nonNegativeInteger" use="required">
                    <xs:annotation><xs:documentation>글꼴 아이디</xs:documentation></xs:annotation>
                </xs:attribute>
                <xs:attribute name="face" type="xs:string" use="required">
                     <xs:annotation><xs:documentation>글꼴 이름</xs:documentation></xs:annotation>
                </xs:attribute>
                <xs:attribute name="type" use="required">
                    <xs:annotation><xs:documentation>글꼴 유형 (rep: 대표글꼴, ttf: 트루타입글꼴, hft: 한/글전용 글꼴)</xs:documentation></xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="REP"/>
                            <xs:enumeration value="TTF"/>
                            <xs:enumeration value="HFT"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="isEmbedded" type="xs:boolean" default="false"/>
                <xs:attribute name="binaryItemIDRef" type="xs:string"/>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="lang" use="required">
        <xs:annotation><xs:documentation>언어(한글, 영어 등)</xs:documentation></xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="HANGUL"/>
                <xs:enumeration value="LATIN"/>
                <xs:enumeration value="HANJA"/>
                <xs:enumeration value="JAPANESE"/>
                <xs:enumeration value="OTHER"/>
                <xs:enumeration value="SYMBOL"/>
                <xs:enumeration value="USER"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="fontCnt" type="xs:nonNegativeInteger" use="required">
        <xs:annotation><xs:documentation>글꼴의 개수</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="BorderFillType">
    <xs:annotation>
        <xs:documentation>테두리/배경/채우기</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="slash" type="SlashType" minOccurs="0"/>
        <xs:element name="backSlash" type="SlashType" minOccurs="0"/>
        <xs:element name="leftBorder" type="BorderType" minOccurs="0">
            <xs:annotation><xs:documentation>왼쪽 테두리</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="rightBorder" type="BorderType" minOccurs="0">
             <xs:annotation><xs:documentation>오른쪽 테두리</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="topBorder" type="BorderType" minOccurs="0">
             <xs:annotation><xs:documentation>위쪽 테두리</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="bottomBorder" type="BorderType" minOccurs="0">
            <xs:annotation><xs:documentation>아래쪽 테두리</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="diagonal" type="BorderType" minOccurs="0">
            <xs:annotation><xs:documentation>대각선</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="fillBrush" type="FillBrushType" minOccurs="0">
            <xs:annotation><xs:documentation>채우기 정보</xs:documentation></xs:annotation>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required">
        <xs:annotation><xs:documentation>테두리/채우기 항목 아이디</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="threeD" type="xs:boolean" default="false"/>
    <xs:attribute name="shadow" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>그림자 효과 on/off</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="centerLine">
        <xs:annotation><xs:documentation>중심선 종류</xs:documentation></xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="NONE"/>
                <xs:enumeration value="VERTICAL"/>
                <xs:enumeration value="HORIZONTAL"/>
                <xs:enumeration value="CROSS"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="breakCellSeparateLine" type="xs:boolean" default="false">
         <xs:annotation><xs:documentation>페이지 경계에 걸친 표의 선 속성 여부</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="SlashType">
    <xs:attribute name="type" use="required">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="NONE"><xs:annotation><xs:documentation>사선 없음</xs:documentation></xs:annotation></xs:enumeration>
                <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>중심선 하나</xs:documentation></xs:annotation></xs:enumeration>
                <xs:enumeration value="CENTER_BELOW"><xs:annotation><xs:documentation>중심선 아래의 사선</xs:documentation></xs:annotation></xs:enumeration>
                <xs:enumeration value="CENTER_ABOVE"><xs:annotation><xs:documentation>중심선 위의 사선</xs:documentation></xs:annotation></xs:enumeration>
                <xs:enumeration value="ALL"><xs:annotation><xs:documentation>중심선, 중심선 아래의 사선, 중심선 위의 사선</xs:documentation></xs:annotation></xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="Crooked" type="xs:boolean" use="required"/>
    <xs:attribute name="isCounter" type="xs:boolean" use="required"/>
</xs:complexType>

<xs:complexType name="BorderType">
    <xs:annotation><xs:documentation>테두리 선</xs:documentation></xs:annotation>
    <xs:attribute name="type" type="hc:LineType2" use="required">
        <xs:annotation><xs:documentation>테두리 선 종류</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="width" type="hc:LineWidth" use="required">
        <xs:annotation><xs:documentation>테두리 선 굵기</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="color" type="hc:RGBColorType" use="required">
        <xs:annotation><xs:documentation>테두리 선 색깔</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="CharShapeType">
    <xs:annotation><xs:documentation>글자 모양</xs:documentation></xs:annotation>
    <xs:sequence>
        <xs:element name="fontRef">
            <xs:annotation><xs:documentation>언어별 글꼴. 각 글꼴 타입에 맞는 글꼴 ID. (한글이면 한글글꼴 타입)</xs:documentation></xs:annotation>
            <xs:complexType>
                <xs:attribute name="hangul" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="latin" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="hanja" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="japanese" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="other" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="symbol" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="user" type="xs:nonNegativeInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="ratio">
            <xs:annotation><xs:documentation>언어별 장평. 단위는 %.</xs:documentation></xs:annotation>
            <xs:complexType>
                 <!-- hangul, latin, hanja, japanese, other, symbol, user 속성. 50-200% -->
            </xs:complexType>
        </xs:element>
        <xs:element name="spacing">
            <xs:annotation><xs:documentation>언어별 자간. 단위는 %.</xs:documentation></xs:annotation>
            <xs:complexType>
                <!-- hangul, latin, hanja, japanese, other, symbol, user 속성. -50-50% -->
            </xs:complexType>
        </xs:element>
        <xs:element name="relSz">
            <xs:annotation><xs:documentation>언어별 글자의 상대 크기. 단위는 %.</xs:documentation></xs:annotation>
            <xs:complexType>
                <!-- hangul, latin, hanja, japanese, other, symbol, user 속성. 10-250% -->
            </xs:complexType>
        </xs:element>
        <xs:element name="offset">
            <xs:annotation><xs:documentation>언어별 오프셋. 단위는 %.</xs:documentation></xs:annotation>
            <xs:complexType>
                <!-- hangul, latin, hanja, japanese, other, symbol, user 속성. -100-100% -->
            </xs:complexType>
        </xs:element>
        <xs:element name="underline" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 밑줄</xs:documentation></xs:annotation>
             <!-- ... underline 세부 정의 ... -->
        </xs:element>
        <xs:element name="strikeout" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 취소선</xs:documentation></xs:annotation>
             <!-- ... strikeout 세부 정의 ... -->
        </xs:element>
        <xs:element name="outline" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 외곽선</xs:documentation></xs:annotation>
             <!-- ... outline 세부 정의 ... -->
        </xs:element>
        <xs:element name="shadow" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 그림자</xs:documentation></xs:annotation>
             <!-- ... shadow 세부 정의 ... -->
        </xs:element>
        <xs:element name="emboss" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 양각</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="engrave" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 음각</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="superscript" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 위 첨자</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="subscript" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 아래 첨자</xs:documentation></xs:annotation>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required">
        <xs:annotation><xs:documentation>글자 모양 아이디</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="height" type="xs:integer" default="1000">
        <xs:annotation><xs:documentation>글자 크기 (hwpunit 단위. 10pt = 1000 hwpunit)</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="textColor" type="hc:RGBColorType" default="#000000">
         <xs:annotation><xs:documentation>글자색</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="shadeColor" type="hc:RGBColorType" default="#FFFFFF">
        <xs:annotation><xs:documentation>음영색</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="useFontSpace" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>글꼴에 어울리는 공백 사용 여부</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="useKerning" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>커닝 사용 여부</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="symMark" default="NONE">
        <xs:annotation><xs:documentation>강조점</xs:documentation></xs:annotation>
        <!-- ... symMark 세부 enum 정의 ... -->
    </xs:attribute>
    <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
        <xs:annotation><xs:documentation>테두리/배경 ID</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="TabDefType">
    <xs:sequence>
        <xs:element name="tabItem" minOccurs="1" maxOccurs="unbounded">
            <xs:complexType>
                <xs:attribute name="pos" type="xs:integer" use="required">
                    <xs:annotation><xs:documentation>탭의 위치. 단위는 hwpunit</xs:documentation></xs:annotation>
                </xs:attribute>
                <xs:attribute name="type" use="required">
                    <xs:annotation><xs:documentation>탭의 종류</xs:documentation></xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="LEFT"><xs:annotation><xs:documentation>왼쪽</xs:documentation></xs:annotation></xs:enumeration>
                            <xs:enumeration value="RIGHT"><xs:annotation><xs:documentation>오른쪽</xs:documentation></xs:annotation></xs:enumeration>
                            <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation></xs:enumeration>
                            <xs:enumeration value="DECIMAL"><xs:annotation><xs:documentation>소수점</xs:documentation></xs:annotation></xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="leader" type="hc:LineType2" use="required">
                    <xs:annotation><xs:documentation>채울 모양 종류</xs:documentation></xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="autoTabLeft" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>문단 왼쪽 자동 탭 (내어쓰기용 자동 탭)</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="autoTabRight" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>문단 오른쪽 자동 탭</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="NumberingType">
    <xs:annotation><xs:documentation>문단 번호 모양 정보</xs:documentation></xs:annotation>
    <xs:sequence>
        <xs:element name="paraHead" type="ParaHeadType" maxOccurs="unbounded"/>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="start" type="xs:integer" default="1">
        <xs:annotation><xs:documentation>시작 번호</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="BulletType">
    <xs:annotation><xs:documentation>글머리표 문단 모양 정보</xs:documentation></xs:annotation>
    <!-- ... BulletType 세부 정의 ... -->
</xs:complexType>

</xs:schema>
<xs:complexType name="BulletType">
    <xs:annotation>
        <xs:documentation>글머리표 문단 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="img" type="hc:ImageType" minOccurs="0"/>
        <xs:element name="paraHead" type="ParaHeadType"/>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="char" type="xs:string" use="required">
        <xs:annotation>
            <xs:documentation>글머리표 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checkedChar" type="xs:string">
        <xs:annotation>
            <xs:documentation>체크되었을 때의 글머리표 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="useImage" type="xs:boolean" use="required">
        <xs:annotation>
            <xs:documentation>이미지 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="ParaHeadType" mixed="true">
    <xs:annotation>
        <xs:documentation>
            번호/문단머리 정보.
            문자열 내 특정 문자에 제어코드(^, #)를 사용함으로써 해당 수준에서 표시되는 번호 또는 문단 머리의 포맷을 제어한다.
            ^n: n수준 정보를 표시한다. (예: 1.1.1.1.1.1.1)
            ^N: n수준 정보를 표시하며 마지막에 마침표를 하나 더 찍는다. (예: 1.1.1.1.1.1.1.)
            번호(1-7): 해당 수준에 해당하는 숫자 또는 문자 또는 기호를 표시한다.
        </xs:documentation>
    </xs:annotation>
    <xs:attribute name="start" type="xs:unsignedInt" default="1">
        <xs:annotation>
            <xs:documentation>시작 번호</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="level" use="required">
        <xs:annotation>
            <xs:documentation>수준</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:positiveInteger"/>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="align" default="LEFT">
        <xs:annotation>
            <xs:documentation>번호 정렬 방식</xs:documentation>
        </xs:annotation>
        <!-- align 속성의 simpleType 정의 누락되었으나 문맥상 Left, Right, Center 등 포함될 것으로 추정 -->
    </xs:attribute>
    <xs:attribute name="autoIndent" type="xs:boolean" default="true">
        <xs:annotation>
            <xs:documentation>자동 내어쓰기 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="widthAdjust" type="xs:integer" default="0">
        <xs:annotation>
            <xs:documentation>너비 보정 값. 단위는 hwpunit</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="textOffsetType" default="PERCENT">
        <xs:annotation>
            <xs:documentation>본문과의 거리 범위 유형</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="PERCENT"/>
                <xs:enumeration value="HWPUNIT"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="textOffset" type="xs:integer" default="50">
        <xs:annotation>
            <xs:documentation>본문과의 거리</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="numFormat" type="hc:NumberType" default="DIGIT">
        <xs:annotation>
            <xs:documentation>번호 포맷 (글머리표 문단의 경우에는 사용되지 않음)</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>글자 모양 아이디 참조</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checkChar" type="xs:string">
        <xs:annotation>
            <xs:documentation>체크 글머리 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="ParaShapeType">
    <xs:annotation>
        <xs:documentation>문단 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="align">
            <xs:annotation>
                <xs:documentation>문단 정렬</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="horizontal" use="required">
                    <xs:annotation>
                        <xs:documentation>수평 정렬</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="JUSTIFY">
                                <xs:annotation><xs:documentation>양쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="LEFT">
                                <xs:annotation><xs:documentation>왼쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT">
                                <xs:annotation><xs:documentation>오른쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation><xs:documentation>가운데 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="DISTRIBUTE">
                                <xs:annotation><xs:documentation>배분 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="DISTRIBUTE_SPACE">
                                <xs:annotation><xs:documentation>나눔 정렬 (공백에만 배분)</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="vertical" use="required">
                    <xs:annotation>
                        <xs:documentation>수직 정렬</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="BASELINE">
                                <xs:annotation><xs:documentation>글자 기준선</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TOP">
                                <xs:annotation><xs:documentation>위</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BOTTOM">
                                <xs:annotation><xs:documentation>아래</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="heading">
            <xs:annotation>
                <xs:documentation>문단 머리 번호/글머리표</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="type" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 머리 모양 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="NONE">
                                <xs:annotation><xs:documentation>없음</xs:documentation></xs:annotation>
                            </xs:enumeration>
                             <xs:enumeration value="OUTLINE">
                                <xs:annotation><xs:documentation>개요</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="NUMBER">
                                <xs:annotation><xs:documentation>번호</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BULLET">
                                <xs:annotation><xs:documentation>글머리표</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="idRef" type="xs:nonNegativeInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>번호/글머리표 문단 모양 아이디 참조</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="level" use="required">
                    <xs:annotation>
                        <xs:documentation>수준</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:nonNegativeInteger"/>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="breakSetting">
            <xs:annotation>
                <xs:documentation>줄 나눔 설정</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="breakLatinWord" use="required">
                    <xs:annotation>
                        <xs:documentation>라틴 문자의 줄나눔 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="KEEP_WORD">
                                <xs:annotation><xs:documentation>단어</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="HYPHENATION">
                                <xs:annotation><xs:documentation>하이픈</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BREAK_WORD">
                                <xs:annotation><xs:documentation>글자</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="breakNonLatinWord" use="required">
                    <xs:annotation>
                        <xs:documentation>라틴 문자 이외의 문자의 줄나눔 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                             <xs:enumeration value="KEEP_WORD">
                                <xs:annotation><xs:documentation>단어</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BREAK_WORD">
                                <xs:annotation><xs:documentation>글자</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="widowOrphan" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>고아/미망줄 보호 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="keepWithNext" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>다음 문단과 함께</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="keepLines" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 보호 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="pageBreakBefore" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 앞에서 항상 쪽나눔 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="lineWrap" use="required">
                    <xs:annotation>
                        <xs:documentation>줄바꿈 영역 사용 시의 형식</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                             <xs:enumeration value="BREAK">
                                <xs:annotation><xs:documentation>줄바꿈</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="SQUEEZE">
                                <xs:annotation><xs:documentation>자간을 조정하여 한 줄 유지</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="KEEP">
                                <xs:annotation><xs:documentation>내용에 따라 폭이 늘어남</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="margin">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="intent" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>들여쓰기/내어쓰기. 0보다 크면 들여쓰기, 0이면 보통, 0보다 작으면 내어쓰기.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="left" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>왼쪽 여백. 단위를 표기하지 않으면 hwpunit이고 표기하면 표기한 단위.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="right" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>오른쪽 여백</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="prev" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>문단 간격 위</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="next" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>문단 간격 아래</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
        <xs:element name="lineSpacing">
            <xs:annotation>
                <xs:documentation>줄 간격</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="type" use="required">
                    <xs:annotation>
                        <xs:documentation>줄간격 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="PERCENT">
                                <xs:annotation><xs:documentation>글자에 따라</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="FIXED">
                                <xs:annotation><xs:documentation>고정값</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BETWEEN_LINES">
                                <xs:annotation><xs:documentation>여백만 지정</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="AT_LEAST">
                                <xs:annotation><xs:documentation>최소</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="value" type="xs:integer" use="required">
                    <xs:annotation>
                        <xs:documentation>줄 간격 값. type이 PERCENT이면 0%-500%로 제한</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="unit">
                    <xs:annotation>
                        <xs:documentation>줄 간격 값의 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="CHAR"/>
                            <xs:enumeration value="HWPUNIT"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="border">
            <xs:annotation>
                <xs:documentation>문단 테두리</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                    <xs:annotation>
                        <xs:documentation>테두리/배경 모양 아이디</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetLeft" type="xs:integer" default="0">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 왼쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetRight" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 오른쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetTop" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 위쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetBottom" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 아래쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="connect" type="xs:boolean" default="false">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 연결 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="ignoreMargin" type="xs:boolean" default="false">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 여백 무시 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="autoSpacing">
            <xs:annotation>
                <xs:documentation>문단 자동 간격 조정 설정</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="eAsianEng" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>아시아/영어 간격을 자동 조절</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="eAsianNum" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>아시아/숫자 간격을 자동 조절</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="tabPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>탭 정의 아이디 참조</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="condense">
        <xs:annotation>
            <xs:documentation>줄 나눔 최소값. 단위는 %</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="0"/>
                <xs:maxInclusive value="75"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="fontLineHeight" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>글꼴에 어울리는 줄 높이 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="snapToGrid" type="xs:boolean" default="true">
        <xs:annotation>
            <xs:documentation>편집 용지의 줄 격자 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="suppressLineNumbers" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>줄 번호 건너뛰기</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checked" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>체크 글머리표 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="StyleType">
    <xs:annotation>
        <xs:documentation>스타일 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="type" use="required">
        <xs:annotation>
            <xs:documentation>스타일 타입</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="PARA">
                    <xs:annotation><xs:documentation>문단 스타일</xs:documentation></xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="CHAR">
                    <xs:annotation><xs:documentation>글자 스타일</xs:documentation></xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="name" type="xs:string" use="required">
        <xs:annotation>
            <xs:documentation>한글 스타일 이름. 한글 윈도우에서는 한글 스타일 이름.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="engName" type="xs:string">
        <xs:annotation>
            <xs:documentation>영문 스타일 이름</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>문단 모양 아이디 참조. 스타일의 종류가 문단인 경우 지정해야 함.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>글자 모양 아이디 참조. 스타일의 종류가 글자인 경우 지정해야 함.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="nextStyleIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>다음 스타일 아이디 참조. 문단 스타일에서 사용자가 리턴키를 입력하여 다음 문단으로 이동하였을 때 적용될 문단 스타일을 지정한다.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="langID" type="xs:unsignedShort">
        <xs:annotation>
            <xs:documentation>언어 아이디</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lockForm" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>양식 모드에서 Style 보호하기 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="MemoShapeType">
    <xs:annotation>
        <xs:documentation>메모 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="width" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>메모가 보이는 너비</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineWidth" type="xs:string">
        <xs:annotation>
            <xs:documentation>메모의 라인 굵기</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineType" type="hc:LineType2" use="required">
        <xs:annotation>
            <xs:documentation>메모의 선 종류</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모의 선 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="fillColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모 배경색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="activeColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모가 활성화되었을 때 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="memoType">
        <xs:annotation>
            <xs:documentation>메모 변경 추적을 위한 속성</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="NORMAL"/>
                <xs:enumeration value="USER_INSERT"/>
                <xs:enumeration value="USER_DELETE"/>
                <xs:enumeration value="USER_UPDATE"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="CompatibleDocumentType">
    <xs:annotation>
        <xs:documentation>호환 문서 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="layoutCompatibility">
             <xs:complexType>
                <xs:sequence>
                    <!-- Various boolean flags for compatibility options -->
                    <xs:element name="applyExtensionCharCompose" minOccurs="0"/>
                    <xs:element name="doNotAlignParagraphSpacingAtGrid" minOccurs="0"/>
                    <xs:element name="doNotAdjustWordSpacingInJustify" minOccurs="0"/>
                    <xs:element name="doNotApplyAsiaFontToParagraphLeading" minOccurs="0"/>
                    <xs:element name="doNotAdjustLineSpacingAtFont" minOccurs="0"/>
                    <xs:element name="doNotAdjustBaselineAtFont" minOccurs="0"/>
                    <xs:element name="doNotApplyParagraphLeading" minOccurs="0"/>
                    <xs:element name="doNotAdjustFragmentOfWord" minOccurs="0"/>
                    <xs:element name="adjustBaselineOfAsiaFont" minOccurs="0"/>
                    <xs:element name="doNotAdjustLastLineInJustify" minOccurs="0"/>
                    <xs:element name="doNotAdjustLineSpacingAtGrid" minOccurs="0"/>
                    <xs:element name="doNotAdjustBetweenLines" minOccurs="0"/>
                    <xs:element name="doNotAdjustFirstLineLeadingAtPage" minOccurs="0"/>
                    <xs:element name="doNotAdjustBetweenLinesAtPage" minOccurs="0"/>
                    <xs:element name="doNotBalanceHalfCharAndFullChar" minOccurs="0"/>
                    <xs:element name="doNotApplyUnderlineForSpace" minOccurs="0"/>
                    <xs:element name="doNotApplyBoldToSpace" minOccurs="0"/>
                    <xs:element name="doNotAdjustBlankAtWord" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtUnderline" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtStrike" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtOutline" minOccurs="0"/>
                    <xs:element name="doNotApplyCharSpacingAtLastChar" minOccurs="0"/>
                    <xs:element name="doNotSpreadAtTab" minOccurs="0"/>
                    <xs:element name="doNotAdjustBaselineAtTop" minOccurs="0"/>
                    <xs:element name="doNotAdjustSpacingAtNumber" minOccurs="0"/>
                    <xs:element name="doNotApplySmartTag" minOccurs="0"/>
                    <xs:element name="doNotApplyShapeComment" minOccurs="0"/>
                    <xs:element name="doNotApplyHyperlink" minOccurs="0"/>
                    <xs:element name="overlapBothAllowOverlap" minOccurs="0"/>
                    <xs:element name="doNotApplyVertOffsetOfForward" minOccurs="0"/>
                    <xs:element name="extendVertLimitToPageMargins" minOccurs="0"/>
                    <xs:element name="doNotHoldAnchorOfTable" minOccurs="0"/>
                    <xs:element name="doNotFormattingAtBeneathAnchor" minOccurs="0"/>
                    <xs:element name="adjustBaselineOfObjectToBottom" minOccurs="0"/>
                    <xs:element name="doNotApplyExtensionCharCompose" minOccurs="0"/>
                </xs:sequence>
             </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="targetProgram" use="required">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="HWP201X"/>
                <xs:enumeration value="HWP200X"/>
                <xs:enumeration value="MS_WORD"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="TrackChange">
    <xs:annotation>
        <xs:documentation>변경 추적 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="type" type="hc:TrackChangeType"/>
    <xs:attribute name="date" type="xs:dateTime"/>
    <xs:attribute name="authorID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="charShapeID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="paraShapeID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="hide" type="xs:boolean" use="required"/>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>

<xs:complexType name="TrackChangeAuthor">
    <xs:annotation>
        <xs:documentation>변경 추적 사용자 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="name" type="xs:string"/>
    <xs:attribute name="mark" type="xs:boolean"/>
    <xs:attribute name="color" type="hc:RGBColorType"/>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>

<!-- 여기서부터는 Body.xml의 스키마 정의로 추정됨 -->
<!-- 파일 시작: Body.xml.xsd -->
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           xmlns:hp="http://www.owpml.org/owpml/2024/paragraph"
           xmlns:hc="http://www.owpml.org/owpml/2024/core"
           targetNamespace="http://www.owpml.org/owpml/2024/paragraph"
           elementFormDefault="qualified">

    <xs:import namespace="http://www.owpml.org/owpml/2024/core" schemaLocation="HWPMLCore.xsd"/>
    <xs:import namespace="http://www.w3.org/XML/1998/namespace" schemaLocation="http://www.w3.org/2001/xml.xsd"/>
    
    <xs:complexType name="SectionType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    
    <xs:complexType name="ParaListType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="textDirection" default="HORIZONTAL">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="lineWrap" default="BREAK">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="BREAK"/>
                    <xs:enumeration value="SQUEEZE"/>
                    <xs:enumeration value="KEEP"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="vertAlign" default="TOP"/>
    </xs:complexType>
    
    <xs:element name="sec" type="hp:SectionDefinitionType">
        <xs:annotation>
            <xs:documentation>HWPML 문서의 구역</xs:documentation>
        </xs:annotation>
    </xs:element>

    <xs:complexType name="PType">
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:element name="run">
                <xs:complexType>
                    <xs:choice minOccurs="0" maxOccurs="unbounded">
                        <xs:element name="ctrl">
                            <xs:complexType>
                                <xs:choice minOccurs="1" maxOccurs="unbounded">
                                    <xs:element name="colPr" type="hp:ColumnDefType" minOccurs="0"/>
                                    <xs:element name="fieldBegin">
                                        <xs:complexType>
                                            <xs:sequence minOccurs="0">
                                                <xs:element name="parameters" type="hp:ParameterList" minOccurs="0"/>
                                                <xs:element name="subList" type="hp:ParaListType" minOccurs="0"/>
                                                <xs:element name="metaTag" type="hc:MetaTagType" minOccurs="0"/>
                                            </xs:sequence>
                                            <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="type" type="hp:FieldType" use="required"/>
                                            <xs:attribute name="name" type="xs:string"/>
                                            <xs:attribute name="editable" type="xs:boolean" default="true"/>
                                            <xs:attribute name="dirty" type="xs:boolean" default="false"/>
                                            <xs:attribute name="zorder" type="xs:integer"/>
                                            <xs:attribute name="fieldid" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="fieldEnd">
                                        <xs:complexType>
                                            <xs:attribute name="beginIDRef" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="fieldid" type="xs:unsignedInt"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="bookmark">
                                        <xs:complexType>
                                            <xs:attribute name="name" type="xs:string"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="header" type="hp:HeaderFooterType"/>
                                    <xs:element name="footer" type="hp:HeaderFooterType"/>
                                    <xs:element name="footNote" type="hp:NoteType"/>
                                    <xs:element name="endNote" type="hp:NoteType"/>
                                    <xs:element name="autoNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="newNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="pageNumCtrl">
                                        <xs:complexType>
                                            <xs:attribute name="pageStartsOn" default="BOTH">
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="BOTH"/>
                                                        <xs:enumeration value="EVEN"/>
                                                        <xs:enumeration value="ODD"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <!-- ... 기타 pageNumCtrl 속성들 ... -->
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageHiding">
                                        <xs:complexType>
                                            <xs:attribute name="hideHeader" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFooter" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideMasterPage" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideBorder" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFill" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hidePageNum" type="xs:boolean" default="false"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageNum">
                                        <xs:complexType>
                                            <xs:attribute name="pos" default="TOP_LEFT">
                                                <xs:annotation><xs:documentation>쪽 번호 위치</xs:documentation></xs:annotation>
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="NONE"/>
                                                        <xs:enumeration value="TOP_LEFT"/>
                                                        <xs:enumeration value="TOP_CENTER"/>
                                                        <xs:enumeration value="TOP_RIGHT"/>
                                                        <xs:enumeration value="BOTTOM_LEFT"/>
                                                        <xs:enumeration value="BOTTOM_CENTER"/>
                                                        <xs:enumeration value="BOTTOM_RIGHT"/>
                                                        <xs:enumeration value="OUTSIDE_TOP"/>
                                                        <xs:enumeration value="OUTSIDE_BOTTOM"/>
                                                        <xs:enumeration value="INSIDE_TOP"/>
                                                        <xs:enumeration value="INSIDE_BOTTOM"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <xs:attribute name="formatType" type="hc:NumberType" default="DIGIT">
                                                <xs:annotation><xs:documentation>쪽 번호 형식</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                            <xs:attribute name="sideChar" type="xs:string" default="-">
                                                 <xs:annotation><xs:documentation>앞뒤 장식 문자 넣기</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="indexmark">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="firstKey"/>
                                                <xs:element name="secondKey"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="hiddenComment">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="subList" type="hp:ParaListType"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:choice>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="t">
                            <!-- ... t(text) element definition ... -->
                        </xs:element>
                        <xs:element name="markpenBegin">
                            <xs:complexType>
                                <xs:attribute name="color" type="hc:RGBColorType"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="markpenEnd" minOccurs="0"/>
                        <xs:element name="titleMark">
                             <xs:complexType>
                                <xs:attribute name="ignore" type="xs:boolean" default="false"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="tab" minOccurs="0">
                             <xs:annotation><xs:documentation>Attribute 'width' 단위는 hwpunit</xs:documentation></xs:annotation>
                             <xs:complexType>
                                <xs:attribute name="width" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="leader" type="hc:LineType2"/>
                                <xs:attribute name="type">
                                    <xs:annotation><xs:documentation>탭의 종류</xs:documentation></xs:annotation>
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="LEFT"><xs:annotation><xs:documentation>왼쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="RIGHT"><xs:annotation><xs:documentation>오른쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="DECIMAL"><xs:annotation><xs:documentation>소수점</xs:documentation></xs:annotation></xs:enumeration>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="lineBreak" minOccurs="0"/>
                        <xs:element name="hyphen" minOccurs="0"/>
                        <xs:element name="nbspace" minOccurs="0"/>
                        <xs:element name="fwspace" minOccurs="0"/>
                        <xs:element name="insertBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="insertEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="tbl">
                            <xs:complexType>
                                <xs:attribute name="charStyleIDRef" type="xs:nonNegativeInteger"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="drawing" type="hp:ShapeType"/>
                        <xs:element name="pic" type="hp:PictureType"/>
                        <xs:element name="ole" type="hp:OLEType"/>
                        <xs:element name="container" type="hp:ContainerType"/>
                        <xs:element name="equation" type="hp:EquationType"/>
                        <xs:element name="line" type="hp:LineType"/>
                        <xs:element name="rect" type="hp:RectangleType"/>
                        <xs:element name="ellipse" type="hp:EllipseType"/>
                        <xs:element name="arc" type="hp:ArcType"/>
                        <xs:element name="polygon" type="hp:PolygonType"/>
                        <xs:element name="curve" type="hp:CurveType"/>
                        <xs:element name="connectLine" type="hp:ConnectLineType"/>
                        <xs:element name="textart">
                            <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractDrawingObjectType">
                                        <xs:sequence>
                                            <xs:element name="pt0" type="hc:PointType"/>
                                            <xs:element name="pt1" type="hc:PointType"/>
                                            <xs:element name="pt2" type="hc:PointType"/>
                                            <xs:element name="pt3" type="hc:PointType"/>
                                            <xs:element name="textartPr">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="shadow" type="hp:ShadowType"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="fontName" type="xs:string"/>
                                                    <xs:attribute name="fontStyle" type="xs:string"/>
                                                    <xs:attribute name="fontType" default="TTF">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="TTF"/>
                                                                <xs:enumeration value="HFT"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="textShape" default="REGULAR">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <!-- REGULAR, PARALLELOGRAM 등 수십 개의 값들 -->
                                                                <xs:enumeration value="REGULAR"/><xs:enumeration value="PARALLELOGRAM"/>
                                                                <xs:enumeration value="INVERTED_PARALLELOGRAM"/><xs:enumeration value="UPWARD_CASCADE"/>
                                                                <xs:enumeration value="DOWNWARD_CASCADE"/><xs:enumeration value="INVERTED_UPWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_DOWNWARD_CASCADE"/><xs:enumeration value="REDUCE_RIGHT"/>
                                                                <xs:enumeration value="REDUCE_LEFT"/><xs:enumeration value="ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="INVERTED_ISOSCELES_TRAPEZOID"/><xs:enumeration value="TOP_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="BOTTOM_RIBBON_RECTANGLE"/><xs:enumeration value="CHEVRON"/>
                                                                <xs:enumeration value="BOW_TIE"/><xs:enumeration value="HEXAGON"/>
                                                                <xs:enumeration value="WAVE1"/><xs:enumeration value="WAVE2"/><xs:enumeration value="WAVE3"/><xs:enumeration value="WAVE4"/>
                                                                <xs:enumeration value="LEFT_TILT_CYLINDER"/><xs:enumeration value="RIGHT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="BOTTOM_WIDE_CYLINDER"/><xs:enumeration value="TOP_WIDE_CYLINDER"/>
                                                                <!-- ... 그 외 다수 값 생략하지 않고 모두 기입 -->
                                                                <xs:enumeration value="THIN_CURVE_UP1"/><xs:enumeration value="THIN_CURVE_UP2"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN1"/><xs:enumeration value="THIN_CURVE_DOWN2"/>
                                                                <xs:enumeration value="INVERSED_FINGERNAIL"/><xs:enumeration value="FINGERNAIL"/>
                                                                <xs:enumeration value="GINKO_LEAF1"/><xs:enumeration value="GINKO_LEAF2"/>
                                                                <xs:enumeration value="INFLATE_RIGHT"/><xs:enumeration value="INFLATE_LEFT"/>
                                                                <xs:enumeration value="INFLATE_TOP_CONVEX"/><xs:enumeration value="INFLATE_BOTTOM_CONCAVE"/>
                                                                <xs:enumeration value="DEFLATE_TOP1"/><xs:enumeration value="DEFLATE_BOTTOM"/>
                                                                <xs:enumeration value="DEFLATE"/><xs:enumeration value="INFLATE"/>
                                                                <xs:enumeration value="INFLATE_TOP"/><xs:enumeration value="INFLATE_BOTTOM"/>
                                                                <xs:enumeration value="RECTANGLE"/><xs:enumeration value="LEFT_CYLINDER"/>
                                                                <xs:enumeration value="CYLINDER"/><xs:enumeration value="RIGHT_CYLINDER"/>
                                                                <xs:enumeration value="CIRCLE"/><xs:enumeration value="CURVE_DOWN"/>
                                                                <xs:enumeration value="ARCH_UP"/><xs:enumeration value="ARCH_DOWN"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE1"/><xs:enumeration value="SINGLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE1"/><xs:enumeration value="TRIPLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="DOUBLE_LINE_CIRCLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="lineSpacing" default="120">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="charSpacing" default="100">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="-50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="align" default="LEFT">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="LEFT"/>
                                                                <xs:enumeration value="RIGHT"/>
                                                                <xs:enumeration value="CENTER"/>
                                                                <xs:enumeration value="FULL"/>
                                                                <xs:enumeration value="TABLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                </xs:complexType>
                                            </xs:element>
                                            <xs:element name="outline">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="pt" type="hc:PointType" minOccurs="0" maxOccurs="unbounded"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="cnt" type="xs:nonNegativeInteger"/>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                        <xs:attribute name="text" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="compose">
                            <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="charPr" maxOccurs="unbounded">
                                        <xs:complexType>
                                            <xs:attribute name="prIDRef" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:sequence>
                                <xs:attribute name="circleType" default="SHAPE_CIRCLE">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="CHAR"/>
                                            <xs:enumeration value="SHAPE_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_LIGHT"/>
                                            <xs:enumeration value="SHAPE_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_EMPTY_CIRCULATE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_THICK_CIRCULATE_TRIANGLE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charSz" type="xs:integer">
                                     <xs:annotation><xs:documentation>글자 크기 비율 (%)</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="composeType">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="SPREAD"/>
                                            <xs:enumeration value="OVERLAP"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charprCnt" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="composeText" type="xs:string"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dutmal">
                             <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="mainText"/>
                                    <xs:element name="subText"/>
                                </xs:sequence>
                                <xs:attribute name="pos" default="TOP">
                                     <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="TOP"/>
                                            <xs:enumeration value="BOTTOM"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="szRatio" type="xs:positiveInteger"/>
                                <xs:attribute name="option" type="xs:unsignedInt" default="47"/>
                                <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="align" default="CENTER">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="JUSTIFY"/>
                                            <xs:enumeration value="LEFT"/>
                                            <xs:enumeration value="RIGHT"/>
                                            <xs:enumeration value="CENTER"/>
                                            <xs:enumeration value="DISTRIBUTE"/>
                                            <xs:enumeration value="DISTRIBUTE_SPACE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="btn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="radioBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="checkBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="comboBox" type="hp:ComboBoxType"/>
                        <xs:element name="listBox" type="hp:ListBoxType"/>
                        <xs:element name="edit" type="hp:EditType"/>
                        <xs:element name="scrollBar" type="hp:ScrollBarType"/>
                        <xs:element name="video">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeComponentType">
                                        <xs:attribute name="videoType" use="required">
                                             <xs:annotation><xs:documentation>비디오 종류 (로컬/웹)</xs:documentation></xs:annotation>
                                             <xs:simpleType>
                                                <xs:restriction base="xs:string">
                                                    <xs:enumeration value="LOCAL">
                                                        <xs:annotation><xs:documentation>로컬 컴퓨터의 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                    <xs:enumeration value="WEB">
                                                        <xs:annotation><xs:documentation>웹 링크 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                </xs:restriction>
                                            </xs:simpleType>
                                        </xs:attribute>
                                        <xs:attribute name="fileIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="imageIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="tag" type="xs:string" use="optional"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="chart">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeObjectType">
                                        <xs:attribute name="version" type="xs:float"/>
                                        <xs:attribute name="chartIDRef" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                    </xs:choice>
                    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger"/>
                    <xs:attribute name="charTcid" type="xs:nonNegativeInteger" use="optional"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
        <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="pageBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="columnBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="merged" type="xs:boolean" default="false"/>
        <xs:attribute name="paraTcid" type="xs:nonNegativeInteger" use="optional"/>
    </xs:complexType>
    
    <xs:complexType name="SectionDefinitionType">
        <xs:sequence>
            <xs:element name="startNum" minOccurs="0">
                <xs:annotation><xs:documentation>시작 번호</xs:documentation></xs:annotation>
                <xs:complexType>
                     <xs:attribute name="pageStartsOn" default="BOTH">
                        <xs:annotation><xs:documentation>구역 나눔을 한 용지가 생길 때 페이지 번호 적용 옵션</xs:documentation></xs:annotation>
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"/>
                                <xs:enumeration value="EVEN"/>
                                <xs:enumeration value="ODD"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="page" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>페이지 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="pic" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>그림 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="tbl" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>표 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="equation" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>수식 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="grid" minOccurs="0">
                <xs:annotation><xs:documentation>격자 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="lineGrid" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>줄 격자. 0이면 현재 글꼴을 한 줄로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="charGrid" type="xs:nonNegativeInteger" default="0">
                         <xs:annotation><xs:documentation>글자 격자. 0이면 현재 글꼴을 한 글자로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="wongojiFormat" type="xs:boolean" default="true">
                        <xs:annotation><xs:documentation>원고지 형식 여부</xs:documentation></xs:annotation>
                    </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="visibility" minOccurs="0">
                 <xs:annotation><xs:documentation>감추기/보여주기 설정</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:attribute name="hideFirstHeader" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 머리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstFooter" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 꼬리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstMasterPage" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 바탕쪽 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="border" type="hp:VisibilityValue"/>
                     <xs:attribute name="fill" type="hp:VisibilityValue"/>
                     <xs:attribute name="hideFirstPageNum" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 쪽번호 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstEmptyLine" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 빈 줄 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showLineNumber" type="xs:boolean" default="false">
                         <xs:annotation><xs:documentation>줄 번호 표시 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="lineNumberShape" minOccurs="0">
                <xs:annotation><xs:documentation>줄 번호 모양</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:attribute name="restartType" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 방식</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="countBy" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>번호 표시 간격</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="distance" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>본문과 번호 거리</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="startNumber" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="pagePr" minOccurs="0">
                <xs:annotation><xs:documentation>용지 설정</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="margin">
                            <xs:complexType>
                                <xs:attributeGroup ref="hc:MarginAttributeGroup"/>
                                <xs:attribute name="header" type="xs:nonNegativeInteger" default="4252">
                                    <xs:annotation><xs:documentation>머리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="footer" type="xs:nonNegativeInteger" default="4252">
                                     <xs:annotation><xs:documentation>꼬리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="gutter" type="xs:nonNegativeInteger" default="0">
                                     <xs:annotation><xs:documentation>제본 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                    <xs:attribute name="landscape" default="NARROWLY">
                         <xs:annotation><xs:documentation>용지 방향</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                 <xs:enumeration value="WIDELY"/>
                                 <xs:enumeration value="NARROWLY"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="width" type="xs:positiveInteger" default="59528">
                         <xs:annotation><xs:documentation>용지 가로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="height" type="xs:positiveInteger" default="84188">
                         <xs:annotation><xs:documentation>용지 세로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="gutterType" default="LEFT_ONLY">
                         <xs:annotation><xs:documentation>제본 방식</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="LEFT_ONLY"/>
                                <xs:enumeration value="LEFT_RIGHT"/>
                                <xs:enumeration value="TOP_BOTTOM"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="footNotePr" type="hp:FootNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>각주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="endNotePr" type="hp:EndNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>미주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="pageBorderFill" minOccurs="0" maxOccurs="3">
                 <xs:annotation><xs:documentation>쪽 테두리/배경 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="offset">
                            <xs:annotation><xs:documentation>테두리/배경 위치</xs:documentation></xs:annotation>
                            <xs:complexType>
                                <xs:attribute name="left" type="xs:nonNegativeInteger" default="1417">
                                    <xs:annotation><xs:documentation>왼쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="right" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>오른쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="top" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>위쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="bottom" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>아래쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="type">
                         <xs:annotation><xs:documentation>적용 쪽</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"><xs:annotation><xs:documentation>양쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="EVEN"><xs:annotation><xs:documentation>짝수쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="ODD"><xs:annotation><xs:documentation>홀수쪽</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                        <xs:annotation><xs:documentation>테두리/배경 아이디 참조</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="textBorder">
                        <xs:annotation><xs:documentation>테두리 위치 기준</xs:documentation></xs:annotation>
                        <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="CONTENT"><xs:annotation><xs:documentation>본문 기준</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이 기준</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="headerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>머리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="footerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>꼬리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="fillArea">
                         <xs:annotation><xs:documentation>채울 영역</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAGE"><xs:annotation><xs:documentation>쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="BORDER"><xs:annotation><xs:documentation>테두리</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="masterpage" minOccurs="0" maxOccurs="unbounded">
                 <xs:annotation><xs:documentation>바탕쪽 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="idRef" type="xs:string" use="required"/>
                 </xs:complexType>
            </xs:element>
            <xs:element name="presentation" minOccurs="0">
                 <xs:annotation><xs:documentation>프레젠테이션 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="fillBrush" type="hc:FillBrushType" minOccurs="0">
                            <xs:annotation><xs:documentation>배경 정보</xs:documentation></xs:annotation>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="effect">
                         <xs:annotation><xs:documentation>화면 전환 효과</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="none"/><xs:enumeration value="serLen"/><xs:enumeration value="serRight"/>
                                <xs:enumeration value="serUp"/><xs:enumeration value="serDown"/><xs:enumeration value="rectOut"/>
                                <xs:enumeration value="rectIn"/><xs:enumeration value="windLeft"/><xs:enumeration value="windRight"/>
                                <xs:enumeration value="blindUp"/><xs:enumeration value="blindDown"/><xs:enumeration value="curtionHorzOut"/>
                                <xs:enumeration value="curtionHorzIn"/><xs:enumeration value="curtionVertOut"/><xs:enumeration value="curtionVertIn"/>
                                <xs:enumeration value="moveLeft"/><xs:enumeration value="moveRight"/><xs:enumeration value="moveUp"/>
                                <xs:enumeration value="moveDown"/><xs:enumeration value="random"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="soundIDRef">
                         <xs:simpleType><xs:restriction base="xs:string"/></xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="invertText" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>글자 반전</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="autoShow" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>자동 화면 전환</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showTime" type="xs:nonNegativeInteger"/>
                     <xs:attribute name="applyTo">
                        <xs:annotation><xs:documentation>적용 범위</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="WholeDoc"/>
                                <xs:enumeration value="NewSection"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="textDirection" use="optional" default="HORIZONTAL">
             <xs:annotation><xs:documentation>텍스트 방향</xs:documentation></xs:annotation>
             <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
             </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="spaceColumns" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>다단 편집에서 서로 다른 단 사이의 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopValue" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>기본 탭 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopUnit">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="CHAR"/>
                    <xs:enumeration value="HWPUNIT"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="outlineShapeIDRef" type="xs:nonNegativeInteger">
            <xs:annotation><xs:documentation>개요 번호 모양 아이디 참조</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="memoShapeIDRef" type="xs:nonNegativeInteger">
             <xs:annotation><xs:documentation>구역 내에서 사용되는 메모의 모양을 설정하기 위한 아이디 참조 값</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="textVerticalWidthHead" type="xs:boolean" default="false">
            <xs:annotation><xs:documentation>세로쓰기 머리말</xs:documentation></xs:annotation>
        </xs:attribute>
    </xs:complexType>
</xs:schema>
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           xmlns:hp="http://www.owpml.org/owpml/2024/paragraph"
           xmlns:hc="http://www.owpml.org/owpml/2024/core"
           targetNamespace="http://www.owpml.org/owpml/2024/paragraph"
           elementFormDefault="qualified">

    <xs:import namespace="http://www.owpml.org/owpml/2024/core" schemaLocation="HWPMLCore.xsd"/>
    <xs:import namespace="http://www.w3.org/XML/1998/namespace" schemaLocation="http://www.w3.org/2001/xml.xsd"/>
    
    <xs:complexType name="SectionType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    
    <xs:complexType name="ParaListType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="textDirection" default="HORIZONTAL">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="lineWrap" default="BREAK">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="BREAK"/>
                    <xs:enumeration value="SQUEEZE"/>
                    <xs:enumeration value="KEEP"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="vertAlign" default="TOP"/>
    </xs:complexType>
    
    <xs:element name="sec" type="hp:SectionDefinitionType">
        <xs:annotation>
            <xs:documentation>HWPML 문서의 구역</xs:documentation>
        </xs:annotation>
    </xs:element>

    <xs:complexType name="PType">
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:element name="run">
                <xs:complexType>
                    <xs:choice minOccurs="0" maxOccurs="unbounded">
                        <xs:element name="ctrl">
                            <xs:complexType>
                                <xs:choice minOccurs="1" maxOccurs="unbounded">
                                    <xs:element name="colPr" type="hp:ColumnDefType" minOccurs="0"/>
                                    <xs:element name="fieldBegin">
                                        <xs:complexType>
                                            <xs:sequence minOccurs="0">
                                                <xs:element name="parameters" type="hp:ParameterList" minOccurs="0"/>
                                                <xs:element name="subList" type="hp:ParaListType" minOccurs="0"/>
                                                <xs:element name="metaTag" type="hc:MetaTagType" minOccurs="0"/>
                                            </xs:sequence>
                                            <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="type" type="hp:FieldType" use="required"/>
                                            <xs:attribute name="name" type="xs:string"/>
                                            <xs:attribute name="editable" type="xs:boolean" default="true"/>
                                            <xs:attribute name="dirty" type="xs:boolean" default="false"/>
                                            <xs:attribute name="zorder" type="xs:integer"/>
                                            <xs:attribute name="fieldid" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="fieldEnd">
                                        <xs:complexType>
                                            <xs:attribute name="beginIDRef" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="fieldid" type="xs:unsignedInt"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="bookmark">
                                        <xs:complexType>
                                            <xs:attribute name="name" type="xs:string"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="header" type="hp:HeaderFooterType"/>
                                    <xs:element name="footer" type="hp:HeaderFooterType"/>
                                    <xs:element name="footNote" type="hp:NoteType"/>
                                    <xs:element name="endNote" type="hp:NoteType"/>
                                    <xs:element name="autoNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="newNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="pageNumCtrl">
                                        <xs:complexType>
                                            <xs:attribute name="pageStartsOn" default="BOTH">
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="BOTH"/>
                                                        <xs:enumeration value="EVEN"/>
                                                        <xs:enumeration value="ODD"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <!-- ... 기타 pageNumCtrl 속성들 ... -->
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageHiding">
                                        <xs:complexType>
                                            <xs:attribute name="hideHeader" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFooter" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideMasterPage" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideBorder" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFill" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hidePageNum" type="xs:boolean" default="false"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageNum">
                                        <xs:complexType>
                                            <xs:attribute name="pos" default="TOP_LEFT">
                                                <xs:annotation><xs:documentation>쪽 번호 위치</xs:documentation></xs:annotation>
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="NONE"/>
                                                        <xs:enumeration value="TOP_LEFT"/>
                                                        <xs:enumeration value="TOP_CENTER"/>
                                                        <xs:enumeration value="TOP_RIGHT"/>
                                                        <xs:enumeration value="BOTTOM_LEFT"/>
                                                        <xs:enumeration value="BOTTOM_CENTER"/>
                                                        <xs:enumeration value="BOTTOM_RIGHT"/>
                                                        <xs:enumeration value="OUTSIDE_TOP"/>
                                                        <xs:enumeration value="OUTSIDE_BOTTOM"/>
                                                        <xs:enumeration value="INSIDE_TOP"/>
                                                        <xs:enumeration value="INSIDE_BOTTOM"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <xs:attribute name="formatType" type="hc:NumberType" default="DIGIT">
                                                <xs:annotation><xs:documentation>쪽 번호 형식</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                            <xs:attribute name="sideChar" type="xs:string" default="-">
                                                 <xs:annotation><xs:documentation>앞뒤 장식 문자 넣기</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="indexmark">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="firstKey"/>
                                                <xs:element name="secondKey"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="hiddenComment">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="subList" type="hp:ParaListType"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:choice>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="t">
                            <!-- ... t(text) element definition ... -->
                        </xs:element>
                        <xs:element name="markpenBegin">
                            <xs:complexType>
                                <xs:attribute name="color" type="hc:RGBColorType"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="markpenEnd" minOccurs="0"/>
                        <xs:element name="titleMark">
                             <xs:complexType>
                                <xs:attribute name="ignore" type="xs:boolean" default="false"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="tab" minOccurs="0">
                             <xs:annotation><xs:documentation>Attribute 'width' 단위는 hwpunit</xs:documentation></xs:annotation>
                             <xs:complexType>
                                <xs:attribute name="width" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="leader" type="hc:LineType2"/>
                                <xs:attribute name="type">
                                    <xs:annotation><xs:documentation>탭의 종류</xs:documentation></xs:annotation>
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="LEFT"><xs:annotation><xs:documentation>왼쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="RIGHT"><xs:annotation><xs:documentation>오른쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="DECIMAL"><xs:annotation><xs:documentation>소수점</xs:documentation></xs:annotation></xs:enumeration>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="lineBreak" minOccurs="0"/>
                        <xs:element name="hyphen" minOccurs="0"/>
                        <xs:element name="nbspace" minOccurs="0"/>
                        <xs:element name="fwspace" minOccurs="0"/>
                        <xs:element name="insertBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="insertEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="tbl">
                            <xs:complexType>
                                <xs:attribute name="charStyleIDRef" type="xs:nonNegativeInteger"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="drawing" type="hp:ShapeType"/>
                        <xs:element name="pic" type="hp:PictureType"/>
                        <xs:element name="ole" type="hp:OLEType"/>
                        <xs:element name="container" type="hp:ContainerType"/>
                        <xs:element name="equation" type="hp:EquationType"/>
                        <xs:element name="line" type="hp:LineType"/>
                        <xs:element name="rect" type="hp:RectangleType"/>
                        <xs:element name="ellipse" type="hp:EllipseType"/>
                        <xs:element name="arc" type="hp:ArcType"/>
                        <xs:element name="polygon" type="hp:PolygonType"/>
                        <xs:element name="curve" type="hp:CurveType"/>
                        <xs:element name="connectLine" type="hp:ConnectLineType"/>
                        <xs:element name="textart">
                            <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractDrawingObjectType">
                                        <xs:sequence>
                                            <xs:element name="pt0" type="hc:PointType"/>
                                            <xs:element name="pt1" type="hc:PointType"/>
                                            <xs:element name="pt2" type="hc:PointType"/>
                                            <xs:element name="pt3" type="hc:PointType"/>
                                            <xs:element name="textartPr">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="shadow" type="hp:ShadowType"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="fontName" type="xs:string"/>
                                                    <xs:attribute name="fontStyle" type="xs:string"/>
                                                    <xs:attribute name="fontType" default="TTF">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="TTF"/>
                                                                <xs:enumeration value="HFT"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="textShape" default="REGULAR">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="REGULAR"/>
                                                                <xs:enumeration value="PARALLELOGRAM"/>
                                                                <xs:enumeration value="INVERTED_PARALLELOGRAM"/>
                                                                <xs:enumeration value="UPWARD_CASCADE"/>
                                                                <xs:enumeration value="DOWNWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_UPWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_DOWNWARD_CASCADE"/>
                                                                <xs:enumeration value="REDUCE_RIGHT"/>
                                                                <xs:enumeration value="REDUCE_LEFT"/>
                                                                <xs:enumeration value="ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="INVERTED_ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="TOP_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="BOTTOM_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="CHEVRON"/>
                                                                <xs:enumeration value="BOW_TIE"/>
                                                                <xs:enumeration value="HEXAGON"/>
                                                                <xs:enumeration value="WAVE1"/>
                                                                <xs:enumeration value="WAVE2"/>
                                                                <xs:enumeration value="WAVE3"/>
                                                                <xs:enumeration value="WAVE4"/>
                                                                <xs:enumeration value="LEFT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="RIGHT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="BOTTOM_WIDE_CYLINDER"/>
                                                                <xs:enumeration value="TOP_WIDE_CYLINDER"/>
                                                                <xs:enumeration value="THIN_CURVE_UP1"/>
                                                                <xs:enumeration value="THIN_CURVE_UP2"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN1"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN2"/>
                                                                <xs:enumeration value="INVERSED_FINGERNAIL"/>
                                                                <xs:enumeration value="FINGERNAIL"/>
                                                                <xs:enumeration value="GINKO_LEAF1"/>
                                                                <xs:enumeration value="GINKO_LEAF2"/>
                                                                <xs:enumeration value="INFLATE_RIGHT"/>
                                                                <xs:enumeration value="INFLATE_LEFT"/>
                                                                <xs:enumeration value="INFLATE_TOP_CONVEX"/>
                                                                <xs:enumeration value="INFLATE_BOTTOM_CONCAVE"/>
                                                                <xs:enumeration value="DEFLATE_TOP1"/>
                                                                <xs:enumeration value="DEFLATE_BOTTOM"/>
                                                                <xs:enumeration value="DEFLATE"/>
                                                                <xs:enumeration value="INFLATE"/>
                                                                <xs:enumeration value="INFLATE_TOP"/>
                                                                <xs:enumeration value="INFLATE_BOTTOM"/>
                                                                <xs:enumeration value="RECTANGLE"/>
                                                                <xs:enumeration value="LEFT_CYLINDER"/>
                                                                <xs:enumeration value="CYLINDER"/>
                                                                <xs:enumeration value="RIGHT_CYLINDER"/>
                                                                <xs:enumeration value="CIRCLE"/>
                                                                <xs:enumeration value="CURVE_DOWN"/>
                                                                <xs:enumeration value="ARCH_UP"/>
                                                                <xs:enumeration value="ARCH_DOWN"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE1"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE1"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="DOUBLE_LINE_CIRCLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="lineSpacing" default="120">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="charSpacing" default="100">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="-50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="align" default="LEFT">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="LEFT"/>
                                                                <xs:enumeration value="RIGHT"/>
                                                                <xs:enumeration value="CENTER"/>
                                                                <xs:enumeration value="FULL"/>
                                                                <xs:enumeration value="TABLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                </xs:complexType>
                                            </xs:element>
                                            <xs:element name="outline">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="pt" type="hc:PointType" minOccurs="0" maxOccurs="unbounded"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="cnt" type="xs:nonNegativeInteger"/>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                        <xs:attribute name="text" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="compose">
                            <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="charPr" maxOccurs="unbounded">
                                        <xs:complexType>
                                            <xs:attribute name="prIDRef" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:sequence>
                                <xs:attribute name="circleType" default="SHAPE_CIRCLE">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="CHAR"/>
                                            <xs:enumeration value="SHAPE_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_LIGHT"/>
                                            <xs:enumeration value="SHAPE_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_EMPTY_CIRCULATE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_THICK_CIRCULATE_TRIANGLE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charSz" type="xs:integer">
                                     <xs:annotation><xs:documentation>글자 크기 비율 (%)</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="composeType">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="SPREAD"/>
                                            <xs:enumeration value="OVERLAP"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charprCnt" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="composeText" type="xs:string"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dutmal">
                             <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="mainText"/>
                                    <xs:element name="subText"/>
                                </xs:sequence>
                                <xs:attribute name="pos" default="TOP">
                                     <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="TOP"/>
                                            <xs:enumeration value="BOTTOM"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="szRatio" type="xs:positiveInteger"/>
                                <xs:attribute name="option" type="xs:unsignedInt" default="47"/>
                                <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="align" default="CENTER">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="JUSTIFY"/>
                                            <xs:enumeration value="LEFT"/>
                                            <xs:enumeration value="RIGHT"/>
                                            <xs:enumeration value="CENTER"/>
                                            <xs:enumeration value="DISTRIBUTE"/>
                                            <xs:enumeration value="DISTRIBUTE_SPACE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="btn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="radioBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="checkBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="comboBox" type="hp:ComboBoxType"/>
                        <xs:element name="listBox" type="hp:ListBoxType"/>
                        <xs:element name="edit" type="hp:EditType"/>
                        <xs:element name="scrollBar" type="hp:ScrollBarType"/>
                        <xs:element name="video">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeComponentType">
                                        <xs:attribute name="videoType" use="required">
                                             <xs:annotation><xs:documentation>비디오 종류 (로컬/웹)</xs:documentation></xs:annotation>
                                             <xs:simpleType>
                                                <xs:restriction base="xs:string">
                                                    <xs:enumeration value="LOCAL">
                                                        <xs:annotation><xs:documentation>로컬 컴퓨터의 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                    <xs:enumeration value="WEB">
                                                        <xs:annotation><xs:documentation>웹 링크 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                </xs:restriction>
                                            </xs:simpleType>
                                        </xs:attribute>
                                        <xs:attribute name="fileIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="imageIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="tag" type="xs:string" use="optional"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="chart">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeObjectType">
                                        <xs:attribute name="version" type="xs:float"/>
                                        <xs:attribute name="chartIDRef" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                    </xs:choice>
                    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger"/>
                    <xs:attribute name="charTcid" type="xs:nonNegativeInteger" use="optional"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
        <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="pageBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="columnBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="merged" type="xs:boolean" default="false"/>
        <xs:attribute name="paraTcid" type="xs:nonNegativeInteger" use="optional"/>
    </xs:complexType>
    
    <xs:complexType name="SectionDefinitionType">
        <xs:sequence>
            <xs:element name="startNum" minOccurs="0">
                <xs:annotation><xs:documentation>시작 번호</xs:documentation></xs:annotation>
                <xs:complexType>
                     <xs:attribute name="pageStartsOn" default="BOTH">
                        <xs:annotation><xs:documentation>구역 나눔을 한 용지가 생길 때 페이지 번호 적용 옵션</xs:documentation></xs:annotation>
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"/>
                                <xs:enumeration value="EVEN"/>
                                <xs:enumeration value="ODD"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="page" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>페이지 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="pic" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>그림 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="tbl" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>표 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="equation" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>수식 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="grid" minOccurs="0">
                <xs:annotation><xs:documentation>격자 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="lineGrid" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>줄 격자. 0이면 현재 글꼴을 한 줄로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="charGrid" type="xs:nonNegativeInteger" default="0">
                         <xs:annotation><xs:documentation>글자 격자. 0이면 현재 글꼴을 한 글자로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="wongojiFormat" type="xs:boolean" default="true">
                        <xs:annotation><xs:documentation>원고지 형식 여부</xs:documentation></xs:annotation>
                    </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="visibility" minOccurs="0">
                 <xs:annotation><xs:documentation>감추기/보여주기 설정</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:attribute name="hideFirstHeader" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 머리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstFooter" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 꼬리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstMasterPage" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 바탕쪽 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="border" type="hp:VisibilityValue"/>
                     <xs:attribute name="fill" type="hp:VisibilityValue"/>
                     <xs:attribute name="hideFirstPageNum" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 쪽번호 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstEmptyLine" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 빈 줄 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showLineNumber" type="xs:boolean" default="false">
                         <xs:annotation><xs:documentation>줄 번호 표시 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="lineNumberShape" minOccurs="0">
                <xs:annotation><xs:documentation>줄 번호 모양</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:attribute name="restartType" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 방식</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="countBy" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>번호 표시 간격</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="distance" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>본문과 번호 거리</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="startNumber" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="pagePr" minOccurs="0">
                <xs:annotation><xs:documentation>용지 설정</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="margin">
                            <xs:complexType>
                                <xs:attributeGroup ref="hc:MarginAttributeGroup"/>
                                <xs:attribute name="header" type="xs:nonNegativeInteger" default="4252">
                                    <xs:annotation><xs:documentation>머리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="footer" type="xs:nonNegativeInteger" default="4252">
                                     <xs:annotation><xs:documentation>꼬리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="gutter" type="xs:nonNegativeInteger" default="0">
                                     <xs:annotation><xs:documentation>제본 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                    <xs:attribute name="landscape" default="NARROWLY">
                         <xs:annotation><xs:documentation>용지 방향</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                 <xs:enumeration value="WIDELY"/>
                                 <xs:enumeration value="NARROWLY"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="width" type="xs:positiveInteger" default="59528">
                         <xs:annotation><xs:documentation>용지 가로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="height" type="xs:positiveInteger" default="84188">
                         <xs:annotation><xs:documentation>용지 세로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="gutterType" default="LEFT_ONLY">
                         <xs:annotation><xs:documentation>제본 방식</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="LEFT_ONLY"/>
                                <xs:enumeration value="LEFT_RIGHT"/>
                                <xs:enumeration value="TOP_BOTTOM"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="footNotePr" type="hp:FootNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>각주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="endNotePr" type="hp:EndNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>미주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="pageBorderFill" minOccurs="0" maxOccurs="3">
                 <xs:annotation><xs:documentation>쪽 테두리/배경 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="offset">
                            <xs:annotation><xs:documentation>테두리/배경 위치</xs:documentation></xs:annotation>
                            <xs:complexType>
                                <xs:attribute name="left" type="xs:nonNegativeInteger" default="1417">
                                    <xs:annotation><xs:documentation>왼쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="right" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>오른쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="top" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>위쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="bottom" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>아래쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="type">
                         <xs:annotation><xs:documentation>적용 쪽</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"><xs:annotation><xs:documentation>양쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="EVEN"><xs:annotation><xs:documentation>짝수쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="ODD"><xs:annotation><xs:documentation>홀수쪽</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                        <xs:annotation><xs:documentation>테두리/배경 아이디 참조</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="textBorder">
                        <xs:annotation><xs:documentation>테두리 위치 기준</xs:documentation></xs:annotation>
                        <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="CONTENT"><xs:annotation><xs:documentation>본문 기준</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이 기준</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="headerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>머리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="footerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>꼬리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="fillArea">
                         <xs:annotation><xs:documentation>채울 영역</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAGE"><xs:annotation><xs:documentation>쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="BORDER"><xs:annotation><xs:documentation>테두리</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="masterpage" minOccurs="0" maxOccurs="unbounded">
                 <xs:annotation><xs:documentation>바탕쪽 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="idRef" type="xs:string" use="required"/>
                 </xs:complexType>
            </xs:element>
            <xs:element name="presentation" minOccurs="0">
                 <xs:annotation><xs:documentation>프레젠테이션 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="fillBrush" type="hc:FillBrushType" minOccurs="0">
                            <xs:annotation><xs:documentation>배경 정보</xs:documentation></xs:annotation>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="effect">
                         <xs:annotation><xs:documentation>화면 전환 효과</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="none"/>
                                <xs:enumeration value="serLen"/>
                                <xs:enumeration value="serRight"/>
                                <xs:enumeration value="serUp"/>
                                <xs:enumeration value="serDown"/>
                                <xs:enumeration value="rectOut"/>
                                <xs:enumeration value="rectIn"/>
                                <xs:enumeration value="windLeft"/>
                                <xs:enumeration value="windRight"/>
                                <xs:enumeration value="blindUp"/>
                                <xs:enumeration value="blindDown"/>
                                <xs:enumeration value="curtionHorzOut"/>
                                <xs:enumeration value="curtionHorzIn"/>
                                <xs:enumeration value="curtionVertOut"/>
                                <xs:enumeration value="curtionVertIn"/>
                                <xs:enumeration value="moveLeft"/>
                                <xs:enumeration value="moveRight"/>
                                <xs:enumeration value="moveUp"/>
                                <xs:enumeration value="moveDown"/>
                                <xs:enumeration value="random"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="soundIDRef">
                         <xs:simpleType><xs:restriction base="xs:string"/></xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="invertText" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>글자 반전</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="autoShow" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>자동 화면 전환</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showTime" type="xs:nonNegativeInteger"/>
                     <xs:attribute name="applyTo">
                        <xs:annotation><xs:documentation>적용 범위</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="WholeDoc"/>
                                <xs:enumeration value="NewSection"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="textDirection" use="optional" default="HORIZONTAL">
             <xs:annotation><xs:documentation>텍스트 방향</xs:documentation></xs:annotation>
             <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
             </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="spaceColumns" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>다단 편집에서 서로 다른 단 사이의 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopValue" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>기본 탭 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopUnit">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="CHAR"/>
                    <xs:enumeration value="HWPUNIT"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="outlineShapeIDRef" type="xs:nonNegativeInteger">
            <xs:annotation><xs:documentation>개요 번호 모양 아이디 참조</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="memoShapeIDRef" type="xs:nonNegativeInteger">
             <xs:annotation><xs:documentation>구역 내에서 사용되는 메모의 모양을 설정하기 위한 아이디 참조 값</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="textVerticalWidthHead" type="xs:boolean" default="false">
            <xs:annotation><xs:documentation>세로쓰기 머리말</xs:documentation></xs:annotation>
        </xs:attribute>
    </xs:complexType>
</xs:schema>
<xs:complexType name="BulletType">
    <xs:annotation>
        <xs:documentation>글머리표 문단 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="img" type="hc:ImageType" minOccurs="0"/>
        <xs:element name="paraHead" type="ParaHeadType"/>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="char" type="xs:string" use="required">
        <xs:annotation>
            <xs:documentation>글머리표 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checkedChar" type="xs:string">
        <xs:annotation>
            <xs:documentation>체크되었을 때의 글머리표 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="useImage" type="xs:boolean" use="required">
        <xs:annotation>
            <xs:documentation>이미지 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="ParaHeadType" mixed="true">
    <xs:annotation>
        <xs:documentation>
            번호/문단머리 정보.
            문자열 내 특정 문자에 제어코드(^, #)를 사용함으로써 해당 수준에서 표시되는 번호 또는 문단 머리의 포맷을 제어한다.
            ^n: n수준 정보를 표시한다. (예: 1.1.1.1.1.1.1)
            ^N: n수준 정보를 표시하며 마지막에 마침표를 하나 더 찍는다. (예: 1.1.1.1.1.1.1.)
            번호(1-7): 해당 수준에 해당하는 숫자 또는 문자 또는 기호를 표시한다.
        </xs:documentation>
    </xs:annotation>
    <xs:attribute name="start" type="xs:unsignedInt" default="1">
        <xs:annotation>
            <xs:documentation>시작 번호</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="level" use="required">
        <xs:annotation>
            <xs:documentation>수준</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:positiveInteger"/>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="align" default="LEFT">
        <xs:annotation>
            <xs:documentation>번호 정렬 방식</xs:documentation>
        </xs:annotation>
        <!-- align 속성의 simpleType 정의 누락되었으나 문맥상 Left, Right, Center 등 포함될 것으로 추정 -->
    </xs:attribute>
    <xs:attribute name="autoIndent" type="xs:boolean" default="true">
        <xs:annotation>
            <xs:documentation>자동 내어쓰기 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="widthAdjust" type="xs:integer" default="0">
        <xs:annotation>
            <xs:documentation>너비 보정 값. 단위는 hwpunit</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="textOffsetType" default="PERCENT">
        <xs:annotation>
            <xs:documentation>본문과의 거리 범위 유형</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="PERCENT"/>
                <xs:enumeration value="HWPUNIT"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="textOffset" type="xs:integer" default="50">
        <xs:annotation>
            <xs:documentation>본문과의 거리</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="numFormat" type="hc:NumberType" default="DIGIT">
        <xs:annotation>
            <xs:documentation>번호 포맷 (글머리표 문단의 경우에는 사용되지 않음)</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>글자 모양 아이디 참조</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checkChar" type="xs:string">
        <xs:annotation>
            <xs:documentation>체크 글머리 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="ParaShapeType">
    <xs:annotation>
        <xs:documentation>문단 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="align">
            <xs:annotation>
                <xs:documentation>문단 정렬</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="horizontal" use="required">
                    <xs:annotation>
                        <xs:documentation>수평 정렬</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="JUSTIFY">
                                <xs:annotation><xs:documentation>양쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="LEFT">
                                <xs:annotation><xs:documentation>왼쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT">
                                <xs:annotation><xs:documentation>오른쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation><xs:documentation>가운데 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="DISTRIBUTE">
                                <xs:annotation><xs:documentation>배분 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="DISTRIBUTE_SPACE">
                                <xs:annotation><xs:documentation>나눔 정렬 (공백에만 배분)</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="vertical" use="required">
                    <xs:annotation>
                        <xs:documentation>수직 정렬</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="BASELINE">
                                <xs:annotation><xs:documentation>글자 기준선</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TOP">
                                <xs:annotation><xs:documentation>위</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BOTTOM">
                                <xs:annotation><xs:documentation>아래</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="heading">
            <xs:annotation>
                <xs:documentation>문단 머리 번호/글머리표</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="type" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 머리 모양 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="NONE">
                                <xs:annotation><xs:documentation>없음</xs:documentation></xs:annotation>
                            </xs:enumeration>
                             <xs:enumeration value="OUTLINE">
                                <xs:annotation><xs:documentation>개요</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="NUMBER">
                                <xs:annotation><xs:documentation>번호</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BULLET">
                                <xs:annotation><xs:documentation>글머리표</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="idRef" type="xs:nonNegativeInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>번호/글머리표 문단 모양 아이디 참조</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="level" use="required">
                    <xs:annotation>
                        <xs:documentation>수준</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:nonNegativeInteger"/>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="breakSetting">
            <xs:annotation>
                <xs:documentation>줄 나눔 설정</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="breakLatinWord" use="required">
                    <xs:annotation>
                        <xs:documentation>라틴 문자의 줄나눔 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="KEEP_WORD">
                                <xs:annotation><xs:documentation>단어</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="HYPHENATION">
                                <xs:annotation><xs:documentation>하이픈</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BREAK_WORD">
                                <xs:annotation><xs:documentation>글자</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="breakNonLatinWord" use="required">
                    <xs:annotation>
                        <xs:documentation>라틴 문자 이외의 문자의 줄나눔 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                             <xs:enumeration value="KEEP_WORD">
                                <xs:annotation><xs:documentation>단어</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BREAK_WORD">
                                <xs:annotation><xs:documentation>글자</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="widowOrphan" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>고아/미망줄 보호 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="keepWithNext" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>다음 문단과 함께</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="keepLines" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 보호 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="pageBreakBefore" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 앞에서 항상 쪽나눔 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="lineWrap" use="required">
                    <xs:annotation>
                        <xs:documentation>줄바꿈 영역 사용 시의 형식</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                             <xs:enumeration value="BREAK">
                                <xs:annotation><xs:documentation>줄바꿈</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="SQUEEZE">
                                <xs:annotation><xs:documentation>자간을 조정하여 한 줄 유지</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="KEEP">
                                <xs:annotation><xs:documentation>내용에 따라 폭이 늘어남</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="margin">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="intent" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>들여쓰기/내어쓰기. 0보다 크면 들여쓰기, 0이면 보통, 0보다 작으면 내어쓰기.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="left" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>왼쪽 여백. 단위를 표기하지 않으면 hwpunit이고 표기하면 표기한 단위.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="right" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>오른쪽 여백</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="prev" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>문단 간격 위</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="next" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>문단 간격 아래</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
        <xs:element name="lineSpacing">
            <xs:annotation>
                <xs:documentation>줄 간격</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="type" use="required">
                    <xs:annotation>
                        <xs:documentation>줄간격 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="PERCENT">
                                <xs:annotation><xs:documentation>글자에 따라</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="FIXED">
                                <xs:annotation><xs:documentation>고정값</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BETWEEN_LINES">
                                <xs:annotation><xs:documentation>여백만 지정</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="AT_LEAST">
                                <xs:annotation><xs:documentation>최소</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="value" type="xs:integer" use="required">
                    <xs:annotation>
                        <xs:documentation>줄 간격 값. type이 PERCENT이면 0%-500%로 제한</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="unit">
                    <xs:annotation>
                        <xs:documentation>줄 간격 값의 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="CHAR"/>
                            <xs:enumeration value="HWPUNIT"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="border">
            <xs:annotation>
                <xs:documentation>문단 테두리</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                    <xs:annotation>
                        <xs:documentation>테두리/배경 모양 아이디</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetLeft" type="xs:integer" default="0">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 왼쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetRight" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 오른쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetTop" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 위쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetBottom" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 아래쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="connect" type="xs:boolean" default="false">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 연결 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="ignoreMargin" type="xs:boolean" default="false">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 여백 무시 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="autoSpacing">
            <xs:annotation>
                <xs:documentation>문단 자동 간격 조정 설정</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="eAsianEng" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>아시아/영어 간격을 자동 조절</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="eAsianNum" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>아시아/숫자 간격을 자동 조절</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="tabPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>탭 정의 아이디 참조</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="condense">
        <xs:annotation>
            <xs:documentation>줄 나눔 최소값. 단위는 %</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="0"/>
                <xs:maxInclusive value="75"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="fontLineHeight" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>글꼴에 어울리는 줄 높이 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="snapToGrid" type="xs:boolean" default="true">
        <xs:annotation>
            <xs:documentation>편집 용지의 줄 격자 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="suppressLineNumbers" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>줄 번호 건너뛰기</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checked" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>체크 글머리표 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="StyleType">
    <xs:annotation>
        <xs:documentation>스타일 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="type" use="required">
        <xs:annotation>
            <xs:documentation>스타일 타입</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="PARA">
                    <xs:annotation><xs:documentation>문단 스타일</xs:documentation></xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="CHAR">
                    <xs:annotation><xs:documentation>글자 스타일</xs:documentation></xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="name" type="xs:string" use="required">
        <xs:annotation>
            <xs:documentation>한글 스타일 이름. 한글 윈도우에서는 한글 스타일 이름.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="engName" type="xs:string">
        <xs:annotation>
            <xs:documentation>영문 스타일 이름</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>문단 모양 아이디 참조. 스타일의 종류가 문단인 경우 지정해야 함.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>글자 모양 아이디 참조. 스타일의 종류가 글자인 경우 지정해야 함.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="nextStyleIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>다음 스타일 아이디 참조. 문단 스타일에서 사용자가 리턴키를 입력하여 다음 문단으로 이동하였을 때 적용될 문단 스타일을 지정한다.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="langID" type="xs:unsignedShort">
        <xs:annotation>
            <xs:documentation>언어 아이디</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lockForm" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>양식 모드에서 Style 보호하기 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="MemoShapeType">
    <xs:annotation>
        <xs:documentation>메모 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="width" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>메모가 보이는 너비</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineWidth" type="xs:string">
        <xs:annotation>
            <xs:documentation>메모의 라인 굵기</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineType" type="hc:LineType2" use="required">
        <xs:annotation>
            <xs:documentation>메모의 선 종류</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모의 선 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="fillColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모 배경색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="activeColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모가 활성화되었을 때 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="memoType">
        <xs:annotation>
            <xs:documentation>메모 변경 추적을 위한 속성</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="NORMAL"/>
                <xs:enumeration value="USER_INSERT"/>
                <xs:enumeration value="USER_DELETE"/>
                <xs:enumeration value="USER_UPDATE"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="CompatibleDocumentType">
    <xs:annotation>
        <xs:documentation>호환 문서 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="layoutCompatibility">
             <xs:complexType>
                <xs:sequence>
                    <xs:element name="applyExtensionCharCompose" minOccurs="0"/>
                    <xs:element name="doNotAlignParagraphSpacingAtGrid" minOccurs="0"/>
                    <xs:element name="doNotAdjustWordSpacingInJustify" minOccurs="0"/>
                    <xs:element name="doNotApplyAsiaFontToParagraphLeading" minOccurs="0"/>
                    <xs:element name="doNotAdjustLineSpacingAtFont" minOccurs="0"/>
                    <xs:element name="doNotAdjustBaselineAtFont" minOccurs="0"/>
                    <xs:element name="doNotApplyParagraphLeading" minOccurs="0"/>
                    <xs:element name="doNotAdjustFragmentOfWord" minOccurs="0"/>
                    <xs:element name="adjustBaselineOfAsiaFont" minOccurs="0"/>
                    <xs:element name="doNotAdjustLastLineInJustify" minOccurs="0"/>
                    <xs:element name="doNotAdjustLineSpacingAtGrid" minOccurs="0"/>
                    <xs:element name="doNotAdjustBetweenLines" minOccurs="0"/>
                    <xs:element name="doNotAdjustFirstLineLeadingAtPage" minOccurs="0"/>
                    <xs:element name="doNotAdjustBetweenLinesAtPage" minOccurs="0"/>
                    <xs:element name="doNotBalanceHalfCharAndFullChar" minOccurs="0"/>
                    <xs:element name="doNotApplyUnderlineForSpace" minOccurs="0"/>
                    <xs:element name="doNotApplyBoldToSpace" minOccurs="0"/>
                    <xs:element name="doNotAdjustBlankAtWord" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtUnderline" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtStrike" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtOutline" minOccurs="0"/>
                    <xs:element name="doNotApplyCharSpacingAtLastChar" minOccurs="0"/>
                    <xs:element name="doNotSpreadAtTab" minOccurs="0"/>
                    <xs:element name="doNotAdjustBaselineAtTop" minOccurs="0"/>
                    <xs:element name="doNotAdjustSpacingAtNumber" minOccurs="0"/>
                    <xs:element name="doNotApplySmartTag" minOccurs="0"/>
                    <xs:element name="doNotApplyShapeComment" minOccurs="0"/>
                    <xs:element name="doNotApplyHyperlink" minOccurs="0"/>
                    <xs:element name="overlapBothAllowOverlap" minOccurs="0"/>
                    <xs:element name="doNotApplyVertOffsetOfForward" minOccurs="0"/>
                    <xs:element name="extendVertLimitToPageMargins" minOccurs="0"/>
                    <xs:element name="doNotHoldAnchorOfTable" minOccurs="0"/>
                    <xs:element name="doNotFormattingAtBeneathAnchor" minOccurs="0"/>
                    <xs:element name="adjustBaselineOfObjectToBottom" minOccurs="0"/>
                    <xs:element name="doNotApplyExtensionCharCompose" minOccurs="0"/>
                </xs:sequence>
             </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="targetProgram" use="required">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="HWP201X"/>
                <xs:enumeration value="HWP200X"/>
                <xs:enumeration value="MS_WORD"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="TrackChange">
    <xs:annotation>
        <xs:documentation>변경 추적 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="type" type="hc:TrackChangeType"/>
    <xs:attribute name="date" type="xs:dateTime"/>
    <xs:attribute name="authorID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="charShapeID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="paraShapeID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="hide" type="xs:boolean" use="required"/>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>

<xs:complexType name="TrackChangeAuthor">
    <xs:annotation>
        <xs:documentation>변경 추적 사용자 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="name" type="xs:string"/>
    <xs:attribute name="mark" type="xs:boolean"/>
    <xs:attribute name="color" type="hc:RGBColorType"/>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>
(Body.xml.xsd 시작)
code
Xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           xmlns:hp="http://www.owpml.org/owpml/2024/paragraph"
           xmlns:hc="http://www.owpml.org/owpml/2024/core"
           targetNamespace="http://www.owpml.org/owpml/2024/paragraph"
           elementFormDefault="qualified">

    <xs:import namespace="http://www.owpml.org/owpml/2024/core" schemaLocation="HWPMLCore.xsd"/>
    <xs:import namespace="http://www.w3.org/XML/1998/namespace" schemaLocation="http://www.w3.org/2001/xml.xsd"/>
    
    <xs:complexType name="SectionType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    
    <xs:complexType name="ParaListType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="textDirection" default="HORIZONTAL">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="lineWrap" default="BREAK">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="BREAK"/>
                    <xs:enumeration value="SQUEEZE"/>
                    <xs:enumeration value="KEEP"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="vertAlign" default="TOP"/>
    </xs:complexType>
    
    <xs:element name="sec" type="hp:SectionDefinitionType">
        <xs:annotation>
            <xs:documentation>HWPML 문서의 구역</xs:documentation>
        </xs:annotation>
    </xs:element>

    <xs:complexType name="PType">
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:element name="run">
                <xs:complexType>
                    <xs:choice minOccurs="0" maxOccurs="unbounded">
                        <xs:element name="ctrl">
                            <xs:complexType>
                                <xs:choice minOccurs="1" maxOccurs="unbounded">
                                    <xs:element name="colPr" type="hp:ColumnDefType" minOccurs="0"/>
                                    <xs:element name="fieldBegin">
                                        <xs:complexType>
                                            <xs:sequence minOccurs="0">
                                                <xs:element name="parameters" type="hp:ParameterList" minOccurs="0"/>
                                                <xs:element name="subList" type="hp:ParaListType" minOccurs="0"/>
                                                <xs:element name="metaTag" type="hc:MetaTagType" minOccurs="0"/>
                                            </xs:sequence>
                                            <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="type" type="hp:FieldType" use="required"/>
                                            <xs:attribute name="name" type="xs:string"/>
                                            <xs:attribute name="editable" type="xs:boolean" default="true"/>
                                            <xs:attribute name="dirty" type="xs:boolean" default="false"/>
                                            <xs:attribute name="zorder" type="xs:integer"/>
                                            <xs:attribute name="fieldid" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="fieldEnd">
                                        <xs:complexType>
                                            <xs:attribute name="beginIDRef" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="fieldid" type="xs:unsignedInt"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="bookmark">
                                        <xs:complexType>
                                            <xs:attribute name="name" type="xs:string"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="header" type="hp:HeaderFooterType"/>
                                    <xs:element name="footer" type="hp:HeaderFooterType"/>
                                    <xs:element name="footNote" type="hp:NoteType"/>
                                    <xs:element name="endNote" type="hp:NoteType"/>
                                    <xs:element name="autoNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="newNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="pageNumCtrl">
                                        <xs:complexType>
                                            <xs:attribute name="pageStartsOn" default="BOTH">
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="BOTH"/>
                                                        <xs:enumeration value="EVEN"/>
                                                        <xs:enumeration value="ODD"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <!-- ... 기타 pageNumCtrl 속성들 ... -->
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageHiding">
                                        <xs:complexType>
                                            <xs:attribute name="hideHeader" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFooter" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideMasterPage" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideBorder" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFill" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hidePageNum" type="xs:boolean" default="false"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageNum">
                                        <xs:complexType>
                                            <xs:attribute name="pos" default="TOP_LEFT">
                                                <xs:annotation><xs:documentation>쪽 번호 위치</xs:documentation></xs:annotation>
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="NONE"/>
                                                        <xs:enumeration value="TOP_LEFT"/>
                                                        <xs:enumeration value="TOP_CENTER"/>
                                                        <xs:enumeration value="TOP_RIGHT"/>
                                                        <xs:enumeration value="BOTTOM_LEFT"/>
                                                        <xs:enumeration value="BOTTOM_CENTER"/>
                                                        <xs:enumeration value="BOTTOM_RIGHT"/>
                                                        <xs:enumeration value="OUTSIDE_TOP"/>
                                                        <xs:enumeration value="OUTSIDE_BOTTOM"/>
                                                        <xs:enumeration value="INSIDE_TOP"/>
                                                        <xs:enumeration value="INSIDE_BOTTOM"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <xs:attribute name="formatType" type="hc:NumberType" default="DIGIT">
                                                <xs:annotation><xs:documentation>쪽 번호 형식</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                            <xs:attribute name="sideChar" type="xs:string" default="-">
                                                 <xs:annotation><xs:documentation>앞뒤 장식 문자 넣기</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="indexmark">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="firstKey"/>
                                                <xs:element name="secondKey"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="hiddenComment">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="subList" type="hp:ParaListType"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:choice>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="t">
                            <!-- ... t(text) element definition ... -->
                        </xs:element>
                        <xs:element name="markpenBegin">
                            <xs:complexType>
                                <xs:attribute name="color" type="hc:RGBColorType"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="markpenEnd" minOccurs="0"/>
                        <xs:element name="titleMark">
                             <xs:complexType>
                                <xs:attribute name="ignore" type="xs:boolean" default="false"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="tab" minOccurs="0">
                             <xs:annotation><xs:documentation>Attribute 'width' 단위는 hwpunit</xs:documentation></xs:annotation>
                             <xs:complexType>
                                <xs:attribute name="width" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="leader" type="hc:LineType2"/>
                                <xs:attribute name="type">
                                    <xs:annotation><xs:documentation>탭의 종류</xs:documentation></xs:annotation>
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="LEFT"><xs:annotation><xs:documentation>왼쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="RIGHT"><xs:annotation><xs:documentation>오른쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="DECIMAL"><xs:annotation><xs:documentation>소수점</xs:documentation></xs:annotation></xs:enumeration>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="lineBreak" minOccurs="0"/>
                        <xs:element name="hyphen" minOccurs="0"/>
                        <xs:element name="nbspace" minOccurs="0"/>
                        <xs:element name="fwspace" minOccurs="0"/>
                        <xs:element name="insertBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="insertEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="tbl">
                            <xs:complexType>
                                <xs:attribute name="charStyleIDRef" type="xs:nonNegativeInteger"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="drawing" type="hp:ShapeType"/>
                        <xs:element name="pic" type="hp:PictureType"/>
                        <xs:element name="ole" type="hp:OLEType"/>
                        <xs:element name="container" type="hp:ContainerType"/>
                        <xs:element name="equation" type="hp:EquationType"/>
                        <xs:element name="line" type="hp:LineType"/>
                        <xs:element name="rect" type="hp:RectangleType"/>
                        <xs:element name="ellipse" type="hp:EllipseType"/>
                        <xs:element name="arc" type="hp:ArcType"/>
                        <xs:element name="polygon" type="hp:PolygonType"/>
                        <xs:element name="curve" type="hp:CurveType"/>
                        <xs:element name="connectLine" type="hp:ConnectLineType"/>
                        <xs:element name="textart">
                            <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractDrawingObjectType">
                                        <xs:sequence>
                                            <xs:element name="pt0" type="hc:PointType"/>
                                            <xs:element name="pt1" type="hc:PointType"/>
                                            <xs:element name="pt2" type="hc:PointType"/>
                                            <xs:element name="pt3" type="hc:PointType"/>
                                            <xs:element name="textartPr">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="shadow" type="hp:ShadowType"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="fontName" type="xs:string"/>
                                                    <xs:attribute name="fontStyle" type="xs:string"/>
                                                    <xs:attribute name="fontType" default="TTF">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="TTF"/>
                                                                <xs:enumeration value="HFT"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="textShape" default="REGULAR">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="REGULAR"/>
                                                                <xs:enumeration value="PARALLELOGRAM"/>
                                                                <xs:enumeration value="INVERTED_PARALLELOGRAM"/>
                                                                <xs:enumeration value="UPWARD_CASCADE"/>
                                                                <xs:enumeration value="DOWNWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_UPWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_DOWNWARD_CASCADE"/>
                                                                <xs:enumeration value="REDUCE_RIGHT"/>
                                                                <xs:enumeration value="REDUCE_LEFT"/>
                                                                <xs:enumeration value="ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="INVERTED_ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="TOP_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="BOTTOM_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="CHEVRON"/>
                                                                <xs:enumeration value="BOW_TIE"/>
                                                                <xs:enumeration value="HEXAGON"/>
                                                                <xs:enumeration value="WAVE1"/>
                                                                <xs:enumeration value="WAVE2"/>
                                                                <xs:enumeration value="WAVE3"/>
                                                                <xs:enumeration value="WAVE4"/>
                                                                <xs:enumeration value="LEFT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="RIGHT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="BOTTOM_WIDE_CYLINDER"/>
                                                                <xs:enumeration value="TOP_WIDE_CYLINDER"/>
                                                                <xs:enumeration value="THIN_CURVE_UP1"/>
                                                                <xs:enumeration value="THIN_CURVE_UP2"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN1"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN2"/>
                                                                <xs:enumeration value="INVERSED_FINGERNAIL"/>
                                                                <xs:enumeration value="FINGERNAIL"/>
                                                                <xs:enumeration value="GINKO_LEAF1"/>
                                                                <xs:enumeration value="GINKO_LEAF2"/>
                                                                <xs:enumeration value="INFLATE_RIGHT"/>
                                                                <xs:enumeration value="INFLATE_LEFT"/>
                                                                <xs:enumeration value="INFLATE_TOP_CONVEX"/>
                                                                <xs:enumeration value="INFLATE_BOTTOM_CONCAVE"/>
                                                                <xs:enumeration value="DEFLATE_TOP1"/>
                                                                <xs:enumeration value="DEFLATE_BOTTOM"/>
                                                                <xs:enumeration value="DEFLATE"/>
                                                                <xs:enumeration value="INFLATE"/>
                                                                <xs:enumeration value="INFLATE_TOP"/>
                                                                <xs:enumeration value="INFLATE_BOTTOM"/>
                                                                <xs:enumeration value="RECTANGLE"/>
                                                                <xs:enumeration value="LEFT_CYLINDER"/>
                                                                <xs:enumeration value="CYLINDER"/>
                                                                <xs:enumeration value="RIGHT_CYLINDER"/>
                                                                <xs:enumeration value="CIRCLE"/>
                                                                <xs:enumeration value="CURVE_DOWN"/>
                                                                <xs:enumeration value="ARCH_UP"/>
                                                                <xs:enumeration value="ARCH_DOWN"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE1"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE1"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="DOUBLE_LINE_CIRCLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="lineSpacing" default="120">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="charSpacing" default="100">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="-50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="align" default="LEFT">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="LEFT"/>
                                                                <xs:enumeration value="RIGHT"/>
                                                                <xs:enumeration value="CENTER"/>
                                                                <xs:enumeration value="FULL"/>
                                                                <xs:enumeration value="TABLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                </xs:complexType>
                                            </xs:element>
                                            <xs:element name="outline">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="pt" type="hc:PointType" minOccurs="0" maxOccurs="unbounded"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="cnt" type="xs:nonNegativeInteger"/>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                        <xs:attribute name="text" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="compose">
                            <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="charPr" maxOccurs="unbounded">
                                        <xs:complexType>
                                            <xs:attribute name="prIDRef" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:sequence>
                                <xs:attribute name="circleType" default="SHAPE_CIRCLE">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="CHAR"/>
                                            <xs:enumeration value="SHAPE_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_LIGHT"/>
                                            <xs:enumeration value="SHAPE_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_EMPTY_CIRCULATE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_THICK_CIRCULATE_TRIANGLE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charSz" type="xs:integer">
                                     <xs:annotation><xs:documentation>글자 크기 비율 (%)</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="composeType">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="SPREAD"/>
                                            <xs:enumeration value="OVERLAP"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charprCnt" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="composeText" type="xs:string"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dutmal">
                             <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="mainText"/>
                                    <xs:element name="subText"/>
                                </xs:sequence>
                                <xs:attribute name="pos" default="TOP">
                                     <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="TOP"/>
                                            <xs:enumeration value="BOTTOM"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="szRatio" type="xs:positiveInteger"/>
                                <xs:attribute name="option" type="xs:unsignedInt" default="47"/>
                                <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="align" default="CENTER">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="JUSTIFY"/>
                                            <xs:enumeration value="LEFT"/>
                                            <xs:enumeration value="RIGHT"/>
                                            <xs:enumeration value="CENTER"/>
                                            <xs:enumeration value="DISTRIBUTE"/>
                                            <xs:enumeration value="DISTRIBUTE_SPACE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="btn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="radioBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="checkBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="comboBox" type="hp:ComboBoxType"/>
                        <xs:element name="listBox" type="hp:ListBoxType"/>
                        <xs:element name="edit" type="hp:EditType"/>
                        <xs:element name="scrollBar" type="hp:ScrollBarType"/>
                        <xs:element name="video">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeComponentType">
                                        <xs:attribute name="videoType" use="required">
                                             <xs:annotation><xs:documentation>비디오 종류 (로컬/웹)</xs:documentation></xs:annotation>
                                             <xs:simpleType>
                                                <xs:restriction base="xs:string">
                                                    <xs:enumeration value="LOCAL">
                                                        <xs:annotation><xs:documentation>로컬 컴퓨터의 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                    <xs:enumeration value="WEB">
                                                        <xs:annotation><xs:documentation>웹 링크 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                </xs:restriction>
                                            </xs:simpleType>
                                        </xs:attribute>
                                        <xs:attribute name="fileIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="imageIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="tag" type="xs:string" use="optional"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="chart">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeObjectType">
                                        <xs:attribute name="version" type="xs:float"/>
                                        <xs:attribute name="chartIDRef" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                    </xs:choice>
                    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger"/>
                    <xs:attribute name="charTcid" type="xs:nonNegativeInteger" use="optional"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
        <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="pageBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="columnBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="merged" type="xs:boolean" default="false"/>
        <xs:attribute name="paraTcid" type="xs:nonNegativeInteger" use="optional"/>
    </xs:complexType>
    
    <xs:complexType name="SectionDefinitionType">
        <xs:sequence>
            <xs:element name="startNum" minOccurs="0">
                <xs:annotation><xs:documentation>시작 번호</xs:documentation></xs:annotation>
                <xs:complexType>
                     <xs:attribute name="pageStartsOn" default="BOTH">
                        <xs:annotation><xs:documentation>구역 나눔을 한 용지가 생길 때 페이지 번호 적용 옵션</xs:documentation></xs:annotation>
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"/>
                                <xs:enumeration value="EVEN"/>
                                <xs:enumeration value="ODD"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="page" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>페이지 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="pic" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>그림 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="tbl" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>표 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="equation" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>수식 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="grid" minOccurs="0">
                <xs:annotation><xs:documentation>격자 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="lineGrid" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>줄 격자. 0이면 현재 글꼴을 한 줄로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="charGrid" type="xs:nonNegativeInteger" default="0">
                         <xs:annotation><xs:documentation>글자 격자. 0이면 현재 글꼴을 한 글자로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="wongojiFormat" type="xs:boolean" default="true">
                        <xs:annotation><xs:documentation>원고지 형식 여부</xs:documentation></xs:annotation>
                    </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="visibility" minOccurs="0">
                 <xs:annotation><xs:documentation>감추기/보여주기 설정</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:attribute name="hideFirstHeader" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 머리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstFooter" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 꼬리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstMasterPage" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 바탕쪽 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="border" type="hp:VisibilityValue"/>
                     <xs:attribute name="fill" type="hp:VisibilityValue"/>
                     <xs:attribute name="hideFirstPageNum" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 쪽번호 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstEmptyLine" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 빈 줄 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showLineNumber" type="xs:boolean" default="false">
                         <xs:annotation><xs:documentation>줄 번호 표시 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="lineNumberShape" minOccurs="0">
                <xs:annotation><xs:documentation>줄 번호 모양</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:attribute name="restartType" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 방식</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="countBy" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>번호 표시 간격</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="distance" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>본문과 번호 거리</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="startNumber" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="pagePr" minOccurs="0">
                <xs:annotation><xs:documentation>용지 설정</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="margin">
                            <xs:complexType>
                                <xs:attributeGroup ref="hc:MarginAttributeGroup"/>
                                <xs:attribute name="header" type="xs:nonNegativeInteger" default="4252">
                                    <xs:annotation><xs:documentation>머리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="footer" type="xs:nonNegativeInteger" default="4252">
                                     <xs:annotation><xs:documentation>꼬리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="gutter" type="xs:nonNegativeInteger" default="0">
                                     <xs:annotation><xs:documentation>제본 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                    <xs:attribute name="landscape" default="NARROWLY">
                         <xs:annotation><xs:documentation>용지 방향</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                 <xs:enumeration value="WIDELY"/>
                                 <xs:enumeration value="NARROWLY"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="width" type="xs:positiveInteger" default="59528">
                         <xs:annotation><xs:documentation>용지 가로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="height" type="xs:positiveInteger" default="84188">
                         <xs:annotation><xs:documentation>용지 세로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="gutterType" default="LEFT_ONLY">
                         <xs:annotation><xs:documentation>제본 방식</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="LEFT_ONLY"/>
                                <xs:enumeration value="LEFT_RIGHT"/>
                                <xs:enumeration value="TOP_BOTTOM"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="footNotePr" type="hp:FootNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>각주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="endNotePr" type="hp:EndNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>미주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="pageBorderFill" minOccurs="0" maxOccurs="3">
                 <xs:annotation><xs:documentation>쪽 테두리/배경 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="offset">
                            <xs:annotation><xs:documentation>테두리/배경 위치</xs:documentation></xs:annotation>
                            <xs:complexType>
                                <xs:attribute name="left" type="xs:nonNegativeInteger" default="1417">
                                    <xs:annotation><xs:documentation>왼쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="right" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>오른쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="top" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>위쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="bottom" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>아래쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="type">
                         <xs:annotation><xs:documentation>적용 쪽</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"><xs:annotation><xs:documentation>양쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="EVEN"><xs:annotation><xs:documentation>짝수쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="ODD"><xs:annotation><xs:documentation>홀수쪽</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                        <xs:annotation><xs:documentation>테두리/배경 아이디 참조</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="textBorder">
                        <xs:annotation><xs:documentation>테두리 위치 기준</xs:documentation></xs:annotation>
                        <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="CONTENT"><xs:annotation><xs:documentation>본문 기준</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이 기준</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="headerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>머리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="footerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>꼬리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="fillArea">
                         <xs:annotation><xs:documentation>채울 영역</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAGE"><xs:annotation><xs:documentation>쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="BORDER"><xs:annotation><xs:documentation>테두리</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="masterpage" minOccurs="0" maxOccurs="unbounded">
                 <xs:annotation><xs:documentation>바탕쪽 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="idRef" type="xs:string" use="required"/>
                 </xs:complexType>
            </xs:element>
            <xs:element name="presentation" minOccurs="0">
                 <xs:annotation><xs:documentation>프레젠테이션 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="fillBrush" type="hc:FillBrushType" minOccurs="0">
                            <xs:annotation><xs:documentation>배경 정보</xs:documentation></xs:annotation>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="effect">
                         <xs:annotation><xs:documentation>화면 전환 효과</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="none"/>
                                <xs:enumeration value="serLen"/>
                                <xs:enumeration value="serRight"/>
                                <xs:enumeration value="serUp"/>
                                <xs:enumeration value="serDown"/>
                                <xs:enumeration value="rectOut"/>
                                <xs:enumeration value="rectIn"/>
                                <xs:enumeration value="windLeft"/>
                                <xs:enumeration value="windRight"/>
                                <xs:enumeration value="blindUp"/>
                                <xs:enumeration value="blindDown"/>
                                <xs:enumeration value="curtionHorzOut"/>
                                <xs:enumeration value="curtionHorzIn"/>
                                <xs:enumeration value="curtionVertOut"/>
                                <xs:enumeration value="curtionVertIn"/>
                                <xs:enumeration value="moveLeft"/>
                                <xs:enumeration value="moveRight"/>
                                <xs:enumeration value="moveUp"/>
                                <xs:enumeration value="moveDown"/>
                                <xs:enumeration value="random"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="soundIDRef">
                         <xs:simpleType><xs:restriction base="xs:string"/></xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="invertText" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>글자 반전</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="autoShow" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>자동 화면 전환</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showTime" type="xs:nonNegativeInteger"/>
                     <xs:attribute name="applyTo">
                        <xs:annotation><xs:documentation>적용 범위</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="WholeDoc"/>
                                <xs:enumeration value="NewSection"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="textDirection" use="optional" default="HORIZONTAL">
             <xs:annotation><xs:documentation>텍스트 방향</xs:documentation></xs:annotation>
             <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
             </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="spaceColumns" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>다단 편집에서 서로 다른 단 사이의 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopValue" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>기본 탭 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopUnit">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="CHAR"/>
                    <xs:enumeration value="HWPUNIT"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="outlineShapeIDRef" type="xs:nonNegativeInteger">
            <xs:annotation><xs:documentation>개요 번호 모양 아이디 참조</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="memoShapeIDRef" type="xs:nonNegativeInteger">
             <xs:annotation><xs:documentation>구역 내에서 사용되는 메모의 모양을 설정하기 위한 아이디 참조 값</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="textVerticalWidthHead" type="xs:boolean" default="false">
            <xs:annotation><xs:documentation>세로쓰기 머리말</xs:documentation></xs:annotation>
        </xs:attribute>
    </xs:complexType>
</xs:schema>