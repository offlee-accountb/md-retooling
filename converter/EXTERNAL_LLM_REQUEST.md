# External LLM Request: Minimal Working HWPX Package

## Context

We are developing a Markdown to HWPX converter. Our current implementation generates HWPX files that fail to open in Hangul (한글) word processor. We need a **minimal but complete working HWPX package** as a reference.

## Goal

Create a **minimal HWPX package that successfully opens in Hangul** with the following characteristics:
- Contains simple text content (single paragraph is sufficient, e.g., "테스트입니다")
- Includes all **required files** for a valid HWPX package
- Uses **minimal but complete** XML structures that Hangul accepts
- Follows the HWPX specification (KS X 6101) where applicable

## Reference Materials Provided

We have two working HWPX files for reference:
1. `test_minimal_manual.hwpx` - A minimal manual test file
2. `test_inputmodel.hwpx` - A more complete example file

Both files successfully open in Hangul.

## Required Output

Please provide **complete XML content** for each of these files:

### Required Files (in order of importance)

1. **mimetype**
   - Plain text file containing MIME type

2. **version.xml**
   - HWPX version information
   - Must include all required attributes

3. **META-INF/manifest.xml**
   - ODF manifest structure
   - Currently missing in our implementation

4. **META-INF/container.xml**
   - OCF container definition
   - Must reference all rootfiles

5. **META-INF/container.rdf**
   - RDF metadata linking document parts
   - Currently missing in our implementation

6. **Contents/header.xml**
   - Document header with:
     - Minimal fontfaces (at least one font, e.g., "맑은 고딕")
     - Minimal charProperties (at least one charPr)
     - Minimal paraProperties (at least one paraPr)
     - Minimal styles (at least one style)
     - Required borderFills, tabProperties

7. **Contents/section0.xml**
   - Document body with:
     - One simple paragraph
     - Proper secPr (section properties) including page settings
     - Correct ID references to header.xml

8. **Contents/content.hpf**
   - Package manifest
   - Must include:
     - metadata section
     - manifest section (listing header.xml, section0.xml)
     - spine section (defining reading order)

9. **settings.xml**
   - Application settings
   - Can be minimal but must be valid

## Current Issues We Identified

Based on comparing our generated files with working examples:

### Missing Files
- ❌ `META-INF/manifest.xml` - completely missing
- ❌ `META-INF/container.rdf` - completely missing

### Incomplete Files
- ⚠️ `content.hpf` - missing spine section, incomplete manifest
- ⚠️ `container.xml` - missing rootfile entries for container.rdf
- ⚠️ `version.xml` - missing attributes: micro, buildNumber, os, xmlVersion, application, appVersion

## Specific Requirements

### 1. Namespace Usage
- Use proper XML namespaces for all elements
- Reference namespaces:
  ```
  ha: http://www.hancom.co.kr/hwpml/2011/app
  hp: http://www.hancom.co.kr/hwpml/2011/paragraph
  hs: http://www.hancom.co.kr/hwpml/2011/section
  hc: http://www.hancom.co.kr/hwpml/2011/core
  hh: http://www.hancom.co.kr/hwpml/2011/head
  hpf: http://www.hancom.co.kr/schema/2011/hpf
  dc: http://purl.org/dc/elements/1.1/
  opf: http://www.idpf.org/2007/opf/
  ocf: urn:oasis:names:tc:opendocument:xmlns:container
  ```

### 2. ID Reference Consistency
- **CRITICAL**: All ID references must be consistent:
  - `section0.xml` → `<hp:p paraPrIDRef="0">` must match `header.xml` → `<hh:paraPr id="0">`
  - `section0.xml` → `<hp:run charPrIDRef="0">` must match `header.xml` → `<hh:charPr id="0">`
  - `charPr fontRef hangul="0"` must match `<hh:font id="0">`

### 3. Minimal Page Settings
Include basic A4 page setup in secPr:
- Width: 59528 (A4 width in HWPUNIT, ~210mm)
- Height: 84186 (A4 height in HWPUNIT, ~297mm)
- Margins: reasonable defaults

### 4. Specification Compliance
- **Primary**: Follow KS X 6101 (HWPX specification)
- **Secondary**: If certain elements are required by Hangul implementation but not in spec, please:
  - Mark with comment: `<!-- Implementation requirement, not in spec -->`
  - Explain why it's needed

### 5. Minimal Font Definition
At minimum, define one font (e.g., "맑은 고딕"):
```xml
<hh:fontface lang="HANGUL" fontCnt="1">
  <hh:font id="0" face="맑은 고딕" type="TTF" isEmbedded="0">
    <!-- include required typeInfo -->
  </hh:font>
</hh:fontface>
```

## Output Format

Please provide:

```markdown
## File: mimetype
[plain text content]

## File: version.xml
[complete XML]

## File: META-INF/manifest.xml
[complete XML]

## File: META-INF/container.xml
[complete XML]

## File: META-INF/container.rdf
[complete XML]

## File: Contents/header.xml
[complete XML with comments explaining critical parts]

## File: Contents/section0.xml
[complete XML with comments explaining critical parts]

## File: Contents/content.hpf
[complete XML]

## File: settings.xml
[complete XML]

## Notes
[Any additional notes about:
- Why certain elements are required
- Which parts are spec-compliant vs implementation-specific
- Any gotchas or common mistakes
]
```

## Success Criteria

The resulting HWPX package must:
1. ✅ Open successfully in Hangul word processor without errors
2. ✅ Display at least one paragraph of text
3. ✅ Use minimal but complete XML structures
4. ✅ Have consistent ID references throughout
5. ✅ Include all required package files

## What We Will Do

After receiving your sample:
1. Save it as `converter/minimal_reference.hwpx`
2. Extract and analyze each XML file
3. Update our `md_to_hwpx.py` generator to match the working structure
4. Run validator to check specification compliance
5. Test in Hangul to verify it opens correctly

## Questions to Address (if possible)

1. Is `META-INF/manifest.xml` absolutely required? (We suspect YES)
2. Is `META-INF/container.rdf` required for basic functionality? (We suspect YES)
3. What is the minimum valid structure for `content.hpf` manifest and spine?
4. Are there any critical attributes in `version.xml` that Hangul checks?

---

**Thank you for your help in creating this minimal working reference!**
